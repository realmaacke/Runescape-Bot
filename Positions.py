class Init:
    Banker_pos_x = 0
    Banker_pos_y = 0

    Grand_exchange_pos_x = 0
    Grand_exchange_pos_y = 0

    def __init__(self, mouse):
        self.mouse = mouse 
        self.start()


    def saveBankerPosition(self, x, y, button, pressed):
        if button == self.mouse.Button.left:  
            if pressed:
                self.Banker_pos_x = self.Banker_pos_x + x
                self.Banker_pos_y = self.Banker_pos_y + y
                return False
                
        else:
            print("User your left click")

    def saveGrandExchangePosition(self, x,y, button, pressed):
        if button == self.mouse.Button.left:
            if pressed:
                self.Grand_exchange_pos_x = self.Grand_exchange_pos_x + x
                self.Grand_exchange_pos_y = self.Grand_exchange_pos_y + y
                return False
        else:
            print("User your left click")

    def start(self):
        print("Drag your cursor to the Banker and left click: ")
        listener = self.mouse.Listener(on_click=self.saveBankerPosition)
        listener.start()
        listener.join()

        print("Drag your cursor to the Grand exchange and left click: ")
        listener = self.mouse.Listener(on_click=self.saveGrandExchangePosition)
        listener.start()
        listener.join()
        
        print("Banker pos:", self.Banker_pos_x, " : ", self.Banker_pos_y)
        print("Grand Exchange pos:", self.Grand_exchange_pos_x, " : ", self.Grand_exchange_pos_y)