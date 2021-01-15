#---------------------DECORATORS---------------------------------

def sat(tri):
    def nowexec():
        print("!! Executing Now !!")
        tri()
        print("!! Executed !!")
    return nowexec


@sat
def who():
    print("@@@@@@@@@@ Satyam Tripathi Is a GoOD BOY @@@@@@@@@@@")

who()
