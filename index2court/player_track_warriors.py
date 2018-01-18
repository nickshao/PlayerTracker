import pandas as pd
import pickle
import numpy as np
import cv2
import copy

color_class = pickle.load( open( "../player_classify/query_method001_warriors_vs_jazz.pkl", "rb" ) )
color_type = [(160,160,160),(255,0,0),(32,32,32),(51,51,255), (255,51,51), (51,255,51), (32,32,32)]

matrix = np.load("../input_frames/warrior_vs_jazz/transform.npy")
index = [[]]

for i in range(1,76):
    fname = 'output{0:03d}'.format(i)

    data = pd.read_json('../yolo/warrior_vs_jazz/result/output{0:03d}.json'.format(i))
    tmp = []
    for j in range(len(data['bottomright'])):
        pts = np.array([[(data['bottomright'][j]['x']+data['topleft'][j]['x'])/2, data['bottomright'][j]['y']]], dtype = "float32")
        pts = np.array([pts])
        pts = cv2.perspectiveTransform(pts, matrix[i-1])
        #cv2.circle(img, (pts[0][0][0], pts[0][0][1]), 10, color_type[color_class[fname][j]], -1)
        if 0<pts[0][0][0] < 940 and 0 < pts[0][0][1] < 500 and (color_class[fname][j] == 1 or color_class[fname][j] == 0) :
            tmp.append([pts[0][0][0], pts[0][0][1], color_class[fname][j]])
            #tmp.append([pts[0][0][0], pts[0][0][1], color_class[fname][j], data['confidence'][j]])
    index.append(tmp)

index[46][5][2] = 0
index[46][-1][2] = 1
track = {}
tmp = {}


for i in range(10):
    tmp[i] = index[46][i]
track[46] = tmp

for i in range(45,0,-1):
    tmp = {}
    tmp_track = copy.deepcopy(track[i+1])
    for (k,ind) in enumerate(index[i]):
        min_index = 0
        min_dis = 9999999
        for j in range(10):
            tr = tmp_track[j]
            dis = ((tr[0]-ind[0])**2+(tr[1]-ind[1])**2)**0.5
            if dis < min_dis:
                min_dis = dis
                min_index = j
        if min_dis > 150:
            continue
        tmp_track[min_index][0] = 9999
        tmp_track[min_index][1] = 9999
        tmp[min_index] = ind

    for j in range(10):
        tr = tmp_track[j]
        if tr[0] != 9999 and tr[1] != 9999:
            tmp[j] = tr
    track[i] = tmp
for i in range(47,76,1):
    tmp = {}
    tmp_track = copy.deepcopy(track[i-1])
    for (k,ind) in enumerate(index[i]):
        min_index = 0
        min_dis = 9999999
        for j in range(10):
            tr = tmp_track[j]
            dis = ((tr[0]-ind[0])**2+(tr[1]-ind[1])**2)**0.5
            if dis < min_dis:
                min_dis = dis
                min_index = j
        if min_dis > 150:
            continue
        tmp_track[min_index][0] = 9999
        tmp_track[min_index][1] = 9999
        tmp[min_index] = ind

    for j in range(10):
        tr = tmp_track[j]
        if tr[0] != 9999 and tr[1] != 9999:
            tmp[j] = tr
    track[i] = tmp

for j in range(10):
    last_x = 0
    last_y = 0
    count = 0
    for i in range(75,0,-1):
        if track[i][j][0] == last_x and track[i][j][1] == last_y:
            count += 1
        else:
            count += 1
            if count > 2:
                inter_x = (track[i+count][j][0] - track[i][j][0]) / count
                inter_y = (track[i+count][j][1] - track[i][j][1]) / count
                for k in range(count):
                    track[i+count-k][j][0] += inter_x * k
                    track[i+count-k][j][1] += inter_y * k
            count = 0
            last_x = track[i][j][0]
            last_y = track[i][j][1]

for i in range(1,75):
    for k in range(10): 
        img= cv2.imread('court.png')
        for j in range(len(track[i])):
            dx = (track[i+1][j][0] - track[i][j][0]) / 10
            dy = (track[i+1][j][1] - track[i][j][1])/ 10
            cv2.circle(img, (int(track[i][j][0] + k * dx), int(track[i][j][1] + k * dy)), 15, color_type[track[46][j][2]], thickness=-1, lineType=8, shift=0)
            img = cv2.resize(img, (940, 500)) 
            cv2.imwrite('game_out2/myfig_{0:03d}-{1:02d}.jpg'.format(i, k), img)
 
