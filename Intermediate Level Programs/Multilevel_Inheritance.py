
#-------------------------Multilevel Inheritance------------------------------------------
class dad:
    basketball=6
    dance=15
class son(dad):
    # dance=1
    def dancechamp(self):
        return f"Dance Champion Mera Junoon Hai!!"
class grandson(son):
    # dance=10
    def dancechamp(self):
        return f"Dance Champion Mera Junoon Hai Michael Jackson Obama a Champion DID!!"

satyam=dad()
shivam=son()
empire=grandson()
print(empire.dancechamp())
print(shivam.dancechamp())
print(empire.dance)
