class Employee:
    def __init__(self, ID, name, department, job):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__job = job

    #mutators
    def set_name(self, name):
        self.__name = name

    def set_ID(self, ID):
        self.__ID = ID

    def set_dept(self, department):
        self.__department = department

    def set_job(self, job):
        self.__job = job

    #accessors
    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job

    def __str__(self):
        return (f"Name: {self.__name}, ID Number: {self.__ID}, "
                f"Department: {self.__department}, Job Title: {self.__job}")


class ShiftEmployee(Employee):

    #initialise ShiftEmployee object
    def __init__(self, ID, name, department, job, shift_number, hourly_pay_rate):
        super().__init(ID, name, department, job)
        self.__shiftNumber = shift_number
        self.__hourlyPayRate = hourly_pay_rate


    #mutators
    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber

    def set_hourlyPayRate(self, hourlyPayRate):
        self.__hourlyPayRate = hourlyPayRate

    #accessors
    def get_shiftNumber(self):
        return self.__shiftNumber

    def get_hourlyPayRate(self):
        return self.__hourlyPayRate

    def __str__(self):
        return f"Employee ID: {self.get_ID()}, Name: {self.get_name()}, Department: {self.get_department()},"\
               f" Job title: {self.get_job()} Shift: {self.__shiftNumber}, Hourly pay rate: {self.__hourlyPayRate}"

class Contractor(Employee):

    #initialise ShiftEmployee object

    def __init__(self, ID, name, department, job, contract_end_date, ABN, fixed_salary):
        super().__init__(ID, name, department, job)
        self.__contract_end_date = contract_end_date
        self.__ABN = ABN
        self.__fixed_salary = fixed_salary


    #mutators
    def set_shiftNumber(self, contract_end_date):
        self.__contract_end_date = contract_end_date

    def set_hourlyPayRate(self, ABN):
        self.__ABN = ABN

    def set_fixed_salary(self, fixed_salary):
        self.__fixed_salary = fixed_salary

    #accessors
    def get_contract_end_date(self):
        return self.__contract_end_date

    def get_ABN(self):
        return self.__ABN

    def get_fixed_salary(self):
        return self.__fixed_salary

contractor1 = Contractor("322645", "Henry Caville", "Construction", "Builder", "20/11/2021", "34567855961", "$69,000")
contractor2 = Contractor("356346", "Ryan Gosling", "Marketing", "Advertiser", "14/2/2022", "35476535730", "$94,000")

print(contractor1.get_name() + "'s contract expires on: ", contractor1.get_contract_end_date())
print(contractor1.get_name() + "'s ABN:", contractor1.get_ABN())
print(contractor1.get_name() + "'s salary:", contractor1.get_fixed_salary())
print(contractor2.get_name() + "'s contract expires on:", contractor2.get_contract_end_date())
print(contractor2.get_name() + "'s ABN:", contractor2.get_ABN())
print(contractor2.get_name() + "'s salary:", contractor2.get_fixed_salary())