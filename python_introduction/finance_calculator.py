def main():
    try:
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your total monthly expenses: "))
        monthly_savings = monthly_income - monthly_expenses
        annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
        print(f"Monthly Savings: ${monthly_savings:.2f}")
        print(f"Projected Annual Savings: ${annual_savings:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
if __name__ == "__main__":
    main()