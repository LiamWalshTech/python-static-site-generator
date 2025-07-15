import os
import shutil
import sys
from textnode import TextNode
from block_markdown import markdown_to_html_node, extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    paths = os.listdir(dir_path_content)
    for path in paths:
        content_path = f"{dir_path_content}/{path}"
        dest_path = f"{dest_dir_path}/{path}"
        html_path = f"{dest_dir_path}/{path.replace('md', 'html')}"
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, html_path, basepath)
        else:
            os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'.")
    with open(from_path) as f:
        content = f.read()

    with open(template_path) as f:
        template = f.read()

    html_string = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    html_full = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace("href=\"/", "href=\"{basepath}").replace("src=\"/", "src=\"{basepath}")

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
    basepath = "/"
    
    if sys.argv[0]:
        basepath = sys.argv[0]

    shutil.rmtree("docs", True)
    copy_contents("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__=="__main__":
    main()
