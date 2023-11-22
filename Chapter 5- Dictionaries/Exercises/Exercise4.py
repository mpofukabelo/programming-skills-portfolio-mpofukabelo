major_rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river, country in major_rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers in the dictionary:")
for river in major_rivers.keys():
    print(river)

print("\nCountries in the dictionary:")
for country in major_rivers.values():
    print(country)
