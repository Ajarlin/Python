def my_nums(*numbers):
    if not numbers:
        return
    if numbers is not None:
        print("First number: " + str(numbers[0]))
        print("Last number: " + str(numbers[-1]))
        print("All my numbers " + str(numbers))

#my_nums('1', '2', '3')
my_nums()

print("2nd Num list")
my_nums(1,2,3,4)

print("3rd Num list")
mylist = [1,2,3,4]
my_nums(mylist)
