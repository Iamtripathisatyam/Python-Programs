import requests
import pickle
data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
sat = data.split("\n")
# tri =[item.split() for item in sat if len(item)!=0]
tri =[item.split(",") for item in sat if len(item)!=0]
with open("myiris.pkl", "wb") as f:
     pickle.dump(tri, f)
with open("myiris.pkl", "rb") as f:
    print(pickle.load(f))
