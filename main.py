from fastapi import FastAPI 
from pydantic import BaseModel
from src.pipeline.Assistant_Flow_Pipeline import AssistantFlow
from openai import OpenAI
import os
import json
from src.utils import categories, post_processing
from logger import logging
import sys
from typing import List
from exceptions import CustomExcetions
from dotenv import load_dotenv
from src.constants import models
import concurrent.futures

load_dotenv()

api_key = os.getenv("OPEN_AI_KEY")
client = OpenAI(api_key=api_key)


class AssistantResponseRequest(BaseModel):
    skill_list: List
    # number_of_questions: int
    # difficulty: str

app = FastAPI()

@app.post("/v1/questions_generation")
async def questions_generation(request: AssistantResponseRequest):
    try:
        final_results = []
        assistant_obj = AssistantFlow(client=client, model_name=models[2])
        # return request.skill_list
        # Use ThreadPoolExecutor as a context manager
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for skill_dict in request.skill_list:
                # print(skill_dict)
                skill = skill_dict["skill"]
                number_of_questions = skill_dict["number_of_questions"]
                difficulty = skill_dict["difficulty"]
                answer_type = skill_dict["answer_type"]

                # category = categories(skill_name=skill.lower(), number_of_questions=number_of_questions)
                future = executor.submit(assistant_obj.assisstant_flow, 
                                          difficulty_level=difficulty, 
                                          number_of_questions=number_of_questions, 
                                          skill_name=skill,
                                          answer_type = answer_type)
                futures.append(future)

            # Wait for all tasks to complete
            for future in futures:
                    result = future.result()
                    if result:
                        final_results.append(json.loads(result))

        return {"questions": post_processing(final_results)}
    
    except Exception as e:
        # Handle exceptions here (e.g., log the error)
        raise CustomExcetions(e, sys)
