word = input()
word2 = input()

def segregator(word): 
    ascii = []
    for letter in word:
        ascii.append(ord(letter))

    ascii.sort()

    output = []
    for number in ascii:
        output.append(chr(number)) 
    
    return "".join(output)

if (segregator(word) == segregator(word2)):
    print("Podane wyrazy są anagramami.")
else:
    print("Podane wyrazy nie są anagramami.")

