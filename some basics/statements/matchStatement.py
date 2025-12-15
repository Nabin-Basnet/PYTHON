# The match statement is used to perform different actions based on different conditions.
day=10

match day:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thirsday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("out of the box choice")


isweekday=9

match isweekday:
    case 1|2|3|4|5|6:
        print("yes")
    case 7:
        print("no")
    case _:
        print("out of the box")