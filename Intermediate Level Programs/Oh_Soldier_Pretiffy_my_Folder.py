import os
def soldier(path,format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    for s in files:
        os.rename(s, s.upper())
        if os.path.splitext(s)[1] == format:
            os.rename(s, f"sat {i} Mp4{format}")
            i+=1
# soldier(r"C:\Users\Dell\Desktop\test",".jpg" )
# soldier(r"C:\Users\Dell\Desktop\Photos",".PNG" )
# soldier(r"C:\Users\Dell\Desktop\Photos",".JPG" )
soldier(r"C:\Users\Dell\Desktop\Photos",".MP4" )
