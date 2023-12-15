from prem import PremAI

api_key = "3EC9HA3EFaQgFbzE8TqsOb0OTrTfFxv2x9"
base_url = "http://localhost:8000"
prem_ai_client = PremAI(api_key=api_key, base_url=base_url)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
]

model = "gpt-3.5-turbo"

response = prem_ai_client.completions.create(
    project_id=1, messages=messages, model=model
)
print(response)
