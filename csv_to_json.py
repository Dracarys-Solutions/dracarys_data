import csv
import json
import requests

with open("VNP14IMGTDL_NRT_South_America_24h.csv") as file:

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

request.post("onde vou mandar", json={'focos':res})

#SALVE
