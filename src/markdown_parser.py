from textnode import TextNode, TextType, text_node_to_html_node
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        match node.text_type:
            case TextType.TEXT:
                pieces = node.text.split(delimiter)
                for i in range(len(pieces)):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(pieces[i], TextType.TEXT))
                    if i % 2 != 0:
                        new_nodes.append(TextNode(pieces[i], text_type))

            case _:
                new_nodes.append(node)

    return new_nodes


def extract_markdown_images(text):
    alt_text = re.findall(r"\[(.*?)\]", text)
    url = re.findall(r"\((.*?)\)", text)
    zipped_list = []
    for alt, url in zip(alt_text, url):
        zipped_list.append((alt, url))
    return zipped_list


def extract_markdown_links(text):
    anchor_text = re.findall(r"\[(.*?)\]", text)
    url = re.findall(r"\((.*?)\)", text)
    zipped_list = []
    for anchor, url in zip(anchor_text, url):
        zipped_list.append((anchor, url))
    return zipped_list
