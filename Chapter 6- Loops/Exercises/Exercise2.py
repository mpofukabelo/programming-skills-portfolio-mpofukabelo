while True:
    try:
        age = int(input("Please enter your age (or enter 0 to exit): "))
        if age < 0:
            print("Please enter a valid age.")
            continue
        elif age == 0:
            break
        elif age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
    except ValueError:
        print("Please enter a valid age.")

