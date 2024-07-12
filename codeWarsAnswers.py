#I'll post my answer and then the most "clever" answer with my explanation on how each works

#1. removing vowels from a string

# def disemvowel(string_):
#     ans = ""
#     vowels = "AEIOU"
#     for x in string_:
#         if x.upper() not in vowels:
#             ans += x
#     return ans


#I was just checking it against the vowels in uppercase to get the case problem out of the way, adding it back to an empty string, mostly because I was worried about string immuatbility, but also something with iterating ints came up

# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")

#list combined after comprehension by using a loop and NOT IN keyword, I'm gona look up the syntax for the LH: [expression for item in iterable if condition]


###############################

#2. checking if one array is a squared version of the other

# def comp(array1, array2):
#     if array1 is None or array2 is None:
#         return False
#     squaredList = []
#     for x in array1:
#         squaredList.append(x**2)
#     squaredList.sort()
#     array2.sort()
#     if squaredList == array2:
#         print(squaredList)
#         print(array2)
#         return True
#     else:
#         print(squaredList)
#         print(array2)
#         return False

#That took a very long time to figure out the edge cases where None was involved. I was just hardcoding it until I put the first evaluation of the arrays for None

#def comp(array1, array2):
#   try:
#       return sorted([i ** 2 for i in array1]) == sorted(array2)
#   except:
#       return False

#List comprehension again, but this one I don't think will get the edge cases of None, tried to read through the comments, but no one knew, just commented that it's bad practice in O(n*log) where it's a O(n) problem
#I see it now, the try and except catch the edges cases of None, clever. Still don't understand if it's bad time complexity or not