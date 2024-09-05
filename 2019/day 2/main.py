file = open('input.txt', 'r')
lines = [int(line) for line in file.read().split(',')]
number = len(lines)
point = 0
lines0 = [i for i in lines]
first, second = [0, 0]

for first in range(0, 100):
  for second in range(0, 100):
    point = 0
    number = len(lines)
    lines = [i for i in lines0]
    lines[1] = first
    lines[2] = second
    while number >=4:
      number -= 4
      if lines[point] == 1:
        lines[lines[point+3]] = lines[lines[point+1]] + lines[lines[point+2]]
      elif lines[point] == 2:
        lines[lines[point+3]] = lines[lines[point+1]] * lines[lines[point+2]]
      elif lines[point] == 99:
        break
      point += 4
      if lines[0] == 19690720:
        print(first*100 + second)