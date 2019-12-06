import re

na = re.compile(r'(na)* Batman!')

t1 = "nana Batman!"
t2 = "nananana Batman!"
t3 = "nanananananananananananananananana Batman!"

f1 = na.search(t1)
f2 = na.search(t2)
f3 = na.search(t3)

print "%s" % f1.group()
print "%s" % f2.group()
print "%s" % f3.group()
print "%s" % f3.group(1)
print "%s" % f3.group(0)