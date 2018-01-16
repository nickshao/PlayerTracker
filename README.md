# PlayerTracker: Neural Basketball Assistant

Final Project of Applied Deep Learning 2017 in NTU.

Track the movements of NBA players and map them onto a tactic board.  

## System Pipeline  

### 0. Preprocessing : 
Extract frames from NBA highlight video taking advantage of ffmpeg.  
p.s. In `warrior_vs_jazz/` directory


### 1. Object Detection : 
Use YOLO or Faster-rcnn to detect players in each frame.  
p.s. In `yolo/` directory


### 2. Team Classifier : 
Tandform each bounding box into histogram vvector and label three bounding box to classify players' corresponding teams.  
p.s. In `player_classify/` directory


### 3. Mapping between video and tatic board : 
Utilize court line to map frame to tatic board.  
p.s. In `src/` directory


### 4. Player Tracking : 
For each frame, use their former or latter frame to delete rebundant point and do track smoothing.  
p.s. In `index2court/` directory

### 5. Postprocessing : 
Convert frames into video with ffmpeg.  
p.s. `warroirs_vs_jazz.mp4`


### Train

```
sh train.sh
```

### Test

```
python3.6 index2court/player_track_warriors.py
```
p.s. Output frames will store in `index2court/game_out2/`.

### Demo

Original image:  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/t_original.jpg" width="50%" height="50%"/>  

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

Step5 : Postprocessing  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/w_j.gif" width="50%" height="50%"/>  

Final Compare :    
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/compare.gif" width="50%" height="50%"/>  

### Dependency
- cv2
- ffmpeg
- matplotlib
- numpy
- pandas
- pickle
- python3.6
- sklearn

### Contributors:
Team : ADL 躺分仔
- 李承軒 [B03902009]("https://github.com/Spicy30")  
- 陳雋 [B03902033]("https://github.com/falloutboyrocks")  
- 顏廷宇 [B03902052]("https://github.com/y95847frank")  
- 紀典佑 [B03902058]("https://github.com/dianyo")  
- 邵楚荏 [B03902090]("https://www.google.com")  
- I'm an inline-style [link](https://www.google.com)
[I'm an inline-style link](https://www.google.com)

### Reference

Todo:

