# In place 
def sort_nums(nums):
    red = 0
    white = 0
    blue = 0

    for color in nums:
        if color == 0:
            nums[red] = 0
            red += 1
        elif color == 1:
            white += 1
        else:
            blue += 1

    for j in range(red, len(nums)-white-1):
        nums[j] = 1

    for k in range(len(nums) - white, len(nums)):
        nums[k] = 2





print(sort_nums([2,0,2,1,1,0]))



