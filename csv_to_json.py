import csv
import json
import requests

with open("dados.txt") as file:

    z=[]
    vec=dict()
    res=[]
    for line in file:
        z=line.split(',')
        vec.clear()
        vec.update({'Lat':z[0]})
        vec.update({'Lon':z[1]})
        vec.update({'Day':z[5]})
        vec.update({'Time':z[6]})
        vec.update({'Level':z[7]})
        res.append(vec)
        

res = dict({'queimadas': res})

print(res)


