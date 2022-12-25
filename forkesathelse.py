Khana = ["roti" ,"sabazi", "chaval", "pizza", "fruits", "jantar_mantar"]
input_string = input("Enter your food item : ")

for item in Khana:
    if item in input_string:
        print("This item was present in manus")
        break
else:
    print("You item was not found")
