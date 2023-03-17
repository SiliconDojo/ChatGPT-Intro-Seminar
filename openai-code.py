import os
import openai

openai.api_key = "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"

question = "how do you turn a queryset into a dictionary in python"
#question = "how do you create a dictionary in python for sue who is 34, tim is 55, fred is 64"

response = openai.Completion.create(
model="text-davinci-003",
prompt=(question),
temperature=0,
max_tokens=300,
top_p=1.0,
frequency_penalt