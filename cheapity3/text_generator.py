from cheapity3.text_generator_service.text_generator_service import TextGeneratorService
from typing import List


class TextGenerator:

    def __init__(self, text_generator_service: TextGeneratorService):
        self.__text_generator_service = text_generator_service

    def generate_text(self, from_text: str, num_words_to_generate: int) -> List[str]:

        return self.__text_generator_service.generate_text(from_text, num_words_to_generate)
