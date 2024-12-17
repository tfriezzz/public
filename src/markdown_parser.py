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


def split_nodes_image(old_nodes):
    def delimiter_constructor(output_node):
        delimiters = []
        for node in output_node:
            delimiters.append(f"![{node[0]}]({node[1]})")
        return delimiters


    pieces = []
    for node in old_nodes:
        output_node = extract_markdown_images(node.text)
        delimiters = delimiter_constructor(output_node)
        node_text = node.text
        for delimiter, node in zip(delimiters, output_node):
            rest_delimiter = node_text.split(delimiter)
            if rest_delimiter[0] != "":
                pieces.append(TextNode(rest_delimiter[0], TextType.TEXT))
            pieces.append(TextNode(node[0], TextType.IMAGE, node[1]))
            node_text = rest_delimiter[1]
    return pieces


def split_nodes_link(old_nodes):
    def delimiter_constructor(output_node):
        delimiters = []
        for node in output_node:
            delimiters.append(f"[{node[0]}]({node[1]})")
        return delimiters


    pieces = []
    for node in old_nodes:
        output_node = extract_markdown_links(node.text)
        delimiters = delimiter_constructor(output_node)
        node_text = node.text
        for delimiter, node in zip(delimiters, output_node):
            rest_delimiter = node_text.split(delimiter)
            if rest_delimiter[0] != "":
                pieces.append(TextNode(rest_delimiter[0], TextType.TEXT))
            pieces.append(TextNode(node[0], TextType.LINK, node[1]))
            node_text = rest_delimiter[1]
    return pieces


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
