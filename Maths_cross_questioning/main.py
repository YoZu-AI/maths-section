import openai
from maths_prompt import prompt_template
openai.api_key = ''

def get_maths_concepts(maths_query):
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
      {"role": "system", "content": 'You are an expert maths AI assistant, you will list 5 concepts name necessary to solve the given problem without giving explanation of each concepts'},
      {"role": "user", "content": maths_query}])
  maths_concepts  = completion.choices[0].message.content.split('\n')
  concepts_list = []
  for sentence in maths_concepts:
      if len(sentence) >= 3 and sentence[0].isdigit() and sentence[1] == '.':
          concepts_list.append(sentence[2:].strip())
  return concepts_list

def get_concept_explanation(concepts_list, student_class):
  definition_prompt = 'The given list is {pre_knowledge}. Provide the precise and best possible explanation with the help of an example to each of the topics in the given list so that a student of class {class_no} can easily understand the definition and example. Follow the the format, Topic: , Definition:, Example:'
  input_definition_prompt = definition_prompt.format(pre_knowledge = str(concepts_list), class_no = student_class)
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
      {"role": "system", "content": 'You are an expert Maths AI tutor.'},
      {"role": "user", "content": input_definition_prompt}])
  maths_concepts_explanation  = completion.choices[0].message.content
  #return maths_concepts_explanation
  maths_concepts_explanation_split = maths_concepts_explanation.split('\n')
  topic = []
  definition = []
  example = []
  for i in maths_concepts_explanation_split:
    if i != '':
      if 'Topic' in i:
        topic.append(i.split('Topic:')[1].strip())
      if 'Definition' in i:
        definition.append(i.split('Definition:')[1].strip())
      if 'Example' in i:
        example.append(i.split('Example:')[1].strip())
  return topic, definition , example

def get_maths_solution(input_question, student_class):
  prompt = prompt_template.format(question = input_question)
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
      {"role": "user", "content": prompt }])
  symbol = completion.choices[0].message.content
  math_prompts = 'Analyze the given input, {symbolic_steps}. Provide the solution for the given input. You should also explain the soultion in precise, concise and step by step approach so that a student of class {student_class_no} can understand the solution'
  input_prompt = math_prompts.format(symbolic_steps = symbol, student_class_no = student_class)
  second_completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
      {"role": "system", "content": 'you are an expert maths symbolic interpreter and AI tutor who provide solution to given input and explains the solution' },
      {"role": "user", "content": input_prompt}])
  return second_completion.choices[0].message.content, input_question

def similar_example(maths_query):
  maths_similar_example_list = []
  similar_example_prompt = 'For the given maths problem, {maths_problem} and {solution}. Provide the similar example problem for the students. Do not provide the answer to the problem.'
  input_prompt = similar_example_prompt.format(maths_problem = maths_query)
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.4,
    messages=[
      {"role": "system", "content": 'You are an expert Maths AI tutor who strictly only provides similar maths problem as the given input. The problem should not be precided with any sentence'},
      {"role": "user", "content": input_prompt}])
  maths_similar_example  = completion.choices[0].message.content
  maths_similar_example_list.append(maths_similar_example)
  return maths_similar_example_list

def get_detailed_solution(previous_solution, student_class):
  prompt_format = 'provide detailed explanation of the following, {solution}. explanation should be easy to understand and simpler but should be in great detail so that a student of class {class_no} can understand'
  prompt = prompt_format.format(solution = previous_solution, class_no = student_class)
  completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0,
  messages=[
     {"role": "system", "content": 'You are an expert maths AI tutor who provides the simpler and detailed explanation of solution for the query'},
     {"role": "user", "content": prompt}])
  #print(completion.choices[0].message.content)
  return completion.choices[0].message.content

def get_detailed_definition(previous_definition, student_class):
  prompt = 'provides the simpler and detailed explanation of the definition, {definition}. Explanation should be suitable for a student studying in class {class_no}'
  provide_definition_explanation_prompt = prompt.format(definition = previous_definition, class_no = student_class)
  completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0,
  messages=[
      {"role": "system", "content": 'You are an expert maths AI tutor who provides the simpler and detailed explanation of the given input'},
      {"role": "user", "content": provide_definition_explanation_prompt}])
  return(completion.choices[0].message.content)

###############################################################

maths_query = 'Use Euclid’s division algorithm to find the HCF of:135 and 225'
student_class ='7'

concepts_list = get_maths_concepts(maths_query)
topics, definitions, examples = get_concept_explanation(concepts_list, student_class) 
maths_solution, maths_query = get_maths_solution(maths_query, student_class)
detailed_solution = get_detailed_solution(maths_query, maths_solution)
provide_definition_explanation = definitions[0]
detailed_definition = get_detailed_definition(provide_definition_explanation, student_class)
print(concepts_list)
print(topics)
print(definitions)
print(examples)
print(maths_solution)
print(detailed_solution)
print(detailed_definition)











