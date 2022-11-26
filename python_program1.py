# new_ar = []
#
# def largetst_no(ar):
#     for i in range(len(ar)):
#         if ar[i] < ar[i+1]:




# Palindrome no

# def palindrome(s):
#     temp = s[::-1]
#     if s == temp:
#         return True
#     else:
#         return False
#
# a = "nitin"
# print(palindrome(a))
#


#
# def palindrome(s):
#     n = len(s)
#     for i in range(n):
#         if s[i] != s[n-i-1]:
#             return False
#         return True
#
# a = "jnitinj"
# print(palindrome(a))

#
# def palindrome(s):
#     temp = "".join(reversed(s))
#     if s == temp:
#         return True
#     return False
# a = "nitin"
# print(palindrome(a))


# def palindrome(s):
#     n = len(s)
#     first = 0
#     last = n-1
#     while first < last:
#         if s[first] == s[last]:
#             first += 1
#             last -= 1
#             return True
#         return False
#
# a = "nitin"
# print(palindrome(a))



# def palindrom_num(num):
#     temp = num
#     rev_num = 0
#     while(temp>0):
#         digit = temp % 10
#         # print(digit)
#         rev_num = rev_num * 10 + digit
#         print(rev_num)
#         temp = temp // 10
#     if num == rev_num:
#         return True
#     return False
#
# a = 1212
# print(palindrom_num(a))





# Fibbonacii series

# def fibbi(n):
#     a,b = 0,1
#     print(a)
#     while b<n:
#         print(b)
#         # c = a+b
#         # a = b
#         # b = c
# #         or
#        # a,b = b,a+b
#
# fibbi(50)



# def fibb(n):
#     a,b = 0,1
#     if (n == 1):
#         print(a)
#         print(b)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             a,b = b,a+b
#             print(b)
#
# fibb(10)


# def fibbi(n):
#     if n<=1:
#         return n
#     else:
#         return fibbi(n-1) + fibbi(n-2)
#
# num = 10
# if num <= 0:
#     print("Invalid")
# else:
#     for i in range(num):
#         print(fibbi(i))




# def string_count(s):
#     n = len(s)
#     new_str = ''
#     count = 1
#     for i in range(n-1):
#         if s[i] == s[i+1]:
#             count += 1
#         else:
#             new_str = new_str + s[i] + str(count)
#             count = 1
#     new_str = new_str + s[n-1] + str(count)
#     return new_str
#
# a = "aabbbcccchhhh"
# print(string_count(a))


# fizz buzz
#
# def fizz_buzz(n):
#     for i in range(1,n):
#         if i%3 == 0 and i%5 == 0:
#             print("fizzbuzz")
#         elif i%3 == 0:
#             print("fizz")
#         elif i%5 == 0:
#             print("buzz")
#         else:
#             print(i)
#
# fizz_buzz(50)


# def fizz_buzz(n):
#     d = {3:"Fizz",5:"Buzz"}
#     for i in range(1,n+1):
#         res = ""
#         for k,v in d.items():
#             if i%k == 0:
#                 res = res+v
#         if not res:
#             res = i
#         print(res)
#
# fizz_buzz(20)


# least count char

# def count_char(s):
#     ch = {}
#     for i in s:
#         if i in ch:
#             ch[i] += 1
#         else:
#             ch[i] = 1
#     result = min(ch , key=ch.get)
#     print(ch)
#     print(result)
#
# count_char("absfgsbxbgsfsfbbbvv")


# from collections import Counter
# s = "jhshsvbvbahgsvsba"
# ch = Counter(s)
# result = max(ch,key=ch.get)
# print(result)



# Prime no

# def prime(n):
#     flag = False
#     for i in range(2,n//2+1):
#         if n%i == 0:
#             flag = True
#             break
#     if flag:
#         print("Not Prime")
#     else:
#         print("Prime")
#
# prime(4)
#


# def prime(n):
#     for i in range(2,n//2+1):
#         if n%i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
#
# prime(14)


# def prime(start,end):
#     for n in range(start,end):
#         for i in range(2,n//2+1):
#             if n%i == 0:
#                 # print("Not Prime")
#                 break
#         else:
#             print(n)
#
# prime(10,50)


# String Manipulation

# def str_mod():
#     s = "Hello_This_Is_Avneesh"
#     l = []
#     temp = s.split('_')
#     print(temp)
#     for i in temp:
#         l.append(i[0].lower() + i[1:].upper())
#     print(l)
#     new_s = ".".join(l)
#     print(new_s)
#
# str_mod()

# def str_man():
#     s = "Hello_This_Is_Avneesh"
#     new_s = ""
#     temp = s.split('_')
#     for i in temp:
#         new_s = new_s + i[0].lower() + i[1:].upper() + '.'
#     print(new_s[:-1])
#
# str_man()


# 2nd maximum no
#
# def second_max(l):
#     if l[0] > l[1]:
#         first = l[0]
#         second = l[1]
#     else:
#         first = l[1]
#         second = l[0]
#     for i in range(2,len(l)):
#         if l[i] > first:
#             second = first
#             first = l[i]
#         elif l[i] > second and first != l[i]:
#             second = l[i]
#     return second
#
#
# print(second_max([1,5,8,6,10,165,165]))



# def secons_max():
#     l = [1,5,5,4,7]
#     s = set(l)
#     s.remove(max(s))
#
#     print(max(s))
# secons_max()
#





# Armstromg

# def armstrong_num(n):
#     temp = n
#     sum = 0
#     while temp >0:
#         digit = temp%10
#         sum = sum+(digit**3)
#         temp = temp//10
#     if sum == n:
#         print("Armstrong")
#     else:
#         print("Not armstrong")
# 
# armstrong_num(153)




# def armstrong_num(m):
#     for n in range(1,m):
#         temp = n
#         sum = 0
#         while temp >0:
#             digit = temp%10
#             sum = sum+(digit**3)
#             temp = temp//10
#         if sum == n:
#             print(n)
#
#
# armstrong_num(2000)




# SUm of Digits

# def sum_of_digit(n):
#     temp = n
#     sum = 0
#     while temp>0:
#         digit = temp%10
#         sum = sum+digit
#         temp = temp//10
#     print("SUm of Digit Is: ",sum)
#
# sum_of_digit(1412)



# Factorial

# def fact(n):
#     res = 1
#     for i in range(1,n+1):
#         res = res * i
#     return res
#
# def new_fact(n):
#     temp = n
#     fact_res = 0
#     while temp>0:
#         digit = temp%10
#         fact_res = fact_res + fact(digit)
#         temp = temp // 10
#     if n == fact_res:
#         print("It is ok")
#     else:
#         print("Not Ok")
#
# new_fact(145)


# Iterator

# l = ['Avneesh',"Kumar","Verma","Shivani Sharma"]
# d = {1:"Avneesh",2:"Shivani"}
# mem = iter(d.items())
# print(next(mem))
# print(next(mem))

# mem = iter(l)
# print(next(mem))
# print(next(mem))
# print(next(mem))
# print(next(mem))
# for i in mem:
#     print(i)
#




# Generator

# def func():
#     print("Avneesh")
#     yield 10
#     print("Shivani")
#     yield 20
#
# mem = func()
# print(next(mem))
# print(next(mem))







