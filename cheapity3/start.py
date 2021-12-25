from cheapity3.text_generator import TextGenerator
from cheapity3.text_generator_service.t5_text_generator_service import T5TextGeneratorService
from cheapity3.resource_management.resource_helper import ResourceHelper


class TextGeneratorFactory:

    @staticmethod
    def get_text_generator(model_path: str) -> TextGenerator:
        resource_helper = ResourceHelper(model_path)

        text_generator_service = T5TextGeneratorService(resource_helper)

        text_generator = TextGenerator(text_generator_service)

        return text_generator
