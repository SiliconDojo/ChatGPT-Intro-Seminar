#import os
import openai

openai.api_key = "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"


slant = ["christian", "scientist", "pastafarian", "republicans", "democrats"]
question = "how did the world begin"

for x in slant:
  submit = ("how do ")+ str(x) +("think") + question
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=(submit),
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
  print(" ")
  print (str('As a ') + str(x))
  print (question)
  answer = str(response["choices"][0]["text"])
  pr