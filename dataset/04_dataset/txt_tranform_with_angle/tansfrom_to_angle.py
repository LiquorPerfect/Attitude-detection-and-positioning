# -*- encoding: utf-8 -*-
'''
-----------------------------------------------
* @File    :   tansfrom.py
* @Time    :   2021/03/22 21:38:41
* @Author  :   zhang_jinlong
* @Version :   1.0
* @Contact :   zhangjinlongwin@163.com
* @Address ：  https://github.com/LiquorPerfect
-----------------------------------------------
'''

import numpy as np
import os
import math
import matplotlib.pyplot as plt


def main():
    file_dir = 'G:/pycharmcode/txt_to_xml/annotation_myself'
    save_dir = 'G:/pycharmcode/txt_to_xml/tansform_annotation'

    filelist = os.listdir(file_dir)

    for file in filelist:
        file_path = os.path.join(file_dir, file)
        f1 = open(file_path, 'r')
        lines = f1.readlines()
        lines_count = len(lines)
        save_path = os.path.join(save_dir, file)  #保存地址
        print(file)
        for n in range(int(lines_count / 4)):
            line1 = lines[4 * n]
            line2 = lines[4 * n + 1]
            line3 = lines[4 * n + 2]

            line_object1 = line1.split(' ')
            line_object2 = line2.split(' ')
            line_object3 = line3.split(' ')

            x1 = float(line_object1[0])
            y1 = float(line_object1[1])
            x2 = float(line_object2[0])
            y2 = float(line_object2[1])
            x3 = float(line_object3[0])
            y3 = float(line_object3[1])
            # sum_pow =math.pow(x1-x2,2)+math.pow(y1-y2,2)
            # print(sum_pow)

            #ang = line_object[4]
            # x1=1
            # y1=2
            # x2=2
            # y2=1
            # x3=4
            # y3=3
            center_x = (x1 + x3) / 2  #矩形中心
            center_y = (y1 + y3) / 2
            #print(x1,y1,x2,y2)

            if x1 != x2:
                theta = math.atan(
                    (y1 - y2) /
                    (x1 -
                     x2))  #*180/math.pi #这边算出来的角度取负值  这边是弧度制  在训练后是多少就是多少度
            if (x1 == x2) & (y1 > y2):  #逆时针
                theta = -math.pi / 2
            if (x1 == x2) & (y1 < y2):  #顺时针
                theta = math.pi / 2
            not_theta = -theta

            theta_ang = theta * 180 / math.pi  #这边正负号要注意

            mat = np.array([[math.cos(not_theta), -math.sin(not_theta)],
                            [math.sin(not_theta),
                             math.cos(not_theta)]])
            #print(mat)

            x1_ = x1 - center_x
            y1_ = y1 - center_y
            x3_ = x3 - center_x
            y3_ = y3 - center_y
            #print(x1_,y1_,x3_,y3_)
            if -90 <= theta_ang < -85:  #ang=-90
                ang = 1
            if -85 <= theta_ang < -75:  #ang=-80
                ang = 2
            if -75 <= theta_ang < -65:  #ang=-70
                ang = 3
            if -65 <= theta_ang < -55:  #ang=-60
                ang = 4
            if -55 <= theta_ang < -45:  #ang=-50
                ang = 5
            if -45 <= theta_ang < -35:  #ang=-40
                ang = 6
            if -35 <= theta_ang < -25:  #ang=-30
                ang = 7
            if -25 <= theta_ang < -15:  #ang=-20
                ang = 8
            if -15 <= theta_ang < -5:  #ang=-10
                ang = 9
            if -5 <= theta_ang < 5:  #ang=0
                ang = 10
            if 5 <= theta_ang < 15:  #ang=10
                ang = 11
            if 15 <= theta_ang < 25:  #ang=20
                ang = 12
            if 25 <= theta_ang < 35:  #ang=30
                ang = 13
            if 35 <= theta_ang < 45:  #ang=40
                ang = 14
            if 45 <= theta_ang < 55:  #ang=50
                ang = 15
            if 55 <= theta_ang < 65:  #ang=60
                ang = 16
            if 65 <= theta_ang < 75:  #ang=70
                ang = 17
            if 75 <= theta_ang < 85:  #ang=80
                ang = 18
            if 85 <= theta_ang <= 90:  #ang=90
                ang = 19

            ang_str = 'ang' + str(ang)

            x1_y1 = np.array([[x1_], [y1_]])
            x3_y3 = np.array([[x3_], [y3_]])
            # print(x1_y1)
            # print(x3_y3)
            matix_x1_y1 = np.dot(mat, x1_y1)
            matix_x3_y3 = np.dot(mat, x3_y3)
            # print(matix_x1_y1)
            # print(matix_x3_y3)

            x1_true = matix_x1_y1[0][0] + center_x
            y1_true = matix_x1_y1[1][0] + center_y
            x3_true = matix_x3_y3[0][0] + center_x  #算出转正的 坐标(x1,y1) (x3,y3)
            y3_true = matix_x3_y3[1][0] + center_y

            x1_true_str = str(int(x1_true))
            y1_true_str = str(int(y1_true))
            x3_true_str = str(int(x3_true))
            y3_true_str = str(int(y3_true))

            #print(float(x1_true),float(y1_true),float(x3_true),float(y3_true),ang_str)
            # plt.plot((x1,x2),(y1,y2),color='red')
            # plt.plot((x1_true,x3_true),(y1_true,y3_true),color='green')
            # plt.show()

            # if os.path.exists(save_path):
            #         #     os.remove(save_path)
            file_write_obj = open(save_path, 'a')
            var = [
                x1_true_str, ' ', y1_true_str, ' ', x3_true_str, ' ',
                y3_true_str, ' ', ang_str, '\n'
            ]
            #for var in range(int(lines_count)/4):
            file_write_obj.writelines(var)

            #print(x1, y1,x2,y2,theta)


if __name__ == "__main__":
    main()