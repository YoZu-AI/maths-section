import openai
from prompt import prompt_template
from config import math_model, API_KEY
openai.api_key = ''

def maths_solution(input_question, student_class):
  prompt = prompt_template.format(question = input_question)
  completion = openai.ChatCompletion.create(
    model = math_model,
    temperature = 0,
    messages=[
      {"role": "user", "content": prompt }])
  symbol = completion.choices[0].message.content
  math_prompts = 'Analyze the given input, {symbolic_steps}. Provide the solution for the given input. You should also explain the soultion in precise, concise and step by step approach so that a student of class {student_class_no} can understand the solution'
  input_prompt = math_prompts.format(symbolic_steps = symbol, student_class_no = student_class)
  second_completion = openai.ChatCompletion.create(
    model = math_model,
    temperature = 0,
    messages=[
      {"role": "system", "content": 'you are an expert maths symbolic interpreter and AI tutor who provide solution to given input and explains the solution' },
      {"role": "user", "content": input_prompt}])
  return(second_completion.choices[0].message.content)
#############################

input_question = '(2*2+7)*8'
class_no = '10'
print(maths_solution(input_question, class_no))