array = [
  {"a":123},
  {"a":'qq'}
]
for i in array:
  print(i["a"])
print(list(map(lambda x:x["a"],array)))