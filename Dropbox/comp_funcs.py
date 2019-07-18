#!/usr/bin/env checkio --domain=py run comp_funcs

# https://py.checkio.org/mission/comp_funcs/

# Okay, I guess we have to turn to plan B.
# What's plan B?
# Why wasn't that plan A?
# 
# 
# - The Big Band Theory : "The Lizard-Spock Expansion"
# 
# doveryai no proveryai (trust, but verify)
# 
# 
# - Russian proverb adopted as signature phrase by Ronald Reagan
# 
# 
# 
# Two functionsfandgare provided as inputs tocheckio.  The first functionfis     the primary function and the second functiongis the backup.  Use your coding skills to return a third functionhwhich returns the same output asfunlessfraises an exception or returnsNone.    In this casehshould return the same output asg.  If bothfandgraise exceptions    or returnNone, thenhshould returnNone.
# 
# As a second output,hshould return a status string indicating whether the function values are the same and    if either function erred.  A function errs if it raises an exception or returns a null value (None).
# 
# The status string should be set to: "same" iffandgreturn the same output and neither errs,    "different" iffandgreturn different outputs and neither errs, "f_error" ifferrs     but notg, "g_error" ifgerrs but notf, or "both_error" if both err.
# 
# Input:Two functions: f (primary) and g (backup).
# 
# Output:A function h which takes arbitrary inputs and returns a two-tuple.
# 
# Precondition:hasattr(f,'__call__');
# hasattr(g,'__call__')
# 
# 
# 
# END_DESC

def checkio(f,g):

    # Replace with your code
    def h(*args,**kwargs):
        return (f(*args,**kwargs),'same')
    return h

if __name__ == '__main__':
       
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"

    # Remove odds from list               
    f = lambda nums:[x for x in nums if ~x%2]
    def g(nums):
      for i in range(len(nums)):
        if nums[i]%2==1:
          nums.pop(i)
      return nums 
    assert checkio(f,g)([2,4,6,8]) == ([2,4,6,8],'same'), "evens, first"
    assert checkio(f,g)([2,3,4,6,8]) == ([2,4,6,8],'g_error'), "evens, second"         
    
    # Fizz Buzz    
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (6)==('Fizz','same'), "fizz buzz, first"      
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (30)==('Fizz Buzz','same'), "fizz buzz, second"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (7)==('7','different'), "fizz buzz, third"