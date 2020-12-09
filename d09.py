def preamble(index, array, many):
    if index < many - 1 or index >= len(array):
        return False
    pos = array[index - many:index]
    neg = []
    goal = array[index]
    for x in pos:
        if goal - x in neg and 2 * x != goal:
            return True
        else:
            neg.append(x)
    return False

f = open("inputd09", "r")
nums = []
limit = -1
goal = -1
for x in f:
    nums.append(int(x))
f.close()
for i in range(25, len(nums)):
    if not preamble(i, nums, 25):
        limit = i
        goal = nums[i]
        print(goal) # 09.1
        break
index = 0
for i in range(limit):
    goal -= nums[i]
    while goal < 0:
        goal += nums[index]
        index += 1
    if goal == 0:
        min = min(nums[index:i+1])
        max = max(nums[index:i+1])
        print(min + max) # 09.2
        break