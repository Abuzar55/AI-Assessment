from openai import OpenAI
from exceptions import CustomExcetions
from logger import logging
import sys

class CreateRun:
    def __init__(self, assistant_id, thread_id, client: OpenAI):
        self.thread_id = thread_id
        self.assistant_id = assistant_id
        self.client = client
        
    def create_run(self):
        try:
            run = self.client.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=self.assistant_id)
            return run
        except Exception as e:
            raise CustomExcetions(e, sys)
    def retrieve_run(self, run_id):
        try:
            run = self.client.beta.threads.runs.retrieve(
            thread_id=self.thread_id,
            run_id=run_id)
            return run
        except Exception as e:
            raise CustomExcetions(e, sys)
