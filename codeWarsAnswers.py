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

#list combined after comprehension by using a loop and NOT IN keyword, I'm gona look up the syntax for the LH