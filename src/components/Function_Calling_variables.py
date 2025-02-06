from openai import OpenAI
from logger import logging
import sys
from exceptions import CustomExcetions

class FunctionCalling:
    def __init__(self, client:OpenAI, run_retrieved):
        self.run_retrieved = run_retrieved
        self.client = client
    
    def function_name(self):
        # everytime when the function calling will be called the status will change to requires action
        try:
            function_name = self.run_retrieved.required_action.submit_tool_outputs.tool_calls[0].function.name
            return function_name
        except Exception as e:
            raise CustomExcetions(e, sys)
    
    def _tool_call_id(self):
        try:
            tool_call_ids = []
            for toll_call in (self.run_retrieved.required_action.submit_tool_outputs.tool_calls):
                tool_call_ids.append(toll_call.id)

            return tool_call_ids
        except Exception as e:
            raise CustomExcetions(e, sys)

    def submit_tool_output(self, thread_id, function_response, run_id):
        try:
            tool_outputs = []
            list_of_ids = self._tool_call_id()
            # print(len(list_of_ids))
            # for call_id in list_of_ids:
            for tool_call_id in list_of_ids:
                tool_output = {
                    "tool_call_id": tool_call_id,
                    "output": function_response
                }
                tool_outputs.append(tool_output)
            run = self.client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread_id,
            run_id=run_id,
            tool_outputs=tool_outputs
            )   
            logging.info("Successfully Function Response Submitted")
            return run.status
        except Exception as e:
            raise CustomExcetions(e, sys)