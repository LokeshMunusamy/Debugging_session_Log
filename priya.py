# balanced charecter

# def is_balanced(word):
#     word = word.upper()
#     mid = len(word) // 2

#     left = word[:-mid]
#     # print(left)
#     right = word[mid:]

#     left_sum = sum(ord(c) - 64 for c in left)
#     # print(left_sum)
#     right_sum = sum(ord(c) - 64 for c in right)
#     # print(right_sum)

#     return left_sum == right_sum

# print(is_balanced("ABCDCBA"))  # True
# print(is_balanced("STEAD"))    # False
# print(is_balanced("XYX"))      # True


# =================================================

# class Rectangle:
#     def __init__(self,width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# r = Rectangle(4, 5)
# print("Area:", r.area())         # 20
# print("Perimeter:", r.perimeter())  # 18


# =====================================================
# secound largest

# def second_largest(lst):
#     unique = list(set(lst))
#     unique.sort(reverse=True)
#     return unique[1] 
#     # return 

# print(second_largest([1, 4, 5, 3, 5]))  # Output: 4


# =====================================================

# def rotate_right(lst, k):
    
#     k = k % len(lst)
#     print(k)
#     return lst[-k:] + lst[:-k]

# print(rotate_right([1, 2, 3, 4, 5], 2)) 

# 4,5,1,2,3

# ==========================================

# def is_custom_pangram(sentence, alphabet):
#     sentence_set = set(sentence)
#     return set(alphabet).issubset(sentence_set)

# tamil_alphabet = "அஆஇஈஉஊஎஏஐஒஓஔக்ங்ச்ஞ்ட்ண்த்ந்ப்ம்ய்ர்ல்வ்ழ்ள்ஹ"
# sentence = "அஆஇஈஉஊஎஏஐஒஓஔகங்சஞ்ட்ண்த்ந்ப்ம்ய்ர்ல்வ்ழ்ள்ஹ"

# print("Is Tamil Pangram:", is_custom_pangram(sentence, tamil_alphabet))


# ===========================================

# class Song:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist

#     def play(self):
#         print(f"🎵 Now playing: {self.title} by {self.artist}")

# class Playlist:
#     def __init__(self):
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)
#         print(id(self.songs))

#     def remove_song(self, title):
#         self.songs = [s for s in self.songs if s.title != title]
#         # print(self.songs)

#     def play_all(self):
#         for song in self.songs:
#             song.play()

# # Usage
# p = Playlist()
# p.add_song(Song("Shape of You", "Ed Sheeran"))
# p.add_song(Song("Believer", "Imagine Dragons"))
# p.remove_song(Song("Shape of You","Ed Sheeran"))
# p.play_all()

# ===========================================================

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def apply_discount(self, percent):
#         discount = self.price * (percent / 100)
#         self.price -= discount
#         return self.price

# p = Product("Headphones", 200)
# print(p.apply_discount(10))  # 180.0


# ===========================================

# import random

# def play_rps(user_choice):
#     options = ["rock", "paper", "scissors"]
#     computer = random.choice(options)
#     print(f"Computer chose: {computer}")

#     if user_choice == computer:
#         return "It's a tie!"
#     elif (user_choice == "rock" and computer == "scissors") or \
#          (user_choice == "paper" and computer == "rock") or \
#          (user_choice == "scissors" and computer == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# print(play_rps("rock"))
