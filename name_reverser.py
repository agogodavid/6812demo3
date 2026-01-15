#!/usr/bin/env python3

# Load the list of names from names.txt
with open('names.txt', 'r') as f:
    names = [line.strip() for line in f if line.strip()]

# Create a set of known names for quick lookup (case insensitive)
known_names = set(name.lower() for name in names)

# Function to reverse a name
def reverse_name(name):
    return name[::-1]

# Process each name
for name in names:
    reversed_name = reverse_name(name)
    is_real = reversed_name.lower() in known_names
    print(f"Original: {name} -> Reversed: {reversed_name} -> Is real name: {is_real}")
