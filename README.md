
# Prem Python SDK

## Installation

You can install the Prem Python SDK directly from PyPI.

```bash
pip install premai
```

## Usage

### Getting Started

To use the Prem Python SDK, you need to obtain an API key from the Prem platform. You can then create a `Prem` instance to make requests to the API.

```python
from premai import Prem

client = Prem(
    api_key=YOUR_API_KEY
)
```

### Chat completion

The `chat.completions` module allows you to generate completions based on user input. Here's an example:

```python
messages = [
    {"role": "user", "content": "Who won the world series in 2020?"},
]
model = "gpt-3.5-turbo" # optional
system_prompt = "You are a helpful assistant." # optional
session_id = "my-session" # optional: a unique identifier to maintain session context, useful for tracking conversations or data across multiple requests
project_id = PROJECT_ID

# Create completion
response = client.chat.completions.create(
    project_id=project_id,
    messages=messages,
    model=model,
    session_id=session_id,
    system_prompt=system_prompt,
    stream=False
)

print(response.choices)

# Create completion with stream
response = client.chat.completions.create(
    project_id=project_id,
    messages=messages,
    model=model,
    session_id=session_id,
    system_prompt=system_prompt,
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta["content"]:
        print(chunk.choices[0].delta["content"], end="")

print(f"\nTrace ID: {response.trace_id}")
```
