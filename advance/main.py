def outter(name:str):
    def inner(message:str):
        print(f"{name} says: {message}")
    return inner

fn = outter("jay")
fn("hello") # jay says: hello

def atm(amount: int):
    def transaction(change:int, isDeposit:bool = True):
        nonlocal amount
        if(isDeposit):
            amount+= change;
        else:
            amount-=change
        print(f"after the transaction, amount is {amount}")
    return transaction
myatm = atm(0)
myatm(100)# after the transaction, amount is 100
myatm(100)# after the transaction, amount is 200
myatm(100, False)# after the transaction, amount is 100



def decorator_outer(func):
    def inner():
        print("before the call")
        func()
        print("after the call")
    return inner

@decorator_outer
def say_hello():
    print("hello")

fn = decorator_outer(say_hello)
fn()

say_hello()
# singleton

from singleton import s1
print(id(s1))
print(id(s1))