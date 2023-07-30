def shuffle_array(nums, n):
    x_values = nums[:n]  # Extract the first half of nums
    y_values = nums[n:]  # Extract the second half of nums

    result = []
    for x, y in zip(x_values, y_values):
        result.append(x)
        result.append(y)

    return result

# Example 1
nums = [2, 5, 1, 3, 4, 7]
n = 3
output = shuffle_array(nums, n)
print(output)  # Output: [2, 3, 5, 4, 1, 7]
