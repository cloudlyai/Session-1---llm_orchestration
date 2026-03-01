from dotenv import load_dotenv
from litellm import completion
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")


load_dotenv()

#========= generate puzzle with help of gpt-4o-mini model ============

Messages =[{ "role": "user", "content": "You are a helpful assistant, please generate an interesting puzzle. don't provide any further line beyond puzzle and don't provide any ans" }]

response= completion(
    model="gpt-4o-mini", 
    messages=Messages
)
puzzle = response.choices[0].message.content
print("Generated Puzzle:")  
print(puzzle)

#========= generate hint with help of claude haiku model =============
Messages.append({ "role": "assistant", "content": puzzle })
Messages.append({ "role": "user", "content": "Generate a hint for the above puzzle." })

response = completion(
    model="claude-3-haiku-20240307",
    messages=Messages,
    max_tokens=300,
    system="You are a helpful assistant that provides hints for puzzles. please start hint with word Anthropic:"    
)
hint = response.choices[0].message.content
print("\nGenerated Hint:") 
print(hint)

#=========  Use Gemini flash model to generate solution =============
Messages.append({ "role": "assistant", "content": hint })
Messages.append({ "role": "user", "content": "Generate the solution for the above puzzle." })
Messages.append({ "role": "system", "content": "You are a helpful assistant that provides solutions for puzzles. please start solution with word Gemini:" })

response = completion(
    model="gemini/gemini-2.0-flash-exp",
    messages=Messages,
)
Solution = response.choices[0].message.content
print("\nGenerated Solution:") 
print(Solution)



  


