def Cloning_List(Given_List):
    Result = Given_List[:]
    return Result


Given_List = [4, 5, 7, 8, 9, 6, 10, 15]
print(Cloning_List(Given_List))


def Cloning_List(Given_List):
    Result = []
    Result.extend(Given_List)
    return Result


Given_List = [4, 5, 7, 8, 9, 6, 10, 15]
print(Cloning_List(Given_List))


def Cloning_List(Given_List):
    Result = list(Given_List)
    return Result


Given_List = [4, 5, 7, 8, 9, 6, 10, 15]
print(Cloning_List(Given_List))


def Cloning_List(Given_List):
    Result = Given_List
    return Result


Given_List = [4, 5, 7, 8, 9, 6, 10, 15]
print(Cloning_List(Given_List))
