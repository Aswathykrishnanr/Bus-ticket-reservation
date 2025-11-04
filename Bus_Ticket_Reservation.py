# Bus Ticket Reservation System

# Customer Details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = input("Enter your phone number: ")
category = input("Enter category (student / senior / general): ")
if age > 60:
    category = "senior"

# Available Routes
routes = {
    'Kochi to Trivandrum': {'time': '08:00 AM', 'price': 300},
    'Kozhikode to Kochi': {'time': '01:30 PM', 'price': 450},
    'Trivandrum to Palakkad': {'time': '10:00 AM', 'price': 550},
    'Kochi to Bangalore': {'time': '09:00 PM', 'price': 900},
}

print("\nAvailable Bus Routes")
print("=" * 60)
print(f"{'Route':<35}{'Time':<12}{'Price (₹)':<10}")
print("-" * 60)
for route, details in routes.items():
    print(f"{route:<35}{details['time']:<12}₹{details['price']:<10}")
print("=" * 60)

# Route selection
while True:
    chosen_route = input("\nEnter your route exactly as shown: ").lower()
    for route in routes:
        if route.lower() == chosen_route:
            print("You selected:", route)
            print("Time:", routes[route]['time'])
            print("Price:", routes[route]['price'])
            break
    else:
        print("Invalid route selected. Please try again.")
        continue
    break

# Seats and price
seats = int(input("\nEnter number of seats: "))
price_per_ticket = routes[route]['price']
total_price = price_per_ticket * seats

# Apply discount
discount = 0
if category.lower() == "student":
    discount = total_price * 0.15
elif category.lower() == "senior":
    discount = total_price * 0.20

final_amount = total_price - discount

# Booking confirmation
confirm = input(f"\nDo you want to confirm the booking for ₹{final_amount}? (yes/no): ").strip().lower()
if confirm != "yes":
    print("\nBooking cancelled. Thank you for visiting!")
    exit()

# Ticket printing
ticket_content = f"""
----------------------------------------
        BUS TICKET - TRAVEL AGENCY
----------------------------------------

Passenger Name : {name.title()}
Phone Number   : {phone}
Age            : {age}
Category       : {category.title()}
Route          : {route}
Departure Time : {routes[route]['time']}
Seats Booked   : {seats}

----------------------------------------
Ticket Price   : ₹{price_per_ticket}
Total Amount   : ₹{total_price}
Discount       : ₹{discount}
Final Amount   : ₹{final_amount}
----------------------------------------

Thank you for booking with us!
Have a safe journey, {name.title()}!
"""

# Print ticket
print(ticket_content)

# Save ticket to file
filename = f"ticket_{name}_{phone}.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(ticket_content)

print(f"Ticket saved as {filename}")
