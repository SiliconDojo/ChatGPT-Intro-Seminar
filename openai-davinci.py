import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="create an email to Sue Perkins and ask her if she wants to buy my ice cream maker for $10",
  temperature=0,
  max_tokens=1000,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(" ")
print(response)

print (response["choices"][0]["text"])