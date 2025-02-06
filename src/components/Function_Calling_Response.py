import sys
from openai import OpenAI
from src.constants import FunctionCallingResponses
import sys
from openai import OpenAI
from exceptions import CustomExcetions
from logger import logging

class FunctonCallingResponse:
    def __init__(self, client: OpenAI, model_name, skill_name, answer_type, category):
        self.client = client
        self.model_name = model_name
        self.skill_name = skill_name
        self.answer_type = answer_type
        self.category = category

    def generate_easy_questions(self):
        try:
            if self.skill_name == "sql" and self.answer_type == "audio":
                response = FunctionCallingResponses.sql_easy_level_topics_audio
                # print("audio---------------------------------")
            if self.skill_name == "sql" and self.answer_type == "coding":
                response = FunctionCallingResponses.sql_easy_level_topics_coding
            if self.skill_name == "python" and self.answer_type == "audio":
                response = FunctionCallingResponses.python_easy_level_topics_audio
            if self.skill_name == "python" and self.answer_type == "coding":
                response = FunctionCallingResponses.python_easy_level_topics_coding                
            if self.skill_name == "ml":
                response = FunctionCallingResponses.ml_easy_level_topics
            if self.skill_name == "statistics":
                response = FunctionCallingResponses.statistics_easy_level_topics

            logging.info(f'Content fetched for easy_level_topics')
            return response
        except Exception as e:
            raise CustomExcetions(e, sys)

    def generate_medium_questions(self):
        try:
            if self.skill_name == "sql" and self.answer_type == "audio":
                response = FunctionCallingResponses.sql_medium_level_topics_audio
            if self.skill_name == "sql" and self.answer_type == "coding":
                response = FunctionCallingResponses.sql_medium_level_topics_coding
            if self.skill_name == "python" and self.answer_type == "audio":
                response = FunctionCallingResponses.python_medium_level_topics_audio
            if self.skill_name == "python" and self.answer_type == "coding":
                response = FunctionCallingResponses.python_medium_level_topics_coding  
            if self.skill_name == "ml":
                response = FunctionCallingResponses.ml_medium_level_topics
            if self.skill_name == "statistics":
                response = FunctionCallingResponses.statistics_medium_level_topics

            logging.info(f'Content fetched for medium_level_topics')
            return response
        except Exception as e:
            raise CustomExcetions(e, sys)

    def generate_advanced_level_questions(self):
        try:
            if self.skill_name == "sql" and self.answer_type == "audio":
                response = FunctionCallingResponses.sql_hard_level_questions_audio
            if self.skill_name == "sql" and self.answer_type == "coding":
                response = FunctionCallingResponses.sql_easy_level_topics_coding
            if self.skill_name == "python" and self.answer_type == "audio":
                response = FunctionCallingResponses.python_hard_level_topics_audio
            if self.skill_name == "python" and self.answer_type == "coding":
                response = FunctionCallingResponses.python_hard_level_topics_coding  
            if self.skill_name == "ml":
                response = FunctionCallingResponses.ml_hard_level_topics
            if self.skill_name == "statistics":
                response = FunctionCallingResponses.statistics_hard_level_topics

            logging.info(f'Content fetched for advanced_level_topics')
            return response
        except Exception as e:
            raise CustomExcetions(e, sys)
    
    def topics(self):
        try:
            if self.category == "easy":
                response = FunctionCallingResponses.python_easy_level_topics_coding
            if self.category == "medium":
                response = FunctionCallingResponses.python_medium_level_topics_coding
            if self.category == "hard":
                response = FunctionCallingResponses.python_hard_level_topics_coding

                
            logging.info(f'Content fetched for topics')
            return response
        except Exception as e:
            raise CustomExcetions(e, sys)
        
    