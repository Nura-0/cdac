#CARGO TRAIN SCANNER
wagons = ["coal", "Iron", "gold", "coal", "timber", "coal"]
Resource = input("enter string : ")

if Resource in wagons:
    a = wagons.count(Resource)  
    print(f"no: of {Resource} wagons: {a}")
    print(f"First {Resource} wagon is at index: {wagons.index(Resource)}")
else:
    print("Resource not found on train")