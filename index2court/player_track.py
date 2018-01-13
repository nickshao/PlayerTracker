import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
import pandas as pd
from Constant import Constant
import pickle
import numpy as np
import cv2
import copy

#color_class = pickle.load( open( "../player_classify/new_threshold.pkl", "rb" ) )
color_class = pickle.load( open( "../player_classify/query_method001.pkl", "rb" ) )
color_type = [(255,255,0),(32,32,32),(51,51,255), (255,51,51), (51,255,51), (32,32,32)]

matrix = np.load("transform.npy")
index = [[],[],[],[]]

for i in range(4,80):
    fname = 'output{0:03d}'.format(i)

    data = pd.read_json('../yolo/jazz_thunder/result/output{0:03d}.json'.format(i))
    #if i == 74:
        #print (data)
    
    img= cv2.imread('court.png')
    tmp = []
    for j in range(len(data['bottomright'])):
        pts = np.array([[(data['bottomright'][j]['x']+data['topleft'][j]['x'])/2, data['bottomright'][j]['y']]], dtype = "float32")
        pts = np.array([pts])
        pts = cv2.perspectiveTransform(pts, matrix[i-4])
        #cv2.circle(img, (pts[0][0][0], pts[0][0][1]), 10, color_type[color_class[fname][j]], -1)
        if 0<pts[0][0][0] < 940 and 0 < pts[0][0][1] < 500 and (color_class[fname][j] == 1 or color_class[fname][j] == 0) :
            tmp.append([pts[0][0][0], pts[0][0][1], color_class[fname][j]])
            #tmp.append([pts[0][0][0], pts[0][0][1], data['confidence'][j]])
    index.append(tmp)
    img = cv2.resize(img, (940, 500)) 
    #cv2.imwrite('game_result/myfig_{0:03d}.jpg'.format(i), img)


#print(color_class['output074'])

track = {}
tmp = {}
for i in range(10):
    tmp[i] = index[74][i]
track[74] = tmp

for i in range(73,3,-1):
    tmp = {}
    tmp_track = copy.deepcopy(track[i+1])
    #print(tmp_track)
    #print()
    for (k,ind) in enumerate(index[i]):
        min_index = 0
        min_dis = 9999999
        for j in range(10):
            tr = tmp_track[j]
            dis = ((tr[0]-ind[0])**2+(tr[1]-ind[1])**2)**0.5
            if dis < min_dis:
                min_dis = dis
                min_index = j
        tmp_track[min_index][0] = 9999
        tmp_track[min_index][1] = 9999
        tmp[min_index] = ind

    for j in range(10):
        tr = tmp_track[j]
        if tr[0] != 9999 and tr[1] != 9999:
            tmp[j] = tr
    track[i] = tmp
#print(track[74])
#print(track[73])
#print(track[72])
for i in range(4,75):
    img= cv2.imread('court.png')
    for j in range(len(track[i])):
        #cv2.circle(img, (pts[0][0][0], pts[0][0][1]), 10, color_type[0], -1)
        cv2.circle(img, (track[i][j][0], track[i][j][1]), 20, color_type[track[i][j][2]], thickness=-1, lineType=8, shift=0)
    img = cv2.resize(img, (940, 500)) 
    cv2.imwrite('game_out/myfig_{0:03d}.jpg'.format(i), img)
    


