class SalaryDeductionCalculator:
    def __init__(self, salary):
        self.salary = salary
        self.sss_contribution = 1200
        self.philhealth_contribution = (salary * 0.05) / 2
        self.pagibig_contribution = 100
        self.tax_amount = 1875

    def calculate_deductions(self):
        return self.sss_contribution + self.philhealth_contribution + self.pagibig_contribution + self.tax_amount

    def calculate_net_salary(self):
        return self.salary - self.calculate_deductions()

    def display_salary_breakdown(self):
        print(f"Gross Salary: {self.salary:.2f}")
        print(f"SSS Deduction: {self.sss_contribution:.2f}")
        print(f"PhilHealth Deduction: {self.philhealth_contribution:.2f}")
        print(f"Pag-IBIG Deduction: {self.pagibig_contribution:.2f}")
        print(f"Tax Deduction: {self.tax_amount:.2f}")
        print(f"Total Deductions: {self.calculate_deductions():.2f}")
        print(f"Net Salary: {self.calculate_net_salary():.2f}")

def main():
    try:
        salary = float(input("Enter your monthly salary: "))
        if salary < 0:
            print("Error: Salary cannot be negative.")
            return
        calculator = SalaryDeductionCalculator(salary)
        calculator.display_salary_breakdown()
    except ValueError:
        print("Error: Please enter a valid numeric salary.")

if __name__ == "__main__":
    main()
