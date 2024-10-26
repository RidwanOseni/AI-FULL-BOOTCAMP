from openai import OpenAI
client = OpenAI()
response = client.images.generate(
    model="dall-e-2",
    prompt="a delicious burrito",
    size="512x512",
    n=1,
 )
print(response.data[0].url)
