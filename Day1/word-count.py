input_str = "Hello world and Hello Earth"
input_str = input_str.lower()
words = input_str.split()
print(words)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
