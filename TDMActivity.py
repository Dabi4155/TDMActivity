class SalaryDeductionCalculator:
  
    SSS_CONTRIBUTION = 1200
    PAGIBIG_CONTRIBUTION = 100
    TAX_AMOUNT = 1875

    def __init__(self, gross_salary):   
        self.gross_salary = gross_salary
        self.philhealth_contribution = (gross_salary * 0.05) / 2

    def calculate_total_deductions(self): 
        return (self.SSS_CONTRIBUTION + self.philhealth_contribution +
                self.PAGIBIG_CONTRIBUTION + self.TAX_AMOUNT)

    def calculate_net_salary(self):
        return self.gross_salary - self.calculate_total_deductions()

    def display_salary_breakdown(self):
        print(f"Gross Salary: {self.gross_salary:.2f}")
        print(f"SSS Deduction: {self.SSS_CONTRIBUTION:.2f}")
        print(f"PhilHealth Deduction: {self.philhealth_contribution:.2f}")
        print(f"Pag-IBIG Deduction: {self.PAGIBIG_CONTRIBUTION:.2f}")
        print(f"Tax Deduction: {self.TAX_AMOUNT:.2f}")
        print(f"Total Deductions: {self.calculate_total_deductions():.2f}")
        print(f"Net Salary: {self.calculate_net_salary():.2f}")


def main():
    try:
        gross_salary = float(input("Enter your monthly salary: "))
        if gross_salary < 0:
            print("Error: Salary cannot be negative.")
            return
        
        calculator = SalaryDeductionCalculator(gross_salary)
        calculator.display_salary_breakdown()
    except ValueError:
        print("Error: Please enter a valid numeric salary.")

if __name__ == "__main__":
    main()