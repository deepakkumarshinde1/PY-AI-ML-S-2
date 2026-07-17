import numpy as np
products = np.array([
    "Rice",
    "Wheat Flour",
    "Sugar",
    "Milk",
    "Eggs",
    "Cooking Oil",
    "Bread"
])


daily_sales = np.array([
    [45, 52, 48, 60, 55, 62, 58],
    [30, 28, 35, 32, 31, 29, 34],
    [20, 18, 25, 22, 21, 19, 24],
    [75, 80, 78, 82, 85, 79, 81],
    [95, 90, 92, 96, 98, 94, 97],
    [40, 38, 42, 45, 44, 43, 46],
    [55, 58, 60, 62, 61, 59, 63]
])


# Calculate the total weekly sales for each product.
result = np.sum(daily_sales,axis=1)
print("Ihe total weekly sales for each product is ", result)

# Find the average weekly sales of every product.
result = np.mean(daily_sales,axis=1)
print("the average weekly sales of every product is ", result)


# Identify the highest-selling product.
result = np.sum(daily_sales,axis=1)
index = np.argmax(result)
print("the highest-selling product is ",products[index])

# Identify the lowest-selling product.
result = np.sum(daily_sales,axis=1)
index = np.argmin(result)
print("the lowest-selling product ",products[index])

# Find products whose average weekly sales are greater than 60.
result = np.mean(daily_sales,axis=1)
_product = products[np.where(result > 60)]
print("products whose average weekly sales are greater than 60 is ",_product)


# Find the day on which Eggs had maximum sales.
index = np.argmax(daily_sales[4])
days = ["Sun","Mon","Tue","Wed","Thus","Fri","Sat"]
print("The day on which Eggs had maximum sales is", days[index])

# Sort the products based on weekly sales.
result = np.sum(daily_sales,axis=1)
result = np.argsort(result)
print(products[result])


# Display only those products whose weekly sales exceed 350 units.
result = np.sum(daily_sales,axis=1)
index = np.where(result > 350)
# print(result)
# print(index)
print("products whose weekly sales exceed 350 units is ",products[index])

# Calculate total sales of the supermarket during the week.
total = np.sum(daily_sales)
print(f'total sales of the supermarket during the week {total} units')

# Find which day total sales were highest.
result = np.sum(daily_sales,axis=0)
index = np.argmax(result)
print("day total sales were highest is ",days[index])


# Find which day and product sales were highest.
result = np.max(daily_sales)
row,col = np.where(daily_sales == result)
print(products[row[0]],days[col[0]])