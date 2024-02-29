# key value pair
# they are mutable
# entities can be changed by assigning that entry

laptop = {"make","lenovo","colour" "black","weight""1.5",}

laptop["colour"] = "red"
laptop["year"] = "2020"

for key,value in laptop.items():
    print(laptop["make"])
    print(laptop["colour"])
    print(laptop["year"])
    

    print(key)
    print("\n")
    print(value)

laptop["size"] = "1100"    
  
