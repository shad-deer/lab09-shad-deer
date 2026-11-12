# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                continue 
    return   

print(two_sum([2, 7, 11, 15], 9))   # [0,1]
print(two_sum([3, 2, 4], 6)) #[1,2]
    # Outline (write your plan here first):
    #   1. ij, i < j, i + j == target. one answer
    # Where to start: 
        #you have list of like five numbers and a atarget.
        # it shpoould return position[i] + position[j] = target
        #num1 < num 2 (if statement)
        # num1 + num2 = target (if )
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.



def max_profit(prices):
    # Outline:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
            else:
                continue
    return max_profit    
print(max_profit([7, 1, 5, 3, 6, 4]))  #returns 5
print(max_profit([7, 6, 4, 3, 1])) #retunrs 0
    #  prices is already initiated
    #  make for int i in range(len(prices)):
    #  then nest a j loop for int j in range(i+1, len(prices)):
    # if prices[j] - prices[i] > max_profit, then max_profit = prices[j] - prices[i]
    # else continue
    #  


    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.



def max_subarray(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subarray = nums[i:j]
            subarray_sum = sum(subarray)
            if subarray_sum > max_sum:
                max_sum = subarray_sum
            else:
                continue
    return max_sum
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) #returns 6
print(max_subarray([5, 4, -1, 7, 8])) #returns 23
    # Outline:
    # we have the whole list of nums
    # we can do a nested loop to find the sum of all contiguous subarrays
    # we can keep track of the max sum found so far and return it at the end

    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
