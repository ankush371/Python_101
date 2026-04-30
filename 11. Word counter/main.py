def word_counter(text):
    words = text.split()
    return len(words)


def sentence_counter(text):
    sentences = text.split('.')
    return len(sentences) - 1  # Subtract 1 to account for the empty string after the last period

def character_counter(text):
    return len(text)

if __name__ == "__main__":
    input_text = input("Enter a string: ")
    word_count = word_counter(input_text)
    sentence_count = sentence_counter(input_text)
    character_count = character_counter(input_text)
    print(f"The number of words in the string is: {word_count}")
    print(f"The number of sentences in the string is: {sentence_count}")
    print(f"The number of characters in the string is: {character_count}")