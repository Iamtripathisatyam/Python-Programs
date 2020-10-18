# def argfunc(*satyam):
#     for i in satyam:
#         print(i)
# sat = ["SATYAM TRIPATHI","SACHIN TRIPATHI","SHIVAM TRIPATHI","DEEP TRIPATHI","SHASHANK TRIPATHI","RAM TRIPATHI","RAJA TRIPATHI","ABHIJEET TRIPATHI"]
# argfunc(*sat)


# def argfunc(normal,*satyam):
#     print(normal)
#     for i in satyam:
#         print(i)
# normal="Hello !! To all the members of our group from mahoba uttar pradesh !!"
# sat = ["SATYAM TRIPATHI","SACHIN TRIPATHI","SHIVAM TRIPATHI","DEEP TRIPATHI","SHASHANK TRIPATHI","RAM TRIPATHI","RAJA TRIPATHI","ABHIJEET TRIPATHI"]
# argfunc(normal,*sat)

# def argfunc(*satyam,normal):
#     print(normal)
#     for i in satyam:   This will through an error !! because we can't use normal as a first !!
#         print(i)
# normal="Hello !! To all the members of our group from mahoba uttar pradesh !!"
# sat = ["SATYAM TRIPATHI","SACHIN TRIPATHI","SHIVAM TRIPATHI","DEEP TRIPATHI","SHASHANK TRIPATHI","RAM TRIPATHI","RAJA TRIPATHI","ABHIJEET TRIPATHI"]
# argfunc(*sat,normal)

# def argfunc(normal,*satyam,**kwargs):
#     print(normal)
#     for i in satyam:
#         print(i)
# normal="Hello !! To all the members of our group from mahoba uttar pradesh !!"
# sat = ["SATYAM TRIPATHI","SACHIN TRIPATHI","SHIVAM TRIPATHI","DEEP TRIPATHI","SHASHANK TRIPATHI","RAM TRIPATHI","RAJA TRIPATHI","ABHIJEET TRIPATHI"]
# argfunc(normal,*sat)

# def argfunc(normal,*satyam,**kwargs):
#     print(normal)
#     for i in satyam:
#         print(i)
# normal="Hello !! To all the members of our group from mahoba uttar pradesh !!"
# sat = ["SATYAM TRIPATHI","SACHIN TRIPATHI","SHIVAM TRIPATHI","DEEP TRIPATHI","SHASHANK TRIPATHI","RAM TRIPATHI","RAJA TRIPATHI","ABHIJEET TRIPATHI"]
# argfunc(normal)

# def argfunc(normal,*satyam,**tri):
#     print(normal)
#     for i in satyam:
#         print(i)
#     for key,value in tri.items():
#         print(f"\n{key} is a {value}\n")
# normal="Hello !! To all the members of our group from mahoba uttar pradesh !!"
# sat = ["SATYAM TRIPATHI","SACHIN TRIPATHI","SHIVAM TRIPATHI","DEEP TRIPATHI","SHASHANK TRIPATHI","RAM TRIPATHI","RAJA TRIPATHI","ABHIJEET TRIPATHI"]
# kw={"Satyam":"Programmer","Shivam":"Monitor","Deep":"IAS","Shashank":"Retired Soobedar"}
# argfunc(normal,*sat,**kw)
