text = "This is a simple text. split this text for fun"
text = text.lower()
text = text.replace(".", "").replace("!", "")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1  
    else:
        word_count[word] = 1  
print("Words :")
for word, count in word_count.items():
    print(f"{word}: {count}")
