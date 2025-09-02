#  1. String Compression


# def string_compression(s: str) -> str:
#     if not s:  
#         return ""
    
#     compressed = []
#     count = 1

#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             count += 1
#         else:
#             compressed.append(s[i] + str(count))
#             count = 1
    
#     compressed.append(s[-1] + str(count))
    
#     return "".join(compressed)


# print(string_compression("aaabbc"))   # a3b2c1
# print(string_compression("aabccccc")) # a2b1c5
# print(string_compression("abcd"))     # a1b1c1d1
# print(string_compression(""))         # (empty string)


# __________________________________________________________________________________________-



# 2 Rotate Matrix 90° (in-place)


# def rotate_matrix(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i, n):
            

#             matrix[i][j],matrix[j][i]  = matrix[j][i],matrix[i][j]

    

#     for row  in matrix:
#         row.reverse()
#     return matrix

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(rotate_matrix(matrix))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]] 



# ________________________________________________________________________________________________


# 3.Longest Palindrome from Letters


# def longest_palindrome(s):
#     freq = []  
    
#     # Count characters manually
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1
    
#     length = 0
#     odd_found = False
    
    
#     for count in freq.values():
#         if count % 2 == 0:
#             length += count      
#         else:
#             length += count - 1   
#             odd_found = False
    

#     if odd_found:
#         length += 1
    
#     return length


# #  Examples
# print(longest_palindrome("abccccdd"))   # 7 dccaccd
# print(longest_palindrome("a"))          # 1
# print(longest_palindrome("abc"))        # 1
# print(longest_palindrome("aaabbbb"))    # 7

# __________________________________________________________________________________________-

# 4 Rotate Array by K

# def rotate_array(nums, k):
#     # k %= len(nums)
    
#     return nums[-k:] + nums[:-k]

# # print(rotate_array([1,2,3,4,5,6,7], 3))  # [5,6,7,1,2,3,4]
# print(rotate_array([1,2,3,4,5,6,7], 5))  # [3, 4, 5, 6, 7, 1, 2]




#___________________________________________________________________________________________

# 5.Spiral Order Traversal (boundary pointers)



# def spiral_order(matrix):
#     if not matrix: 
#         return []
#     top, bottom = 0, len(matrix) - 1
#     left, right = 0, len(matrix[0]) - 1
#     res = []
#     while top <= bottom and left <= right:
#         # left -> right
#         for j in range(left, right + 1):
#             res.append(matrix[top][j])
#         top += 1

#         # top -> bottom
#         for i in range(top, bottom + 1):
#             res.append(matrix[i][right])
#         right -= 1

#         if top <= bottom:
#             # right -> left
#             for j in range(right, left-1, -1):
#                 res.append(matrix[bottom][j])
#             bottom -= 1

#         if left <= right:
#             # bottom -> top
#             for i in range(bottom, top-1, -1):
#                 res.append(matrix[i][left])
#             left += 1

#     return res



# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(spiral_order(matrix))  #[1, 2, 3, 6, 9, 8, 7, 4, 5]


# ______________________________________________________________________________________



#6. Diagonal Sum Excluding Middle


# def diagonal_sum_exclude_middle(matrix):
#     n = len(matrix)
#     total = 0

#     for i in range(n):
#         total += matrix[i][i]         
#         total += matrix[i][n-1-i]        
#     print(total)
    
#     if n % 2 != 0:
#         total -= matrix[n//2][n//2]

#     return total


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# print(diagonal_sum_exclude_middle(matrix))  #25

# matrix = [
#  [1, 2, 3, 4, 5],
#  [6, 7, 8, 9,10],
#  [11,12,13,14,15],
#  [16,17,18,19,20],
#  [21,22,23,24,25]
# ]

# print(diagonal_sum_exclude_middle(matrix))  #117


# ____________________________________________________________________________



# def solution(s, ending):
#     arr = s[len(s) - len(ending):]
#     print(arr)
#     return arr == ending

# print(solution('sumo', 'umo'))
# print(solution('alice','ica'))


# ________________________________________________________________-


# 7. Element with highest frequency

# def repeated_number(arr):
#     max_count = 0
#     value = None

#     for i in range(len(arr)):
#         count = 0
#         for j in range(len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#         if count > max_count:
#             max_count = count
#             value = arr[i]
#             print(f"The value is: {value} , count is: {max_count}")


# repeated_number([2, 5, 1, 4, 9, 2, 1, 0, 2, 9, 9, 9])
# repeated_number([3, 3, 3, 2, 2, 1, 4, 3])
# repeated_number([10, 20, 20, 10, 20, 30, 10, 10])
# repeated_number([5, 1, 5, 2, 1, 5, 3, 2, 1])
