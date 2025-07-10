import os
import shutil
from textnode import TextNode
from block_markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'.")
    with open(from_path) as f:
        content = f.read()

    with open(template_path) as f:
        template = f.read()

    html_string = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    html_full = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    open(dest_path, "x")
    with open(dest_path, "w") as page_file:
        page_file.write(html_full)

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
    shutil.rmtree("public", True)
    copy_contents("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__=="__main__":
    main()
