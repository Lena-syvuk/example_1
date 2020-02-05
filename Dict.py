d1 = dict({'clothes':'dress','color':'green', 'size':'eleven'})
d2 = dict({1:'one', 2:'two', 3:'three'})
d3 = dict({'city':'Kyiv','population':'four million', 'Independence Day':'24 August'})
z = {**d1,**d2,**d3}
print(z)
