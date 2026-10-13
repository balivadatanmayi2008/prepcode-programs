nums = [1, 2, 3, 4]
n = len(nums)
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += nums[i - 1] ** 2
print(total)
