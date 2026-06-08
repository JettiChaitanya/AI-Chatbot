import google.generativeai as genai

genai.configure(api_key="AQ.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

for model in genai.list_models():
    print(model.name)