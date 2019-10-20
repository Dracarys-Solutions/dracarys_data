import csv
import json
import requests

res = requests.get("https://nrt4.modaps.eosdis.nasa.gov/api/v2/content/archives/FIRMS/viirs/South_America/VIIRS_I_South_America_VNP14IMGTDL_NRT_2019292.txt", headers={'Authorization': 'Bearer CFD564D4-F2A2-11E9-A611-68F3207B60E0'})


print(res.content)
'''
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
requests.post("localhost:3333/fires", json=res)


'''