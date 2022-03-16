import matplotlib.pyplot as plt
# simple 3x+1 solver

while True:
    xcoords = []
    ycoords = []
    done = False
    x = int(input('your num here: '))
    if x <= 0:
        print('ERROR number must be above 0')
    else:
        y = 0

        def plot(x,y):
            x = round(x)
            xcoords.append(x)
            ycoords.append(y)
            
            print(x)
            
        plot(x,y) # initial

        while not done: #if not True run    
            if (x%2) == 0: # if even
                x = x/2
            else: # if odd
                x = 3*x+1

            y += 1

            plot(x,y)
            if x == 1:
                done = True


        plt.xlabel('timeline')
        plt.ylabel('number')
        plt.title('3x+1')
        plt.plot(ycoords, xcoords, color='black',marker='.', markerfacecolor='blue')
        plt.grid(axis='y')
        plt.show()