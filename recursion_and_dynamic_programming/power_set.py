def power_set(oset, collection=[]):
    if set(oset) not in collection:
        collection.append(set(oset))

    if len(oset) == 0:
        return
    else:
        for index, item in enumerate(oset):
            power_set(oset[:index]+oset[index+1:], collection)

collection = []
power_set([1, 2, 3, 4], collection)
print(collection)