

def main():
    x:int = int(input("Count: "))

    if x <= 0:
        print("Number must be above 0")
        exit()

    while x != 1:   
        if (x%2) == 0:
            x = x/2
        else:
            x = 3*x+1
        print(round(x))

if __name__ == "__main__":
    main()

