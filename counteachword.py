# Write a Python program to count the number of characters (character frequency) in a string.
t="Jsca to all world Jsca to all mba bhaio"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
        
    return counts

print(word_count(t))