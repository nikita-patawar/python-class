def EmployeeInfo(Name = "Nikita", Age=21, City = "Pune", Salary=50000):
    print("Name: ",Name)
    print("Age: ",Age)
    print("Salary: ",Salary)
    print("City: ",City)

def main():

    EmployeeInfo(Age=27,Name="Nikita")
    EmployeeInfo()
   
if __name__ == "__main__":
    main()