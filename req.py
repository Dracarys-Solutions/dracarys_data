import requests
import csv


res = requests.get("https://nrt4.modaps.eosdis.nasa.gov/api/v2/content/archives/FIRMS/viirs/South_America/VIIRS_I_South_America_VNP14IMGTDL_NRT_2019292.txt", headers={'Authorization': 'Bearer CFD564D4-F2A2-11E9-A611-68F3207B60E0'})
print(res.content)
