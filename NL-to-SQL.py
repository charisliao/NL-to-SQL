# Author: Charis Liao 
# Date: 2/11/2024 
# Description: This file contains the code for the NL-to-SQL model.

import pandas as pd 
import openai

def create_table_definition_prompt(df):
    """
    Create a prompt that informs GPT that we want to work 
    with SQL table and what our overall goal is 
    """
    prompt = '''Give the following sqlite SQL definition, write queries based on the request \n###
    sqlite SQL table, with its properties: 
    #
    # Sales({})
    '''.format(",".join(str(x) for x in df.columns))

    return prompt

def user_query_input():
    """Ask the user what they want to know about the data.

    Returns:
        string: User input
    """
    user_input = input("Tell OpenAi what you want to know about the data: ")
    return user_input