def containsDuplicate(nums) -> bool:
    result = False
    while result != True and len(nums) > 1:
        for x in nums[1:]:
            if nums[0] == x:
                result = True
        nums = nums[1:]
    return result

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))