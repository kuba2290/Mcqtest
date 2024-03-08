import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utilis import read_file,get_table_data
from src.mcqgenerator.logger import logging


#Importing necessary packages from langchain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

#load environment variables from the.env file
load_dotenv()

#Access the environment variables 
key = "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"

llm= ChatOpenAI(openai_api_key=key, model_name= "gpt-3.5-turbo", temperature=0.7)

template= """
TEXT : {text}
You are an expert MCQ maker, Given the above text, it is your job to 
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
make sure the questions are not repeated and check all the questions to be conforming the text as well.
 make sure to format your response like RESPONSE_JSON below and use it as a guide. 
 Ensure to make {number} MCQs 
 ### RESPONSE_JSON
 {response_json}

"""

quiz_generation_prompt = PromptTemplate(
    input_variables= ["text", "number","subject", "tone","response_json" ],
    template=template
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

template2 = """
You are an expert english gramarian and writer, Given a multiple choice quiz for {subject} students.
You need to evaluate the complexity of the question and give a complete analysis of the quiz, only use at max 50 words for complexity
if the quiz is not at per the cognitive and analytical abilities of thes students.
update the quiz questions which needs to be changed and change[the tone such that it perfectly the students ability]
Quiz_MCQS:
{quiz}

Check from an expert English Writer of the above quiz:"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables= ["subject", "quiz" ],
    template=template2
)

review_chain =LLMChain(
    llm=llm,
    prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject","tone", "response_json"],output_variables=["quiz","review"], verbose=True)



