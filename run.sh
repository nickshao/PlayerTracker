#!/bin/bash
wget https://pjreddie.com/media/files/yolo.weights -O bin/yolo.weights
YOLO_PATH='yolo/darkflow'
./${YOLO_PATH}/flow --imgdir input_frames/jazz_thunder/ --model cfg/yolo.cfg --load bin/yolo.weights --gpu 1.0

