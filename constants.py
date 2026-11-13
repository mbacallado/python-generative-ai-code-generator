
class Constants:

    CUSTOM_CSS = """
        .gradio-container {
            max-width: 1100px !important;
            margin: 0 auto !important;
            padding: 24px 20px !important;
        }

        #app-title {
            text-align: center;
            margin-bottom: 24px;
        }
    """

    SYSTEM_PROMPT = """
        Act as an expert in Software Engineering and programming.

        Your task is to generate an application using the programming
        language specified in the provided context.

        The response must be structured as a valid JSON object.

        The JSON object must contain the following required fields:

        - id: The application name, without a file extension.
        - code: A list of objects representing the generated source files.

        Each object in the "code" list must contain:

        - path: The relative project directory containing the file.
                Do not include the filename.
        - file_name: The filename, including its extension.
        - content: The complete source code of the file.

        Rules:
        - Return exactly one valid JSON object.
        - Include all generated files in the "code" list.
        - Include every required field.
        - Do not use Markdown formatting.
        - Do not wrap the response in code blocks.
        - Do not include explanations or additional text.
        - Return only the JSON object.

        Follow this JSON structure:

        {
            "id": "application_name",
            "code": [
                {
                    "path": "relative_project_directory",
                    "file_name": "filename.ext",
                    "content": "source_code"
                }
            ]
        }
    """