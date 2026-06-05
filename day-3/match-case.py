#switch

courseNumber = int(input("Enter a course number = "))
match courseNumber:
    case 1:
        print("You have got a course i.e AI")
    case 2:
        print("You have got a course i.e AI/ML")
    case 3:
        print("You have got a course i.e Java")
    case _:
        print("Wrong Selection , try again")