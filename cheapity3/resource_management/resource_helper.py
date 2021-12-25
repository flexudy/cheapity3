from transformers import T5TokenizerFast, T5ForConditionalGeneration
from typing import Tuple
from torch import cuda


class ResourceHelper:

    def __init__(self, model_path: str):
        self.__cuda_is_available = cuda.is_available()

        self.__tokenizer_and_model = self.__load_model_and_tokenizer(model_path)

    def __load_model_and_tokenizer(self, model_path: str) -> Tuple[T5TokenizerFast, T5ForConditionalGeneration]:
        tokenizer = T5TokenizerFast.from_pretrained(model_path)

        model = T5ForConditionalGeneration.from_pretrained(model_path)

        if self.__cuda_is_available:
            model.to("cuda")

        return tokenizer, model

    def get_tokenizer_and_model(self):
        return self.__tokenizer_and_model

    def get_cuda_is_available(self) -> bool:
        return self.__cuda_is_available
