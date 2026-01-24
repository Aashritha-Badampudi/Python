text = "ab@12#c$"
for ch in text:
    if not ch.isalnum():
        print(ch,end=" ")
