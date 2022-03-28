countdown = int(input("How long until the party starts? "))

if countdown < 1:
    print("Party Happening Now!")
else:
    for i in range(countdown, 0, -1):
        print(i)
        if i == 1:
            print("Party Time!")