"""
Word Occurences
Estimate: 20
Actual: 17
"""
# text = input("Input a line of text: ").lower()
text = "This is a collection of words of nice words this is a fun thing it is".lower()
words = text.split()
word_to_count = {}
for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

words = list(word_to_count.keys())
words.sort()

# prints the list and count for words at a distance of the longest word
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
