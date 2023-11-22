glossary = {
    'variable': 'a named location in memory used to store data',
    'function': 'a block of organized, reusable code that is used to perform a single, related action',
    'loop': 'a sequence of instructions that is continually repeated until a certain condition is reached',
    'list': 'a collection of items in a particular order',
    'dictionary': 'a collection of key-value pairs',
    'tuple': 'an immutable sequence of Python objects',
    'set': 'an unordered collection of unique items',
    'class': 'a blueprint for creating objects',
    'method': 'a function that is associated with an object',
    'module': 'a file containing Python definitions and statements'
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")
