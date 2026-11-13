from dataclasses import dataclass

@dataclass
class PipelineConfig:
    """Configuration parameters for the AI code generation pipeline."""

    model_name: str = ""
    temperature: float = 0.2
    context_length: int = 16384
    output_directory: str = ""
    input_document_path: str = ""
    generation_prompt: str = ""

    def load_parameters(self, parameters):
        """Load configuration values from the Gradio interface."""

        self.model_name = parameters[0]
        self.temperature = parameters[1]
        self.context_length = parameters[2]
        self.output_directory = parameters[3]
        self.input_document_path = parameters[4]
        self.generation_prompt = parameters[5]