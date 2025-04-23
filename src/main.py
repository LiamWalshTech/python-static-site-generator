from textnode import TextNode

def main():
    example = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(repr(example))

if __name__=="__main__":
    main()
