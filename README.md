# PlayerTracker

Track the movements of NBA players and map them onto a tactic board.  

## System Pipeline  

### 0. Preprocessing : 
Extract frames from NBA highlight video taking advantage of ffmpeg.
---

### 1. Object Detection : 
Use YOLO or Faster-rcnn to detect players in each frame.
---

### 2. Team Classifier : 
Tandform each bounding box into histogram vvector and label three bounding box to classify players' corresponding teams.
---

### 3. Mapping between video and tatic board : 
Utilize court line to map frame to tatic board.
---

### 4. Player Tracking : 
For each frame, use their former or latter frame to delete rebundant point and do track smoothing.
---

### 5. Postprocessing : 
Convert frames into video with ffmpeg.
---

### Train

```
sh train.sh
```

### Test

```
python3.6 index2court/player_track_warriors.py
```

### Demo

Original image:  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/t_original.jpg" width="50%" height="50%"/>  

Target tactic board:  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/court.jpg" width="50%" height="50%"/>  

Step1 : Object detection (YOLO)  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/Picture1.png" width="50%" height="50%"/> 

Step2 : Team Classifier  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/Picture3.png" width="50%" height="50%"/>

Step3 : Mapping
1, Line detection and DBSCAN:  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/t_houghlines.jpg" width="50%" height="50%"/>  

2, Warped Frame:  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/t_warped.jpg" width="50%" height="50%"/>

Step4 : Player Tracking  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/Picture4.png" width="50%" height="50%"/>  

### Dependency
- cv2
- ffmpeg
- matplotlib
- numpy
- pandas
- pickle
- python3.6
- sklearn

### Reference

Todo:













