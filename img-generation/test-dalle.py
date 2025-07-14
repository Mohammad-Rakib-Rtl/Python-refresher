import openai

response = openai.Image.create(

    prompt = "Cat with glasses",
    n = 1, 
    size = "1024x1024"


)

print(response)