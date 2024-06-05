
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

The `chat.completions` module allows you to generate completions based on user input.

Note that `system` is NOT an acceptable role: to use a system prompt you should define and pass `system_prompt`.

Here's an example:

```python
system_prompt = "You're an helpful assistant"
messages = [
    {"role": "user", "content": "Who won the world series in 2020?"},
]
project_id = PROJECT_ID

# Create completion
response = client.chat.completions.create(
    project_id=project_id,
    system_prompt=system_prompt,
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

### Prompt Templates

Should your operations entail the frequent utilization of identical prompt structures, the **Prompt Template** functionality facilitates the streamlining of this process. It enables the instantiation and subsequent reuse of predefined prompts, thereby optimizing efficiency and maintaining uniformity across interactions.

#### Creating a Prompt Template
Create your own Prompt Template in just a few steps:

- Navigate to the **Launchpad** section of your project.
- Click on the **Templates** tab.
- Hit the button to create a new Prompt Template.

From here, you can either create your custom Prompt Template or choose one of our default presets.

Within the template, you can include placeholders for dynamic content by using the `${placeholder_name}` syntax, as illustrated below:

```markdown
Summarize the following text:
"""
${text}
"""
```

In this example, we have a placeholder named `text`. To implement this through our SDK, follow this sample code:

```python
# Text you want to summarize
text_to_summarize = "This is the great tale of ... "
# Construct the message with the template
messages = [
    {
        "role": "user",
        "template_id": TEMPLATE_ID,  # Your template's ID
        "params": {"text": text_to_summarize}
    }
]

response = client.chat.completions.create(
    project_id=project_id,
    messages=messages
)
```

#### Key Points for Using Prompt Templates
When using prompt templates, remember these important guidelines:
- Replace the `content` field with `template_id` and `params`.
- Both `template_id` (the unique ID of your prompt template) and `params` (a key-value object mapping your placeholders to their desired values) are required to utilize prompt templates.

Any keys in `params` not matching placeholders will be ignored. If a placeholder is omitted in `params`, it defaults to an empty string. For instance, if you provide the following message set, the `${text}` placeholder will be left empty:

```python
messages = [
    {
        "role": "user",
        "template_id": TEMPLATE_ID,
        "params": {}  # No parameters provided for placeholders
    }
]
```
### Optional parameters

By default, the `chat.completions` module uses the default launchpad parameters. You can also specify the following optional parameters:

- `model`: The model to use for completion. If omitted, the default launchpad model will be used.
- `system_prompt`: The system prompt to use for completion. If omitted, the default launchpad system prompt will be used.
- `session_id`: A unique identifier to maintain session context, useful for tracking conversations or data across multiple requests.
- `temperature`: The temperature to use for completion. If omitted, the default launchpad temperature will be used.
- `max_tokens`: The maximum number of tokens to generate for completion. If omitted, the default launchpad max tokens will be used.

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
### Repository  creation
To create a repository, you can use the `create` method provided by the `repositories` API. Here's an example of how to create a repository:
```python

response = client.repositories.create(
	name="Test",
	description="Test Repository",
    organization="org-test@premai.io"
)
```
### Document creation
To add a document to a repository, you can use the `create` method provided by the `document` API. Here's an example of how to create and upload a document:

```python
FILE_PATH = "pets_and_their_owners.txt"
# Content: "My friend Jack has a beautiful pet, he gave it the name Sparky, [...]"

response = client.repository.document.create(
	repository_id=REPOSITORY_ID,
	file=FILE_PATH
)

print(response)
# E.g., DocumentOutput(repository_id=4, document_id=14, name="pets_and_their_owners.txt", type="text", status="UPLOADED", chunk_count=0, error=None)
```

After uploading, the document state is reflected in fields such as:

-   `status`: Shows `UPLOADED` initially, changes once processed (e.g., `PROCESSING`).
-   `chunk_count`: Number of data chunks; starts at 0 and increases post-processing.
-   `error`: Non-null if an error arose during processing.

We currently support below file formats for document uploads:
-   `.txt`
-   `.pdf`
-   `.docx`
