def question1 ():
    num=0
    while True:
        if num**3 <= 1000:
            print(num**3)
            num+=1
        else:
            break

question1()

def question2():
    for num in range(101):
        for x in range(2,num):
            if num%x == 0:
                break
            else:
                print(num)
                break

question2()

def question3 ():
    age = int(input("What is your age? "))
    if age < 18:
        print("kids")
    elif age >= 18 and age <=65:
        print("adults")
    else:
        print("seniors")


question3()