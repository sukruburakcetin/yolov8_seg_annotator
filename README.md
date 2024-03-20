<h1 align="center">
  <img src="https://images2.imgbox.com/23/3b/oPFjdMcK_o.png"><br/>yolov8_seg_annotator
</h1>

<h4 align="center">
  Image Polygonal Annotation with Python
</h4>

<div align="center">
  <a href="https://pypi.org/project/yolov8-seg-annotator/"><img src="https://img.shields.io/badge/pypi-v1.1.0-v1?logo=python"></a>
  <a href="#"><img src="https://img.shields.io/pypi/pyversions/labelme.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Open%20Source-%C2%A9?style=plastic&logo=python&logoColor=green&color=black&cacheSeconds=3600"></a>
  <a href="#"><img src="https://img.shields.io/badge/Made%20By-sukruburakcetin-a?style=plastic&logo=python&logoColor=green&color=black&cacheSeconds=3600"></a>
</div>

<div align="center">
  <a href="#starter-guide"><b>Starter Guide</b></a>
  | <a href="#installation"><b>Installation</b></a>
  | <a href="#usage"><b>Usage</b></a>
  | <a href="#examples"><b>Examples</b></a>
  | <a href="https://x.com/labelmeai"><b>X/Twitter</b></a>
  <!-- | <a href="https://github.com/wkentaro/labelme/discussions"><b>Community</b></a> -->
  <!-- | <a href="https://www.youtube.com/playlist?list=PLI6LvFw0iflh3o33YYnVIfOpaO0hc5Dzw"><b>Youtube FAQ</b></a> -->
</div>

## Description
A simple tool for labeling object maks in images, implemented with Python Tkinter. 


![Alt text](https://images2.imgbox.com/5d/04/RrK3Ocy5_o.png?raw=true "Title")


Data Organization
-----------------
```bash
├── app
│   ├── data # directory containing the images to be labeled
│       ├── annotated # after the pictures are annotated, they are saved in this folder.
│       └── samples # main image directory
│   ├── dist # exe file of the script
│   ├── logo
│   └── results # directory for the Yolo formatted labeling results
│       └── labels # converted to YOLO format result txt according to image file name
├── main # source code for the tool
├── main.spec # exe supplementary
├── README.md
└── requirements.txt
```

## Starter Guide

If you're new to Labelme, you can get started with [yolov8_seg_annotator Guide]() which contains:

- **Installation guides** for all platforms: Windows. 💪🏼
- **Step-by-step tutorials**: first annotation to editing, exporting, and integrating with other programs. 🤭
- **A compilation of valuable resources** for further exploration. 🤗

## Installation

### Windows
```bash
pip install -r requirements.txt
```

## Usage
### Command Line Arguments
Run `yolov8_seg_annotator` to start/execute.
The annotations are saved as a [TXT]() file in result/labels and annotations are saved in data/annotated.


## Results
### Sample
Result_YOLO (yolo format) : 
```
8 0.002286 0.750400 0.003429 0.820800 0.037143 0.817600 0.078286 0.801600 0.113143 0.788800 0.152000 0.768000 0.176571 0.756800 0.208000 0.731200 0.241143 0.705600 0.270286 0.680000 0.294857 0.659200 0.326286 0.635200 0.349714 0.617600 0.376571 0.590400 0.392000 0.574400 0.412571 0.542400 0.428000 0.531200 0.423429 0.521600 0.396571 0.536000 0.356571 0.568000 0.315429 0.595200 0.269714 0.619200 0.228000 0.651200 0.173714 0.684800 0.117143 0.710400 0.081143 0.724800 0.044000 0.736000 0.017714 0.747200
0 0.002857 0.990400 0.004000 0.833600 0.050857 0.822400 0.108000 0.800000 0.149143 0.777600 0.182857 0.764800 0.230286 0.718400 0.273143 0.688000 0.313714 0.654400 0.353143 0.612800 0.384571 0.577600 0.412000 0.547200 0.430857 0.529600 0.444571 0.542400 0.453143 0.532800 0.457714 0.523200 0.473714 0.518400 0.491429 0.518400 0.494286 0.542400 0.510857 0.593600 0.545143 0.662400 0.573714 0.740800 0.607429 0.811200 0.628000 0.848000 0.654857 0.884800 0.680571 0.931200 0.701714 0.961600 0.717143 0.992000 0.602857 0.993600 0.582857 0.969600 0.555429 0.940800 0.525143 0.929600 0.503429 0.924800 0.477143 0.924800 0.447429 0.923200 0.420000 0.923200 0.400000 0.929600 0.374286 0.936000 0.353143 0.960000 0.328000 0.984000 0.319429 0.987200
```
