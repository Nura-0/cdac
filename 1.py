#WIZARD'S MAGIC BAG
txt = ["Staff","potion", "Spellbook"]
a = input("enter string:")

poped_item = txt.pop(0)
print(poped_item)
txt.append(a)
print("portal transition activated")
#print(f"ejected item:{txt.pop(0)}")
print(txt)

