test = [
    {"Gfg": 5, "is": 8, "best": 0},
    {"Gfg": 5, "is": 1, "best": 0},
    {"Gfg": 5, "is": 0, "best": 0},
]

key = list(test[0].keys())
result = []
for ke in key:
    final = all(test[0][ke] == ele[ke] for ele in test)
    if final:
        result.append(ke)

print(result)
