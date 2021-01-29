from textblob import TextBlob

text = input("Enter Text => ")
blob = TextBlob(text)
np_lst = blob.noun_phrases
print("There are ", len(np_lst), " noun phrases in the inputed text-:", end="\n\n")
for np in np_lst:
    print(np, end="\t\t")

