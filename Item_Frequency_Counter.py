def count_items(items_list):
    counts={}
    for item in items_list:
        counts[item]=counts.get(item,0)+1
    return counts
items = ['apple','banana','apple','cherry','banana','apple']
print(count_items(items))
