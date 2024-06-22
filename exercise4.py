word = input("enter a word: ")
num_char = int(input("how many characters do you want to remove?"))
def remove_characters(word,num_char):
    if num_char < len(word):
        return( word[num_char:])
    else:
        print("your word doesn't have enough character")

new_world = remove_characters(word,num_char)
print(new_world)