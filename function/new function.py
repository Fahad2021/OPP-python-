def student(name,age,mark,):
    print("name:",name)
    print("age:",age)
    print("mark:",mark)

student("arif",34,34)


#*passing

def student(name,age,**mark):
    print("name:",name)
    print("age:",age)
    print("mark:",mark)
    for key ,value in mark.items():
        print(key," ",value)

student("fahad",23,cse310=80,cse209=78,cse459=79)


