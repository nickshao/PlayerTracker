# PlayerTracker

Track the movements of NBA players and map them onto a tactic board.  

## System Pipeline  

0. Preprocessing : Extract frames from NBA highlight video taking advantage of ffmpeg.
1. Object Detection : Use YOLO or Faster-rcnn to detect players in each frame.
2. Team Classifier : Tandform each bounding box into histogram vvector and label three bounding box to classify players' corresponding teams.
3. Mapping between video and tatic board : Utilize court line to map frame to tatic board.
4. Player Tracking : For each frame, use their former or latter frame to delete rebundant point and do track smoothing.
5. Postprocessing : Convert frames into video with ffmpeg.

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

After Line detection and DBSCAN:  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/t_houghlines.jpg" width="50%" height="50%"/>  

Warped Frame:  
<img src="https://github.com/nickshao/PlayerTracker/blob/master/assets/t_warped.jpg" width="50%" height="50%"/>  

### Environment


### Reference

To do:













