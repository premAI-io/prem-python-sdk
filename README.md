
# Prem Python SDK

## Installation

You can install the Prem Python SDK directly from npm.

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

## Chat completion

The `chat.completions` module allows you to generate completions based on user input. Here's an example:

```python
messages = [
    {"role": "user", "content": "Who won the world series in 2020?"},
]
project_id = PROJECT_ID

# Create completion
response = client.chat.completions.create(
    project_id=project_id,
    messages=messages,
)

print(response.choices)
```

### Chat completion with stream

You can also create a completion with a stream to receive the response in chunks by passing the `stream` parameter as `true` (default is `false`).

```python
# Create completion with stream
response = client.chat.completions.create(
    project_id=project_id,
    messages=messages,
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta["content"]:
        print(chunk.choices[0].delta["content"], end="")
```

### Optional parameters

By default, the `chat.completions` module uses the default launchpad parameters. You can also specify the following optional parameters:

- `model`: The model to use for completion. If omitted, the default launchpad model will be used.
- `system_prompt`: The system prompt to use for completion. If omitted, the default launchpad system prompt will be used.
- `session_id`: A unique identifier to maintain session context, useful for tracking conversations or data across multiple requests.
- `temperature`: The temperature to use for completion. If omitted, the default launchpad temperature will be used.
- `max_tokens`: The maximum number of tokens to generate for completion. If omitted, the default launchpad max tokens will be used.
- `top_p`: The nucleus sampling probability to use for completion. If omitted, the default launchpad top p will be used.
- `frequency_penalty`: The frequency penalty to use for completion. If omitted, the default launchpad frequency penalty will be used.
- `presence_penalty`: The presence penalty to use for completion. If omitted, the default launchpad presence penalty will be used.

Example:

```python
model = "gpt-3.5-turbo"
system_prompt = "You are a helpful assistant."
session_id = "my-session"
temperature = 0.7
messages = [
    { "role": "user", "content": "Who won the world series in 2020?" },
]

response = client.chat.completions.create(
    project_id=project_id,
    messages=messages,
    model=model,
    system_prompt=system_prompt,
    session_id=session_id,
    temperature=temperature
)

print(response)
```

## Enhanced Chat Completion with Retrieval Augmented Generation (RAG)

Enhance your chat completions by leveraging contextual data from specified `repositories`. A `repository` is a collection of `documents`, each containing information that can be utilized by the RAG system to provide enriched and context-aware responses.

**If you've linked your repositories in the launchpad, relax—you're all set for effortless chat completions!** The system automatically uses those parameters by default, ensuring a seamless and easy experience. However, if you wish to customize the process, you can specify the `repositories` parameter to fit your exact needs. Just define:

-   `ids`: Your selected repository IDs.
-   `similarity_threshold`: The least similarity score for content relevance.
-   `limit`: The number of content pieces to include.

For guidance on managing repositories, see the [Repositories](#repositories) section.

```python
messages = [
    { "role": "user", "content": "Which is Jack's pet name?" },
]

repositories = dict(
  ids=[REPOSITORY_ID, ...],
  similarity_threshold=0.65,
  limit=3
)

# Create completion
response = client.chat.completions.create(
  project_id=PROJECT_ID,
  messages=messages,
  repositories=repositories,
  stream=False
)

print(response.choices[0].message.content)
# "Jack's pet name is Sparky."

print(response.document_chunks)
# E.g., [DocumentChunks(repository_id=4, document_id=14, chunk_id=15, document_name="pets_and_their_owners.txt", similarity_score=0.67, content="..."), ...]
```

## Repositories
Repositories act as storage for documents, organized to facilitate efficient information retrieval. Manipulating repository content is straightforward.
### Document creation
To add a document to a repository, you can use the `create` method provided by the `document` API. Here's an example of how to create and upload a document:

```python
FILE_CONTENT = "My friend Jack has a beautiful pet, he gave it the name Sparky, [...]"

response = client.repository.document.create(
	repository_id=REPOSITORY_ID,
	name="pets_and_their_owners.txt",
	content=FILE_CONTENT,
	document_type="text",
)

print(response)
# E.g., DocumentOutput(repository_id=4, document_id=14, name="pets_and_their_owners.txt", type="text", status="UPLOADED", chunk_count=0, error=None)
```

After uploading, the document state is reflected in fields such as:

-   `status`: Shows `UPLOADED` initially, changes once processed (e.g., `PROCESSING`).
-   `chunk_count`: Number of data chunks; starts at 0 and increases post-processing.
-   `error`: Non-null if an error arose during processing.
