pets = [
    {'animal': 'dog', 'owner': 'emiko'},
    {'animal': 'cat', 'owner': 'megatron'},
    {'animal': 'parrot', 'owner': 'p,j'}
]

for pet in pets:
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print()
