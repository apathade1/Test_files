mark = 100

class Illegal(Exception):
    pass

while True:
    try:
        uMark = int(input("Enter a mark out of 100 "))
        if 100 < uMark < 0:
            raise Illegal
        break
    except Illegal:
        print("Invalid mark")

print("Valid mark")



