"""Convert SODA-D dataset to yolo format

Usage:
    >>> python DOTA_D_to_yolo.py /Volumes/ZX7/Datasets/SODA-D-COCO-format/Annotations /Volumes/ZX7/Datasets/SODA-D-YOLO-format
"""

from ultralytics.data.converter import convert_coco
import sys

labels_dir = str(sys.argv[1])
save_dir = str(sys.argv[2]) if len(sys.argv) == 3 else "coco_converted/"

convert_coco(labels_dir=labels_dir, save_dir=save_dir, cls91to80=False)