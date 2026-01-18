No = 11        # Global
def Fun():
    No = 21    # Local
    print("Value of No from Fun is: ",No)

print("Value of No is: ",No)
Fun()