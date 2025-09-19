# 1. Question 

# def exist(board, word):
#         for i in word:
#             for row  in board:
#                 if i in row:
#                     row.remove(i)  
#                     break
#             else:
#                 return False
#         return  True

# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) #op: True
# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # op:True
# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) #op: False

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 2. Question 

# variables = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 40,
#     'e': 50,
#     'f': 60
# }
# res = 0

# inp = input("enter a or b or c or d ")
# for i in inp:
#     if i in variables:
#         res += variables[i]
#     else:
#         print(f"Warning: Variable '{i}' not found.")
# print(res)




# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 3. Question 

# def maximumGap(nums):
#     if len(nums) <= 1:
#         return 0
        
#     nums.sort()
#     max_gap = 0
        
#     for i in range(1,len(nums)):
        
#         max_gap = max(max_gap, nums[i] - nums[i-1])
        
#     return max_gap


# s = maximumGap([1,3,5,9,15])
# print(s)  

# output: 4

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 4. Question 

# n = 5
# for i in range(1,n+1):
#     if i == 1 or i == n:
#         print("* " * n)
#     else:
#         print("* "+"  "*(n-2)+"* ")

# output:
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 5. Question 

# nums = [11,210,2020,333,1,34567,14]
# count = 0
# for i in nums:
#     if len(str(i)) % 2 == 0:
#         count += 1
# print(count)

# output : 2

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 6. Question 

# num = [-4,-1,0,10,3,10]
# nums = []

# for j in num:
#     nums.append(j*j)

# i = 0
# while i < len(nums)-1:
#     if nums[i] > nums[i+1]:
#         nums[i],nums[i+1] = nums[i+1],nums[i]
#         i = 0
#     else:
#         i += 1

# print(nums)

# output : [0,1,9,16,100]

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 7. Question

# nums = [1,1,0,0,0,0,4,4,4,4]
# maxxx = 0
# count = 1

# for i in range(1,len(nums)-1):
#     if nums[i] == nums[i-1]:
#         count += 1
#         if count >= maxxx :
#             maxxx = max(maxxx,count)
#     else:
#         count = 1
# print(maxxx)


# output: 4
