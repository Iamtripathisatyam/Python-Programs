from covid import Covid

covid = Covid()
name = input("Country: ")
cases = covid.get_status_by_country_name(name)
for x in cases:
    print(x, ":", cases[x])