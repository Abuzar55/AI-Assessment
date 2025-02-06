import sys
from openai import OpenAI
from exceptions import CustomExcetions
from logger import logging
from src.components.Function_Calling_Response import FunctonCallingResponse
from src.components.Function_Calling_variables import FunctionCalling

class FunctionCallingPipeline:
    def __init__(self, run_retrieved, client:OpenAI, run_id, thread_id, model_name, skill_name, answer_type, category):
        self.client = client
        self.run_retrieved = run_retrieved
        self.thread_id = thread_id
        self.run_id = run_id
        self.model_name = model_name
        self.skill_name = skill_name
        self.answer_type = answer_type
        self.category = category

    def function_calling(self):
        try:
            func_call_vars = FunctionCalling(client=self.client, run_retrieved=self.run_retrieved)
            function = func_call_vars.function_name()
            function_calling_response_obj = FunctonCallingResponse(
                            client=self.client,
                            model_name=self.model_name,
                            skill_name=self.skill_name,
                            answer_type=self.answer_type,
                            category=self.category 
                            )
 
            if hasattr(function_calling_response_obj, function):
                func_to_call = getattr(function_calling_response_obj, function)
                response = func_to_call()

                logging.info(f'{function} function called')

                completion = func_call_vars.submit_tool_output(thread_id=self.thread_id, function_response=response, run_id=self.run_id)

                return completion
        except Exception as e:
            raise CustomExcetions(e, sys)