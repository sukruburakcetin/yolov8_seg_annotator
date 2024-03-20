from setuptools import setup, find_packages


setup(
    name="yolov8_seg_annotator",
    version="1.1",
    packages=find_packages(),
    install_requires=[
        "pillow==10.2.0",
        "ttkthemes==3.2.2"
    ],
    entry_points={
        "console_scripts": [
            "yolov8_seg_annotator = yolo8_seg_annotator:execute"
        ]
    }
)