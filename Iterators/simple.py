my_list = [4, 7, 0, 3]

my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))  This will raise error


iter = iter (my_list)

while True:
    try:
        element=next(iter)
    except StopIteration:
        print("Finished")
        break