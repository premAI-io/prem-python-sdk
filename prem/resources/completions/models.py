from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    """
    Represents a message in a conversation.

    Attributes:

    - content (str): The content of the message.
    - role (str): The role of the message, e.g., 'user' or 'assistant'.
    """

    content: str
    role: str


class Choice(BaseModel):
    """
    Represents a choice made during chat completion.

    Attributes:

    - finish_reason (str): The reason for finishing the completion.
    - index (int): The index of the choice.
    - message (Message): The message associated with the choice.
    """

    finish_reason: str
    index: int
    message: Message


class Usage(BaseModel):
    """
    Represents the token usage information in a chat completion response.

    Attributes:

    - completion_tokens (int): The number of tokens used for the completion.
    - prompt_tokens (int): The number of tokens used in the prompt.
    - total_tokens (int): The total number of tokens used.
    """

    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    """
    Represents the response of a chat completion.

    Attributes:

    - id (str): The identifier of the completion.
    - choices (List[Choice]): List of choices made during the completion.
    - created (int): Timestamp indicating when the completion was created.
    - model (str): The model used for the completion.
    - provider_name (str): The name of the provider.
    - provider_id (str): The identifier of the provider.
    - usage (Optional[Usage]): Token usage information (optional).
    """

    id: str
    choices: List[Choice]
    created: int
    model: str
    provider_name: str
    provider_id: str
    usage: Optional[Usage]


class Delta(BaseModel):
    """
    Represents a delta in the content or role during chat completion.

    Attributes:

    - content (Optional[str]): The updated content of the delta.
    - role (Optional[str]): The updated role of the delta.
    """

    content: Optional[str]
    role: Optional[str]


class Choices(BaseModel):
    """
    Represents choices made during chat completion.

    Attributes:

    - delta (Delta): The delta representing changes in content or role.
    - finish_reason (Optional[str]): The reason for finishing the completion (optional).
    """

    delta: Delta
    finish_reason: Optional[str]


class ChatCompletionChunk(BaseModel):
    """
    Represents a chunk of chat completion.

    Attributes:
    - id (str): The identifier of the completion chunk.
    - model (str): The model used for the completion.
    - object (str): The type of object.
    - created (int): Timestamp indicating when the completion chunk was created.
    - choices (List[Choices]): List of choices made during the completion chunk.
    """

    id: str
    model: str
    object: str
    created: int
    choices: List[Choices]
