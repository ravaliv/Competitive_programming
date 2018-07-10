
def randomnumber(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(list_nums):
    if len(list_nums) <= 1:
        return list_nums

    length = len(list_nums) - 1

    for r in range(0, length):
        rndmnum = randomnumber(r, length)
        if rndmnum != r:
            list_nums[r], list_nums[rndmnum] = list_nums[rndmnum], list_nums[r]


print('--------------')
sample_list = [1, 2, 3, 4, 5,-1,-2,-3,-4,-5]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [-10,10,-20,20,-30,30,-40,40,-50,50]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5,6,7,8,9,10]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5,0,0,0,0,0]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5,-3,-5,-6,-7,-9]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
