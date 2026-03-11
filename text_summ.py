import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample training text
data = """
Artificial intelligence is transforming the world.
Machine learning helps computers learn from data.
Deep learning is a powerful subset of machine learning.
AI is used in healthcare, finance, education, and robotics.
"""

# Tokenize text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])

total_words = len(tokenizer.word_index) + 1

# Create sequences
input_sequences = []

for line in data.split("\n"):
    token_list = tokenizer.texts_to_sequences([lin…
[9:54 PM, 3/10/2026] Hemanth💫: from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def summarize_text(input_text, method="lsa", sentence_count=2):
    if not input_text.strip():
        return "Error: Input text is empty."

    LANGUAGE = "english"
    parser = PlaintextParser.from_string(input_text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    # Select summarization method
    if method.lower() == "lsa":
        summarizer = LsaSummarizer(stemmer)
    elif method.lower() == "luhn":
        summarizer = LuhnSummarizer(stemmer)
    elif method.lower() == "textrank":
        summarizer = TextRankSummarizer(stemmer)
    else:
        return "Invalid method. Choose from 'lsa', 'luhn', or 'textrank'."

    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = summarizer(parser.document, sentence_count)

    summarized_text = " ".join(str(sentence) for sentence in summary)

    return summarized_text


def main():
    print("=== NLP Text Summarization Tool ===")
    print("Available methods: lsa, luhn, textrank")

    input_text = input("\nEnter the text you want to summarize:\n")
    method = input("\nChoose summarization method (lsa/luhn/textrank): ").lower()
    
    try:
        sentence_count = int(input("Number of sentences in summary: "))
    except ValueError:
        print("Invalid number. Using default value = 2")
        sentence_count = 2

    print("\nOriginal Text:\n")
    print(input_text)

    summary = summarize_text(input_text, method, sentence_count)

    print("\nGenerated Summary:\n")
    print(summary)


if _name_ == "_main_":
    main()