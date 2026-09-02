#NIGHT CLUB VIP QUE
VIP = ["Guido", "Esha", "Rajan", "Kishori"]

while True:
    print(f"Enter VIP : {VIP}")
    guest = input("Enter name: ")
    
    if guest in VIP:
        print(f"{guest} has moved front!")
        a = VIP.index(guest)
        VIP.pop(a)
        VIP.insert(0, guest)
        print(f"current que : {VIP}")
    else:
        print("Access denied! Not on VIP list")
        print(f"current que : {VIP}")
        
    if guest == 'Exit':
        break