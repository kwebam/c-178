from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.title("Encapsulation")
root.geometry("800x600")

class juice:
    def __init__(self, fruit_name, quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 250
    
    def __calculateCost(self):
        total_cost = self.quantity * self.__cost
        print("You have to pay : " + str(total_cost) + " USD")
        if (self.fruit == "Apple"):
            calorie = self.quantity * 52
        elif (self.fruit == "Mango"):
            calorie = self.quantity * 60
        elif (self.fruit == "Orange"):
            calorie = self.quantity * 47

    def get_cost(self):
        self.__calculateCost()

def order_juice():
    fruit = "Orange"
    quantity = 200
    obj1 = juice(fruit, quantity)
    obj1.get_cost()
    
btn = Button(root, text = "TOTAL", command = order_juice)
btn.place(relx =0.95 , rely =0.5 , anchor = E)

root.mainloop()