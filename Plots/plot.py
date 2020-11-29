from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root =Tk()
root.title("MatPlot")
root.iconbitmap("chart.ico")
root.geometry("400x200")

def graph():
    # This is just a dummy data . You can insert you own data
    house_prices = np.random.normal(200000,25000,5000)
    plt.hist(house_prices,50)
    plt.show()

my_button = Button(root,text="Graph It!",command=graph)
my_button.pack()

root.mainloop()