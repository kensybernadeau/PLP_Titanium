

p = list()
p.append("a")
p.append("b")
p.append("c")
p.append("d")
p.append("e")
print(p)
p[0] = (p[3], p[1])
print(p[0])

print(p)
print(p[0][1])