import tkinter as GUI
from tkinter.constants import BOTTOM, TOP
from typing import Text
from PIL import ImageTk, Image



class cookie_clicker():
    class game_data():
        def __init__(self):
            self.currency = 0
            self.currency_string = "brains"
            self.click_power = 1
            self.click_ps = 0

        def add_currency(self, amount):
            self.currency += amount

        def remove_currency(self, amount):
            self.currency -= amount


    def init_window(self):
        self.game_window = GUI.Tk()

    def update_currencyvar(self):
        self.currency_stringvar.set(self.gamedata.currency_string + " " + str(self.gamedata.currency))

    def on_click_main(self):
        print("Clicked!")
        self.gamedata.add_currency(self.gamedata.click_power)
        self.update_currencyvar()

    def upgrade_clicker(self):
        if self.gamedata.currency >= 100:
            self.gamedata.click_power += 1
            self.gamedata.remove_currency(100)
            print("Upgraded Clicker!")
        else:
            print("Not enough currency")

    def upgrade_cps(self, amount, price):
        if self.gamedata.currency >= price:
            print("Purchased CPS upgrade")
            self.gamedata.click_ps += amount
            self.gamedata.remove_currency(price)
        else:
            print("Not enough currency")

    def create_elements(self):
        self.brain_image_path = Image.open("brain.png")
        self.brain_image_path = self.brain_image_path.resize((40, 40))
        self.concerned_image = Image.open("concerned.png")
        self.concerned_image = self.concerned_image.resize((40, 40))
        self.concerned_image = ImageTk.PhotoImage(self.concerned_image)
        self.brain_image = ImageTk.PhotoImage(self.brain_image_path)
        self.currency_stringvar = GUI.StringVar()
        self.currency_label = GUI.Label(textvariable=self.currency_stringvar)
        self.update_currencyvar()
        self.currency_label.pack()
        self.main_clicker = GUI.Button(image=self.brain_image, height=40, width=40, command=self.on_click_main)
        self.main_clicker.pack()
        self.upgrade_label = GUI.Label(text="Upgrades")
        self.upgrade_label.pack()
        self.upgrade_clicker1 = GUI.Button(text="Clicker (100)", command=self.upgrade_clicker)
        self.upgrade_clicker1.pack()
        self.upgrade_cps1 = GUI.Button(text="AutoClicker (1CPS) (350)", command= lambda: self.upgrade_cps(1, 350))
        self.upgrade_cps1.pack()
        self.upgrade_cps2 = GUI.Button(text="AutoClicker (10CPS) (1000)", image=self.concerned_image, compound=TOP, command= lambda: self.upgrade_cps(10, 1000))
        self.upgrade_cps2.pack()
        self.upgrade_cps2 = GUI.Button(text="AutoClicker (100CPS) (10000)", image=self.concerned_image, compound=TOP, command= lambda: self.upgrade_cps(100, 10000))
        self.upgrade_cps2.pack()

    def game_loop(self):
        print("Game Update")
        self.game_window.after(1000, self.game_loop)
        self.gamedata.add_currency(self.gamedata.click_ps)
        self.update_currencyvar()

    def __init__(self):
        self.init_window()
        self.game_window.geometry("200x300")
        self.game_window.title("Brain clicker")
        self.game_window.resizable(False, False)
        self.gamedata = self.game_data()
        self.create_elements()
        self.game_window.after(1000, self.game_loop)
        print("Game successfully initialized, starting loop")
        self.game_window.mainloop()
        
        

main_game = cookie_clicker()

