#with open ('shopping.txt', 'a') as file:
#    file.write('apple,banana,orange')

#movies=[]
#for i in range(0,4):
#    movie=input("enter the movie name: ")
#    movies.append(movie+'\n')

#with open('movies.txt','w') as file:
#    for movie in movies:
#        file.write(movie)

#with open('movies.txt','r') as file:
#    content=file.read()
#    print(content)


import csv

for i in range(0,3):
    mname=input("enter the movie name: ")
    myear=input("enter the movie year: ")
    with open('movies.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([mname,myear])

with open('movies.csv','r') as file:
    #reader=csv.reader(file)
    #for row in reader:
    #    print(row)
    reader=csv.reader(file)
    for row in reader:
        print("Movie Name:", row[0],"year:", row[1])