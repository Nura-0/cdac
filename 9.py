#THE JOSEPHUS ELIMINATION GAME
N = int(input("Enter number of oldiers:"))
K = int(input("Enter elimination interval:"))
Soldiers = list(range(1,N+1))
print("soldier circle initialized:", Soldiers)
index = 0
while len(Soldiers)>1:
    index = (index+K-1)%len(Soldiers)
    eliminated = Soldiers.pop(index)
    print(f"eliminated soldier:{eliminated}")
    print(f"remaining:{Soldiers}")
print("the sole survivor is:", Soldiers[0])    