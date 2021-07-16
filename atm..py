class Atm:
    #constructor
    def __init__(self,CardNumber, Pin):
        self.CardNumber = CardNumber
        self.Pin = Pin
        #checkbalance and withdrawl is a function/method
    def CheckBalance(self):
        print("Your balance is 1 lakh")
    def WithDrawl(self,amount):
        newAmount = 100000 - amount
        print("Your remaining balance is "+ str(newAmount))
def main():
    Card_number = input("Insert your card number")
    Pin = input("Enter your pin number")

    ishita = Atm(Card_number, Pin)
    print("Choose the activity 1)Check Balance, 2) Withdrawl")
    Activity = int(input("Enter activity number"))
    if(Activity == 1):
        ishita.CheckBalance()
    elif(Activity == 2):
        amount = int(input("Enter amount to withdrawl"))
        ishita.WithDrawl(amount)
    else:
        print("You can only click 1 and 2, you can't click other numbers than 1 and 2")

main()