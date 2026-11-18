
def subsets(nums):
    result = [[]]

    for num in nums:
        new_subsets = []

        for subset in result:
            new_subsets.append(subset + [num])

        result.extend(new_subsets)

    return result


nums = list(map(int, input("Enter array elements: ").split()))

print("All subsets:")
print(subsets(nums))
