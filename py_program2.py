# FInd Duplicate Character

# def duplicate(s):
#     d = {}
#     for i in s:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     for i in d.values():
#         if i>1:
#             return True
#
#
# print(duplicate("Hello"))




# Is 13th a friday

# from datetime import date
# def hasfriday(y,m):
#     res = date(y,m,13).strftime("%A")
#     if res == "Friday":
#         return True
#     else:
#         return False
#
# print(hasfriday(2020,4))




# Find Domain

# import socket
#
# def find_domain(ip):
#     res = socket.gethostbyaddr(ip)
#     return list(res)[0]
#
# print(find_domain("192.168.1.5"))



# Get Dictronary eleminating 0s

# def get_detaiils(s):
#     b = s.split('0')
#     c = []
#     for i in b:
#         if i != "":
#             c.append(i)
#     d = {'fn': c[0], 'ln': c[1], 'dept': c[2]}
#     return d
#
# print(get_detaiils("Avneesh00000Kumar00000CS"))


# decimal to hexadecimal
#
# def dec_to_hex(n):
#     i = 0
#     l = []
#     hex = ""
#     while n>0:
#         rem = n%16
#         if rem<10:
#             rem = rem+48
#         else:
#             rem = rem+55
#         l.insert(i,chr(rem))
#         i = i+1
#         n = int(n/16)
#     for i in l:
#         hex = hex+i
#     return hex
#
# print(dec_to_hex(107))


# decimal to octol

# def dec_to_octo(n):
#     oct = []
#     strr = ""
#     while n>0:
#         rem = n % 8
#         oct.append(rem)
#         n = int(n/8)
#     oct = oct[::-1]
#     for i in oct:
#         strr = strr+str(i)
#     return strr
#
# print(dec_to_octo(33))


# Reverse Number

# def reverse_no(n):
#     temp = n
#     rev = 0
#     while temp>0:
#         rem = temp%10
#         rev = rev*10 + rem
#         temp = int(temp//10)
#     return rev
#
# print(reverse_no(5487))
#


# fibbinacci using recursion

#
# def fibb_using_recursion(n):
#     if n <= 1:
#         return n
#     else:
#         return fibb_using_recursion(n-1) + fibb_using_recursion(n-2)
#
# num = 10
# for i in range(num):
#     print(fibb_using_recursion(i))



# avarage of numbers

# def avarage(l):
#     sum = 0
#     list_len = len(l)
#     for i in l:
#         sum = sum+i
#     return int(sum//list_len)
#
#
# print(avarage([5,5,5,]))



# Convert Temprature

# def celsius_to_faranite(n):
#     return n*9/5 + 32
#
# print(celsius_to_faranite(50))
#
#
# def faranite_to_celsius(n):
#     return ((n-32)*5)/9
#
# print(faranite_to_celsius(122))



# Maximun and Minimum

#
# def max_and_min_num(l):
#     maxi = l[0]
#     mini = l[0]
#     for i in l:
#         if i > maxi:
#             maxi = i
#         if i < mini:
#             mini = i
#     return mini,maxi
#
# print(max_and_min_num([4,1,8,5,9,50,4,85]))




# 2nd largest number

# def second_largest(l):
#     first = l[0]
#     second = l[1]
#     for i in l:
#         if i > first:
#             second = first
#             first = i
#         elif second > i and first != i:
#             second = i
#     return first,second
#
# print(second_largest([4,5,1,8,7,9,9]))



# insert elememt at last
#
# def insert_eement_at_last(l,n):
#     lenn = len(l)
#     l.insert(lenn,n)
#     return l
#
# print(insert_eement_at_last([1,2,3,4],5))


# sort and merge array

#
# def sort_array_and_merge(l1,l2,l3):
#     n1 = len(l1)
#     n2 = len(l2)
#     i,j,k = 0,0,0
#     while i<n1:
#         l3.insert(k,l1[i])
#         i += 1
#         k += 1
#     while j<n2:
#         l3.insert(k,l2[j])
#         j += 1
#         k += 1
#     l3.sort()
#     return l3
#
# print(sort_array_and_merge([1,5,4],[4,5,8],[]))



# Format the number place , in thousand position
#
# def format_no(n):
#     temp = str(n)
#     t = temp[::-1]
#     new_str = ""
#     count = 0
#
#     for i in t:
#         count = count+1
#         if count%3 == 0:
#             if len(t) == count:
#                 new_str = i + new_str
#             else:
#                 new_str = ',' + i +new_str
#         else:
#             new_str = i + new_str
#     print(new_str)


# format_no(1000)



# program for check all the values are true

# def triple_and(bool1,bool2,bool3):
#     if bool1 and bool2 and bool3:
#         return True
#     return False
#
# print(triple_and(True,True,True))
#


# Check all the element of list are equal
#
# def all_equal(l):
#     temp = False
#     for i in l:
#         if i != l[0]:
#             temp = False
#             break
#         else:
#             temp = True
#     if temp == True:
#         return True
#     else:
#         return False
# print(all_equal([1,1,1,1]))


# Palindrom String
#
# def palindrom_str(s):
#     n = len(s)
#     flag = False
#     for i in range(n):
#         if s[i] != s[n-i-1]:
#             flag = False
#             break
#         else:
#             flag = True
#     if flag:
#         return True
#     else:
#         return False
# print(palindrom_str("nitinn"))
#



# Add first and last digit

# def add_first_last_digit(n):
#     last = n%10
#     first = 0
#     while n>9:
#         n = n//10
#         first = n
#     return first+last
#
# print(add_first_last_digit(1218))



# Convert list into dict

# def list_to_dict(l):
#     d = {}
#     for i in l:
#         mid = len(str(i))//2
#         key = int(str(i)[:mid])
#         val = int(str(i)[mid:])
#         d[key] = val
#     return d
#
# print(list_to_dict([15,45,8877,747]))
#



# Convert string into dict

#
# def str_to_dict(s):
#     l = s.split(" ")
#     d = {}
#     for i in l:
#         key = i[:1]
#         val = i
#         d[key] = val
#     print(d)
#
# str_to_dict("Hello World")




# def specific_digit(l,digit):
#     l1 = []
#     for i in l:
#         c = str(i)
#         for s in c:
#             if str(digit) in s:
#                 l1.append(c)
#                 break
#     print(l1)
#
# specific_digit([10,50,44,88,4,64],4)












# def extract_tuple(l,k):
#     res = [sub for sub in l if all(len(str(ele)) == k for ele in sub)]
#     print(res)
#
# extract_tuple([(11,1),(11,45),(74,87)],2)





# def extract_tuple(l,k):
#     l1 = []
#     for sub in l:
#         for ele in sub:
#             if all(len(str(ele))) == k:
#                 l1.append(sub)
#     print(l1)
#
#
# extract_tuple([(11,1),(11,45),(74,87)],2)


# Print adjecent element

# def adjecant_ele(l):
#     l1 = []
#     for i,ele in enumerate(l):
#         if i == 0:
#             l1.append((None,l[i+1]))
#         elif i == len(l) - 1:
#             l1.append((l[i-1],None))
#         else:
#             l1.append((l[i-1],l[i+1]))
#     return l1
#
#
# print(adjecant_ele([1,2,4,8,]))
#


# chech dict values are equals

# def dict_equal_value(d):
#     l = list(d.values())[0]
#     res = False
#     for i in d:
#         if d[i] != l:
#             res = False
#             break
#         else:
#             res =  True
#     return res
# print(dict_equal_value({'a':1,'b':10}))
#



# def list_dict(l):
#     d = {}
#     for i in l:
#         i = str(i)
#         midx = len(i)//2
#         key = i[:midx]
#         val = i[midx:]
#         d[key] = val
#     print(d)
#
# list_dict([11,1147,478,85])


# Match the list value in 2nd list

#
# def match_list(l1,l2):
#     l3 = []
#     for i in l1:
#         i = str(i)
#         for j in l2:
#             j = str(j)
#             if j not in i:
#                 break
#             else:
#                 l3.append(i)
#                 break
#
#     print(l3)
#
# match_list([23,235,47,875,2],[2,3,5])
#

#Find the orderd Substring

#
# def find_substring_order(s1,s2):
#     res = ""
#     for i in s1:
#         if i in set(s2):
#             res = res + str(i)
#     v = s2 in res
#     return v
#
#
# print(find_substring_order("geeksforgeeks","seek"))
#




# def slice_dict(d,k):
#     for i,j in d.items():
#         d[i] = j[:k]
#     print(d)
#
#
# slice_dict({"A":[4,8,7],"B":[8,7,5,8],"C":[8,7,9,7],"D":[88,78,9,5]},2)


# def check_dict_value(d):
#      l = list(d.values())
#      res = False
#      for i in d.values():
#          if i != l[0]:
#              res = False
#              break
#          else:
#              res = True
#      return res
#
#
#
# print(check_dict_value({1:1,2:1,3:1,4:1}))
#


 # list and dict comprehension

#
# f = ['apple','banana','mango','orange']
# # f1 = [x for x in f if x!= 'apple']
# # print(f1)
#
# f2 =["orange" if x == 'apple' else x for x in f]
# print(f2)



# n = [x for x in range(10)]
# print(n)





# t = [(11,2),(54,21),(55,74),(7,88)]
#
# l = [x for x in t if all(len(str(ele)) == 2 for ele in x)]
# print(l)
#




# l1 = [1,2,3,4]
# l2 = ['apple','banana','mango','orange']
# t = zip(l1,l2)
# d = {k:v for k,v in t}
# print(d)

# d1 = {x:x*2 for x in l1}
# print(d1)

# d2 = {x.upper():x[:1] for x in l2}
# print(d2)



# d3 = {x:x for x in range(10) if x%2 == 0}
# print(d3)




# Start Pattern




# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#     print()

# *
# **
# ***
# ****






# n= 5
# for i in range(n):
#     for j in range(n,i,-1):
#         print("*",end="")
#     print()

# ****
# ***
# **
# *



# n=6
# for i in range(1,n):
#     for j in range(i,n-1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

#     *
#    **
#   ***
#  ****
# *****



# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n,i,-1):
#         print("*",end="")
#     print()

 # ****
 #  ***
 #   **
 #    *





# n = 7
# for i in range(1,n):
#     for j in range(i,n-1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     for j in range(i-1):
#         print("*",end="")
#     print()


#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#





# n = 7
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-1,i,-1):
#         print("*",end="")
#     for j in range(n,i,-1):
#         print("*",end="")
#     print()


# *************
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *


# n = 5
#
# for i in range(n):
#     for j in range(i,n-1):
#         print(" ",end="")
#     for j in range(i-1):
#         print("*",end="")
#     for j in range(i-1):
#         print("*",end="")
#     print()
#
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-2,i,-1):
#         print("*",end="")
#     for j in range(n-1,i,-1):
#         print("*",end="")
#     print()


#
# def sort_num(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i] == 0:
#                 l[i],l[j] = l[j],l[i]
#     print(l)
#
#
# sort_num([4,5,0,4,0,0,8,0,8,8,7])




# def sort_num(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 a = l[i]
#                 l[i] = l[j]
#                 l[j] = a
#     print(l)
#
#
# sort_num([4,5,0,4,0,0,8,0,8,8,7])


