import math
# read file into memory
lines = open("day5.txt").readlines()

# initialize dictionary to keep track of values
d = {}
for k in range(1, 10):
  d[k] = []


i = 0
for line in lines:
  i += 1 # to keep track of lines array after we break out of the loop
  idx = 1
  if line[1] == "1": # this is our exist condition - we read the line with indices of towers
    i += 1 # next line is a newline - don't want to read this into a loop
    break
  # loop over every other character until we find something that isn't a space or a newline
  for char in line[1::2]:      
    if char != " " and char != "\n":
      # char is an element of a tower - add it to the dictionary at specific index
      d[math.ceil(idx/2)].append(char)
    idx += 1

for line in lines[i:]:
  # split line by spaces and extract information we need
  parts = line.strip().split(' ')
  num = int(parts[1]) # number of blocks to move
  fromIdx = int(parts[3]) # tower moving from
  toIdx = int(parts[5]) # tower moving to
  # SOLUTION TO FIRST PART
  # logic to move parts between towers
  # for _ in range(num): 
  #   d[toIdx].insert(0, d[fromIdx].pop(0))
  
  # SOLUTION TO SECOND PART
  # move all pieces from one tower into temp array
  temp = []
  for _ in range(num):
    temp.append(d[fromIdx].pop(0))
  
  # move pieces out of temp array in reverse order to maintain structure
  for _ in range(num):
    d[toIdx].insert(0, temp.pop())

# build solution
res = ""
for key in d.keys():
  res += d[key][0]
print(res)