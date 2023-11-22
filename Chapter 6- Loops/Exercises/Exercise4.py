# Create a list of sandwich orders
sandwich_orders = ['tuna', 'turkey', 'chicken', 'vegetable', 'ham']

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Remove the first sandwich order from the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)  # Add the finished sandwich to the list of finished sandwiches

# Print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
