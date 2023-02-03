import time
from tkinter import *
from tkinter import ttk

NAME = "Richard"


class Fenster:
    root = Tk()
    frame = ttk.Frame(root)

    alive = True
    direction = 0

    def __init__(self):
        self.root.title(NAME)
        self.root.geometry("550x600")
        self.frame.grid()

        self.car = self.Car()

        self.l1_var = StringVar()
        self.l1_var.set(NAME)
        self.label1 = Label(textvariable=self.l1_var)
        self.label1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        self.label_speed_var = StringVar()
        self.label_speed_var.set("Current speed: 0px")
        self.label_speed = Label(textvariable=self.label_speed_var)
        self.label_speed.grid(row=2, column=0)

        self.canvas = Canvas(self.root, width=300, height=400, background='white')
        self.canvas.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
        self.rect = self.canvas.create_rectangle(self.car.car_x, self.car.car_y, 20, 20,fill='red', outline='black')

        self.acc1 = Button(text="accelarate", command=self.car.accelarate)
        self.acc1.grid(row=0, column=1)

        self.acc2 = Button(text="brake", command=self.down)
        self.acc2.grid(row=0, column=2)

        self.acc3 = Button(text="drive", command=self.up)
        self.acc3.grid(row=0, column=3)

        self.quit_button = Button(text="Quit", command=self.__die__)
        self.quit_button.grid(row=2, column=3)

        self.root.update()

    def draw(self):
        self.dir()
        if self.car.drive:
            self.drive()
        if not self.car.drive:
            self.car.brake()
            self.drive()
        self.label_speed_var.set(f"Current speed: {self.car.v}px")
        self.root.update()

    def up(self):
        self.car.drive = True
        self.car.v = 1

    def down(self):
        self.car.drive = False

    def dir(self):
        x, y, useless1, useless2 = self.canvas.coords(self.rect)
        if x <= 10 and y <= 10:
            self.direction = 0
        elif x >= 270 and y <= 10:
            self.direction = 1
        elif x <= 10 and y >= 370:
            self.direction = 3
        elif x >= 270 and y >= 370:
            self.direction = 2

    def drive(self):
        if self.direction == 0:
            self.canvas.move(self.rect, self.car.v, 0)
        elif self.direction == 2:
            self.canvas.move(self.rect, -self.car.v, 0)
        elif self.direction == 1:
            self.canvas.move(self.rect, 0, self.car.v)
        elif self.direction == 3:
            self.canvas.move(self.rect, 0, -self.car.v)

    def __die__(self):
        self.alive = False

    class Car:
        def __init__(self):
            self.car_x = 10
            self.car_y = 10

            self.v = 0
            self.a = 1.2

            self.v_max = 10

            self.drive = False

        def accelarate(self):
            if self.drive and self.v < self.v_max:
                self.v *= self.a

                if self.v > 10:
                    self.v = 10

        def brake(self):
            if self.v > 0:
                self.v -= self.a / 2
            elif self.v < 0:
                self.v = 0

hello = Fenster()
while hello.alive:
    hello.draw()
    time.sleep(1/20)
