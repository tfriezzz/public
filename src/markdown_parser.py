from textnode import TextNode, TextType, text_node_to_html_node
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    pattern = f"{re.escape(delimiter)}(.*?){re.escape(delimiter)}"

    for node in old_nodes:
        match node.text_type:
            case TextType.TEXT:
                current_index = 0
                for delimiter_match in re.finditer(pattern, node.text):
                    match_start_index = delimiter_match.start()
                    if match_start_index > current_index:
                        new_nodes.append(TextNode(node.text[current_index:match_start_index], TextType.TEXT))
                    new_nodes.append(TextNode(delimiter_match.group(1), text_type))
                    current_index = delimiter_match.end()
                if current_index < len(node.text):
                    new_nodes.append(TextNode(node.text[current_index:], TextType.TEXT))
            case _:
                new_nodes.append(node)
    
    return new_nodes


def split_nodes_image(old_nodes):
    pieces = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            extracted_images = extract_markdown_images(node.text)
            remaining_text = node.text
            for alt_text, url in extracted_images:
                parts = remaining_text.split(f"![{alt_text}]({url})")
                if parts[0]:
                    pieces.append(TextNode(parts[0], TextType.TEXT))
                pieces.append(TextNode(alt_text, TextType.IMAGE, url))
                if len(parts) > 1:
                    remaining_text = parts[1]
            if remaining_text:
                pieces.append(TextNode(remaining_text, TextType.TEXT))
        if node.text_type is not TextType.TEXT:
            pieces.append(node)
    return pieces


def split_nodes_link(old_nodes):
    pieces = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            extracted_images = extract_markdown_links(node.text)
            remaining_text = node.text
            for anchor_text, url in extracted_images:
                parts = remaining_text.split(f"[{anchor_text}]({url})")
                if parts[0]:
                    pieces.append(TextNode(parts[0], TextType.TEXT))
                pieces.append(TextNode(anchor_text, TextType.LINK, url))
                if len(parts) > 1:
                    remaining_text = parts[1]
            if remaining_text:
                pieces.append(TextNode(remaining_text, TextType.TEXT))
        if node.text_type is not TextType.TEXT:
            pieces.append(node)
    return pieces


"""def extract_markdown_images(text):
    alt_text = re.findall(r"\[(.*?)\]", text)
    url = re.findall(r"\((.*?)\)", text)
    zipped_list = []
    for alt, url in zip(alt_text, url):
        zipped_list.append((alt, url))
    return zipped_list"""

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.group(1), match.group(2)))
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    anchor_text = re.findall(r"\[(.*?)\]", text)
    url = re.findall(r"\((.*?)\)", text)
    zipped_list = []
    for anchor, url in zip(anchor_text, url):
        zipped_list.append((anchor, url))
    return zipped_list
