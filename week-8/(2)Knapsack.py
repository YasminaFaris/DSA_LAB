class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def knapsack(item_list, amount):
    print(f"Knapsack Size: {amount} kg")
    print("===============================")
    
    items_sorted = sorted(item_list, key=lambda x: (x.price/x.weight), reverse=True)
    
    total_price = 0
    remaining_capacity = amount
    selected_items = []
    
    for item in items_sorted:
        if item.weight <= remaining_capacity:
            selected_items.append(item)
            remaining_capacity -= item.weight
            total_price += item.price
    
    for item in selected_items:
        print(f"{item.name} -> {item.weight} kg -> {item.price} THB")
    
    print(f"Total: {total_price} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
        
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)

main()