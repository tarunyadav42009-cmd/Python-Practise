# Set how high you want the numbers to go
max_value = 900

a, b = 0, 1

while a < max_value:
    print(a, end=" ")
    a, b = b, a + b

