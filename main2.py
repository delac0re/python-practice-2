from unicodedata import category

name = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
price = float(input("Enter fuel price (KZT): "))
category = "undefined"
litres_needed = distance * consumption / 100
fuel_cost = litres_needed * price
cost_per_km = fuel_cost / distance


if distance < 100:
    category = "Short trip"
elif distance >= 100 and distance < 500:
    category = "Medium trip"
elif distance > 500:
    category = "Long trip"

print("Driver :",name)
print("Destination :",destination)
print("Distance :",distance)
print("Consumption :",consumption,"L/100km")
print("Fuel cost :",fuel_cost,"KZT")
print("Category :",category)

for i in range(100, int(distance) + 1, 100):
    live_cost = cost_per_km * i
    print(i, "km", "->", live_cost, "KZT")

print("Destination uppercase :", destination.upper())
print("Destination lowercase :", destination.lower())
print("Length :", len(destination))
print("Letter 'a' count :", destination.count("a"))
