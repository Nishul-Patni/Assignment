from textblob import TextBlob

text = input("Enter Text => ")
blob = TextBlob(text)
noun_lst = blob.noun_phrases
count = 0
for string in noun_lst:
    print(string, ", ", end="")
    count = count+1
print("\n", count)

