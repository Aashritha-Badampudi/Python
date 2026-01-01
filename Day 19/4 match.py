status=(75, "yes")
match status:
    case (75,"yes"):
        print("Good attendance and assignment submitted")
    case (75,"no"):
        print("Good attendance but assignment is not submitted")
    case (50,"yes"):
        print("Low attendance but assignment submitted")
    case _:
        print("Low attendance and assignment is not submitted")