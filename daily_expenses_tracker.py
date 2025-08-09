name = input("Please enter your name: ")
age = 0 # Initialize age to 0
while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        
        print("Oops! That was an invalid number. Please enter your age using numbers (e.g., 25).")

print(f"\nHello {name}, you are {age} years old. Welcome to your Daily Expenses Tracker!\n")

all_items = []
total_cost = 0.0


while True:
    
    item = input("Enter the item you bought today (or type 'done' to finish): ")

    if item.lower() == 'done':
        break

  
    while True:
        try:
            item_price = float(input(f"How much did the {item} cost? "))
            total_cost += item_price
            # Başındaki gereksiz boşluk kaldırıldı
            all_items.append(f"{item}: {item_price:.2f} dollars")
            break # Fiyat doğru girilince bu iç döngüden çıkıp ana döngüye döner
        except ValueError:
            print("Invalid price! Please enter a number (e.g., 25.50).")


print("\n-------------------- YOUR SUMMARY -------------------")
if not all_items:
    print("You didn't buy anything today.")
else:
    print("Today you bought:")
    
    for item in all_items:
        print(f"- {item}")

    
    print(f"\nTotal spent: {total_cost:.2f} dollars. Great job tracking, {name}!")
