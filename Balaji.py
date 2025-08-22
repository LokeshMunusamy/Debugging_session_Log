
# # week 1 - 22/08/2025

# # # 1. plus one 

# def plusOne(digits):
#     n = len(digits)
#     for i in reversed(range(n)):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         digits[i] = 0 
#     return [1] + digits

# print(plusOne([9,9,9])) 
# print(plusOne([1,2,9]))


# # # 2. search insert position

# def searchInsert(nums,target):
#     for i in range(0,len(nums)):
#         if nums[i] == target:
#             return i
#         elif nums[i] > target:
#             return i
#     return len(nums)

# print(searchInsert([1,2,4,5],1))
# print(searchInsert([1,2,4,5],2))
# print(searchInsert([1,2,4,5],6))


# # # 3. missing letters

# def missing_letters(s):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     result = ""
#     for ch in alphabet:
#         if ch not in s.lower():
#             result += ch
#     return result

# print(missing_letters("abcdefgp")) 
# print(missing_letters("xyz"))
# print(missing_letters("xYz"))



# # # 4. Find the Bugs: Returning Valid Prices

# def has_valid_price(product):
#     if product is None: 
#         return False
    
#     if "price" not in product:
#         return False
    
#     price = product["price"]

    
#     if (type(price) == int or type(price) == float) and price >= 0:
#         return True
#     else:
#         return False

# print(has_valid_price({ "product": "Milk", "price": 1.50 }))    
# print(has_valid_price({ "product": "Cheese", "price": -1 }))    
# print(has_valid_price({ "product": "Eggs", "price": 0 }))       
# print(has_valid_price({ "product": "Cereals", "price": "3.0" }))
# print(has_valid_price(None))         


# # # 5. likes vs dislikes

# def like_or_dislike(actions):
   
#     state = "Nothing"
    
#     for action in actions:
#         if action == state:  
#             state = "Nothing"
#         else:
#             state = action
    
#     return state

# print(like_or_dislike(["Dislike"]))                   
# print(like_or_dislike(["Like", "Like"]))              
# print(like_or_dislike(["Dislike", "Like"]))           
# print(like_or_dislike(["Like", "Dislike", "Dislike"]))


# # # 6. get_name

# def get_name(email):
#     name = ''
#     for ch in email:
#         if ch == "@": 
#             break
#         if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
#             name += ch
#     return name

# print(get_name("yourname@example.com"))       
# print(get_name("john64@gmail.com"))           
# print(get_name("pamela78_Cole@hotmail.com"))
# print(get_name("Chickenlololol29@yahoo.com"))


# # # 7. loves me / loves me not

# def loves_me(petals):
#     phrases = []
#     for i in range(petals):
#         if i % 2 == 0:
#             phrases.append("Loves me")
#         else:
#             phrases.append("Loves me not")
#     phrases[-1] = phrases[-1].upper()
#     return ", ".join(phrases)

# print(loves_me(3))
# print(loves_me(1))
# print(loves_me(4))


# # # 8. lost dog

# def lost_dog(*houses):
#     dogs = {}
#     dog_num = 1
#     for h in range(len(houses)):          
#         for r in range(len(houses[h])):   
#             if houses[h][r] == 0:         
#                 dogs[f"Dog{dog_num}"] = f"House ({h+1}) and Room ({r+1})"
#                 dog_num += 1
    
#     if dogs:
#         return dogs
#     else:
#         return "Dog not found!"


# print(lost_dog([1,0,1,0,1,1], [1,1,1,1,1,1]))
# print(lost_dog([1,1,1,1,1,1], [0,1,1,1,1,1]))

