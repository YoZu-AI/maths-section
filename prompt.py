prompt_template = '''
Let's solve mathematical word problems in a careful, formal manner. The solution will follow the Peano format: 
1- Each sentence in the solution either introduces a new variable or states a new equation. 
2- The last sentence gives the goal: which variable will contain the answer to the problem. 
3- Each equation only uses previously introduced variables. 
4- Each quantity is only named by one variable.
5- Use all the numbers in the question.
Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?
Peano solution:
Let a be the number of apples Mary started with [[var a]]. We have [[eq a = 5]]. 
Let b be how many apples she had in the morning after eating 2 apples [[var b]]. We have [[eq b = a - 2]]. 
Let c be the apples she bought in the afternoon [[var c]]. 
Since she bought as many as she had after eating, we have [[eq c = b]]. 
Let d be how many apples she ended up with [[var d]]. We have [[eq d = b + c]]. 
The answer is the value of d [[answer d]]. 
Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?
Peano solution:
Let a be the number of years Mario had [[var a]]. 
Let b be the number of years Luigi had [[var b]]. We have [[eq a + b = 10]]. We also have [[eq b = a + 3]]. 
The answer is the value of a [[answer a]].
Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?
Peano solution:
Let a be the number of hours in a week [[var a]]. We have [[eq a = 168]]. 
Let b be the number of hours in a revolution [[var b]]. We have [[eq b = a * 2]]. 
Let c be the number of hours in half a revolution [[var c]]. We have [[eq c = b / 2]]. 
The answer is the value of c [[answer c]].
Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
Peano solution:
Let a be the number of cars in the parking lot [[var a]]. We're given [[eq a = 3]]. 
Let b be the number of cars arrived [[var b]]. We're given [[eq b = 2]]. 
Let c be the number of cars in the parking lot now [[var c]]. We have [[eq c = a + b]]. 
The answer is the value of c [[answer c]].
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Peano solution:
Let a be the number of trees in the grove [[var a]]. We're given [[eq a = 15]]. 
Let b be the number of trees Grove workers will plant [[var b]].
Let c be the number of trees in the grove after the workers are done [[var c]]. We have [[eq c = a + b]]. We're given [[eq c = 21]].
The answer is the value of b [[answer b]].
Q: {question}
Peano solution:
'''.strip() + '\n\n\n'