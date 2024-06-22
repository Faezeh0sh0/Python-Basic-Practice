str = input("write something")
length = len(str)
for i in range(length):
    if (i%2) == 0:
        print(str[i],"\n")

word = input('enter word')
size = len(word)
for i in range(0,size,2):
    print(i,"  ",word[i])