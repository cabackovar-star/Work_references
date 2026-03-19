class Employeesalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, hours, rest_days):
        if hours is None:
            if rest_days is not None:
                return (7 - rest_days) * 8
            else:
                return 0
        return hours

    @classmethod
    def get_email(cls, name, email):
        if email is None:
            return f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        hours_worked = self.get_hours(self.hours, self.rest_days)
        return hours_worked * self.hourly_payment
    
emp = Employeesalary("Иван", hours=40, email="ivan@company.com")
print(Employeesalary.get_email(emp.name, emp.email))  # ivan@company.com
print(Employeesalary.get_hours(emp.hours, emp.rest_days))  # 40
print(emp.salary())  # 16000