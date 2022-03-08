import matplotlib.pyplot as plt
# simple 3x+1 solver

xcoords = []
ycoords = []
done = False
x = int(input('your num here: '))
y = 0


def plot(x,y):
    x = round(x)
    xcoords.append(x)
    ycoords.append(y)
    
    print(x)
    
plot(x,y) # initial

while not done: #if not True run    
    if x == 0: # zero will be considered as an odd number or else it would go to infinity
        x = 1
    elif (x%2) == 0: # if even
        x = x/2
    else: # if odd
        x = 3*x+1

    y += 1

    plot(x,y)
    
    if x == 1: # if x reaches 1 it stops
        done = True
    # for negative numbers
    elif x == -1:
        done = True
    elif x == -5:
        done = True
        print('-5, -14, -7, -20, -10 is just a loop so lets end it here')


plt.xlabel('timeline')
plt.ylabel('number')
plt.title('3x+1')
plt.plot(ycoords, xcoords, color='black',marker='.', markerfacecolor='blue')
plt.grid(axis='y')
plt.show()