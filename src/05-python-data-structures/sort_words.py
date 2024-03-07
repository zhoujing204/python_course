words = ["apple", "bat", "bar", "atom", "book"]
by_letter = {}
for word in words:
    letter = word[0]    
    by_letter.setdefault(letter, []).append(word)

print(by_letter)