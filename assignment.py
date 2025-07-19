class Company:

    def __init__(self):
        print("Welcome to Employee Management System (EMS)")
        self.employees = {
            101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
        }
        self.main_menu()

    # 🔹 Main Menu Function
    def main_menu(self):
        while True:
            choice = input("""
===============================
   Employee Management System
===============================
1. Add Employee
2. View All Employees
3. Search for Employee by ID
4. Exit
Enter your choice (1-4): """)

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                print("Thank you for using EMS. Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please try again.\n")

    # 🔹 Function to Add Employee
    def add_employee(self):
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in self.employees:
                print("❌ Employee ID already exists. Please enter a unique ID.")
                return  # early exit if duplicate ID

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            salary = int(input("Enter Salary: "))

            self.employees[emp_id] = {
                'name': name,
                'age': age,
                'department': department,
                'salary': salary
            }

            print("✅ Employee added successfully!")

        except ValueError:
            print("❌ Invalid input! Please enter correct data types.")

    # 🔹 Function to View All Employees
    def view_employees(self):
        if not self.employees:
            print("⚠️ No employees available.")
            return

        print(f"\n{'ID':<5} {'Name':<10} {'Age':<5} {'Department':<12} {'Salary':<10}")
        print("-" * 50)
        for emp_id, details in self.employees.items():
            print(f"{emp_id:<5} {details['name']:<10} {details['age']:<5} {details['department']:<12} {details['salary']:<10}")
        print()

    # 🔹 Function to Search Employee by ID
    def search_employee(self):
        try:
            emp_id = int(input("Enter Employee ID to search: "))
            if emp_id in self.employees:
                details = self.employees[emp_id]
                print("\n✅ Employee Found:")
                print(f"ID: {emp_id}")
                print(f"Name: {details['name']}")
                print(f"Age: {details['age']}")
                print(f"Department: {details['department']}")
                print(f"Salary: {details['salary']}")
            else:
                print("❌ Employee not found.")
        except ValueError:
            print("❌ Please enter a valid numeric Employee ID.")


# 🔹 Start the EMS program
if __name__ == "__main__":
    Company()
