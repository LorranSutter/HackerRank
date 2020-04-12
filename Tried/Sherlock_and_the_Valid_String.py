# Cases aaaaabc and aaaaabbcc does not work

from collections import Counter

s = input()
print(s)
s = Counter(s)
print(s)
s = s.values()
print(s)
s = Counter(s)
print(s)

if len(s) == 1:
    print('YES')
if len(s) > 2:
    print('NO')
if min(s.values()) == 1:
    print('YES')
print('NO')

# if len(s) == 1:
#     print('YES')
# elif len(s) > 2:
#     print('NO')
# else:
#     keys = [k for k in s.keys()]
#     if abs(keys[0] - keys[1]) == 1:
#         print('YES')
#     else:
#         print('NO')
    
#     # minKey = min(s, key=s.get)
#     # if max(s.values()) - 1 == min(s.values()):
#     #     print('YES')
#     # else:
#     #     print('NO')
