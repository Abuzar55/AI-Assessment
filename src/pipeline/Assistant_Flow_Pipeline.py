import sys
from logger import logging
from exceptions import CustomExcetions
from openai import OpenAI
from src.pipeline.Function_Calling_pipeline import FunctionCallingPipeline
from src.components.Create_Run import CreateRun
from src.components.Messages import Messages
from src.components.Assisstant_Definition import Assistants
import time

class AssistantFlow:
    def __init__(self, client: OpenAI, model_name):
        self.client = client
        self.model_name = model_name 
        self.role = "user"
    
    def assisstant_flow(self, difficulty_level, number_of_questions, skill_name, answer_type):
        try:
            assistant_obj = Assistants(client=self.client, model_name=self.model_name, skill_name=skill_name, answer_type=answer_type)
            thread_id, assisstant_id = assistant_obj.fetch_assisstant_id()

            if skill_name == "sql":
                content = f"Generate {number_of_questions} {difficulty_level} level questions of {answer_type}. When generating multiple questions, cover all QUESTION CATEGORIES and generate equal number of quesitons for each category"
            if skill_name == "python" and answer_type == "audio":
                content = f"Generate {number_of_questions} {difficulty_level} level questions. Make sure to cover purely the conceptual side of python concepts. Answer type must be audio. When generating multiple questions, cover more than one category"
            if skill_name == "python" and answer_type == "coding":
                content = f"Generate {number_of_questions} {difficulty_level} level questions. Make sure to include code snippet if needed. When generating multiple questions, cover more than one category"
            if skill_name == "statistics":
                content = f"Generate {number_of_questions} {difficulty_level} level questions. When generating multiple questions, cover more than one category"
            if skill_name == "ml":
                content = f"Generate {number_of_questions} {difficulty_level} level questions. When generating multiple questions, cover more than one category"


            create_message = Messages(client=self.client, thread_id=thread_id)
            create_message.create_messages(role = self.role, content = content)
            logging.info('Message created in thread successfully')
            
            create_run = CreateRun(assistant_id=assisstant_id, thread_id=thread_id, client=self.client)
            run = create_run.create_run()
            logging.info('Run created successfully')

            status = True
            retries = 0
            while status and retries < 100:
                retries += 1
                retrieved_run = create_run.retrieve_run(run_id=run.id)
                logging.info(f'Status: {retrieved_run.status}')
                # print(type(retrieved_run.status))
                if retrieved_run.status in ['queued', 'in_progress']:
                    time.sleep(3)
                    
                    continue

                elif retrieved_run.status == 'requires_action':
                    # print("entered--------------------------------")
                    if retrieved_run.required_action.submit_tool_outputs.tool_calls[0].function.name == "finish_session":
                        return "Thanks"
                    
                    else:
                        function_calling_obj = FunctionCallingPipeline(run_retrieved=retrieved_run,
                                                                    client=self.client,
                                                                    run_id=run.id,
                                                                    thread_id=thread_id,
                                                                    model_name=self.model_name,
                                                                    skill_name=skill_name,
                                                                    answer_type=answer_type,
                                                                    category=difficulty_level
                                                                    )
                        function_calling_obj.function_calling()
                        continue

                elif retrieved_run.status == 'completed':

                    show_message = create_message.show_messages()
                    logging.info('Successfully shown message')
                    status = False
                    return (show_message)

                elif retrieved_run.status in ['cancelling', 'cancelled', 'failed', 'expired']:
                    user_message = f"Run Status: {retrieved_run.status}"
                    logging.info(user_message)
                    return user_message
                

                break
                
        except Exception as e:
            raise CustomExcetions(e, sys)