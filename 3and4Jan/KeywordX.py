def EmployeeInfo(Name, Age, Salary, City):
    print("Name: ",Name)
    print("Age: ",Age)
    print("Salry: ",Salary)
    print("City: ",City)


def main():

    #Keyword Arguments
    EmployeeInfo(Age=27,Name="Nikita",City="Pune,",Salary=None)

   
if __name__ == "__main__":
    main()