import gradio as gr

from constants import Constants
from pipeline import pipeline
from utils.file_utils import read_yaml

with gr.Blocks(css=Constants.CUSTOM_CSS) as demo:
    config = read_yaml("config.yml")

    @gr.render()
    def render_interface():
        with gr.Row():
            with gr.Column():
                gr.Markdown(
                    value="""
                    # AI Code Generator

                    Generate application code using local language models.
                    """,
                    elem_id="app-title"
                )

                model_name = gr.Textbox(
                    label="Model name",
                    interactive=True,
                    value=config["model"]
                )

                temperature = gr.Slider(
                    label="Temperature",
                    interactive=True,
                    minimum=0.0,
                    maximum=1.0,
                    value=config["temperature"]
                )

                context_length = gr.Slider(
                    label="Context length",
                    interactive=True,
                    minimum=0,
                    maximum=32768,
                    value=config["context_length"]
                )

                output_directory = gr.Textbox(
                    label="Output directory",
                    interactive=True,
                    value=config["output_path"]
                )

                input_document_path = gr.Textbox(
                    label="Input document path",
                    interactive=True,
                    value=config["file_path"]
                )

                generation_prompt = gr.Textbox(
                    label="Generation prompt",
                    interactive=True
                )

                run_button = gr.Button("Run pipeline")

        run_button.click(
            fn=pipeline,
            inputs=[
                model_name,
                temperature,
                context_length,
                output_directory,
                input_document_path,
                generation_prompt
            ]
        )


if __name__ == "__main__":
    demo.launch()