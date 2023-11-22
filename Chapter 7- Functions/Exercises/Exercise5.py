def describe_city(city, country='USA'):
    """Prints a message about the city and its country."""
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city('new york')
describe_city('Reykjavik', 'Iceland')
describe_city('London', 'United Kingdom')
