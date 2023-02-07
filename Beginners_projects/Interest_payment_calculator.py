def main():
    print("This is monthly payment loan calculator")
    print("")


    principle = float(input("Input the loan amount: "))
    apr = float(input("Input the anual interest rate: "))
    years = int(input("Input amount of years: "))


    monthly_interest_rate = apr/ 1200
    amount_of_months = years * 12
    monthly_payment = principle * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))


    print("The monthly payment for this loan is : %.2f " % monthly_payment)

main()