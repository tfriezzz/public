import os
from markdown_to_blocks import markdown_to_html_node, extract_title


def generate_page(from_path, template_path, dest_path):
    print(
        f'Generating page from "{from_path}" to "{dest_path}" using "{template_path}".'
    )
    with open(from_path) as file:
        page_contents = file.read()
        # print(f"page contents: {page_contents}")
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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"\nProcessing: {dir_path_content}")
    print(f"Destination: {dest_dir_path}")

    if os.path.isdir(dir_path_content):
        os.makedirs(dest_dir_path, exist_ok=True)
        print(f"Created directory: {dest_dir_path}")
        for item in os.listdir(dir_path_content):
            content_item_path = os.path.join(dir_path_content, item)
            dest_item_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(content_item_path, template_path, dest_item_path)
        return

    # Only process markdown files
    if not dir_path_content.endswith(".md"):
        print(f"Skipping non-markdown file: {dir_path_content}")
        return

    print(f"Converting markdown file: {dir_path_content}")
    dest_dir_path = dest_dir_path.replace(".md", ".html")
    generate_page(dir_path_content, template_path, dest_dir_path)
