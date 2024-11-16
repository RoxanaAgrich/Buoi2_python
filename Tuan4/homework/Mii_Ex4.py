"""
base class:
    Transaction()
        -transaction_id
        -date
        -quantity
        -calculate_price()
        -display()
derived class:
    -GoldTransaction()
        -unit_price
        -type_of_gold
        -calculate_price()<duck method>
        -display()<duck method>

    -CurrencyTransaction()
        -exchange_rate
        -type_of_currency
        -type_of_transaction
         -calculate_price()<duck method>
        -display()<duck method>
concrete class: TransactionManagement(this class have a list_transaction,having Transaction type)
"""
from datetime import datetime

class Transaction():
    def __init__(self,transaction_id="001",
                 date=datetime.now(),
                 quantity=0):
        self.transaction_id = transaction_id
        self.date =date
        self.quantity = quantity
    def inputInfo(self):
        self.transaction_id = input("Enter the transaction id: ")
        self.date =  datetime.strptime(input("Enter the  date :(YYYY-MM-DD): "),"%Y-%m-%d")
        self.quantity = int(input("Enter the quantity: "))
    def calculate_price(self):
        pass
    def display(self):
        print("============================")
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Date: {self.date} ")
        print(f"Quantity: {self.quantity}")
        print(f"The total price: {self.calculate_price()}")


class GoldTransaction(Transaction):
    def __init__(self,transaction_id="001",
                 date=datetime.now(),
                 quantity=0,
                 unit_price= 20000,
                 type_of_gold="18K"):
        super().__init__(transaction_id,date,quantity)
        self.unit_price = unit_price
        self.type_of_gold = type_of_gold
    def inputInfo(self):
        super().inputInfo()
        self.unit_price =float(input("Enter the unit price"))
        self.type_of_gold =input("Enter the type of gold(18K,24K,9999): ")
    def calculate_price(self):
        return self.quantity*self.unit_price
    def display(self):
        super().display()
        print(f" the unit of price: {self.unit_price}")
        print(f" the type of gold: {self.type_of_gold}")


class CurrencyTransaction(Transaction):
    def __init__(self,transaction_id="001",
                 date=datetime.now(),
                 quantity=0,
                 exchange_rate=23,
                 type_of_currency="USD",
                 type_of_transaction="buy"):
        super().__init__(transaction_id,date,quantity)
        self.exchange_rate = exchange_rate
        self.type_of_currency = type_of_currency
        self.type_of_transaction = type_of_transaction
    def inputInfo(self):
            super().inputInfo()
            self.exchange_rate = float(input("Enter the exchange-rate: 2"))
            self.type_of_currency = input("Enter the type of currency(USD, EUR, AUD): ")
            self.type_of_transaction = input("Enter the type of transaction(buy-sell): ")
    def calculate_price(self):
        if(self.type_of_transaction=="buy"):
            return self.quantity*self.exchange_rate
        else:
            return (self.quantity*self.exchange_rate)*1.05
    def display(self):
        super().display()
        print(f" the exchange rate: {self.exchange_rate}")
        print(f" the type of currency: {self.type_of_currency}")
        print(f" the type of transaction: {self.type_of_transaction}")


class TransactionManagement:
    def __init__(self):
        self.transactions =[]
    def add(self,transaction):
        self.transactions.append(transaction)
    def delete(self):
        transaction_id = input(f"Enter the transaction id to delete: ")
        for transaction in self.transactions:
            if transaction.transaction_id==transaction_id:
                self.transactions.pop(transaction)
                break
    def display(self):
        for transaction in self.transactions:
            print("===========================")
            transaction.display()

    # Main program
def main():
        transaction_manager = TransactionManagement()

        while True:
            print("\nTransaction Management System")
            print("1. Add Gold Transaction")
            print("2. Add Currency Transaction")
            print("3. Display Transactions")
            print("4. Delete Transaction")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice ==1 :
                gold_transaction =GoldTransaction()
                gold_transaction.inputInfo()
                transaction_manager.add(gold_transaction)
            elif choice == 2:
                currency_transaction = CurrencyTransaction()
                currency_transaction.inputInfo()
                transaction_manager.add(currency_transaction)
            elif choice == 3:
                transaction_manager.display()
            elif choice ==4:
                transaction_manager.delete()
            elif choice == 5:
                break
            else:
                print("Your choice is invalid. Please try again. ")

if __name__=="__main__":
    main()





