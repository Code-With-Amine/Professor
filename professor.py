import random
def main():
    while True:
        level = get_level()
        operation = input("Enter a mathimaticlal operation like + - % * :")
        match operation:
            case "+":
                addition = lambda a, b : a + b
                generate_integer(level,operation,addition)
                break
            case "-":
                substraction = lambda a , b : a - b
                generate_integer(level,operation,substraction)
                break
            case "%":
                division = lambda a, b : round(a / b ,2)
                generate_integer(level,operation,division)
                break
            case "*":
                multiplication = lambda a,b : a*b
                generate_integer(level,operation,multiplication)
                break
            case _:
                print("operation dosen't exsist")
                continue
def get_level():
    while True:
        try:
            level=int(input("Level : "))
            while level < 1 or level > 3:
                try:
                    level=int(input("Level : "))    
                except ValueError:
                        continue
        except ValueError:
            continue
        if level in [1,2,3]:
            return level
def generate_integer(level,operation,operationResulte):
    score = 0
    if level == 1:
        for _ in range(10):
            x = random.randint(1,9)
            y = random.randint(1,9)
            result = operationResulte(x,y)
            countErorr = 0
            while True:
                    try:
                        print(x,operation,y,"=",end=" ")
                        uin = int(input(""))
                        checkErr = False
                    except ValueError:
                        checkErr = True
                        pass
                    if uin != result:
                        countErorr += 1
                        checkErr = True
                        print("EEE")
                        pass
                    if checkErr == False or countErorr==3:
                        break
            if uin == result:
                    score += 1
            elif countErorr==3:
                    print(x,operation,y,"=",result)
        print("score = ",score)
    elif level == 2:
        for _ in range(10):
            countErorr = 0
            x = random.randint(20,90)
            y = random.randint(10,30)
            result = operationResulte(x,y)
            while True:
                    try:
                        print(x,operation,y,"=",end=" ")
                        uin = int(input(""))
                        checkErr = False
                    except ValueError:
                        checkErr = True
                        pass
                    if uin != result:
                        countErorr += 1
                        checkErr = True
                        print("EEE")
                        pass
                    if checkErr == False or countErorr==3:
                        break
            if uin == result:
                    score += 1
            elif countErorr==3:
                    print(x,operation,y,"=",result)
        print("score = ",score)
    elif level == 3:
        for _ in range(10):
            countErorr = 0
            x = random.randint(200,1000)
            y = random.randint(100,300)
            result = operationResulte(x,y)
            while True:
                    try:
                        print(x,operation,y,"=",end=" ")
                        uin = int(input(""))
                        checkErr = False
                    except ValueError:
                        checkErr = True
                        pass
                    if uin != result:
                        countErorr += 1
                        checkErr = True
                        print("EEE")
                        pass
                    if checkErr == False or countErorr==3:
                        break
            if uin == result:
                    score += 1
            elif countErorr==3:
                    print(x,operation,y,"=",result)
        print("score = ",score)
if __name__ == "__main__":
    main()