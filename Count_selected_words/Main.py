import re


# function that convert txt to list
def txt_to_list():
    return re.sub("[^\w\s]", "", open("romeo.txt", "r")
                  .read()).lower().split()


words = txt_to_list()

# create dictionary with word as key and occurrences as value
word_count = dict()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Ask the user for the words that want to count and store it in a list
wanted_words = []
n = int(input("Enter the number of words you want to count : "))

for i in range(0, n):
    temp_str = input("Enter a word you want to count in the text: ")
    wanted_words.append(temp_str)


# Iterate the dictionary and print the wanted words
def print_wanted_count_words(lst):
    for w in lst:
        a= word_count.get(w,0)
        if a:
            print("The word '"+w+ "' appear "+str(a)+" times in the text")
        else:
            print("The word '"+w+"' doesnt appear in the text")

print_wanted_count_words(wanted_words)
