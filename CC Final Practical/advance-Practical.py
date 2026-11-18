
def subsets(nums):
    result = []
    current = []

    def backtrack(index):
        if index == len(nums):
            result.append(current.copy())
            return

        current.append(nums[index])
        backtrack(index + 1)

        current.pop()
        backtrack(index + 1)

    backtrack(0)
    return result


nums = list(map(int, input("Enter array elements: ").split()))

print("All subsets:")
print(subsets(nums))
