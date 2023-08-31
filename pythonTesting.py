array = [1,3,0,0,2,0,0,4]


def zeroFilledSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    streak = [0]
    score = [0]
    timesRan = [0]
    timesRan1 = [0]
    def zeroStreak(index, i1):
        while(len(nums) > index+i1):
            if nums[index+i1] == 0:
                streak[0] += 1
                timesRan1[0] += 1
            if nums[index+i1] != 0:
                score[0] = streak[0]+score[0]
                streak[0] = 0
                return 
            index += 1
    i = 0
    for num in nums:
        if num == 0:
            zeroStreak(0, i)
            timesRan[0] += 1
        i += 1
    answer = timesRan1[0]
    timesRan1[0] = 0
    return answer


print(zeroFilledSubarray(0, array))
print(zeroFilledSubarray(0, [0,0,0,2,0,0]))
print(zeroFilledSubarray(0, [2,10,2019]))
