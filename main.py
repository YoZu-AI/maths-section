import openai
from prompt import prompt_template
from config import math_model, API_KEY
openai.api_key = ''

def maths_solution(input_question, student_class):
  try:
    prompt = prompt_template.format(question = input_question)
    completion = openai.ChatCompletion.create(model = math_model,temperature = 0,
        messages=[{'role': 'system', 'content': 'You are a helpful assistant that can write Python code that solves mathematical reasoning questions similarly to the examples that you will be provided.'},
        {'role': 'user', 'content': prompt}])
    python_function = completion['choices'][0]['message']['content']
    completion2 = openai.ChatCompletion.create(
          model = 'gpt-3.5-turbo',
          temperature = 0,
          messages=[{'role': 'system', 'content': 'You are a python compiler who strictly provides only the answer'},
        {'role': 'user', 'content': python_function}])
    final_answer = completion2['choices'][0]['message']['content']
    lines = python_function.split('return')[0].split('def solution():')[1].split('\n')
    step_num = 1
    for i, line in enumerate(lines):
        num_hashes = line.count('#')
        if num_hashes > 0:
            lines[i] = line.replace('#'*num_hashes, f"Step {step_num}: ")
            step_num += 1
    output_str = '\n'.join(lines) + '\n' + str(final_answer)
    return output_str
  except:
    maths_prompt = 'explain the solution to the following maths problem, {question}. Provide solution in a step by step approach such that a student of class {student_class_no} can understand'
    input_prompt = maths_prompt.format(question = input_question, student_class_no = student_class)
    #print(input_prompt)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
        {"role": "system", "content": "You are a kind and helpful AI maths tutor you provide solution in step by step manner"},
        {"role": "user", "content": input_prompt}
        ]
        )
    return completion['choices'][0]['message']['content']
  ######################################################
  
#################################################

input_question = 'A bag contains 5 red balls and some blue balls. If the probability of drawing a blue ball is double that of a red ball, determine the number of blue balls in the bag.'
solution = maths_solution(input_question,'8')
print(solution)
     
