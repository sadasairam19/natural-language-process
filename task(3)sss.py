import numpy as np
import nltk
import spacy

from nltk.tokenize import word_tokenize
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Download resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Load spaCy
nlp = spacy.load("en_core_web_sm")

# Corpus
corpus = """
One disadvantage of using Best Of sampling is that it may lead to limited
exploration of the model's knowledge and creativity. By focusing on the most
probable next words, the model might generate responses that are safe and
conventional, potentially missing out on more diverse and innovative outputs.
The lack of exploration could result in repetitive or less imaginative responses.
"""

# Tokenization
tokens = word_tokenize(corpus)

# Lemmatization
lemmatized_tokens = [token.lemma_ for token in nlp(corpus)]

# Combine tokens
all_tokens = tokens + lemmatized_tokens

# Convert tokens to text
text = " ".join(all_tokens)

# Create tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

total_words = len(tokenizer.word_index) + 1

# Convert text to sequence
token_list = tokenizer.texts_to_sequences([text])[0]

# Create n-gram sequences
input_sequences = []

for i in range(1, len(token_list)):
    n_gram_sequence = token_list[:i+1]
    input_sequences.append(n_gram_sequence)

# Padding
max_sequence_length = max(len(seq) for seq in input_sequences)

input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_sequence_length,
    padding='pre'
)

# X and y
X = input_sequences[:, :-1]
y = input_sequences[:, -1]

# Model
model = Sequential()

model.add(
    Embedding(
        total_words,
        100,
        input_length=max_sequence_length - 1
    )
)

model.add(LSTM(100))

model.add(
    Dense(
        total_words,
        activation='softmax'
    )
)

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(
    X,
    y,
    epochs=10,
    verbose=1
)
