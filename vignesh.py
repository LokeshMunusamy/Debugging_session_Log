# n = 7
# a=n
# for i in range(n):
#     a=a-1
#     for j in range(n):
#             if j==a or j==i:
#               print("*",end="")
#             else:
#                   print(" ",end="")

#     print()


# class Movie:

#     def __init__(self, title, total_seats):
#         self.title = title
#         self.total_seats = total_seats
#         self.booked_seats = 0

#     def book_ticket(self, seats):
#         if self.booked_seats + seats <= self.total_seats:
#             self.booked_seats += seats
#             print(f"{seats} seat(s) booked successfully for '{self.title}'.")
#         else:
#             print("Not enough seats available.")

#     def available_seats(self):
#         return self.total_seats - self.booked_seats

#     def display_status(self):
#         print(f"Movie: {self.title} | Available Seats: {self.available_seats()}")


# # Usage
# movie = Movie("Leo", 100)
# movie.display_status()
# movie.book_ticket(30)
# movie.book_ticket(50)
# movie.book_ticket(25)
# movie.display_status()


# class Details:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def add_attr(self, newKeyword, newValues):
#         setattr(self,newKeyword, newValues)


# person = Details("Vignesh", 20)

# print(f"Name: {person.name}, Age: {person.age}")

# person.add_attr("phoneno", "9876543210")

# person.add_attr("city", "Chennai")

# print(person.__dict__)

# Name: Vignesh, Age: 20
# {'name': 'Vignesh', 'age': 20, 'phoneno': '9876543210', 'city': 'Chennai'}


# # 8. Function with All Types
# # Create a function with the following signature:


# def config( app,/,*, mode="light", **extras):
#     return f"Positional-Only Arguments:{app}, Keyword-Only Arguments:{mode}, **kwargs:{extras}"
# print(config("myApp", mode="dark", version="1.0",font="arial"))

# Positional-Only Arguments:myApp, Keyword-Only Arguments:dark, **kwargs:{'version': '1.0', 'font': 'arial'}

# print(1<2>4)
