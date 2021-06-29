for item in "python": #item is for variable that will hold the character in the iteration.
    print(item)

for item in ["Mosh", "Jhon", "Sarah"] #square brackets define a list og items etc.
for item in [1, 2, 3, 4, 5, 6]
for item in range(10, 20) #this defines the range of which it will start and stop. by default goes one by one and, but this can be changed in the range func by changing the steps


# this is a "shoppingtrip" string
#prices are defined here
prices = [10, 20, 30]

total = 0 #total is 0 at the start of the shopping
for price in prices: #for price variable in the prices list
    total += price #augmented the total + price = price for each iteration
print(f"Total:  {total}") # prints the "variable by the "f" at the start and curly bracets for the total that is undefined until the end.