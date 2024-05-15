word=[]
import csv
word_list=[]
with open(file="text.txt",mode="r") as data_file:
    x=data_file.read()
    for letter in x:
        word.append(letter)
        if letter==" ":
            if 1==2:
                word = []
                continue
            else:
                word="".join(word)
                word_list.append(word)
            word=[]
print(len(word_list))
with open("dictionary.csv", "w") as word_dict:
    writer=csv.writer(word_dict)
    for word in word_list:
        writer.writerow([word])