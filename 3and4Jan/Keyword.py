def EmployeeInfo(Name, Age, Salary, City):
    print("Name: ",Name)
    print("Age: ",Age)
    print("Salry: ",Salary)
    print("City: ",City)


def main():
    #Positional
    EmployeeInfo("Nikita",27,5000.98,"Pune")

    #Keyword Arguments
    EmployeeInfo(Age=27,Name="Nikita",City="Pune,",Salary=500.5)

   
if __name__ == "__main__":
    main()