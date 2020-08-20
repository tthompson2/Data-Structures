new_list = []

n = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def function(n):
   print(n)
   for x in range(len(n)):
      if n[x] % 3 == 0:
        new_list.append(n[x])
        print(n[x])
      else:
        continue 

function(n)
