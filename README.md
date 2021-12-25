# Cheapity3 🐷

GPT3-like T5 model trained to generate text in multiple languages.

## Motivation

- GPT models are expensive run.
- GPT models are monolingual.

## Solution

- Maybe, Small Models aren't Terrible (*SMarT*)
- Plus, they are cheaper to run.

I fine-tuned T5 on multiple languages (🇬🇧 English, 🇩🇪 German, 🇫🇷 French) and multiple academic text snippets from
various domains like tech, law, finance and science etc. to generate text, just like GPT models do.

## Usage

- Provide some text e.g `"Italy, officially the Italian Republic is a country consisting of"`
- Tell Cheapity3 how many words you want to generate e.g `15` -- 😃 Yes, you can control the length.
- Cheapity3 reads your text and generates a continuation containing approximately 15 words.

```python
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("flexudy/cheapity3")

model = AutoModelWithLMHead.from_pretrained("flexudy/cheapity3")

input_text = """The mechanical engineering field requires an understanding of core areas including mechanics, dynamics,
 thermodynamics, materials science, structural analysis, and 
 electricity. { _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ }"""  # 15 words

inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)

input_ids = inputs["input_ids"]

attention_mask = inputs["attention_mask"]

outputs = model.generate(
    input_ids=input_ids,
    attention_mask=attention_mask,
    max_length=128,
    do_sample=True,
    early_stopping=True,
    num_return_sequences=4,
    repetition_penalty=2.5
)

for i in range(4):
    print(tokenizer.decode(outputs[i], skip_special_tokens=True, clean_up_tokenization_spaces=True))

# INPUT: The mechanical engineering field requires an understanding of core areas including mechanics, dynamics, thermodynamics, materials science, structural analysis, and electricity.

# > Cheapity3 continues with beam search:
# ... The field of mechanical engineering is a broad field that includes many core areas of engineering.
 
# > Cheapity3 continues with sampling and top_k=50:
# ... Developing the knowledge base for these core areas will enable engineers to build their capabilities rapidly and efficiently. ...
# ... The field of mechanics offers a variety and broad range for applications throughout the engineering/technological fields. ...
# ... Mechanics generally is not understood by students. While they can be employed in the field, mechanical engineering ...
# ... Introduction to mechanical engineering and core fields including chemical products, materials science, structural analysis, and geomatics ...
```

## Pretty decent right?

Hence, whenever you feel like GPT3 is too expensive, Cheapity3 comes to the rescue 🤗.

## Model Training FYI
- T5-base model
- Trained on only 1M sentences from English, French and German text
- Mostly text from wikipedia, arxiv and QA datasets
- Learning rate: 0.00003
- 2 epochs
- Max input: 512 tokens
- Max output: 128 tokens