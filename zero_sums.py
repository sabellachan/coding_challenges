def zero_sums(nums):
    for num in nums:
        if -num in nums:
            return True
            break
    else:
        return False


zero_sums([1, 2, -1, 2, 3])

zero_sums([1, 2, 3])

zero_sums([])
