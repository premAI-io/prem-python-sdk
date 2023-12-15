<div align="center">
  <h1 align="center">🚀 Prem Python SDK</h1>
  <p align="center">The Prem Python SDK is a Python library for interacting with the <a href="https://github.com/premAI-io/prem-saas">Prem  API</a></p>

[![GitHub contributors](https://img.shields.io/github/contributors/premAI-io/prem-python-sdk.svg)](https://github.com/premAI-io/prem-python-sdk/graphs/contributors)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/prem-python-sdk-io/prem-python-sdk.svg)](https://github.com/premAI-io/prem-python-sdk/commits/master)
[![GitHub last commit](https://img.shields.io/github/last-commit/premAI-io/prem-python-sdk.svg)](https://github.com/premAI-io/prem-python-sdk/commits/master)
[![GitHub top language](https://img.shields.io/github/languages/top/premAI-io/prem-python-sdk.svg)](https://github.com/premAI-io/prem-python-sdk)
[![GitHub issues](https://img.shields.io/github/issues/premAI-io/prem-python-sdk.svg)](https://github.com/premAI-io/prem-python-sdk/issues)
</div>


<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <ol>
            <li><a href="#getting-started">Getting Started</a></li>
            <li><a href="#completions">Completions</a></li>
            <li><a href="#embeddings">Embeddings</a></li>
            <li><a href="#data-points">DataPoints</a></li>
        </ol>
    </ol>
</details>

## Installation

1. Clone the Prem Python SDK repository:

   ```bash
   git clone https://github.com/premAI-io/prem-python-sdk.git
   ``````

2. Install the SDK
    ```bash
    cd prem-python-sdk
    python -m venv venv
    source venv/bin/activate
    pip install .
    ```
## Usage
### Getting Started
To use the Prem Python SDK, you need to obtain an API key from the Prem platform. You can then create a `PremAI` instance to make requests to the API.

```python
from prem import PremAI

api_key = "YOUR_API_KEY"
base_url = "https://api.prem.com"  # Update with the base URL of the Prem API

client = PremAI(api_key=api_key, base_url=base_url)
```

### Completions
The `completions` module allows you to generate completions based on user input. Here's an example:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
]
model = "gpt-3.5-turbo"

# Create completion
response = client.completions.create(project_id=1, messages=messages, model=model, stream=False)
print(response)
```

### Embeddings
The `embeddings` module enables you to create embeddings for given input. Example:

```python
input_text = "What is a transformer?"
model = "text-embedding-ada-002"

# Create embeddings
response = client.embeddings.create(project_id=1, input=input_text, model=model)
print(response)
```

### Data Points
The `datapoints` module allows you to manage data points, including creating, updating, retrieving, and deleting. Example:
```python
input_text = "What is a transformer?"

# Create 10 data points
for _ in range(10):
    data_point = client.datapoints.create(project_id=1, input=input_text, positive=True)

# Update the last data point
patched_data_point = client.datapoints.update(datapoint_id=data_point.id, data={"positive": False})

# Retrieve the updated data point
print(client.datapoints.retrieve(datapoint_id=data_point.id))

# Delete the updated data point
client.datapoints.delete(datapoint_id=data_point.id)

# List all data points
datapoints = client.datapoints.list(project_id=1)
print("Total number of datapoints:", len(datapoints))
for datapoint in datapoints:
    print("Deleted data point with ID:", datapoint.id)
    client.datapoints.delete(datapoint_id=datapoint.id)
```
