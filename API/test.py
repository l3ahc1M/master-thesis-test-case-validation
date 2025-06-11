import os

def count_json_files(root_dir):
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.json'):
                count += 1
    return count

if __name__ == "__main__":
    base_folder = os.path.dirname(os.path.abspath(__file__))
    json_count = count_json_files(base_folder)
    print(f"Total JSON files in subfolders: {json_count}")