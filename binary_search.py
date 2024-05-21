def binary_search(list, item):
  lowIndex = 0
  highIndex = len(list) - 1

  while lowIndex <= highIndex:
    middleIndex = (lowIndex + highIndex) // 2

    middleItem = list[middleIndex]

    if middleItem == item:
      return middleIndex
    
    if middleItem > item:
      highIndex = middleIndex - 1
    else:
      lowIndex = middleIndex + 1

  return None


testList = [1, 3, 5, 7, 9, 11, 13, 15]

print(binary_search(testList, 9))