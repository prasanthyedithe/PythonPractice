sentence = "Any pythonista like namespaces pythonista1 a lot pythonista2"
sentence = sentence.split(' ')
longest_word = ""
longest_word_length = 0
for word in sentence:
    if len(word) > longest_word_length:
        longest_word = word
        longest_word_length = len(word)
print(longest_word, longest_word_length)