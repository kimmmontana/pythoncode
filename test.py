class Customers:
    greeting = "Welcome to Coffee Palace!"

c1 = Customers()
c1.name = "Samira"
c1.beverage = "Iced coffee latte"
c1.food = "Cinnamon Roll"
c1.total = 225

c2 = Customers()
c2.name = "Jerry"
c2.beverage = "Caramel macchiato"
c2.food = "Glazed Doughnut"
c2.total = 230

print(Customers.greeting)
print(c1.beverage)
print(c2.food)