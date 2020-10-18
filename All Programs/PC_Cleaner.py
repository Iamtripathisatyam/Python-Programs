import os
os.chdir("C:\\Users\\Dell\\Desktop\\Application & Letters & Documents")
def create(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
def move(foldername,files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")
files=os.listdir()
# print(files)
create("Docs")
create("Pdfs")
create("PPTS")
docsext=['.docx','.doc']
pdext=['.pdf']
ppt=['.pptx']
docs=[file for file in files if os.path.splitext(file)[1].lower() in docsext]
pd=[file for file in files if os.path.splitext(file)[1].lower() in pdext]
ppts=[file for file in files if os.path.splitext(file)[1].lower() in ppt]
move("Docs",docs)
move("Pdfs",pd)
move("PPTS",ppts)







import os
# os.chdir("C:\\Users\\Dell\\Desktop\\Photos")
def create(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
def move(foldername,files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")
files=os.listdir()
create("Python Programs")
create("Text Files")
create("Pickle Files")
create("mp3 sounds")
create("Pdfs Files")
mext=['.py']
vdext=['.txt']
bc=['.pkl']
mp=['.mp3']
pdf=['.pdf']

docs=[file for file in files if os.path.splitext(file)[1].lower() in mext]
pd=[file for file in files if os.path.splitext(file)[1].lower() in vdext]
bcc=[file for file in files if os.path.splitext(file)[1].lower() in bc]
mpp=[file for file in files if os.path.splitext(file)[1].lower() in mp]
pdfs=[file for file in files if os.path.splitext(file)[1].lower() in pdf]
move("Python Programs",docs)
move("Text Files",pd)
move("Pickle Files",bcc)
move("mp3 sounds ",mpp)
move("Pdfs Files",pdfs)

