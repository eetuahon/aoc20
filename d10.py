f = open("inputd10", "r")
nums = []
for x in f:
    nums.append(int(x))
f.close()
prev = 0
counter = [0, 0, 0]
nums.sort()
for i in nums:
    diff = i - prev
    prev = i
    if diff == 1:
        counter[0] += 1
    elif diff == 2:
        counter[1] += 1
    elif diff == 3:
        counter[2] += 1
    else:
        print("Error")
        break
counter[2] += 1 # last always +3 higher
print(counter[0] * counter[2]) # 10.1
diffs = [1]
if nums[1] <= 3:
    diffs.append(2)
else:
    diffs.append(1)
if nums[2] - nums[0] <= 3:
    diffs.append(diffs[0] + diffs[1])
else:
    diffs.append(diffs[1])
if nums[2] == 3:
    diffs[2] += 1
for i in range(3, len(nums)):
    if nums[i] - nums[i - 3] <= 3:
        diffs.append(diffs[i - 1] + diffs[i - 2] + diffs[i - 3])
    elif nums[i] - nums[i - 2] <= 3:
        diffs.append(diffs[i - 1] + diffs[i - 2])
    else:
        diffs.append(diffs[i - 1])
print(max(diffs)) # 10.2