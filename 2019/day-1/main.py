import math

file = open('input.txt', 'r')
lines = file.read().split('\n')

def convert(module):
  mass = int(module)
  divided = mass / 3
  rounded = math.floor(divided)
  fuel = rounded - 2
  return fuel
  
sum = 0

for module in lines:
  fuel = convert(module)
  while fuel >= 1:
    sum += fuel
    fuel = convert(fuel)
    
print(sum)