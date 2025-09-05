# 05/09/2025 Friday

# 1. Your order, please

# def order(sentence):
#     if sentence == '':
#         return ''
#     word=sentence.split(" ")
#     words=[' ']* len(word)
#     for i in word:
#         for j in i:
#             if j.isdigit():
#                 index=int(j) 
#                 words[index-1]=i
#     return ' '.join(words)
    

# print(order('is2 Thi1s T4est 3a'))      #output : Thi1s is2 3a T4est
# print(order(''))                        #output : 


#2. Find The Parity Outlier

# def find_outlier(integers):
#     three_value = integers[:3]
#     high_value = sum(num % 2 == 0 for num in three_value)   
#     majority_even = high_value >= 2 
#     for num in integers:
#         if majority_even and num %2 != 0:
#             return num
#         elif not majority_even and num %2 == 0:
#             return num

# print(find_outlier([160,3,17,100, 4, 11, 2602, 36]))  #output : 160
# print(find_outlier([160,61,100,18,12,4,36]))        #output : 61


# 3. Find all non-consecutive numbers

# def all_non_consecutive(arr):
#     result = []
#     i = 1
#     while i < len(arr):
#         if arr[i] != arr[i-1]+1 :
#             result.append({'i': i, 'n': arr[i]})
#         i += 1
#     return result

# print(all_non_consecutive([1,2,3,4,6,7,8,10]))     #output : [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}]


# 4. Pascal's Triangle

# numRows = 5
# output = []
# for i in range(0,numRows):
#     temp = []
#     for j in range(i+1):
#         if j == 0 or j == i:
#             temp.append(1)
#         else:
#             temp.append(output[i-1][j] + output[i-1][j-1])
#     output.append(temp)
# print(output)                  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]



# 5. Shuffle string


# def restoreString(s: str, indices: list) -> str:

#     result = [' '] * len(s)
#     print(result)
#     for i, char in enumerate(s):
#         result[i] = s[indices[i]]
        

#     return ''.join(result)

# print(restoreString('abdce',[0,1,3,2,4]))      #output : abcde



# 6.  Maximum number of this word 

# from collections import Counter

# def maxNumberOfWord(text: str, word: str) -> int:
#     text_count = Counter(text)
#     word_count = Counter(word)
    

#     max_times = 10000

#     for char in word_count:
#         if char not in text_count:
#             return 0
#         max_times = min(max_times, text_count[char] // word_count[char] )

#     return max_times
# print(maxNumberOfWord("loonbalxballpobonallnoo", "balloon"))    #output :2