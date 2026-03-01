# class Solution(object):
#     def isPalindrome(self, num):
#         digit = ""
#         if num >= 0:
#             for char in str(num)[::-1]:
#                 digit += char
#             digit = int(digit)
#             if num == digit:
#                 return True
#             else:
#                 return False
#         else:
#             return False

# using another logic

def solve(num):
    num = str(num)
    print(num[::-1])
    return num[::-1] == num

print(solve(+121))
