"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here    
    for item in items:
        # If the item is already in the dictionary, increment its count
        item = str(item)
        if item in frequencies:
            frequencies[item] += 1
        # If the item is not in the dictionary, add it with count 1
        else:
            frequencies[item] = 1

    return frequencies
