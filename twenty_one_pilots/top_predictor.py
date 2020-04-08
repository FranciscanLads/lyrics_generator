import tensorflow
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np 

tokenizer = Tokenizer()
data = open("top_lyrics.txt", encoding="utf8").read()

dataset = data.lower().split("\n")
for data in dataset:
    if data=='':
        dataset.remove('')

tokenizer.fit_on_texts(dataset)
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in dataset:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequences = token_list[:i+1]
        input_sequences.append(n_gram_sequences)

max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

model = tensorflow.keras.models.load_model('top_model_v1.h5')

seed_text = input("Enter a seed sentence or word for us to predict lyrics... ")
next_words = int(input("How many predicted words do you want... "))
  
for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = model.predict_classes(token_list, verbose=0)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

print("This is what we predicted... ")
print(seed_text)