global choice
class Calculator:
    def __init__(self):
        self.result = 0 

    def add(self, a, b):
        self.result = a + b
        return self.result

    def sub(self, a, b):
        self.result = a - b
        return self.result

    def mul(self, a, b):
        self.result = a * b
        return self.result

    def div(self, a, b):
        # if b == 0:
        #     print("Error: Division by zero.")
        # else:
        self.result = a / b
        return self.result

    #menu
    def menu(self):
        print("\n\n\tUser commands")
        print("\t1. Addition")
        print("\t2. Subtraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Previous result")
        print("\t6. Exit\n")
        print("Note: Only accepts two values at a time")
        print("\n\n")

    #menuchoice
    def menuchoice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1<= choice <= 6:
                    return choice
                else:
                    print("Please enter the valid choice (1 to 6)")
            except ValueError:
                print("Value error please enter valid choice (1 to 6)")

    #header
    def header(self):
        print("  ____  _                 _         ____      _            _       _              ")
        print(" / ___|(_)_ __ ___  _ __ | | ___   / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __  ")
        print(" \\___ \\| | '_ ` _ \\| '_ \\| |/ _ \\ | |   / _` | |/ __| | | | |/ _` | __/ _ \\| '__| ")
        print("  ___) | | | | | | | |_) | |  __/ | |__| (_| | | (__| |_| | | (_| | || (_) | |    ")
        print(" |____/|_|_| |_| |_| .__/|_|\\___|  \\____\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|    ")
        print("                   |_|                                                            ")

    @staticmethod
    def boxoutput(message,result):
        result_str = str(result)
        box = len(message) + len(result_str) * 4
        boxresult = f'|{message} {result}|'
        print('+' + '-' * box +'+')
        print('|'+boxresult+'|')
        print('+' + "-" * box +'+')
