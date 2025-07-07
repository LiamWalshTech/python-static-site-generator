def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    valid_blocks = []

    for block in blocks:
        if len(block) > 0:
            valid_blocks.append(block.strip())

    return valid_blocks
