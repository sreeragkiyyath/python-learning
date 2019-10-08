
data = [12, 13, 45, 54, 542]

def printArray(datas):
 for data in range(len(datas)):
  print(datas[data], end=", ")

def rotateList(datas, no__of_rotation):
  for item in range(no__of_rotation):
    temp = datas[0]
    for data in range(len(datas)-1):
      datas[data] = datas[data + 1]
    datas[len(datas) - 1] = temp

rotateList(data, 4)
printArray(data)
print(len(data))