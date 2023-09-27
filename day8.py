# # # function and argument
# #
# # def greet_with_name(name):
# #     print(f"hello {name}")
# #     print(f"how do yo do?  {name}")
# # greet_with_name("piyush")
# # ## arguments are actual piece of data which is actually passing
# # ## parameters are name of data which is passing
# # def greer_with(name1, name2):
# #     print(f"hello {name1} and {name2}")
# # greer_with(name2="piyush", name1="angela")
#
# # import math
# # def paint_calc(height,width,cover):
# #     area=height*width
# #     num_of_cane=math.ceil(area/cover)
# #     print(f"You will need {num_of_cane} can of paints")
# # test_h = int(input("Height of wall : "))
# # test_w=int(input("Width of wall : "))
# # coverage=5
# # paint_calc(height=test_h,width=test_w,cover=coverage)
#
# # def prime_checker(number):
# #     is_prime=True
# #     for i in range(2,number):
# #         if number %i==0:
# #             is_prime=False
# #     if is_prime:
# #         print(f"{n} is a prime number")
# #     else:
# #         print(f"{n} is not a prime number")
# # n=int(input("check this number?\n"))
# # prime_checker(number=n)
#
#
# alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction=input("Type 'encode' to encrupt , Type 'decode' to decrupt:\n")
# text=input("Type your message\n").lower()
# shift=int(input("type shift number:\n"))
# def encrupt(plain_text,shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position + shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the encode text is {cipher_text}")
#
# def decrupt(cipher_text,shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         new_letter =alphabet[new_position]
#         plain_text +=new_letter
#     print(f"the decode text is {plain_text}")
#
# if direction=="encode":
#     encrupt(plain_text=text,shift_amount=shift)
# elif direction=="decode":
#     decrupt(cipher_text=text,shift_amount=shift)
# else:
#     print("invalid input")
