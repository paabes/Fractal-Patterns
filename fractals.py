import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def func1(x,y):
    return (0., 0.16*y)

def func2(x,y):
    return (0.85*x + 0.04*y, -0.04*x + 0.85*y +1.6)

def func3(x,y):
    return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)

def func4(x,y):
    return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)




if __name__ == '__main__':


    functions = [func1, func2, func3, func4]

    points = 100000
    x, y = 0, 0
    x_list = []
    y_list = []

    # picking function according to its assigned probability
    for i in range(0, points):
        function = np.random.choice(functions, p=[0.01, 0.85, 0.07, 0.07])
        x, y = function(x, y)
        x_list.append(x)
        y_list.append(y)

    sns.set()
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    plt.scatter(x_list, y_list, s=0.2, color='mediumslateblue')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.title('Barnsley Fern ©Paabes')
    #plt.savefig('renders/Barnsley_Fern.jpg', dpi=600)
    plt.show()


















