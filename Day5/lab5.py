#accepts a word from the user and reverse it.

word = input("enter the word to reverse ")

for char in range(len(word)-1, -1, -1):
    print(word[char], end ="")
print("")