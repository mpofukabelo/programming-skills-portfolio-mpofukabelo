def make_shirt(size='large', message='WOOKIE'):
    """Prints a message about the size and text of a T-shirt."""
    print(f"The shirt size is {size} and the message on the shirt is: '{message}'.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt('medium')

# Make a custom shirt of any size with a different message
make_shirt('small', 'WOOKIE FOR CAPTAIN')
