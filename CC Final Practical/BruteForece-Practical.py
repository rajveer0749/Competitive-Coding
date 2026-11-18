
def subsets(nums):
    n = len(nums)
    result = []

    for i in range(1 << n):
        subset = []

        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])

        result.append(subset)

    return result


nums = list(map(int, input("Enter array elements: ").split()))

print("All subsets:")
print(subsets(nums))
