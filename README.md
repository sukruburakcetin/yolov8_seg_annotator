yolov8-annotator
===============

A simple tool for labeling object maks in images, implemented with Python Tkinter. 

![Alt text](logo/yolov8_annotator_logo.png?raw=true "Title")


| title    | Yolov8 Annotation Tool |
|----------|------------------------|
| app_file | main.py                |
| dist     | annotator.exe          |

![Static Badge](https://img.shields.io/badge/Open%20Source-%C2%A9?style=plastic&logo=python&logoColor=green&color=black&cacheSeconds=3600)
![Static Badge](https://img.shields.io/badge/Made%20By-sukruburakcetin-a?style=plastic&logo=python&logoColor=green&color=black&cacheSeconds=3600)

Data Organization
-----------------
yolov8-annotator  
|  
|--data/                    *# directory containing the images to be labeled* <br>
&nbsp;&nbsp;&nbsp;|--annotated/               *# After the pictures are annotated, they are saved in this folder.e*  
&nbsp;&nbsp;&nbsp;|--samples/               *# main image directory*  
|--results/                    *# directory for the Yolo formatted labeling results*  
&nbsp;&nbsp;&nbsp;|--labels/       *# converted to YOLO format result txt according to image file name* <br>
|--dist/                    *# exe file of the script*  
|--main.py                    *# source code for the tool*  


# Requirements

- [pillow](https://pypi.org/project/pillow/)
pip install pillow==10.2.0
- [ttkthemes](https://pypi.org/project/ttkthemes/)
pip install ttkthemes==3.2.2


## Usage
1. ..
2. ..


Result_YOLO (yolo format) : 
```
8 0.002286 0.750400 0.003429 0.820800 0.037143 0.817600 0.078286 0.801600 0.113143 0.788800 0.152000 0.768000 0.176571 0.756800 0.208000 0.731200 0.241143 0.705600 0.270286 0.680000 0.294857 0.659200 0.326286 0.635200 0.349714 0.617600 0.376571 0.590400 0.392000 0.574400 0.412571 0.542400 0.428000 0.531200 0.423429 0.521600 0.396571 0.536000 0.356571 0.568000 0.315429 0.595200 0.269714 0.619200 0.228000 0.651200 0.173714 0.684800 0.117143 0.710400 0.081143 0.724800 0.044000 0.736000 0.017714 0.747200
0 0.002857 0.990400 0.004000 0.833600 0.050857 0.822400 0.108000 0.800000 0.149143 0.777600 0.182857 0.764800 0.230286 0.718400 0.273143 0.688000 0.313714 0.654400 0.353143 0.612800 0.384571 0.577600 0.412000 0.547200 0.430857 0.529600 0.444571 0.542400 0.453143 0.532800 0.457714 0.523200 0.473714 0.518400 0.491429 0.518400 0.494286 0.542400 0.510857 0.593600 0.545143 0.662400 0.573714 0.740800 0.607429 0.811200 0.628000 0.848000 0.654857 0.884800 0.680571 0.931200 0.701714 0.961600 0.717143 0.992000 0.602857 0.993600 0.582857 0.969600 0.555429 0.940800 0.525143 0.929600 0.503429 0.924800 0.477143 0.924800 0.447429 0.923200 0.420000 0.923200 0.400000 0.929600 0.374286 0.936000 0.353143 0.960000 0.328000 0.984000 0.319429 0.987200
```
