#!/usr/bin/env python
# coding: utf-8

# 1) What are the two values of the Boolean data type? How do you write them?

# In[ ]:


Answer: The possible two values of boolean data type are True and False. In which True represents 1 and False represents 0.
        In these two data types first letter would be in capital followed by lower cases.


# 2)  What are the three different types of Boolean operators?

# In[ ]:


Answer: The three different types of boolean operators are and, or, not.


# 3) Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# In[ ]:


Answer: x and y: True True = True
                 True False= False
                 False True= True
                 False False= False
                    
        x or y:  True True= True
                 True False=True
                 False True=True
                 False False=False
                
        x not y: False =True
                 True =False
                 
        


# 4) What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
# 

# In[1]:


(5 > 4) and (3 == 5)


# In[2]:


not (5 > 4)


# In[3]:


(5 > 4) or (3 == 5)


# In[4]:


not ((5 > 4) or (3 == 5))


# In[5]:


(True and True) and (True == False)


# In[6]:


(not False) or (not True)


# 5) What are the six comparison operators?

# In[ ]:


Answer: Less than(<)
        Less than or equal to(<=)
        Greater than(>)
        Greater than or equal to(>=)
        Equal to(==)
        Not equal to(!=)


# 6) How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# In[ ]:


Answer: = is an assignment operator which is used to assign a value to a variable but == is an operator which checks
          whether the two operands are equal or not.
For example:
    a=10
    b=20
    a+b 
where = is an assignment operator
 
Another example:
    a=1
    b=1
    if a==b:
        print('equal')
in this case == is a comparison operator


# 7) Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 

# In[9]:


spam = 0
if spam == 10:
 print('eggs')
if spam > 5:
 print('bacon')
else:
 print('ham')
print('spam')
print('spam')


# In[ ]:


Answer: The three blocks are everything inside the if statement. The line print('eggs'), print('bacon') and print('ham')
        are the three blocks.


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[5]:


spam=int(input('enter spam:'))
if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings!')


# 9. If your programme is stuck in an endless loop, what keys you’ll press?

# In[ ]:


Answer: ctrl+c


# 10. How can you tell the difference between break and continue?

# In[ ]:


Answer: break statement stops the loop in the program. It eliminates the execution of remaining iterations of the loop.
        continue statement instructs the loop to continue to the next iteration. It can be used to skip over part of a loop
        when a condition is met.
        


# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[ ]:


Answer:
1)range(10) takes 10 as the lower bound and returns value from 0 to 9 in list format by omitting the lower bound which is 10.
  Here upper bound is not present.
2)range(0,10) assigns 0 as the upper bound and 10 as lower bound. This also acts same like the above range function and 
  returns value from 0 to 9.
3)range(0,10,1) has 0 in place of upper bound, 10 in place of lower bound and indicates 1 as the step size. This also gives
  the same result as above since even if we did not mention the step size it by default take it as 1. So the above three 
  gives the same result


# In[5]:


list(range(10))


# In[6]:


list(range(0,10))


# In[7]:


list(range(0,10,1))


# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[10]:


for i in range(1,11):
    print(i)


# In[1]:


i=1
while(i<=10):
    print(i)
    i+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 

# In[ ]:


Answer: spam.bacon()

