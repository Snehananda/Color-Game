class NormalMessage:
    def __init__(self, element, command):
        self.element = element 
        self.command = command 
      
    def getMessage(self):
        print(f"I'm {self.element.title()}! I'm sometimes {self.command.title()}")


class FrogMessage:
    def __init__(self, element, command):
        self.element = element 
        self.command = command
        
    def getMessage(self):
        print(f"I'm {self.element.title()}! I am {self.command.title()} today")



#Observer Design Pattern

class ColorGameClass:
    
    def __init__(self):
        self.subscriber = []
        self.color = {
            "green":["apple","banana"],
            "red":["ink","blood","apple"],
            "black":["ink","sky"],
            "blue":["sky","frog"],
            "yellow":["banana","frog"],
            "white":["salt"]
        }
        
       
    def subscriberList(self):
        for ele in self.subscriber:
            print(ele, end=" ")
        print("")
    
    
    def subscribe(self,element):
        if element in self.subscriber:
            print("Already Subscribed")

        print(f"Subscribing {element.title()}")
        self.subscriber.append(element)
    

    def unSubscribe(self, element):
        if element not in self.subscriber:
            print("Already Unsubscribed")
        
        print(f"Unsubscribing {element.title()}")
        self.subscriber.remove(element)
        
    
    
    #This is a Factory function 
    
    def printColor(self,command):
        outList = []
        for element in self.color[command]:
            if element in self.subscriber:
                if element=="frog":
                    outList.append(FrogMessage(element, command))
                else:
                    outList.append(NormalMessage(element, command))
        return outList
    
    
    
    def evaluateInput(self, command):

        subscribers = ["banana", "ink", "salt", "frog", "blood", "sky", "apple"]

        if type(command)==str:

            if command == "list":
                self.subscriberList()
            elif command in self.color:
                colorObjs = self.printColor(command)
                for obj in colorObjs:
                    obj.getMessage()
            elif command[0]=="+" and command[1:] in subscribers:
                self.subscribe(command[1:])
            elif command[0]=="-" and command[1:] in subscribers:
                self.unSubscribe(command[1:])
            else:
                print("Invalid Command")
        else:
            print("Invalid Command")
        
    
if __name__ == "__main__":

    gameObj = ColorGameClass()
    print("Whats your command?")
    
    command = input()

    while command!="exit":
  
        if command=="":
            pass
        else:
            gameObj.evaluateInput(command.strip().lower())
        print()
        command = input()