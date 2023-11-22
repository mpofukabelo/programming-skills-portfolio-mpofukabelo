places_to_visit = ['kenay', 'zimbabwe', 'Bora Bora', 'Machu Picchu', 'pakistan']

print("Original order:")
print(places_to_visit)

print("\nAlphabetical order:")
print(sorted(places_to_visit))

print("\nStill in original order:")
print(places_to_visit)

print("\nReverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))

print("\nStill in original order:")
print(places_to_visit)

places_to_visit.reverse()
print("\nReversed order:")
print(places_to_visit)

places_to_visit.reverse()
print("\nBack to original order:")
print(places_to_visit)

places_to_visit.sort()
print("\nSorted in alphabetical order:")
print(places_to_visit)

places_to_visit.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places_to_visit)
