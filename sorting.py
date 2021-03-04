def sort_integers():
    empty_list = []
    even_list = []
    odd_list = []
    number = input("Enter multiple number separated by space: ")
    nn_number = number.split()
    for numbers in nn_number:
        newNumber = int(numbers)
        empty_list.append(newNumber)
        empty_list.sort()
    # print(empty_list)

    for num in empty_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    newShit = even_list + odd_list

    print(newShit)


sort_integers()
