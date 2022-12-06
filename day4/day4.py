lines = open("day4.txt").readlines()
l = [line.strip() for line in lines]

count = 0
for line in l:
  p1, p2 = line.split(",")
  x1, x2 = p1.split("-")
  y1, y2 = p2.split("-")

  # if int(x1, base=0) <= int(y1, base=0) and int(x2, base=0) >= int(y2, base=0): # If x range encapsulates y range
  #   count += 1
  # elif int(y1, base=0) <= int(x1, base=0) and int(y2, base=0) >= int(x2, base=0): # if y range encapsul;ates x range
  #   count += 1
  if (int(x2, base=0) >= int(y1, base=0)) and (int(x2, base=0) <= int(y2, base=0)): # endpoint of x is in range of y
    count += 1
  elif (int(y2, base=0) >= int(x1, base=0)) and (int(y2, base=0) <= int(x2, base=0)): # endpoint of y is in range of x
    count += 1
print(count)