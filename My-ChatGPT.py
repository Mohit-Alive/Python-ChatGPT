import openai
 
# Openai api key
openai.api_key = "YOUR OPENAI TOKEN"
 
# Here are the prompt and model
model_engine = "text-davinci-003"
prompt = input()
 
# Set the maximum number of tokens to generate in the response
max_tokens = 1024
 
# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
 
# Print the response
print(completion.choices[0].text)