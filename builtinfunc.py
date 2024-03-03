from functools import reduce
import operator 
  

def multi(numbers):
    if not numbers:
        return None
    else:
        return reduce(operator.mul,numbers)
list=[1,2,3,4,5]
print(multi(list))



def calculate(letter):
    sum1=0
    sum=0
    for i in letter:
        if 'A'<=i<='Z' :
            sum1+=1
        if 'a'<=i<='z':
            sum+=1

    print("number of upper case",sum)
    print("number of lower case",sum1)

letter="BekzatSila"
calculate(letter)



def palindrome(letter):
    if letter==letter[::-1]:
        print(f"{letter} palindrome")
    else:
        print(f"{letter} is not palindrome")

letter="akaa"
palindrome(letter)



def square(a,millisecond):
    import math
    import time
    time.sleep(millisecond/1000)
    print(f"Square root of {a} after {millisecond} miliseconds is {math.sqrt(a)}")

a=25100
time=2123
square(a,time)



def all_true(t):
    return all(t)
tuple1=(True,True,False)
tuple2=(True,True,True)
print(all_true(tuple1))
print(all_true(tuple2))