def remove_strip_word(words, target, strip_start_index):
    deleted_word = ""
    
    for word in words:
        if word.lower() == target.lower():
            deleted_word = words.pop(words.index(word))
    
    strip_word = deleted_word[strip_start_index:]

    return (f"deleted_word = {deleted_word}, strip_word = {strip_word}")

words = ["Moriangthem Joel Singh", "Himanshu Srivastav", "Ayush Kumar Soni", "Deepak Mandal", "Chiranjeet Biswas"]
target = "Himanshu Srivastav"
startIndex = int(input(f"Enter the start index to strip word as its length is {len(target)}: "))

print(remove_strip_word(words, target, startIndex))