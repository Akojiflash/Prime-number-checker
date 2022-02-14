def prime(enter):
        number = []
        checker = []
        for items in range(enter):
                if items == 0:
                        pass
                elif items == 1:
                        pass
                else:
                        number.append(items)

        for items in number:
                if enter % items == 0:
                        checker.append(items)
                else:
                        continue
        if len(checker) > 0:
                return 0
        else:
                return enter

deck = []

primer = int(input("Enter a number: "))
print(prime(primer))
for items in range(primer+1):

        if prime(items) == 0:
                pass
        elif prime(items)==1:
                pass
        else:
                print(prime(items))


