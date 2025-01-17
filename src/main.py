import os
import shutil

root_dir = os.getcwd()
scrip_dir = os.path.join(root_dir, "src")
static_dir = os.path.join(root_dir, "static")
public_dir = os.path.join(root_dir, "public")


def tree_diver(filetree):
    firtst_item = filetree[0]
    current_path = os.join(src_path, firtst_item)
    if os.path.isfile(firtst_item):
        shutil.copy(current_path, dest_path)


def copy_static(src_path, dest_path):
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    dir_contents = os.listdir(src_path)
    os.mkdir("public")
    print(f"contents: {dir_contents}")
    for content in dir_contents:
        print(content)
        if os.path.isfile(os.path.join(src_path, content)):
            print(f"file: {content}")
        if os.path.isdir(os.path.join(src_path, content)):
            print(f"dir: {content}")

    #shutil.copy(src_path, dest_path)


def main():
    copy_static(static_dir, public_dir)

main()
