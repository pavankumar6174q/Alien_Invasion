# Multiplication table from 1 to 20 (only up to * 10)
print("Multiplication Tables (1 to 20, up to 10):")
print("-" * 40)  # Separator line for visual appeal

for i in range(11 , 21):
    print(f"Table of {i}:".center(40, " "))  # Centered header for each table
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}".center(40))
    print("-" * 40)  # Separator line between tables

# Squares up to 30
print("\nSquares of numbers up to 30:")
print("-" * 40)
for i in range(1, 31):
    print(f"{i}^2 = {i**2}".center(40))
print("-" * 40)

# Cubes up to 20
print("\nCubes of numbers up to 20:")
print("-" * 40)
for i in range(1, 21):
    print(f"{i}^3 = {i**3}".center(40))
print("-" * 40)
