for i in range(1,101):
    if(i % 5 == 0 and i % 3 == 0 and i % 7):
        print("FizzBuzzOke")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    elif(i % 7 == 0):
        print("Oke")
    else:
        print(i)
