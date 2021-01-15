test = [
    {"Gfg": 8, "is": 1, "Best": 9},
    {"Gfg": 2, "is": 9, "Best": 1},
    {"Gfg": 5, "is": 10, "Best": 7},
]
result = {}
for stuffs in test:
    for key, val in stuffs.items():
        if key in result:
            result[key] = max(result[key], val)
        else:
            result[key] = val

print(result)
