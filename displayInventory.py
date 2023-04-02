stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}
total = None
def displayInventory(inventory):
    # your code goes here
    print('Inventory: ')
    for a,b in stuff.items():
        print(a, b)
        total = b + b
    print('Total number of items:', total)
if __name__ == "__main__":
    displayInventory(stuff)
