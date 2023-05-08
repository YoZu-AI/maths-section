import openai
from prompt import prompt_template
from config import math_model, API_KEY
openai.api_key = API_KEY

def maths_solution(input_question):
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
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
        {"role": "system", "content": "You are a kind and helpful AI maths tutor you provide solution in step by step manner"},
        {"role": "user", "content": input_question}
        ]
        )
    return completion['choices'][0]['message']['content']
  
#################################################

input_question = 'An army contingent of 616 members is to march behind an army band of 32 members in a parade. The two groups are to march in the same number of columns. What is the maximum number of columns in which they can march?'
solution = maths_solution(input_question)
print(solution)
     
