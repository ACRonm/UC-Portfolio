## Author: Aiden Rogers, u3204426

## Date created: 7 April 2022

## Date last changed: 12 April 2022

## Fixed-rate mortgage calculator and comparison with graphical user interface

from tkinter import *
import sys
import os.path


def main():
    root = Tk()
    root.title("Fixed-rate Loan Calculator")
    root.geometry("600x600")
    root.configure(bg="#c6eafa")
    loans = {}

    def repaymentCalculation(TOTAL_LOAN_AMOUNT, interestRate, paymentsPerYear, numberOfYears):
        repayments = (TOTAL_LOAN_AMOUNT * (interestRate / paymentsPerYear) * (1 + interestRate / paymentsPerYear) ** (
                paymentsPerYear * numberOfYears)) / (
                             (1 + interestRate / paymentsPerYear) ** (paymentsPerYear * numberOfYears) - 1)
        return repayments

    ## Loan calculation function
    def option_1():
        ## Initialise window
        newWindow = Toplevel(root)
        newWindow.configure(bg="#c6eafa")
        newWindow.title("Calculate a loan")
        newWindow.geometry("400x400")
        OPTIONS = [
            "Weekly",
            "Fortnightly",
            "Monthly"
        ]
        variable = StringVar(newWindow)
        variable.set(OPTIONS[0])  # default value
        ## Labels
        Label(newWindow, text="Amount borrowed:", bg="#c6eafa").grid(row=0, column=0, sticky="w")
        Label(newWindow, text="Interest rate:", bg="#c6eafa").grid(row=1, column=0, sticky="w")
        Label(newWindow, text="Length of loan: ", bg="#c6eafa").grid(row=2, column=0, sticky="w")
        Label(newWindow, text="Payment frequency:", bg="#c6eafa").grid(row=3, column=0, sticky="w")

        ## Entries
        loanEntry = Entry(newWindow)
        loanEntry.grid(row=0, column=1)
        interestRateEntry = Entry(newWindow)
        interestRateEntry.grid(row=1, column=1)
        numberOfYearsEntry = Entry(newWindow)
        numberOfYearsEntry.grid(row=2, column=1)
        ## This is my drop down menu
        numberOfPaymentsMenu = OptionMenu(newWindow, variable, *OPTIONS)
        numberOfPaymentsMenu.grid(row=3, column=1)

        ## Calculate function
        def submit():
            textBox.delete("1.0", END)
            TOTAL_LOAN_AMOUNT = float(loanEntry.get())
            interestRate = interestRateEntry.get()
            numberOfYears = float(numberOfYearsEntry.get())
            loanNumber = max(loans, default=0, key=int)
            loanNumber += 1
            interestRate = interestRate.strip("%")
            interestRate = float(interestRate) / 100
            paymentRecurrence = variable.get().lower()
            print(variable.get())
            if paymentRecurrence == "weekly":
                paymentsPerYear = 52
            elif paymentRecurrence == "fortnightly":
                paymentsPerYear = 26
            elif paymentRecurrence == "monthly":
                paymentsPerYear = 12

            print("Calculating loan repayments...")

            textBox.insert(END, "Submitted.\n")
            textBox.insert(END, "The " + paymentRecurrence + " repayments for a ${:,}".format(TOTAL_LOAN_AMOUNT) +
                           " loan are: ${:0.2f}".format(
                               repaymentCalculation(TOTAL_LOAN_AMOUNT, interestRate, paymentsPerYear,
                                                    numberOfYears)) + "\n")

            totalRepayments = repaymentCalculation(TOTAL_LOAN_AMOUNT, interestRate, paymentsPerYear,
                                                   numberOfYears) * paymentsPerYear * numberOfYears

            textBox.insert(END, "You will pay ${:,.2f}".format(totalRepayments) + " over the life of the loan.\n")

            totalRepayments = repaymentCalculation(TOTAL_LOAN_AMOUNT, interestRate, paymentsPerYear,
                                                   numberOfYears) * paymentsPerYear * numberOfYears

            loans[loanNumber] = totalRepayments

            textBox.insert(END, "Submitted.\n")

        quitButton = Button(newWindow, text="Quit", command=newWindow.destroy)
        quitButton.grid(row=4, column=1)
        calculateButton = Button(newWindow, text="Calculate and submit", command=submit)
        calculateButton.grid(row=4, column=0)

    def option_2():
        print(loans)
        textBox.delete("1.0", END)

        if loans:
            cheapestLoan = min(loans, key=loans.get)
            # When the program leaves the loop, it will print the cheapest loan and the total amount for the term of the
            # loan.
            print("The best loan for you is loan number",
                  str(cheapestLoan) + ". You will pay ${:,.2f}".format(float(loans[cheapestLoan])),
                  "over the course of the loan.")
            textBox.insert(END,
                           "The best loan for you is loan number " + str(
                               cheapestLoan) + ".\nYou will pay ${:,.2f}".format(
                               float(loans[cheapestLoan])) +
                           " over the course of the loan.")
        else:

            textBox.insert(END, "There are no loans recorded.")

    def option_3():
        textBox.delete("1.0", END)
        file_exists = os.path.isfile("loans.txt")
        if file_exists:
            textBox.insert(END, "Loading loans from text document...\n")
            with open("loans.txt") as infile:
                for line in infile:
                    (k, v) = line.strip().split(":")
                    loans[int(k)] = v
        else:
            textBox.insert(END, "No file detected. Please calculate a loan and save it.")

    def option_4():
        textBox.delete("1.0", END)

        if loans:
            textBox.insert(END, "Saving loans to text document...")
            infile = open("loans.txt", "a")
            for k in loans.keys():
                infile.write("{}:{}\n".format(k, loans[k]))
            infile.close()
        else:
            textBox.insert(END, "You have no loans to save. Please calculate a loan.")

    def option_5():
        if loans:
            infile = open("loans.txt", "a")
            for k in loans.keys():
                infile.write("{}:{}\n".format(k, loans[k]))
            infile.close()
            sys.exit()
        else:
            sys.exit()

    spacer = Label(root, bg="#c6eafa").pack(pady=15)
    calculateLoanButton = Button(root, text="1- Calculate new loan", command=option_1, width=50, pady=5)
    calculateLoanButton.pack()
    bestLoanButton = Button(root, text="2 - Calculate best loan", command=option_2, width=50, pady=5)
    bestLoanButton.pack()
    loadLoanButton = Button(root, text="3 - Load loans from text document", command=option_3, width=50, pady=5)
    loadLoanButton.pack()
    saveLoanButton = Button(root, text="4 - Save loans to text document", command=option_4, width=50, pady=5)
    saveLoanButton.pack()
    saveAndExitButton = Button(root, text="5 - Save and exit", command=option_5, width=50, pady=5)
    saveAndExitButton.pack()
    spacer = Label(root, bg="#c6eafa").pack(pady=15)
    textBox = Text(root, width=60, height=10, padx=(10))
    textBox.pack()
    root.mainloop()


main()
