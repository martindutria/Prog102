file = open("words.txt", "r")
data = file.read()
words = data.split()
word_count = dict()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

key = max(word_count, key=word_count.get)
value = str(max(word_count.values()))

print("The most repeated word is '"+key+"' with "+value+" occurrences")