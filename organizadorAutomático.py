from pathlib import Path
import os
import shutil

print("#"*50)
diretorio = input("Qual  o driretorio voce quer organizar:")
print("#"*50)
print(f"organizando didetorio {diretorio}...")

print ("CRIANDO AS PASTAS")
pdf = diretorio + "/pdf/"
docs = diretorio + "/docs/"
PowerPoint = "/docs/PowerPoint"
Word = "/docs/Word"
imagens = diretorio + "/imagens/"
png = diretorio + "/imagens/png/"
jpg = diretorio + "/imagens/jpg/"
Compactados = diretorio + "/Compactados/"
ProjetosElets = diretorio + "/ProjetosElets/"

if not os.path.isdir(pdf): os.mkdir(pdf)
if not os.path.isdir(imagens): os.mkdir(imagens)
if not os.path.isdir(jpg): os.mkdir(jpg)
if not os.path.isdir(png): os.mkdir(png)

if not os.path.isdir(docs): os.mkdir(docs)
if not os.path.isdir(PowerPoint): os.mkdir(PowerPoint)
if not os.path.isdir(Word): os.mkdir(Word)
if not os.path.isdir(Compactados): os.mkdir(Compactados)
if not os.path.isdir(ProjetosElets): os.mkdir(ProjetosElets)

path = Path(diretorio)

for filename in path.glob('*'):
    if filename.suffix == ".pdf" :
        basename = os.path.basename(filename)
        os.rename(filename, pdf + basename)

    elif filename.suffix == [".jpg",".jpeg"]:
        basename = os.path.basename(filename)
        os.rename(filename, jpg + basename)

    elif filename.suffix == ".png":
        basename = os.path.basename(filename)
        os.rename(filename, png + basename)

    elif filename.suffix == [".doc",".docx"]:
        basename = os.path.basename(filename)
        os.rename(filename, Word + basename)


    elif filename.suffix == ".pptx":
        basename = os.path.basename(filename)
        os.rename(filename, PowerPoint + basename)

    elif filename.suffix == [".zip",".iso"]:
        basename = os.path.basename(filename)
        os.rename(filename, Compactados + basename)

    elif filename.suffix == [".circ",".pdsprj"]:
        basename = os.path.basename(filename)
        os.rename(filename, ProjetosElets + basename)
