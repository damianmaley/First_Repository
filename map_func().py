'''
Creating a list of number, finding the to total sum and
using a regular function and a map function to return the 
percentage each element in the list occupy in the total sum.
'''

#create a list of numbers
lst = [25,30,45,40,60]

def find_percent(lst):
    
    #find the total sum of the list
    sum_lst = 0
    for i in lst:
        sum_lst  +=  i
    print(sum_lst )
    
    # create a empty list
    new_lst = []

    # divide each member of the list with the total sum of the list and multiply by 100
    # to know how many percent each member occupy in the total sum...
    for i in lst:
        ans = (i / sum_lst)  * 100
        new_lst.append(ans)
    return new_lst
print(find_percent(lst))


print('-' *100)

''' A map function takes 2 arguments: a funtion, iterables.'''

# make the defualt value of 's' equal to the total sum of the list
def percent_sum(n, s = sum(lst)):
    return n/s *100
percent_ = list(map(percent_sum, lst))
print(percent_)

# printing out the sum of all percentages which must be equal to 100%
sum_percent = 0
for i in percent_:
    sum_percent += i
print('The sum of the output is : %d%%' %(sum_percent))

        
