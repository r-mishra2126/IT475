try:
     data={ 1:'one', 2:'two'}
     print(data[1])
except KeyError as e:
     print("KEY NOT FOUND")
else:
     raise ValueError()
