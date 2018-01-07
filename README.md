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
![alt text](https://github.com/nickshao/PlayerTracker/blob/master/assets/t_original.jpg)<!-- .element height="50%" width="50%" -->  

Target tactic board:  
![alt text](https://github.com/nickshao/PlayerTracker/blob/master/assets/court.jpg)<!-- .element height="50%" width="50%" -->  

After Line detection and DBSCAN:  
![alt text](https://github.com/nickshao/PlayerTracker/blob/master/assets/t_houghlines.jpg)<!-- .element height="50%" width="50%" -->  

Warped Frame:  
![alt text](https://github.com/nickshao/PlayerTracker/blob/master/assets/t_warped.jpg)<!-- .element height="50%" width="50%" -->  

### Defects/Improvements

Several parameters need to be tuned to suit each video.













