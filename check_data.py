import os


def check_matching_files(image_dir, label_dir, image_ext=".jpg", label_ext=".txt"):
    """
    检查image_dir中的每个图像文件是否在label_dir中有对应的标签文件

    参数:
        image_dir: 图像文件目录
        label_dir: 标签文件目录
        image_ext: 图像文件扩展名(默认.jpg)
        label_ext: 标签文件扩展名(默认.txt)

    返回:
        missing_files: 在label_dir中找不到对应标签文件的图像文件列表
    """
    # 获取图像文件名(不带扩展名)
    image_files = {os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith(image_ext)}

    # 获取标签文件名(不带扩展名)
    label_files = {os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith(label_ext)}

    # 找出没有对应标签文件的图像文件
    missing_files = image_files - label_files

    # 转换回列表并排序
    return sorted(list(missing_files))


base_image_dir = "E:\\Datasets\\SODA-D-YOLO-format\\images"
base_label_dir = "E:\\Datasets\\SODA-D-YOLO-format\\labels"

split = ["train", "test", "val"]
for s in split:
    image_dir = os.path.join(base_image_dir, s)
    label_dir = os.path.join(base_label_dir, s)

    print(f"Checking split: {s}")
    missing = check_matching_files(image_dir, label_dir)

    if missing:
        print(f"Found {len(missing)} images without corresponding labels:")
        for file in missing[:10]:  # 只打印前10个，避免输出太多
            print(f"  - {file}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")
    else:
        print("All images have corresponding labels!")
    print()
