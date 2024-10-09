print(f"name: {__name__}")
print("hello world")
name = "hei ma is great for what"
print(len(name))
print(name.title())


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"string {data} length is {count}")


my_len("heima")


def print_type(input):
    """
    this is to print input type
    :param input: input to check
    :return: type
    """
    result = type(input)
    print(f"input {input} typ is {result}")


print_type(2)

print_type("asd")
print_type(True)
print_type(1.1)
print_type(my_len("a"))
print_type(["asd"])
print_type(("asd","as"))
print_type({"asd"})
print_type({"asd":1,"as":2})
list = [1,2,3,4,9,1,2,3,1]
for i,value in enumerate(list):
    print(f"element {i} is {value}")

print(f"list count {list.count(1)}")

mytuple = (1,2,3,8)
print(f"len of tuple: {len(mytuple)}")

for i,value in enumerate("abc"):
    print(f"element  {i} is {value}")

list=[0,1,2,3,4]
print(list[0:5:2])

