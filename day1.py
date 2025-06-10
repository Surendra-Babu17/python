# user_number=int(input("enter a number"))
# rev=0
# temp=user_number
# while temp>0:
#     rem=temp%10
#     rev=(rev*10)+rem 
#     temp=temp//10
# if rev==user_number:
#     print("palindrome")
# else:
#     print("Not palindrome")



# user_input=int(input("enter a number:"))
convert_str=input("enter a string:")

rev=""
for char in convert_str:
    reverse=char+rev
if reverse==convert_str:
    print("palindrome")
else:
    print("Not PALINDROME")