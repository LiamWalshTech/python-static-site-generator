import os
import shutil
from textnode import TextNode

def copy_contents(srcDir, destDir):
    shutil.rmtree(destDir, True)
    os.mkdir(destDir)
    paths = os.listdir(srcDir)
    for path in paths:
        if os.path.isfile(f"{srcDir}/{path}"):
            print(f"Copying `{path}` to {destDir}")
            shutil.copy(f"{srcDir}/{path}", destDir)
        else:
            print(f"Directory found... `{path}`")
            print("Recursion commence!")
            copy_contents(f"{srcDir}/{path}", f"{destDir}/{path}")

    print("All done!")

def main():
    copy_contents("static", "public")

if __name__=="__main__":
    main()
