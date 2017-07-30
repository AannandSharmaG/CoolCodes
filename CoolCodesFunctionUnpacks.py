def StuffsInMybasket(fruits,vegetables,others):
    return fruits + vegetables + others
# Arguments passed directly
print("Total number of stuffs in my basket are ",StuffsInMybasket(10,20,20))
MyItems = [10,20,20]
# Example of arguments unpacking
print("Total number of stuffs in my basket are ",StuffsInMybasket(*MyItems))