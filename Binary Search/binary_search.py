def binary_search(l, target, low=0, high=None):
  high = len(l) - 1 if high == None else high
  midpoint = (low + high) // 2
  if low > high:
    return -1
  if l[midpoint] == target:
    return midpoint
  if target > l[midpoint]:
    return binary_search(l, target, midpoint + 1, high)
  return binary_search(l, target, low, midpoint - 1)


l = [1, 2, 6, 7, 10, 20, 25]
target = 3

print(binary_search(l, target))