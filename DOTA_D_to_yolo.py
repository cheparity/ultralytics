"""Convert SODA-D dataset to yolo format

Usage:
    >>> python DOTA_D_to_yolo.py /Volumes/ZX7/Datasets/SODA-D-COCO-format/Annotations /Volumes/ZX7/Datasets/SODA-D-YOLO-format
"""

from ultralytics.data.converter import convert_coco

labels_dir = "E:\\Datasets\\SODA-D-COCO-format\\Annotations"
save_dir = 'E:\\Datasets\\SODA-D-YOLO-format'

convert_coco(labels_dir=labels_dir, save_dir=save_dir, cls91to80=False)