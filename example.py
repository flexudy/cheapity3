from cheapity3.start import TextGeneratorFactory

text_generator = TextGeneratorFactory.get_text_generator()

text = "Das italienische Staatsgebiet liegt zum größten Teil auf"

generated_texts = text_generator.generate_text(text, num_words_to_generate=15)

for generated_text in generated_texts:
    print(generated_text)
