import os
import shutil

root_dir = os.getcwd()
script_dir = os.path.join(root_dir, "src")
static_dir = os.path.join(root_dir, "static")
public_dir = os.path.join(root_dir, "public")


def copy_static(src_path, dest_path):
    if os.path.isfile(src_path):
        print(f"copying file: {src_path}")
        shutil.copy(src_path, dest_path)
        return

    if os.path.isdir(src_path):
        if not os.path.exists(dest_path):
           os.mkdir(dest_path)

        for item in os.listdir(src_path):
            src_item_path = os.path.join(src_path, item)
            dest_item_path = os.path.join(dest_path, item)
            copy_static(src_item_path, dest_item_path)



def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        print(f"deleting: {public_dir}")
    copy_static(static_dir, public_dir)

main()
