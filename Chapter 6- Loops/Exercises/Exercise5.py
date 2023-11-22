# Create a list of sandwich orders
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'turkey', 'pastrami', 'chicken', 'vegetable', 'ham', 'pastrami']

# Ensure 'pastrami' appears at least three times
while sandwich_orders.count('pastrami') < 3:
    sandwich_orders.append('pastrami')

# Print a message indicating the deli has run out of pastrami
print("The deli has run out of pastrami.")

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Remove the first sandwich order from the list
    if current_sandwich != 'pastrami':
        print(f"I made your {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)  # Add the finished sandwich to the list of finished sandwiches

# Print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
