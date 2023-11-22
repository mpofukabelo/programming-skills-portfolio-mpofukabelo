def make_shirt(size, message):
    """Prints a message about the size and text of a T-shirt."""
    print(f"The shirt size is {size} and the message on the shirt is: '{message}'.")

# Call the function using positional arguments
make_shirt("medium", "WOOKIE")

# Call the function using keyword arguments
make_shirt(size="large", message="ASHLEY LOOK AT MEE")

