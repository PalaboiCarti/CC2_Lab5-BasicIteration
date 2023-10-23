user_num = []
found = False

for i in range(7):
    while True:
        try:
            new_num = int(input(f"Enter item {i+1}: "))
            user_num.append(new_num)
            break  
        except ValueError:
            print("Please enter an integer")

for num1 in user_num:
    for num2 in user_num:
        if num1 != num2:
            numsum = num1 + num2
            if numsum == 0:
                found = True
                print(f"The pair ({num1}, {num2}) have the sum of 0")

if found == False:
    print("No pairs found with the sum of 0")



