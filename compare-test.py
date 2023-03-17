import os
import openai

openai.api_key = "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"

question = "does god exist"

print ("Question: ",question)

response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[ {"role": "system", "content": "answer this question"}, 
              {"role": "user", "content": question }
            ]
)

print("Turbo Says:")
print(response['choices'][0]['message']['content'])

response = openai.Completion.create(
model="text-davinci-003",
prompt=(question),
temperature=0,
max_tokens=500,
top_p=1.0,
frequency_penalty=0.0,
presence_penalty=0.0
)

print(" ")
print("Davinci Says:")
print(response["choices"][0