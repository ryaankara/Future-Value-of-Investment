def calculate(n1, n2, n3):
	return (n1 * ((1 + (n2 / 100)) ** n3))

print()
print("Hello! Welcome to the savings calculator.")
print()

#storing the user's name in a variable
name = input("What is your name? ")

print()
print(name + ", today we will find out how much money you can save up.")
print()

initial = int(input("Firstly, what amount are you willing to use as the initial investment? [Disregard the $ symbol] (20000, 40000, 60000): "))
        #error message sent if user does not enter a proper amount
if(initial != 20000 and initial != 40000 and initial != 60000):

        print()
        print("Please retry and enter a proper number from the given choices.")
else:
        print()

        years = int(input("Next, for how many years do you wish to save? (2, 3, 4): "))
        #error message sent if user does not enter a proper amount
        if(years != 2 and years != 3 and years != 4):
                print()
                print("Please retry and enter a proper number from the given choices.")
        else:
                print()
        
                rate = int(input("Great, we're almost through " + name +
                ". What interest rate do you want to apply? [Disregard the % symbol] (6, 9, 12): "))
                #error message sent if user does not enter a proper amount
                if(rate != 6 and rate != 9 and rate != 12):
                        print()
                        print("Please retry and enter a proper number from the given choices.")
                else:
                        print()
                        print("With the given information, your future value will be:")
                        print()
                        #calculating and printing the final amount
                        print(calculate(initial, rate, years))
