# Salary Deduction Calculator Refactoring  

## Technical Debt Identified  
During the review of the initial Salary Deduction Calculator code, we identified the following technical debt issues:  
- *Poor naming conventions:* Variables such as sss, philhealth, and pagibig lacked clarity.  
- *Lack of modular functions:* The code performed multiple tasks in a single function, reducing reusability.  
- *Hardcoded values:* Fixed amounts for SSS, Pag-IBIG, and tax instead of allowing dynamic inputs.  
- *No error handling:* The program did not handle invalid inputs (e.g., non-numeric values, negative salaries).  
- *Code duplication:* Repetitive print statements instead of a formatted output method.  

## Improvements Made  
To address the identified technical debt, we made the following improvements:  
- *Enhanced variable naming:* Renamed variables for better readability (e.g., sss_contribution, net_salary).  
- *Modular functions:* Split the code into smaller functions for calculating deductions and displaying results.  
- *Implemented OOP:* Introduced a SalaryDeductionCalculator class to improve maintainability.  
- *Added input validation:* Ensured that the user input is numeric and non-negative.  
- *Optimized code structure:* Used formatted string outputs to eliminate redundancy in print statements.  

## Challenges Faced & Solutions  
### *1. Merge Conflicts in Git*  
- *Challenge:* Multiple team members worked on different parts of the code, leading to merge conflicts.  
- *Solution:* We used git pull --rebase to incorporate remote changes and resolved conflicts manually before committing.  

### *2. Handling Invalid User Input*  
- *Challenge:* The program crashed when non-numeric or negative values were entered.  
- *Solution:* Added a try-except block to handle ValueError and a condition to prevent negative salary input.  

### *3. Hardcoded Tax and Deductions*  
- *Challenge:* The original code used fixed values, making it inflexible.  
- *Solution:* Refactored deductions into functions so they can be updated dynamically in the future.  

---
