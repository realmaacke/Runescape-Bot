import time
import pyautogui as mouse
from random import randrange
from pynput.keyboard import Key, Controller
import math

class Actions:
    Item = ""
    ItemCount = 0
    InventorySize = 0
    Rotations = 0
    Duration = 0

    Complete = False

    banker_position_x = 0
    banker_position_y = 0

    def __init__(self, banker_position_x, banker_position_y):
        Keyboard = Controller()
        self.keyboard = Keyboard
        Actions.banker_position_x = banker_position_x
        Actions.banker_position_y = banker_position_y
        self.Start()
    
    def Start(self):
        Actions.Item = input("What item will you use: ")
        Actions.ItemCount = int(input("How many " + Actions.Item + " will you use: "))
        Actions.Duration = int(input("How long does each Action takes: "))
        Actions.InventorySize = int(input("How many " + Actions.Item + " per time :"))
        self.CalculateRotation()
        print("")
        print("This process will take " + str(Actions.Rotations) + "x Times")
        print("Press F to Abandom the action")
        self.InitAction()


    def CalculateRotation(self):
        RotationCount = Actions.ItemCount / Actions.InventorySize
        Actions.Rotations = math.ceil(RotationCount)


    def OnAction(self):
        time.sleep(2)
        mouse.moveTo(Actions.banker_position_x, Actions.banker_position_y)
        mouse.click()
        time.sleep(2)
        self.keyboard.press(Key.f3)
        self.keyboard.release(Key.f3)
        time.sleep(2)
        self.keyboard.press(Key.f3)
        self.keyboard.release(Key.f3)
        time.sleep(3)
        self.keyboard.press(Key.space)
        self.keyboard.release(Key.space)
        time.sleep(Actions.Duration) 

    def InitAction(self):
        times = 0
        for _ in range(Actions.Rotations):
            times += 1
            print("[" + Actions.Item+ "] x [" + str(Actions.InventorySize) +"] |" + str(times) + "/" + str(Actions.Rotations) + "|")
            self.OnAction()
        
        if times >= Actions.Rotations:
            Actions.Complete = True