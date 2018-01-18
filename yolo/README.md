# YOLO Detection

## Video to frame

```
ffmpeg -i [input_video] -r [number of frames per second] -qscale:v [video quality] [image name]
```

* `-r` : 1 frame per second would be `-r 1`, one frame every four seconds would be `-r 0.25`
* `-qscale:v` :  Effective range for JPEG is 2-31 with 31 being the worst quality  

example

```
ffmpeg -i video.mpg -r 10 -qscale:v 2 output_%04d.jpg
```

## Darkflow

### Dependencies
```
pip3 install --user cython
pip3 uninstall protobuf
pip3 uninstall google
pip3 install --user google
pip3 install --user protobuf
```

### Setup

1. clone this project
	```
	git clone https://github.com/thtrieu/darkflow.git
	```

2. build
	```
	python3 setup.py build_ext --inplace
	```

3. modify `flow`
	```
	#! /usr/bin/env python3
	```

4. Dowload `yolo.cfg` in `cfg` and `yolo.weights` in `bin`
	```
	wget https://pjreddie.com/media/files/yolo.weights
	wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolo.cfg
	```


### Usage

Forward all images in `sample_img/` using yolo and 100% GPU usage and predictions are put in `sample_img/out/`
```
./flow --imgdir sample_img/ --model cfg/yolo.cfg --load bin/yolo.weights --gpu 1.0
```

Forward all images in `sample_img/` using yolo and JSON output are put in `sample_img/out/`
```
./flow --imgdir sample_img/ --model cfg/yolo.cfg --load bin/yolo.weights --gpu 1.0 --json
```

## Darknet

### Setup

1. clone this project
	```
	git clone https://github.com/pjreddie/darknet.git
	```

2. build
	```
	make
	```
3. Download `yolo.weights`
	```
	wget https://pjreddie.com/media/files/yolo.weights
	```

### Usage

run the detection
```
./darknet detect cfg/yolo.cfg yolo.weights data/dog.jpg
```
