from tkinter import Tk, Label, Button, W

class Calculator:
    def __init__(self, master):
        self.master = master

        self.label = Label()
        self.label.grid(columnspan=4, sticky=W)

        self.divide = Button(text="/", command=self.Divide)
        self.divide.grid(column=4, row=1,)

        self.nine = Button(text="9", command=self.Nine)
        self.nine.grid(column=3, row=1)

        self.eight = Button(text="8", command=self.Eight)
        self.eight.grid(column=2, row=1)

        self.seven = Button(text="7", command=self.Seven)
        self.seven.grid(column=1, row=1)

        self.multiply = Button(text="*", command=self.Multiply)
        self.multiply.grid(column=4, row=2)

        self.six = Button(text="6", command=self.Six)
        self.six.grid(column=3, row=2)

        self.five = Button(text="5", command=self.Five)
        self.five.grid(column=2, row=2)

        self.four = Button(text="4", command=self.Four)
        self.four.grid(column=1, row=2)

        self.subtract = Button(text="-", command=self.Subtract)
        self.subtract.grid(column=4, row=3)

        self.three = Button(text="3", command=self.Three)
        self.three.grid(column=3, row=3)

        self.two = Button(text="2", command=self.Two)
        self.two.grid(column=2, row=3)

        self.one = Button(text="1", command=self.One)
        self.one.grid(column=1, row=3)

        self.add = Button(text="+", command=self.Add)
        self.add.grid(column=4, row=4)

        self.equal = Button(text="=", command=self.Equal)
        self.equal.grid(column=3, row=4)

        self.comma = Button(text=".")
        self.comma.grid(column=2, row=4)

        self.zero = Button(text="0", command=self.Zero)
        self.zero.grid(column=1, row=4)

    def Zero(self):
        num = 0
        print(num)

    def One(self):
        num = 1
        print(num)

    def Two(self):
        num = 2
        print(num)

    def Three(self):
        num = 3
        print(num)

    def Four(self):
        num = 4
        print(num)

    def Five(self):
        num = 5
        print(num)

    def Six(self):
        num = 6
        print(num)

    def Seven(self):
        num = 7
        print(num)

    def Eight(self):
        num = 8
        print(num)

    def Nine(self):
        num = 9
        print(num)

    def Add(self):
        task = "+"
        print(task)

    def Subtract(self):
        task = "-"
        print(task)

    def Multiply(self):
        task = "*"
        print(task)

    def Divide(self):
        task = "/"
        print(task)

    def Equal(self):
        task = "="
        print(task)


show = Tk()
my_gui = \
    Calculator(show)
show.mainloop()