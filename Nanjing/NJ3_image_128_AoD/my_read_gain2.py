# -*- coding: utf-8 -*-


import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linalg as LA
from scipy.interpolate import griddata
from matplotlib import cm
from matplotlib.patches import Ellipse
import os
from PIL import Image
c = 3*10**8
f = 28*10**9
lmd = c/f

RT_TX_POWER_dBm=0 #required to calculate the path gain based on the path power

# UE_num=123201    #Number of UE
# tx_1=np.array([1800.0, 600.0, 39.0])
# tx_2=np.array([1900.0, 600.0, 91.0])
# tx_3=np.array([2000.0, 600.0, 51.0])
# tx_4=np.array([2100.0, 600.0, 42.0])
# tx_5=np.array([1800.0, 700.0, 71.0])
# tx_6=np.array([1900.0, 700.0, 98.0])
# tx_7=np.array([2000.0, 700.0, 85.0])
# tx_8=np.array([2100.0, 700.0, 15.0])
# tx_9=np.array([1800.0, 800.0, 73.0])
# tx_10=np.array([1900.0, 800.0, 40.0])
# tx_11=np.array([2000.0, 800.0, 20.0])
# tx_12=np.array([2100.0, 800.0, 105.0])
# tx_13=np.array([1800.0, 900.0, 65.0])
# tx_14=np.array([1900.0, 900.0, 16.0])
# tx_15=np.array([2000.0, 900.0, 20.0])
# tx_16=np.array([2100.0, 900.0, 20.0])
# tx_1=np.array([1800.0, -200.0, 39.0])
# tx_2=np.array([1900.0, -200.0, 91.0])
# tx_3=np.array([2000.0, -200.0, 51.0])
# tx_4=np.array([2100.0, -200.0, 42.0])
# tx_5=np.array([1800.0, -100.0, 71.0])
# tx_6=np.array([1900.0, -100.0, 98.0])
# tx_7=np.array([2000.0, -100.0, 85.0])
# tx_8=np.array([2100.0, -100.0, 15.0])
# tx_9=np.array([1800.0, 0.0, 73.0])
# tx_10=np.array([1900.0, 0.0, 40.0])
# tx_11=np.array([2000.0, 0.0, 20.0])
# tx_12=np.array([2100.0, 0.0, 105.0])
# tx_13=np.array([1800.0, 100.0, 65.0])
# tx_14=np.array([1900.0, 100.0, 16.0])
# tx_15=np.array([2000.0, 100.0, 20.0])
# tx_16=np.array([2100.0, 100.0, 20.0])
# tx=np.array([tx_1,tx_2,tx_3,tx_4,tx_5,tx_6,tx_7,tx_8,tx_9,tx_10,tx_11,tx_12,tx_13,tx_14,tx_15,tx_16])

UE_num=123201    #Number of UE
tx_1=np.array([-100.0, -900.0, 39.0])
tx_2=np.array([0.0, -900.0, 91.0])
tx_3=np.array([100.0, -900.0, 51.0])
tx_4=np.array([200.0, -900.0, 42.0])
tx_5=np.array([-100.0, -800.0, 71.0])
tx_6=np.array([0.0, -800.0, 98.0])
tx_7=np.array([100.0, -800.0, 85.0])
tx_8=np.array([200.0, -800.0, 15.0])
tx_9=np.array([-100.0, -700.0, 73.0])
tx_10=np.array([0.0, -700.0, 40.0])
tx_11=np.array([100.0, -700.0, 20.0])
tx_12=np.array([200.0, -700.0, 105.0])
tx_13=np.array([-100.0, -600.0, 65.0])
tx_14=np.array([0.0, -600.0, 16.0])
tx_15=np.array([100.0, -600.0, 20.0])
tx_16=np.array([200.0, -600.0, 20.0])

tx=np.array([tx_1,tx_2,tx_3,tx_4,tx_5,tx_6,tx_7,tx_8,tx_9,tx_10,tx_11,tx_12,tx_13,tx_14,tx_15,tx_16])

PATH_FILE_DIR='area11.paths.t0'

def read_ray_tracing_data():
    # path_knowl = np.array([], dtype=np.float64).reshape(0, 3)
    path_knowl = np.array([], dtype=np.float64).reshape(0, 4)

    path_file_name_M1 = PATH_FILE

    with open(path_file_name_M1, 'r') as f1:
        all_lines_M1 = f1.readlines()

    s = 22

    for j in range(UE_num):

        p_n = all_lines_M1[s].split()
        PATH_num = int(p_n[1])


        if PATH_num == 0:
            s = s + 1
        else:
            path = s + 2
            angle = all_lines_M1[path].split()
            gain1 = float(angle[2])


            for i in range(PATH_num):
                data = all_lines_M1[path].split()
                interactions = int(data[1])
                path = path + 4 + interactions

            RX1 = path - 1
            loc_inform = all_lines_M1[RX1].split()

            u_heit = float(loc_inform[2])

            inform = np.array([[float(loc_inform[0]), float(loc_inform[1]), float(gain1), u_heit]])
            path_knowl = np.concatenate((path_knowl, inform))

            s = path

    return path_knowl


def choose_point():
    # useful_point = np.array([], dtype=np.float64).reshape(0, 3)
    useful_point = np.array([], dtype=np.float64).reshape(0, 4)
    for n in range(p_num):
        if path_knowl[n, 0] >= center_x - 200 and path_knowl[n, 0] < center_x + 200 and path_knowl[
            n, 1] >= center_y - 200 and path_knowl[n, 1] < center_y + 200:
            # aa = np.array([[float(path_knowl[n, 0]), float(path_knowl[n, 1]), float(path_knowl[n, 2])]])
            aa = path_knowl[n].reshape(1, 4)
            useful_point = np.concatenate((useful_point, aa))

    return useful_point

for BS_num in range(16):

    if BS_num + 1 <= 9:
        BS_name_str = str(BS_num + 1).zfill(2)
    else:
        BS_name_str = str(BS_num + 1)  # 把数字转换成字符串

    PATH_FILE = PATH_FILE_DIR+BS_name_str+'_08.r010.p2m'

    path_knowl = read_ray_tracing_data()
    BS_num_str=str(BS_num+1)

    p_num = path_knowl.shape[0]

    BS_num_str = str(BS_num + 1)

    tx_x=tx[BS_num,0]
    tx_y=tx[BS_num,1]

    center_x = tx_x
    center_y = tx_y

    useful_point = np.array([], dtype=np.float64).reshape(0, 3)

    BS_num_str = str(BS_num + 1)



    x = np.arange(center_x-200, center_x+200, 2)
    y = np.arange(center_y-200, center_y+200, 2)
    # 使用meshgrid生成二维网格
    X, Y = np.meshgrid(x, y)

    grid_shape = X.shape
    default_gain = -250
    default_extra = -250
    num_points = X.size  # 总点数

    # 创建一个与X, Y相同大小的数组，用于存储插值结果
    # Z = np.empty(X.shape)
    #
    # # 将0填充到Z数组中
    # Z.fill(-250)

    # 创建一个包含x, y坐标和值0的数组
    # points = np.column_stack((X.ravel(), Y.ravel(), Z.ravel()))

    points = np.column_stack((X.ravel(), Y.ravel(),
                              np.full(num_points, default_gain),
                              np.full(num_points, default_extra)))

    useful_point = choose_point()

    # 将points数组的值展平为一维数组，便于索引
    points_flat = points.reshape(-1)

    # 遍历useful_points中的每个点
    for idx, (x, y, ugain, uh) in enumerate(useful_point):
                # 找到points数组中x和y坐标匹配的点的索引
                idx_points = np.where((points[:, 0] == x) & (points[:, 1] == y))

                # 更新points数组中的值
                for idx_point in idx_points[0]:
                    # points_flat[idx_point * 3 + 2]  = value
                    points[idx_point, 2] = ugain
                    points[idx_point, 3] = uh
    # 将points数组恢复为原来的(N, 3)形状
    # points = points_flat.reshape(-1, 3)
    points = points_flat.reshape(-1, 4)


    # Z_values = points_flat[2::3]  # 从索引2开始，步长为3

    # 重新塑形为 64x64 的矩阵
    # Z_matrix = Z_values.reshape(200, 200)

    Z_gain = points[:, 2].reshape(200, 200)
    Z_uh = points[:, 3].reshape(200, 200)
    # 合并为一个多通道数组：最后 shape (200,200,2)
    Z_matrix = np.stack((Z_gain, Z_uh), axis=-1)

    # Z_matrix = Z_matrix[::200 // 128, ::200 // 128]  # 每隔 (200//128) 取一个值
    filename = f'2_gain3_CNJ_{BS_num_str}.npz'
    np.savez(filename, Z_matrix)


    # # 归一化 Z_matrix 到 0～255（注意：这里需要根据实际数值范围进行调整）
    # Z_min = Z_matrix.min()
    # Z_max = Z_matrix.max()
    # norm_matrix = (Z_matrix - Z_min) / (Z_max - Z_min) * 255
    # norm_matrix = norm_matrix.astype(np.uint8)
    #
    # # 利用 Image.fromarray 转换为灰度图（mode='L' 表示灰度图）
    # img = Image.fromarray(norm_matrix, mode='L')
    #
    # # 指定保存文件夹，如 'output_images'，如果文件夹不存在则创建它
    # output_folder = 'czt_output_BJ1'
    # if not os.path.exists(output_folder):
    #     os.makedirs(output_folder)
    #
    # # 构造图片文件名，例如 gain1_1.png、gain1_2.png 等
    # img_filename = os.path.join(output_folder, f'BJ1_128_BS{BS_num_str}.png')
    #
    # # 保存图片
    # img.save(img_filename)











