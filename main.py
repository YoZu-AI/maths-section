import openai
import math
from prompt import prompt_template
from config import math_model, API_KEY
openai.api_key = ''

def maths_solution(input_question, student_class):
  try:
    input_question = input_question.lower()
    def sin(x):
      return math.sin(math.radians(x))
    def cos(x):
      return math.cos(math.radians(x))
    def tan(x):
      return math.tan(math.radians(x))
    def ln(x):
      return math.log2(math.radians(x))
    def log(x):
      return math.log10(x)
    def fact(x):
      return math.factorial(x)
    def root(x):
      return math.sqrt(x)
    def pow(x, y):
      return math.pow(x, y)
    pi = 3.14

    solution = (eval(input_question))
    #print((solution))
    math_prompts = 'Analyze the given query, {query} And its solution,{eval_solution}. You should explain the soultion in precise, concise and step by step approach so that a student of class {student_class_no} can understand the solution'
    input_prompt = math_prompts.format(query = input_question, eval_solution = solution, student_class_no = student_class)
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0,
        messages=[
        {"role": "system", "content": 'you are an expert maths AI tutor who explains the solution' },
        {"role": "user", "content": input_prompt}])
    #print('Answer from calculator part')
    return(completion.choices[0].message.content)
    #completion.choices[0].message.content
  except:
    prompt = prompt_template.format(question = input_question)
    second_completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[{"role": "user", "content": prompt }])
    symbol = second_completion.choices[0].message.content
    math_prompts = 'Analyze the given input, {symbolic_steps}. Provide the solution for the given input. You should also explain the soultion in precise, concise and step by step approach so that a student of class {student_class_no} can understand the solution'
    input_prompt = math_prompts.format(symbolic_steps = symbol, student_class_no = student_class)
    Third_completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0,
        messages=[
          {"role": "system", "content": 'you are an expert maths symbolic interpreter and AI tutor who provide solution to given input and explains the solution' },
          {"role": "user", "content": input_prompt}])
    #print('Answer from except part')
    return(Third_completion.choices[0].message.content)
    #Third_completion.choices[0].message.content


################################################

input_question = '2+4*5'
class_no = '10'
print(maths_solution(input_question, class_no))



