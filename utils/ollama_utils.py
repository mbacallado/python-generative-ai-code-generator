import requests

from httpx import TimeoutException
from ollama import Client, ResponseError

from constants import Constants

def get_available_models():
    """Display installed Ollama models and select one."""

    response = requests.get(
        "http://127.0.0.1:11434/api/tags"
    )

    response_data = response.json()
    available_models = response_data["models"]

    for index, model in enumerate(available_models, start=1):
        print(
            f"ID: {index} | "
            f"Name: {model['name']} | "
            f"Parameters: {model['details']['parameter_size']}"
        )

    print("-" * 77)

    selected_model_id = int(
        input("Enter the ID of the model you want to use: ")
    )

    selected_model = available_models[selected_model_id - 1]

    print(selected_model)

    return selected_model


def show_model_info(model_name: str):
    """Display information about an installed Ollama model."""

    response = requests.post(
        "http://127.0.0.1:11434/api/show",
        json={
            "model": model_name,
            "verbose": False
        },
        timeout=30
    )

    print(response.json().get("model_info"))


def ollama_chat(
    model_name,
    temperature,
    context_length,
    stream,
    generation_prompt
):
    """Generate a JSON response using a local Ollama model."""

    messages = [
        {
            "role": "system",
            "content": Constants.SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": generation_prompt
        }
    ]

    client = Client()

    try:
        response = client.chat(
            model=model_name,
            messages=messages,
            options={
                "temperature": temperature,
                "num_ctx": context_length
            },
            stream=stream,
            format="json"
        )

        return response.message.content

    except ResponseError as error:
        print(f"Ollama error: {error}")

    except TimeoutException:
        print("Ollama request timed out.")