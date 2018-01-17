#!/bin/bash

YOLO_PATH='yolo/darkflow'
./${YOLO_PATH}/flow --imgdir input_frames/jazz_thunder/ --model ${YOLO_PATH}/cfg/yolo.cfg --load ${YOLO_PATH}/bin/yolo.weights --gpu 1.0

