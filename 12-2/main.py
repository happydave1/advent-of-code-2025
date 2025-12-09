import math

INPUT_FILE = "./input.txt"
TEST_FILE = "./test.txt"


def isPalindrome(num: int) -> bool:
    num = str(num)
    if len(num) % 2 == 1:
        return False

    halfway = len(num) // 2
    return num[:halfway] == num[halfway:]

def isSilly(num: int) -> bool:
    num = str(num)
    
    # check all sequences up to ceil(len(num) / 2)
    N = len(num)

    if N == 1:
        return False  # cannot have a silly num if only 1 digit
    
    limit = math.ceil(N / 2)

    for i in range(1, limit + 1):
        if N % i != 0:
            continue  # we cannot have a pattern which doesnt repeat cleanly
            
        num_times = N // i
        base = num[0:i]
        if base * num_times == num:
            return True
    return False

# read thru the input file, gather ranges
silly_nums = []
with open(INPUT_FILE, 'r') as file:
    l = file.read().strip()
    ranges = l.split(",")
    
    for r in ranges:
        lower, upper = map(int, r.split('-'))
        
        for num in range(lower, upper+1):
            # if isPalindrome(num):
            #     silly_nums.append(num)

            if isSilly(num):
                # print(f"found silly num {num}")
                silly_nums.append(num)
total = 0
for num in silly_nums:
    total += num
print(total)


### TESTING
# print(isSilly(12))
# print(isSilly(11))
# print(isSilly(1010))
