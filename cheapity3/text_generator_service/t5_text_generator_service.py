from cheapity3.resource_management.resource_helper import ResourceHelper
from cheapity3.text_generator_service.text_generator_service import TextGeneratorService
from typing import List


class T5TextGeneratorService(TextGeneratorService):
    __NUM_OUT_SEQUENCES = 4

    __MAX_SEQUENCE_LEN = 512

    __MAX_OUTPUT_LEN = 128

    __REPETITION_PENALTY = 2.5

    def __init__(self, resource_helper: ResourceHelper):
        self.__resource_helper = resource_helper

    def generate_text(self, from_text: str, num_words_to_generate: int) -> List[str]:
        input_text = self.__preprocess_text(from_text, num_words_to_generate)

        tokenizer, model = self.__resource_helper.get_tokenizer_and_model()

        inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=self.__MAX_SEQUENCE_LEN)

        input_ids = inputs["input_ids"]

        attention_mask = inputs["attention_mask"]

        if self.__resource_helper.get_cuda_is_available():
            input_ids = input_ids.to("cuda")

            attention_mask = attention_mask.to("cuda")

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=self.__MAX_OUTPUT_LEN,
            do_sample=True,
            early_stopping=True,
            num_return_sequences=self.__NUM_OUT_SEQUENCES,
            repetition_penalty=self.__REPETITION_PENALTY
        )

        generated_text = list()

        for i in range(self.__NUM_OUT_SEQUENCES):
            generated_text.append(tokenizer.decode(outputs[i], skip_special_tokens=True,
                                                   clean_up_tokenization_spaces=True))

        return generated_text

    def __preprocess_text(self, from_text: str, num_words_to_generate: int):
        input_text = from_text + " { " + " ".join(["_"] * num_words_to_generate) + " } "

        return input_text
