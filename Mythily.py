#==========Remove evens

# def remove_evens(nums):
#     for num in nums:
#         if num % 2 == 0:
#             nums.remove(num)
#     return nums

# print(remove_evens([2, 4, 6, 7, 8, 9]))

#=============Adding value to dict according to length

# def group_by_length(words):
#     groups = {}
#     groups=''
#     for word in words:
#         key = len(word)
#         groups.get(key,[]).append(word)
#     return groups

# print(group_by_length(["a", "at", "bat", "cat", "dog", "me", "i"]))


#==============class variables and instance variables diff


# class Student:
#     grades = []

#     def __init__(self, name):
#         self.name = name

#     def add_grade(self, grade):
#         self.grades.append(grade)

# s1 = Student("Arun")
# s2 = Student("Priya")

# s1.add_grade(90)
# s1.add_grade(100)
# s2.add_grade(80)

# print(s1.grades)
# print(s2.grades)

#===========Change lowercase to uppercase

# def to_uppercase(s):
#     for ch in s:
#         if ch.islower():
#             ch.upper()
#     return s

# print(to_uppercase("hello"))

#===========Find First Non-Repeating Character

# s = "aabbccd"
# #o/p : 6
# for ch in s:
#     count=1
#     if ch.count(s) == 1 :
#         if ch.count(s)!=1:
#             print(s.index(ch))
#         else:
#             print(-1)

#==========count words starting with vowel

# sentence = "An apple a day keeps the doctor away ee u"
# wordss = sentence.split()
# count = 0
# vowels = "aeiou"
# for words in wordss:
#     if wordss is vowels:
#         count += 1
# print(count)

#=========Check Armstrong Number

# num = 153
# total = 1
# for n in str(num):
#     total += int(n)*3
#     if n == num:
#         print("Armstrong")
#     else:
#         print("Not Armstrong")

#==========remove duplicate elements

# data = [(1,2),(2,3),(1,2),(4,5),(5,8),(5,8)]
# unique = None
# for item in data:
#     if item == unique:
#         unique=item
# print(unique)


#========find anagram and display the index

# s = "cbaebabacd"
# p = "abc"
# temp=[]

# for i,e in enumerate(s):
#     sp=s[i:len(p)]
#     if "".join(sorted(sp)) == p:
#         temp.append(i)
# print(temp)

#========list is empty

# def squares(n):
#     result = (i*i for i in range(n))
#     return (result)

# gen = squares(5)
# print(list(gen))
# print(list(gen))

###############################