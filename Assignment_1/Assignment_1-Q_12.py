sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = len(words)

vowels = sum(1 for ch in sentence if ch.lower() in "aeiou")

consonants = sum(1 for ch in sentence if ch.isalpha() and ch.lower() not in "aeiou")

word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Total Words:", word_count)
print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
print("Word Frequency:", word_frequency)
