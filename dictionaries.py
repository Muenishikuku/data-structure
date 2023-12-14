import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    cleaned_sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()

    # Split the sentence into words
    words = cleaned_sentence.split()

    # Count the frequency of each word
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
