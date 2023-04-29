import openai
from prompt import prompt_template
from config import math_model, API_KEY
openai.api_key = API_KEY


def maths_solution(input_question):
  prompt = prompt_template.format(question = input_question)
  try:
    completion = openai.ChatCompletion.create(
      model = math_model,
      temperature = 0,
      messages=[{'role': 'system', 'content': 'You are a helpful assistant that can write Python code that solves mathematical reasoning questions similarly to the examples that you will be provided.'},
    {'role': 'user', 'content': prompt}])
    python_function = completion['choices'][0]['message']['content']
    completion2 = openai.ChatCompletion.create(
      model = math_model,
      temperature = 0,
      messages=[{'role': 'system', 'content': 'You are a helpful assistant who compiles python functions and returns only the answer'},
    {'role': 'user', 'content': python_function}])
    final_answer = completion2['choices'][0]['message']['content']
    #print(python_function.split('return')[0].split('def solution():')[1])
    #print(final_answer)
    return str(python_function.split('return')[0].split('def solution():')[1]) + '\n' + str(final_answer)
  except:
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
      {"role": "system", "content": "You are a kind and helpful AI maths tutor"},
      {"role": "user", "content": input_question}
    ]
    )
    return completion['choices'][0]['message']['content']
  

  ######################################################

input_question = 'Find the 31st term of an A.P. whose 11th term is 38 and the 16th term is 73'
solution = maths_solution(input_question)
print(solution)