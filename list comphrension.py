x,y=[int(y) for y in input().split()]
print(x)
print(y)
print()
numbers=[1,2,3,4,5]
double_numbers=[num*2 for num in numbers]
print(double_numbers)
print()
numbers=[1,2,3,4,5]
double_numbers=[num*num for num in numbers]
print(double_numbers)
print()
numbers=[1,2,3,4,5]
square_numbers=[]
for num in numbers:
     square_numbers.append(num*num)
print(square_numbers)
print()
word='pavithra'
vowels='aeiou'
constant='bcdfghjklmnpqrstvwxyz'
result=[char for char in word if char in vowels]
result1=[char for char in word if char in constant]
print(result)
print(result1)