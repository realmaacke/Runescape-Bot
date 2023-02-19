#imports
import time, math
from random import randrange
from pynput.keyboard import Key, Controller, Listener
from pynput import mouse

#modules
from Positions import Init
from notifications import Notify
from actions import Actions

#instances

while True:
    instance = Init(mouse)
    notifications = Notify()
    action = Actions(instance.Banker_pos_x, instance.Banker_pos_y)

    if action.Complete == True:
        notifications.SendNotification(False)

# if complete dont continue

# Notifications

# notifications.SendNotification(True)