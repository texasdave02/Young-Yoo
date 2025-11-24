# CS11A - HOS06: Classes & Intro to OOP
# I wrote this as a simple practice file. Nothing fancy, just the basics.

class Employee:
    # shared across all employees
    employee_count = 0

    def __init__(self, first_name: str, last_name: str, email: str):
        # instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Employee.employee_count += 1

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def contact_card(self) -> str:
        return f"Name: {self.full_name()} | Email: {self.email}"

    def __repr__(self) -> str:
        # useful when printing objects while testing
        return f"Employee({self.first_name!r}, {self.last_name!r}, {self.email!r})"


if __name__ == "__main__":
    # quick manual test
    e1 = Employee("Ada", "Lovelace", "ada.lovelace@cityu.edu")
    e2 = Employee(first_name="Alan", last_name="Turing", email="alan.turing@cityu.edu")

    print("== Contact Cards ==")
    print(e1.contact_card())
    print(e2.contact_card())

    print("\n== Class Variable ==")
    print("Total employees:", Employee.employee_count)

    print("\n== Debug ==")
    print(e1)
    print(e2)
