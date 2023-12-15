from prem import PremAI

api_key = "3EC9HA3EFaQgFbzE8TqsOb0OTrTfFxv2x9"
base_url = "http://localhost:8000"
client = PremAI(api_key=api_key, base_url=base_url)

# Test Completions
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
]
model = "gpt-3.5-turbo"
response = client.completions.create(
    project_id=1, messages=messages, model=model, stream=False
)
print(response)
response = client.completions.create(
    project_id=1, messages=messages, model=model, stream=True
)
print(response)

# Test Embeddings
input = "What is a transformer?"
model = "text-embedding-ada-002"
response = client.embeddings.create(project_id=1, input=input, model=model)
print(response)
