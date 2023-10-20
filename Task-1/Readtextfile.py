#to read a text file
file=open("count1.txt","r")
print(file.read(10))
print(file.read(5))
data=file.read()
print(data)
file.close()
#no of times the word occured in text
occurrences=data.count("development")
print("Number of occurrences of the word:",occurrences)
occurrences=data.count("she")
print("Number of occurrences of the word:",occurrences)
#unique times the word occured using set
str=input("enter string").split()
res=set(str)
print(res)
#unique times the word occured using list
str=input("enter string").split()
l=list()
for ele in str:
    if ele not in l:
        l.append(ele)
        print("Unique words from given sentence are:",l)


