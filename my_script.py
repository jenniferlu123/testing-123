
def enlarge(i):
    return i * 100


# need to remove from global scope in order to import things from this script
# my_number = float(input("Please input a number: "))

# # n = enlarge(8)
# n = enlarge(my_number)
# print("Enlargine the number:", n)

if __name__ == "__main__":
    my_number = float(input("Please input a number: "))
    n = enlarge(my_number)
    print("Enlargine the number:", n)