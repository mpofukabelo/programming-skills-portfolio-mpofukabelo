while True:
    topping = input("Enter a pizza topping (enter 'exit' to exit): ")
    if topping.lower() == 'exit':
        break
    print(f"I'll add {topping} to your pizza.")

print("Your pizza is well done and ready!")
