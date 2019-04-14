size = input("Enter board size: ")
size = int(size)

for i in range(size):
    print(" --- " * (size))
    print("|    " * (size + 1))
print(" --- " * (size))