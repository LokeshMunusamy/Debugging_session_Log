# Date: 12/09/2025

users = [
            {"Id": 2, "Name" : "Divakar", "Age": 70, "Gender": "Male"}, 
            {"Id": 1, "Name" : "Lokesh", "Age": 21, "Gender": "Male"}, 
            {"Id": 3, "Name" : "Lokeshwara", "Age": 22, "Gender": "Male"}, 
            {"Id": 4, "Name" : "Bala", "Age": 40, "Gender": "Male"}, 
            {"Id": 5, "Name" : "Vignesh", "Age": 35, "Gender": "Male"}
        ]   


# # Question 1
# for user in users:

#     if user.get("Name", False):
#         print(f"Name: {user['Name']}, Age: {user['Age']}, Gender: {user['Gender']}")


# # Question 2
# update = list(map(lambda user : {**user,"Age" : 25} if user["Id"] == 2 else user, users))

# print(update)


# Question 3

# ids = list(map(lambda u: u['Name'], filter(lambda u: u['Age'] > 30, users)))
# print(ids)

#question 4

# result = list(map(lambda u: 
#     f"Young User: {u['Name']}" if u['Age'] < 25 else 
#     f"Adult User: {u['Name']}" if u['Age'] <= 50 else 
#     f"Senior User: {u['Name']}",
#     users))

# print(result)


# Question 5 Pascal's Triangle II

# def getRow(rowIndex):
#     output = []
#     for i in range(rowIndex+1):
#         temp = [1,]
#         for j in range(i+1):
#             if j == 0 or i == j:
#                 temp.append(1)
#             else:
#                 temp.append(output[i-1][j-1] + output[i-1][j])
                
#         output.append(temp)
#     return output[rowIndex]

# print(getRow(3))


# Question 7 remove dupicates

# l = [2,2,2,3,4,6,7,2,3,4,6,8]

# for i in range(len(l)-2, -1, -1):
#     for j in range(i+1,len(l)):
#         if l[i] == l[j]:
#             l.pop(i)
#             break
# print(l)