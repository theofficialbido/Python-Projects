weight = float(input('Enter your weight: '))vis
unit = input("[L]bs or [K]g: ")
if unit.upper() == "L":
    weight = weight * 0.45
    print(f"You are {weight}")
elif unit.upper() == "K":
    weight = weight * 2.23
    print(f"You are {weight} Lbs")
