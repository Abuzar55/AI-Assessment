from openai import OpenAI
from exceptions import CustomExcetions
from logger import logging
import sys

class Messages:
    def __init__(self, client: OpenAI, thread_id):
        self.client = client
        self.thread_id = thread_id
        
    def create_messages(self, role, content):
        try:
            message = self.client.beta.threads.messages.create(
            thread_id=self.thread_id,
            role=role,
            content=content
            )
            return message
        except Exception as e:
            # print(e)
            raise CustomExcetions(e, sys)
        
    def show_messages(self):
        try:
            messages = self.client.beta.threads.messages.list(
            thread_id= self.thread_id)
            response = (messages)

            return (response.data[0].content[0].text.value)
        except Exception as e:
            raise CustomExcetions(e, sys)
        
    