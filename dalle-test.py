import openai

openai.api_key = "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"

response = openai.Image.create(
  prompt="a kid riding a lama in the circus",
  n=5,
  size="256x256"
)
image_url = response['data'][0]['url']
print(response)

f = open("dalle-test.html", "w")
f.write("")
f.close()

f = open("dalle-test.html", "a")
for x in response['data']:
  f.write("<img src='"+(str(x['url']))+"'>")
f.close()
