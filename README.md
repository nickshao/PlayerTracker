# PlayerTracker

Track the movements of NBA players and map them onto a tactic board.  

## System Pipeline  

1. Bounding boxes and locations detection.  
2. Locations tranformation from video frames to tactic board.  
3. Reconstruction of movements on the tactic board.  

## Location Transformation

Takes a frame and returns the transformation matrix for mapping between video and tactic board.

### To Test

```
python3 src/tranform.py
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

### Defects/Improvements

Several parameters need to be tuned to suit each video.













