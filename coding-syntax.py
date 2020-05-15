#Write a function called compute_sum() that takes in a single integer argument n 
# and returns the sum of the positive integers from 1 to n. For example compute_sum(4) 
# would return 10, or 1+2+3+4. 

def compute_sum(n):
    sum = n
    # while n > 0:
    #     sum += (n-1)
    #     n -=1
    sum = (n/2)*(n+1)
    print (sum)
    

compute_sum(8)
compute_sum(10)
compute_sum(12)
compute_sum(14)
    

#Write a function that will reverse a integer number using a stack and return the reversed number as an integer. 
# For example, if your input number is 3479 the function will return 9743. 

def size(stack): 
    return len(stack) 
  
def isEmpty(stack): 
    if size(stack) == 0: 
        return true 
  
def push(stack,item): 
    stack.append(item) 
  
def pop(stack): 
    if isEmpty(stack): return
    return stack.pop() 
  
def reverse_num(num): 
    stack = []

    n = len(num)
  
    for i in range(0,n,1): 
        push(stack,num[i]) 
  
    number="" 

    for i in range(0,n,1): 
        number+=pop(stack) 
          
    return number 

print(reverse_num("3479")) 
print(reverse_num("85612")) 
print(reverse_num("895572")) 
print(reverse_num("752725")) 
  