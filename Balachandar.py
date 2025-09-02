##1. Second largest number in a list

# a = [8,10,113,111,20,1000,500,19]
# largest=a[0]
# secLargest=a[0]

# for val in a:
#     if val > largest:
#         secLargest=largest
#         largest = val
#     elif(val>secLargest):
#         secLargest = val 
# print(secLargest,largest) 

##2.Longest substring

# def lengthOfLongestSubstring(s):
#     result=0
#     for i in range(len(s)):
#         temp=''
#         for j in s[i:]:
#             if j in temp: break
#             temp+=j
#             result=max(result,len(temp)) 
                              
#     return result

# print(lengthOfLongestSubstring("abcabcadefag"))


# a = "aa"

# if "a" in a:
#     print(True)


##3. Sort

# a = [9,5,10,7,2,4,1]

# i=0
# while i<len(a)-1:
#     j=i+1
#     while j<len(a):
#         if(a[i]<a[j]):
#             [a[i],a[j]]=[a[j],a[i]]
#             j=j+1
#         else:j=j+1    
#     i=i+1
# print(a)

# a = [9,5,10,7,2,4,1]
# i = 0
# while i < len(a)-1:
#     if a[i] > a[i+1]:
#         a[i],a[i+1] = a[i+1],a[i]
#         i = 0
#     else:
#         i += 1
# print(a)