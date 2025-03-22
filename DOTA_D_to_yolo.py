"""Convert SODA-D dataset to yolo format

Usage:
>>> python DOTA_D_to_yolo.py "path/to/annotation/dir/"
"""

from ultralytics.data.converter import convert_coco
import sys

labels_dir = str(sys.argv[1])
convert_coco(labels_dir=labels_dir, cls91to80=False)
