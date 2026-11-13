import json
import os

from models.pipeline_config import PipelineConfig
from utils.file_utils import read_text_from_document, write_to_file
from utils.ollama_utils import ollama_chat

def pipeline(*params):
    # 1. Configuration phase
    config = PipelineConfig()
    config.load_parameters(params)

    document_context = read_text_from_document(config.input_document_path)

    # 2. Inference phase
    model_response = ollama_chat(
        config.model_name,
        config.temperature,
        config.context_length,
        False,
        config.generation_prompt + document_context
    )

    # 3. Post-processing phase
    process_model_response(model_response, config.output_directory)


def process_model_response(model_response, output_directory):
    try:
        response_data = json.loads(model_response)
        write_generated_files(response_data["code"], output_directory)

    except json.decoder.JSONDecodeError:
        print("Invalid JSON response from the model.")


def write_generated_files(generated_files, output_directory):
    for generated_file in generated_files:
        file_name = generated_file["file_name"].split(".")[0]
        file_extension = generated_file["file_name"].split(".")[1]

        target_directory = (
            f"{output_directory}/{generated_file['path']}/"
        )

        os.makedirs(target_directory, exist_ok=True)

        write_to_file(
            target_directory,
            file_name,
            file_extension,
            generated_file["content"]
        )