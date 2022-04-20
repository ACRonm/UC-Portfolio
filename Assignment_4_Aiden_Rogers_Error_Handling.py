## Author: Aiden Rogers, u3204426

## Date created: 7 April 2022

## Date last changed: 12 April 2022

## Fixed-rate mortgage calculator and comparison with command line menu and error handling

import sys
import os.path

## Create dictionary
loans = {}
## Create list for command line options
options = ["1 - Calculate loan repayments", "2 - Calculate best loan", "3 - Load loans from text document", "4 - Save "
                                                                                                            "loans to"
                                                                                                            " text "
                                                                                                            "document",
           "5 - Exit"]


## Calculates the amount per repayment
def repaymentCalculation(TOTAL_LOAN_AMOUNT, interestRate, paymentsPerYear, numberOfYears):
    repayments = (TOTAL_LOAN_AMOUNT * (interestRate / paymentsPerYear) * (1 + interestRate / paymentsPerYear) ** (
            paymentsPerYear * numberOfYears)) / (
                         (1 + interestRate / paymentsPerYear) ** (paymentsPerYear * numberOfYears) - 1)
    return repayments


def mainMenu():
    try:
        print("================================\n"
              "FIXED-RATE LOAN CALCULATOR\n"
              "================================\n" +
              options[0] + "\n" + options[1] + "\n" + options[2] + "\n" + options[3] + "\n" + options[4] + "\n",
              "===============================\n"
              "Enter a choice and press enter: ", end="")

    except ValueError as error:  # If the input is invalid (a string where an integer is supposed to be), the program
        # will loop back.
        print(error, "Invalid input. Please enter an integer.")
        mainMenu()
    else:
        menuInput = int(input())
        if menuInput == 1:
            option_1()
        elif menuInput == 2:
            option_2()
        elif menuInput == 3:
            option_3()
        elif menuInput == 4:
            option_4()
        elif menuInput == 5:
            option_5()


def yes_or_no(question):
    reply = str(input(question + " (y/n): ")).lower().strip()
    if reply[:1] == "y":
        return True
    if reply[:1] == "n":
        return False
    else:
        return yes_or_no("I didn't get that. Please enter y or n.")


def option_1():  # Commandline menu option 1
    print("Calculating loan repayments...")

    try:  # Exception handling. If the input is incorrect value, loop. If the output is too large, loop.
        newLoan = True
        TOTAL_LOAN_AMOUNT = int(input("How much do you want to borrow? "))  # This is my constant
        while newLoan:
            ## Initialise variables
            loanNumber = max(loans, default=0, key=int)
            loanNumber += 1
            interestRate = input("What is the interest rate? Input as percentage E.g.: 5%: ")
            interestRate = interestRate.strip("%")
            interestRate = float(interestRate) / 100
            numberOfYears = int(input("How many years do you want to pay off the loan? "))

            ## Input validation for the numberOfPayments
            while True:
                try:
                    paymentRecurrence = input("Do you want to pay weekly, fortnightly, or monthly? ")
                    paymentRecurrence = paymentRecurrence.lower()
                    if paymentRecurrence == "weekly":
                        paymentsPerYear = 52
                    elif paymentRecurrence == "fortnightly":
                        paymentsPerYear = 26
                    elif paymentRecurrence == "monthly":
                        paymentsPerYear = 12
                    paymentsPerYear = paymentsPerYear
                except NameError:  # If the input is spelt incorrectly, loop.
                    print("Sorry, I didn't understand that. Please try again.")
                    continue
                else:
                    break

            print("The", paymentRecurrence, "repayments for a ${:,}".format(TOTAL_LOAN_AMOUNT),
                  " loan are: ${:0.2f}".format(
                      repaymentCalculation(TOTAL_LOAN_AMOUNT, interestRate, paymentsPerYear, numberOfYears)))
            totalRepayments = repaymentCalculation(TOTAL_LOAN_AMOUNT, interestRate, paymentsPerYear,
                                                   numberOfYears) * paymentsPerYear * numberOfYears

            print("You will pay ${:,.2f}".format(totalRepayments), "over the life of the loan.")

            loans[loanNumber] = totalRepayments

            newLoan = yes_or_no("Do you want to calculate another loan?")  # While the user wants to continue the
            # program, it will loop indefinitely.
    except ValueError as error:  # Invalid input, restart function.
        print(error, "Invalid input. Please enter an integer. Restarting...")  # Output for ValueError
        option_1()
    except OverflowError as error:  # If the output is too large to display, it will handle the error and restart
        # function
        print(error,
              "Result too large to display. Please try again with lower values. Restarting...")  # Output for
        # OverflowError
        option_1()
    finally:
        mainMenu()


def option_2():  # Commandline menu option 2
    if loans:
        cheapestLoan = min(loans, key=loans.get)
        # When the program leaves the loop, it will print the cheapest loan and the total amount for the term of the
        # loan.
        print("The best loan for you is loan number",
              str(cheapestLoan) + ". You will pay ${:,.2f}".format(float(loans[cheapestLoan])),
              "over the course of the loan.")
    else:
        print("There are no loans recorded. Please calculate a loan or load from text document.")
    backToMenu = yes_or_no("Do you want to continue?")
    if backToMenu:
        mainMenu()
    else:
        option_5()


def option_3():  # Command line menu option 3
    execute = input("Press ENTER to execute. Enter ANYTHING to go back: ")
    if execute == "":
        try:
            print("Loading loans")
            with open("loans.txt") as infile:
                if os.stat("loans.txt").st_size == 0:
                    print("File is empty. Please calculate and save a loan.")
                    mainMenu()
                else:
                    for line in infile:
                        (k, v) = line.strip().split(":")
                        loans[int(k)] = v
        except FileNotFoundError as error:  # IF the file is not found, the code will create a new file.
            print(error, "File not found. Creating loans.txt.")
            infile = open("loans.txt", "w")
            infile.close()

        except ValueError as error:  # If the data in the file is corrupt/invalid, the program will destroy the file
            # and remake it.
            print(error, "Invalid data in text file. Recreating file...")
            os.remove("loans.txt")
            infile = open("loans.txt", "w")
            infile.close()
        finally:
            mainMenu()


def option_4():
    print("Saving loans to text document...")
    if loans:
        infile = open("loans.txt", "a")
        for k in loans.keys():
            infile.write("{}:{}\n".format(k, loans[k]))
        infile.close()
    else:
        print("You have no loans to save. Please calculate a loan.")
    backToMenu = yes_or_no("Do you want to continue?")
    if backToMenu:
        mainMenu()
    else:
        option_5()


def option_5():
    print("Exiting...")
    sys.exit()


def main():
    mainMenu()


main()
