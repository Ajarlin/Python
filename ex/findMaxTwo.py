def find_secondmax(mylist):
    if len(mylist) is 0:
        return 1
    if len(mylist) is 1:
        return max(mylist)

    else:
        return max(alist)



alist = [-1, -1, -1, -1, -1]
first_max = max(alist)

second_max = find_secondmax(alist)
sum_of_highest_two = first_max + second_max
print("The first max is {} and the second max is {} which together is {}".format(first_max, second_max, sum_of_highest_two))
