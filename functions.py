# def my_func():
#     print("Hello world")

# my_func()

# def my_func(a,b):
#     res=a+b
#     print(res)
# my_func(10,39)

# def my_func(a,b):
#     res=a+b
#     return res
# ans=my_func(b=10,a=39)
# print(ans+30)

# def my_func(a,b):
#     res=a+b
#     return res
# ans=my_func(b=10,a=39)
# print(ans)
# print(ans+30)
# print(type(ans))

# name="Alice"
# age=23
# message="My name is " + name + " and I am " + str(age) + " years old."
# print(message)

# with f'string
# name="Alice"
# age=23
# message=f"My name is {name} and I am {age} years old."
# print(message)

# def my_func(a,b,c=15):
#     res = f"{a + c}"
#     print(b)
#     return res
# ans = my_func(a=12,b={"c":123 , "a":320})
# print(type(ans))

# if u specify ** it is said as keyword arguments which is kwargs
# def my_func(a,c=15,**b):
#     res = f"{a + c}"
#     print(type(b)) #dict
#     return res
# ans = my_func(a=12,b={"c":123 , "a":320})
# print(type(ans))

# def my_func(*args,**kwargs):
#     print(args,kwargs)
#     return
# ans=my_func(10,20,120,340,23,45,a=120,b=12)
# print(ans)

# def my_func(*args,**kwargs):
#     res=sum(args)
#     for v in kwargs.values():
#         res += v
#     return res
# ans=my_func(10,20,120,340,23,45,a=120,b=12)
# print(ans)

def my_func(a,b,*args,**kwargs):
    res=sum(args)
    for v in kwargs.values():
        res += v
    return res
ans=my_func(10,20,120,340,23,45,lik=67,abc=12)
print(ans)
