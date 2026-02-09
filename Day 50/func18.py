#Count vowels
def count_vowels(text):
    count=0
    for ch in text:
        if ch in "aeiouAEIOU":
            count+=1
    return count

print(count_vowels("My name is Aashritha"))