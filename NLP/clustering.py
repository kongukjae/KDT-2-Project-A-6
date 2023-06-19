import beautifulfulsoup
import json

def jsonOpen(directory):
    with open(directory, "r") as f:
        data = json.load(f)
    return data
def jsonSave(directory,result):
    with open(directory, "w") as f:
        json.dump(result, f, ensure_ascii=False,indent=4)
def clustering():
    result = {}
    indexJson = jsonOpen('indexResult.json')
    indexJsonKeys = indexJson.keys()
    for i in indexJsonKeys:
        nowCluster = beautifulfulsoup.getTopTen(i)
        for j in nowCluster:
            if j[0] in result:
                result[j[0]].append(i)
            else:
                result[j[0]] = [i]

    jsonSave('clusterResult.json',result)

clusterJson = jsonOpen('clusterResult.json')


print(len(sorted(clusterJson,key=lambda x:len(clusterJson[x]))))