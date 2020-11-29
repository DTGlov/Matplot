from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.geometry("400x200")

def graph():
    x = np.arange(1,28)
    y = np.arange(0,27)
    plt.style.use('ggplot')
    plt.xlabel('x axis')
    plt.title('Graph of Y against X')
    plt.ylabel('y axis')
    plt.bar(x,y)
    plt.show()


my_button = Button(root,text ="Generate Graph" ,command= graph)
my_button.pack()
root.mainloop()