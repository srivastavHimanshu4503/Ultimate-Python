# 4. What will be the length of following set s:
# length of s after these operations?
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s)) # Ans: 2 as 20 and 20.0 are bascially same thing
