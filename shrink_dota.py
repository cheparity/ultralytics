import os
import shutil
from tqdm import tqdm

base_dir = "/Volumes/ZX7/Datasets/SODA-D-Yolo-format"
labels_dir = "/Volumes/ZX7/Datasets/SODA-D-Yolo-format/labels"
images_dir = "/Volumes/ZX7/Datasets/SODA-D-Yolo-format/images"
coco_images_dir = "/Volumes/ZX7/Datasets/SODA-D-COCO-format/Images"

# 定义子目录
splits = ["train", "test", "val"]

# 选择比例（例如 20%）
select_ratio = 0.2

# 确保 images/ 下的子目录存在
for split in splits:
    split_images_dir = os.path.join(images_dir, split)
    os.makedirs(split_images_dir, exist_ok=True)

# 遍历每个 split（train/test/val）
for split in splits:
    # 获取 labels 目录下的 .txt 文件
    split_labels_dir = os.path.join(labels_dir, split)
    split_images_dir = os.path.join(images_dir, split)

    if not os.path.exists(split_labels_dir):
        print(f"Directory {split_labels_dir} does not exist, skipping...")
        continue

    # 获取所有 .txt 文件，并按文件名排序
    txt_files = sorted([f for f in os.listdir(split_labels_dir) if f.endswith(".txt")])
    if not txt_files:
        print(f"No .txt files found in {split_labels_dir}, skipping...")
        continue

    # 按比例选择前 N 个文件
    num_selected = max(1, int(len(txt_files) * select_ratio))  # 至少保留 1 个文件
    selected_txt_files = txt_files[:num_selected]  # 按顺序选择前 num_selected 个文件

    # 统计未选中的 .txt 文件（需要删除）
    unselected_txt_files = txt_files[num_selected:]

    # 删除未选中的 .txt 文件
    for txt_file in unselected_txt_files:
        txt_path = os.path.join(split_labels_dir, txt_file)
        os.remove(txt_path)
        print(f"Removed unselected label: {txt_path}")

    # 搬运对应的 .jpg 文件
    for txt_file in tqdm(selected_txt_files):
        # 获取对应的图像文件名（例如 image1.txt -> image1.jpg）
        image_file = txt_file.replace(".txt", ".jpg")
        src_image_path = os.path.join(coco_images_dir, image_file)
        dst_image_path = os.path.join(split_images_dir, image_file)

        # 检查图像文件是否存在
        if not os.path.exists(src_image_path):
            print(f"Image {src_image_path} not found, skipping...")
            # 如果图像不存在，删除对应的 .txt 文件
            os.remove(os.path.join(split_labels_dir, txt_file))
            print(f"Removed label without corresponding image: {txt_file}")
            continue

        # 复制图像文件
        shutil.copy(src_image_path, dst_image_path)
        print(f"Copied {src_image_path} to {dst_image_path}")

print("Dataset selection and image copying completed!")
