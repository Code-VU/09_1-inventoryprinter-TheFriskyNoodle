stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    for a,b in stuff.items():
        print(a, b)

if __name__ == "__main__":
    displayInventory(stuff)
