# Installation

## From Source

1\. Clone the Prem Python SDK repository:
```bash
git clone https://github.com/premAI-io/prem-python-sdk.git
```

2\. Install the SDK
```bash
cd prem-python-sdk
python -m venv venv
source venv/bin/activate
pip install .
```

## From PyPI
You can also install the Prem Python SDK directly from PyPI.

```bash
pip install premai
```

# Usage
## Getting Started
To use the Prem Python SDK, you need to obtain an API key from the Prem platform. You can then create a `Prem` instance to make requests to the API.

```python
from premai import Prem

api_key = "YOUR_API_KEY"
client = Prem(api_key=api_key)
```

## Chat completion
The `chat.completions` module allows you to generate completions based on user input. Here's an example:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
]
model = "gpt-3.5-turbo"
project_id = YOUR_PROJECT_ID

# Create completion
response = client.chat.completions.create(
  project_id=project_id,
  messages=messages, 
  model=model
)

print(response.choices)
```

## Embeddings
The `embeddings` module enables you to create embeddings for given input. Example:

```python
input_text = "What is a transformer?"
model = "text-embedding-ada-002"
project_id = YOUR_PROJECT_ID

# Create embeddings
response = client.embeddings.create(project_id=project_id, input=input_text, model=model)

print(response.data)
```

## Data Points
The `datapoints` module allows you to manage data points, including creating, updating, retrieving, and deleting. Example:
```python
input_text = "What is a transformer?"
output_text = "A transformer is a deep learning model that uses self-attention."
project_id = YOUR_PROJECT_ID

# Create 10 data points
for _ in range(10):
    data_point = client.datapoints.create(project=project_id, input=input_text, output=output_text, positive=True)

# Update the last data point
patched_data_point = client.datapoints.patch(id=data_point.id, positive=False)

# Retrieve the updated data point
print(client.datapoints.retrieve(id=data_point.id))

# Delete the updated data point
client.datapoints.delete(id=data_point.id)

# List all data points
datapoints = client.datapoints.list(project=project_id)
print("Total number of datapoints:", len(datapoints))
for datapoint in datapoints:
    print("Deleted data point with ID:", datapoint.id)
    client.datapoints.delete(id=datapoint.id)
```