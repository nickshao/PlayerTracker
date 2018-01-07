import cv2
import numpy as np
from sklearn.cluster import dbscan


# Input: A frame of basketball game
# Output: 
# 1. A transformation matrix that maps frame coordinate to tactic board coordinate
# 2. Warped frame

def intersection(o1, p1, o2, p2, img_size):
    def minus(p1, p2):
        return (p1[0] - p2[0], p1[1] - p2[1])

    x = minus(o2, o1)
    d1 = minus(p1, o1)
    d2 = minus(p2, o2)

    cross = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(cross) < 1e-8:
        return [False, (0, 0)]
    t1 = (x[0] * d2[1] - x[1] * d2[0]) / cross
    rx = int(o1[0] + d1[0] * t1)
    ry = int(o1[1] + d1[1] * t1)
    tf = False
    if img_size[1] > rx and rx > 0 and img_size[0] > ry and ry > 0:
        tf = True
    return [tf, (rx, ry)]

def getMatrix(img_path):
    img = cv2.imread(img_path)

    # mask floor color
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    lower = np.array([95, 50, 50], dtype ="uint8")
    upper = np.array([115, 255, 255], dtype="uint8")
    mask = cv2.inRange(img_hsv, lower, upper)

    # erosion and dilation
    kernel = np.ones((9, 9), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=3)
    mask = cv2.dilate(mask, kernel, iterations=3)
    #cv2.imwrite('test.jpg', mask)

    # get edge
    edges = cv2.Canny(mask,50,150,apertureSize = 3)

    #filter range
    fil = np.zeros(img.shape[:2], np.uint8)
    for i in range(int(img.shape[0] / 3), int(img.shape[0] * 2 / 3)):
        for j in range(int(img.shape[1] * 2 / 3)):
            fil[i, j] = 255
    edges = cv2.bitwise_and(edges, edges, mask=fil)
    #cv2.imwrite('edge.jpg', edges)

    # calculate Hough lines
    lines = cv2.HoughLines(edges,1,np.pi/180, 50)
    lines_points = []
    for i in range(len(lines)):
        for rho,theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            lines_points.append([(x1, y1), (x2, y2)])
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    # find intersection points
    points = []
    for i in range(len(lines_points)):
        for j in range(len(lines_points)):
            if i >= j:
                continue
            tf, r = intersection(lines_points[i][0], lines_points[i][1],
                         lines_points[j][0], lines_points[j][1], img.shape[:2])
            if tf == True:
               points.append(r)
               cv2.circle(img, r, 5, (0, 255, 0), -1)
    points = np.array(points)

    # cluster points and find centers
    core, lab = dbscan(points, eps=30, min_samples=10)
    centers = []
    for i in range(np.amax(lab) + 1):
        count = 0
        total = [0, 0]
        for p in range(len(points)):
            if lab[p] == i:
                count += 1
                total[0] += points[p][0]
                total[1] += points[p][1]
        total[0] = int(total[0] / count)
        total[1] = int(total[1] / count)
        centers.append(total)
        cv2.circle(img, (total[0], total[1]), 10, (255, 0, 0), -1)
    #cv2.imwrite('houghlines.jpg',img)

    # order centers
    max_x = 0
    min_x = img.shape[1]
    point0, point2 = -1, -1
    for i in range(len(centers)):
        if centers[i][0] > max_x:
            point0 = i
            max_x = centers[i][0]
        if centers[i][0] < min_x:
            point2 = i
            min_x = centers[i][0]
    max_y = 0
    min_y = img.shape[0]
    point1, point3 = -1, -1
    for i in range(len(centers)):
        if i == point0 or i == point2:
            continue
        if centers[i][1] > max_y:
            point1 = i
            max_y = centers[i][1]
        if centers[i][1] < min_y:
            point3 = i
            min_y = centers[i][1]

    # define court point and calculate the transformation matrix
    court0, court1, court2, court3 = (190, 0), (190, 328), (0, 328), (0, 0)
    dst_points = np.array([court0, court1, court2, court3], np.float32)
    src_points = np.array([centers[point0], centers[point1], centers[point2], centers[point3]], np.float32)
    M = cv2.getPerspectiveTransform(src_points, dst_points)
    warped = cv2.warpPerspective(img, M, (500, 470))
    cv2.imwrite('warped.jpg', warped)
    return M

if __name__ == '__main__':
    # test
    M = getMatrix('assets/a.jpg')
    print(M)
