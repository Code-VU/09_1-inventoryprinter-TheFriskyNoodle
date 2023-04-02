stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    print('Inventory: ')
    total = 0 
    for a,b in stuff.items():
        print(a, b)
        total = total + b
    print('Total number of items:', total)
if __name__ == "__main__":
    displayInventory(stuff)
