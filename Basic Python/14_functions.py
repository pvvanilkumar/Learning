#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Simple function
def hello():
    pass
hello()


# In[ ]:


#function with single argument
def hello(name):
    print("Hello {}, how are you doing today?".format(name))
hello('Ujwal')
    


# In[ ]:


#function with two arguments
def add(x,y):
    return x+y
print(add(100,10))
z=add(3,10)
print(z)


# In[ ]:


#function with default arguments
def circle(radius,pi= 3.14159):
    return pi*radius**radius
print(circle(3))
print(circle(5,3.14))


# In[ ]:


#fuction with keyword arguments
def hello(name,age):
    return "Hello {} you are {} years old ".format(name,age)
print(hello(age=19,name='Ujwal'))
print(hello('Vishal',17))


# In[ ]:


#function that returns multiple values
def calculator(a,b):
    return a+b, a*b, a-b
print(calculator(9,20))


# In[ ]:


#doc String
#function with default arguments
def circle1(radius,pi= 3.14159):
    '''
    Function returns area of circle
    Formula : pi*r*r
    '''
    return pi*radius**radius
print(circle1(3))
print(circle1(5,3.14))
help(circle1)

