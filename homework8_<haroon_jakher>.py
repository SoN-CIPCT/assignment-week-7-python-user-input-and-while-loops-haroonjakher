# Week 7 Homework Assignment

#Lists of pizzas
pizza_orders= ["Pepperoni", "Supreme", "Margherita", "Puttanesca", "Quattro Formaggi"]

finished_pizzas= []

#Loop through the pizzas and moving them to the new list
while pizza_orders:
    recent_order = pizza_orders.pop()

    print(f"{recent_order.title()}: Your pizza pie is finished!")
    finished_pizzas.append(recent_order)

#Print what pizzas have been made
for pizzas in finished_pizzas:
    print(f"The pizza {pizzas} was made." )