from FancyShoppingListMG import FancyFoodItem

def create_food_item_list():
    food_item_list = []

    num_items = int(input("How many items will you order today? "))
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today? "))

    for i in range(1, num_items + 1):
        print(f"Item #{i}-")
        food = input("Enter food: ")
        amount = float(input("Enter amount of pounds: "))
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input("Enter amount of pounds: "))

        food_item = FancyFoodItem(food, amount)
        food_item_list.append(food_item)

    return food_item_list

def display_food_item_list(food_item_list):
    for item in food_item_list:
        print(item)
        print()

def calculate_total_cost(food_item_list):
    total_cost = sum(item.get_calculated_price() for item in food_item_list)
    return total_cost

def main():
    food_items = create_food_item_list()
    display_food_item_list(food_items)

    total_cost = calculate_total_cost(food_items)
    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
