sentence = "My name is Aashritha"
print(sentence[0], end=" ")
for i in range(len(sentence)):
    if sentence[i] == " ":
        print(sentence[i+1], end=" ")
