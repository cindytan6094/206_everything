# Your name:
# Your student id:
# Your email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  

# The goal of this homework is to practice basic debugging and get familar with
# Python 3 basics.  It includes work with functions, strings, for-each loop,
# for loop, range, and conditionals

# Fix errors in the function below. It should return a count of the number
# of values less than or equal to the passed target value
# in the passed list nums. 
#
# For example count_lte(2, [-2, 2, 3]) should return 2.
def count_lte(target, nums)
    count = 0
    for Num in nums:
        if nums > target:
            count += 1

# Testing the count_lte function
def test_count_lte():
    print("Testing count_lte")
    res = count_lte(2, [-2, 2, 3])
    print("Expected: 2, Actual: ", res)
    res = count_lte(2, [0, 1, -2, 2, 3])
    print("Expected: 4, Actual: ", res)
    res = count_lte(3, [0, 1, -2, 2, 3])
    print("Expected: 5, Actual: ", res)
    res = count_lte(-2, [0, 1, -2, -3])
    print("Expected: 2, Actual: ", res)
    res = count_lte(10, [])
    print("Expected: 0, Actual: ", res)

# Fix errors in the function below.  It should return a total of the values from 1
# to the specified end (inclusive) when counting by 3's (1, 4, 7, etc).
#
# For example total_by_threes(4) should return 5 (1 + 4).
def total_by_threes(end)
    total = 0
    for x in range(0, End, 2)
        total += x
        return total

# Testing the total_by_threes function
def test_total_by_threes():
    print("Testing total_by_threes")
    res = total_by_threes(4)
    print("Expected: 5, Actual: ", res)
    res = total_by_threes(0)
    print("Expected: 0, Actual: ", res)
    res = total_by_threes(1)
    print("Expected: 1, Actual: ", res)
    res = total_by_threes(7)
    print("Expected: 12, Actual: ", res)
    res = total_by_threes(5)
    print("Expected: 5, Actual: ", res)

# Return true if all the values in num_list are negative (< 0) and false otherwise.  
# 
# For example check_all_neg([1, -2]) should return False and check_all_neg([-5, -3]) should
# return True.
def check_all_neg(num_list):
    for num in numlist:
        if num < 0:
            return false
        return true

# Testing the check_all_neg function
def test_check_all_neg():
    print("Testing check_all_neg")
    res = check_all_neg([-1, -2])
    print("Expected: True, Actual: ", res)
    res = check_all_neg([5, -3])
    print("Expected: False, Actual: ", res)
    res = check_all_neg([-1, -3, -5])
    print("Expected: True, Actual: ", res)
    res = check_all_neg([-100, 30, 5])
    print("Expected: False, Actual: ", res)
    res = check_all_neg([0, -3])
    print("Expected: False, Actual: ", res)


# Fix the function below to return the index of the minimum value in the list nums
# or -1 if there aren't any values in the list.  If the minimum value appears more than
# once in the list you should return the index of the first one.  
# 
# For example get_index_min([20, 100, 10, 10]) should return 2.
def get_index_min(nums):

    # init the min and min_index
    min = 0
    min_index = 0

    # loop through the list
    for index in nums:

        # get the current value
        current = nums[index]

        # if new min
        if current > min:

            # reset min and min index
            current = min
            min_index = index

    return current

# Testing the get_index_min function
def test_get_index_min():
    print("Testing get_index_min")
    res = get_index_min([2, -3, 5])
    print("Expected: 1, Actual: ", res)
    res = get_index_min([-2, 3, -5])
    print("Expected: 2, Actual: ", res)
    res = get_index_min([1])
    print("Expected: 0, Actual: ", res)
    res = get_index_min([14, 20, 4, 14])
    print("Expected: 2, Actual: ", res)
    res = get_index_min([])
    print("Expected: -1, Actual: ", res)
    res = get_index_min([20, 100, 20, 100])
    print("Expected: 0, Actual: ", res)

# Fix the function below to:
# return 3 if score > 75 
# return 2 if score > 50 and <= 75
# return 1 if score > 25 and <= 50
# else return 0
#
# For example: get_group(75) should return 2.
def get_group(score):
    group = 3
    if score >= 75:
        group = 3
    if score >= 50:
        group = 2
    if score >= 25:
        group = 3
    else:
        return 0
    return group

# Test the get_group function
def test_get_group():
    print("Testing get_group")
    res = get_group(75)
    print("Expected: 2, Actual: ", res)
    res = get_group(100)
    print("Expected: 3, Actual: ", res)
    res = get_group(40)
    print("Expected: 1, Actual: ", res)
    res = get_group(18)
    print("Expected: 0, Actual: ", res)
    res = get_group(200)
    print("Expected: 3, Actual: ", res)

# Fix errors in the function below.  It should return a password (string)
# created from the first two letters of each word in the passed string
# followed by a '@' and then the last two digits of the passed year.
#
# For example create_pass("Hello world", 2021) should return "Hewo@21"
def create_pass(the_str, year)
    words = the_str.split()
    pass = ""
    for word in words
        pass + word[0:1]
    pass = pass + "@' + year[-1:]
    return pass

# Testing the create_pass function
def test_create_pass():
    print("Testing create_pass")
    res = create_pass("Hello world", 2021)
    print("Expected: Hewo@21, Actual: ", res)
    res = create_pass("Some one stop me", 2020)
    print("Expected: Soonstme@20, Actual: ", res)
    res = create_pass("Walk", 2019)
    print("Expected: Wa@19, Actual: ", res)
    res = create_pass("Walk for Hope", 2019)
    print("Expected: WafoHo@19, Actual: ", res)
    res = create_pass("aa bb cc", 2021)
    print("Expected: aabbcc@21, Actual: ", res)

# Extra credit - up to 5 points
# Finish the function below to take a list of numbers, nums, and return a new list where the numbers are replaced with a string if they 
# meet the following critera:
# If the number is divisible by both 2 and 5 use "both"
# If the number is only divisible by 2 use "two"
# If the number is only divisible by 5 use "five"
# Otherwise use the number
def divs(nums):
    pass

# Testing the divs function
def test_divs():
    print("Testing divs")
    res = divs([1, 3, 9])
    print("Expected: [1, 3, 9], Actual: " + str(res))
    res = divs([1, 2])
    print("Expected: [1, 'two'], Actual: " + str(res))
    res = divs([5, 7])
    print("Expected: ['five', 7], Actual: " + str(res))
    res = divs([4, 10])
    print("Expected: ['two', 'both'], Actual: " + str(res))
    res = divs([25, 20, 1])
    print("Expected: ['five', 'both', 1], Actual: " + str(res))
    
test_divs()


# declare the main method
def main():
    test_count_lte()
    print()
    test_total_by_threes()
    print()
    test_check_all_neg()
    print()
    test_get_index_min()
    print()
    test_get_group()
    print()
    test_create_pass()
    print()
    #test_divs() # remove the # to test the extra credit

# call the main method
main()
