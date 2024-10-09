import re

s = "python itheima"
result = re.match("python",s)# only start from beginning
print(result)
result = re.search("python",s)
print(result)
result = re.findall("python",s)
print(result)

s = "itemheima1@python2 !! 66"
result = re.findall(r'\d',s)
print(result)

result = re.findall(r'[a-zA-Z]',s)
print(result)

