def solve(meal_cost, tip_percent, tax_percent):
   
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)

    total_meal = meal_cost + tip + tax
    print(round(total_meal))


solve(12.00, 20, 8)
