#SPY'S WORD REVERSER
Message = input("enter message: ").split()
Reversed = [Word[::-1] for Word in Message]

Result = " ".join(Reversed)

print(Reversed)