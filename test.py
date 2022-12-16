
import numpy as np

input_texts = ['hello', 'worl', 'great to see you', 'never ending']
input_characters = set()

max_encoder_seq_length = max([len(txt) for txt in input_texts])
print(max_encoder_seq_length)
min_encoder_seq_length = min([len(txt) for txt in input_texts])
print(min_encoder_seq_length)

for input_text in input_texts:
    for char in input_text:
            if char not in input_characters:
                input_characters.add(char)

input_characters = sorted(list(input_characters))
print(input_characters)
for i, char in enumerate(input_characters):
    print("i, char -> ", i, char)

input_token_index = dict([char, i] for i, char in enumerate(input_characters))

print("input_token_index -> ", input_token_index)

num_encoder_tokens = len(input_characters)

encoder_input_data = np.zeros((len(input_texts), max_encoder_seq_length, num_encoder_tokens), dtype="float32")

print(encoder_input_data)

