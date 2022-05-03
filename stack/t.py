sampleDict = {'Ritika': 5, 'Sam': 27, 'John': 12, 'Sachin': 14, 'Mark': 19, 'Shaun' : 27}
itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
print('Maximum Value in Dictionary : ', itemMaxValue[1])
listOfKeys = list()
# Iterate over all the items in dictionary to find keys with max value
for key, value in sampleDict.items():
    if value == itemMaxValue[1]:
        listOfKeys.append(key)
print('Keys with maximum Value in Dictionary : ', listOfKeys)