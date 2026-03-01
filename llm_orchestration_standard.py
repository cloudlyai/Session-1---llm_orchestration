from dotenv import load_dotenv
import os

from openai import OpenAI

from anthropic import Anthropic

load_dotenv()

openai_client = OpenAI()

Messages =[{ "role": "user", "content": "You are a helpful assistant, please generate an interesting puzzle. don't provide any further line beyond puzzle and don't provide any ans" }]

response= openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=Messages
)

puzzle = response.choices[0].message.content
print("Generated Puzzle:")
print(puzzle)

#========= generate hint with help of claude haiku model =============

Messages.append({ "role": "assistant", "content": puzzle })
Messages.append({ "role": "user", "content": "Generate a hint for the above puzzle." })


Anthropic_client = Anthropic() 

response = Anthropic_client.messages.create(
    model="claude-3-haiku-20240307",
    messages=Messages,
    max_tokens=300,
    system="You are a helpful assistant that provides hints for puzzles. please start hint with word Anthropic:"    
)

hint = response.content[0].text
print("\nGenerated Hint:")  
print(hint)

#=========  Use Gemini flash model to generate solution =============

Messages.append({ "role": "assistant", "content": hint })
Messages.append({ "role": "user", "content": "Generate the solution for the above puzzle." })
Messages.append({ "role": "system", "content": "You are a helpful assistant that provides solutions for puzzles. please start solution with word Gemini:" })

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_client = OpenAI(api_key=gemini_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai")

response = gemini_client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=Messages
)   
solution = response.choices[0].message.content
print("\nGenerated Solution:")  
print(solution)

