import os
from markdown_to_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from \"{from_path}\" to \"{dest_path}\" using \"{template_path}\".")
    with open(from_path) as file:
        page_contents = file.read()
        #print(f"page contents: {page_contents}")
        parent_node = markdown_to_html_node(page_contents)
        html_string = parent_node.to_html()
        page_title = extract_title(page_contents)

    with open(template_path) as file:
        template = file.read()
        with_title = template.replace("{{ Title }}", page_title)
        with_content = with_title.replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(with_content)
