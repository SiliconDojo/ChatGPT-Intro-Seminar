import openai

openai.api_key = "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"

nationality = "brazil"

response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[ {"role": "system", "content": "act like you are a travel advisor"}, 
              {"role": "assistant", "content": "answer as a" +(nationality)+ " citizen"},
              {"role": "user", "content": "who was the leader in 2000" }
            ]
)

output_text = response['choices'][0]['message']['content']
print(response)
pri