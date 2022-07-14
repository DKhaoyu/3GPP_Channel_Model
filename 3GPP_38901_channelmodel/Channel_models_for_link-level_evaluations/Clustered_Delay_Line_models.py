#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Clustered_Delay_Line_models.py  (CDL)
@Time    :   2022/06/29
@Author  :   LuDaYong
@Version :   1.0
@parameter:   
'''



import numpy as np
import docx
from docx import Document #导入库

CDL_A = []
def read_docx():

    path = "C:\\Users\\15751002165\\Downloads\\38901-h00\\38901-h0000.docx" #文件路径
    document = Document(path) #读入文件
    tables = document.tables #获取文件中的表格集
    table = tables[43]#获取文件中的第43个表格   
    for i in range(1,16):#从表格第二行开始循环读取表格数据
        result = table.cell(i,0).text + " " +table.cell(i,1).text+ " "+table.cell(i,2).text+ " " + table.cell(i,3).text
        CDL_A.append([float(table.cell(i,0).text),float(table.cell(i,3).text),float(table.cell(i,4).text ) ,float(table.cell(i,5).text ),float(table.cell(i,6).text) ,float(table.cell(i,8).text), float(table.cell(i,9).text )])
        #cell(i,0)表示第(i+1)行第1列数据，以此类推
        #由于Word中的表格实际的列标号可能并非所见的按1、2、3、4....这般顺序进行（怀疑在制表的时候对某些单元格进行了合并），因此需查看每一个table.cell(i,3).text的具体内容，按照实际获取到的值调整table.cell（）的第二个参数

    print(len(tables),'1111111111111111111111')
    print(CDL_A)



#Cluster	Normalized delay	Power in [dB]	AOD in [°]	AOA in [°]	ZOD in [°]	ZOA in [°]
CDL_A_1 = [[1.0, 0.0, -13.4, -178.1, 51.3, 50.2, 125.4], [2.0, 0.3819, 0.0, -4.2, -152.7, 93.2, 91.3], [3.0, 0.4025, -2.2, -4.2, -152.7, 93.2, 91.3], [4.0, 0.5868, -4.0, -4.2, -152.7, 93.2, 91.3], [5.0, 0.461, -6.0, 90.2, 76.6, 122.0, 94.0], [6.0, 0.5375, -8.2, 90.2, 76.6, 122.0, 94.0], [7.0, 0.6708, -9.9, 90.2, 76.6, 122.0, 94.0], [8.0, 0.575, -10.5, 121.5, -1.8, 150.2, 47.1], [9.0, 0.7618, -7.5, -81.7, -41.9, 55.2, 56.0], [10.0, 1.5375, -15.9, 158.4, 94.2, 26.4, 30.1], [11.0, 1.8978, -6.6, -83.0, 51.9, 126.4, 58.8], [12.0, 2.2242, -16.7, 134.8, -115.9, 171.6, 26.0], [13.0, 2.1718, -12.4, -153.0, 26.6, 151.4, 49.2], [14.0, 2.4942, -15.2, -172.0, 76.6, 157.2, 143.1], [15.0, 2.5119, -10.8, -129.9, -7.0, 47.2, 117.4], [16.0, 3.0582, -11.3, -136.0, -23.0, 40.4, 122.7], [17.0, 4.081, -12.7, 165.4, -47.2, 43.3, 123.2], [18.0, 4.4579, -16.2, 148.4, 110.4, 161.8, 32.6], [19.0, 4.5695, -18.3, 132.7, 144.5, 10.8, 27.2], [20.0, 4.7966, -18.9, -118.6, 155.3, 16.7, 15.2], [21.0, 5.0066, -16.6, -154.1, 102.0, 171.7, 146.0], [22.0, 5.3043, -19.9, 126.5, -151.8, 22.7, 150.7], [23.0, 9.6586, -29.7, -56.2, 55.2, 144.9, 156.1]]
CDL_A_2 = {
    'c_ASD_in':5,
    'c_ASA_in':11,
    'c_ZSD_in':3,
    'c_ZSA_in':3,
    'XPR_in':10 
}

CDL_B_1 = [[1.0, 0.0, 0.0, 9.3, -173.3, 105.8, 78.9], [2.0, 0.1072, -2.2, 9.3, -173.3, 105.8, 78.9], [3.0, 0.2155, -4.0, 9.3, -173.3, 105.8, 78.9], [4.0, 0.2095, -3.2, -34.1, 125.5, 115.3, 63.3], [5.0, 0.287, -9.8, -65.4, -88.0, 119.3, 59.9], [6.0, 0.2986, -1.2, -11.4, 155.1, 103.2, 67.5], [7.0, 0.3752, -3.4, -11.4, 155.1, 103.2, 67.5], [8.0, 0.5055, -5.2, -11.4, 155.1, 103.2, 67.5], [9.0, 0.3681, -7.6, -67.2, -89.8, 118.2, 82.6], [10.0, 0.3697, -3.0, 52.5, 132.1, 102.0, 66.3], [11.0, 0.57, -8.9, -72.0, -83.6, 100.4, 61.6], [12.0, 0.5283, -9.0, 74.3, 95.3, 98.3, 58.0], [13.0, 1.1021, -4.8, -52.2, 103.7, 103.4, 78.2], [14.0, 1.2756, -5.7, -50.5, -87.8, 102.5, 82.0], [15.0, 1.5474, -7.5, 61.4, -92.5, 101.4, 62.4], [16.0, 1.7842, -1.9, 30.6, -139.1, 103.0, 78.0], [17.0, 2.0169, -7.6, -72.5, -90.6, 100.0, 60.9], [18.0, 2.8294, -12.2, -90.6, 58.6, 115.2, 82.9], [19.0, 3.0219, -9.8, -77.6, -79.0, 100.5, 60.8], [20.0, 3.6187, -11.4, -82.6, 65.8, 119.6, 57.3], [21.0, 4.1067, -14.9, -103.6, 52.7, 118.7, 59.9], [22.0, 4.279, -9.2, 75.6, 88.7, 117.8, 60.1], [23.0, 4.7834, -11.3, -77.6, -60.4, 115.7, 62.3]]
CDL_B_2 = {
    'c_ASD_in':10,
    'c_ASA_in':22,
    'c_ZSD_in':3,
    'c_ZSA_in':7,
    'XPR_in':8
}

CDL_C_1 = [[1.0, 0.0, -4.4, -46.6, -101.0, 97.2, 87.6], [2.0, 0.2099, -1.2, -22.8, 120.0, 98.6, 72.1], [3.0, 0.2219, -3.5, -22.8, 120.0, 98.6, 72.1], [4.0, 0.2329, -5.2, -22.8, 120.0, 98.6, 72.1], [5.0, 0.2176, -2.5, -40.7, -127.5, 100.6, 70.1], [6.0, 0.6366, 0.0, 0.3, 170.4, 99.2, 75.3], [7.0, 0.6448, -2.2, 0.3, 170.4, 99.2, 75.3], [8.0, 0.656, -3.9, 0.3, 170.4, 99.2, 75.3], [9.0, 0.6584, -7.4, 73.1, 55.4, 105.2, 67.4], [10.0, 0.7935, -7.1, -64.5, 66.5, 95.3, 63.8], [11.0, 0.8213, -10.7, 80.2, -48.1, 106.1, 71.4], [12.0, 0.9336, -11.1, -97.1, 46.9, 93.5, 60.5], [13.0, 1.2285, -5.1, -55.3, 68.1, 103.7, 90.6], [14.0, 1.3083, -6.8, -64.3, -68.7, 104.2, 60.1], [15.0, 2.1704, -8.7, -78.5, 81.5, 93.0, 61.0], [16.0, 2.7105, -13.2, 102.7, 30.7, 104.2, 100.7], [17.0, 4.2589, -13.9, 99.2, -16.4, 94.9, 62.3], [18.0, 4.6003, -13.9, 88.8, 3.8, 93.1, 66.7], [19.0, 5.4902, -15.8, -101.9, -13.7, 92.2, 52.9], [20.0, 5.6077, -17.1, 92.2, 9.7, 106.7, 61.8], [21.0, 6.3065, -16.0, 93.3, 5.6, 93.0, 51.9], [22.0, 6.6374, -15.7, 106.6, 0.7, 92.9, 61.7], [23.0, 7.0427, -21.6, 119.5, -21.9, 105.2, 58.0], [24.0, 8.6523, -22.8, -123.8, 33.6, 107.8, 57.0]]
CDL_C_2 = {
    'c_ASD_in':2,
    'c_ASA_in':15,
    'c_ZSD_in':3,
    'c_ZSA_in':7,
    'XPR_in':7
}

CDL_D_1 = [[1.0, 0.0, -0.2, 0.0, -180.0, 98.5, 81.5], [1.0, 0.0, -13.5, 0.0, -180.0, 98.5, 81.5], [2.0, 0.035, -18.8, 89.2, 89.2, 85.5, 86.9], [3.0, 0.612, -21.0, 89.2, 89.2, 85.5, 86.9], [4.0, 1.363, -22.8, 89.2, 89.2, 85.5, 86.9], [5.0, 1.405, -17.9, 13.0, 163.0, 97.5, 79.4], [6.0, 1.804, -20.1, 13.0, 163.0, 97.5, 79.4], [7.0, 2.596, -21.9, 13.0, 163.0, 97.5, 79.4], [8.0, 1.775, -22.9, 34.6, -137.0, 98.5, 78.2], [9.0, 4.042, -27.8, -64.5, 74.5, 88.4, 73.6], [10.0, 7.937, -23.6, -32.9, 127.7, 91.3, 78.3], [11.0, 9.424, -24.8, 52.6, -119.6, 103.8, 87.0], [12.0, 9.708, -30.0, -132.1, -9.1, 80.3, 70.6], [13.0, 12.525, -27.7, 77.2, -83.8, 86.5, 72.9]]
CDL_D_2 = {
    'c_ASD_in':5,
    'c_ASA_in':8,
    'c_ZSD_in':3,
    'c_ZSA_in':3,
    'XPR_in':11
}

CDL_E_1 = [[1.0, 0.0, -0.03, 0.0, -180.0, 99.6, 80.4], [1.0, 0.0, -22.03, 0.0, -180.0, 99.6, 80.4], [2.0, 0.5133, -15.8, 57.5, 18.2, 104.2, 80.4], [3.0, 0.544, -18.1, 57.5, 18.2, 104.2, 80.4], [4.0, 0.563, -19.8, 57.5, 18.2, 104.2, 80.4], [5.0, 0.544, -22.9, -20.1, 101.8, 99.4, 80.8], [6.0, 0.7112, -22.4, 16.2, 112.9, 100.8, 86.3], [7.0, 1.9092, -18.6, 9.3, -155.5, 98.8, 82.7], [8.0, 1.9293, -20.8, 9.3, -155.5, 98.8, 82.7], [9.0, 1.9589, -22.6, 9.3, -155.5, 98.8, 82.7], [10.0, 2.6426, -22.3, 19.0, -143.3, 100.8, 82.9], [11.0, 3.7136, -25.6, 32.7, -94.7, 96.4, 88.0], [12.0, 5.4524, -20.2, 0.5, 147.0, 98.9, 81.0], [13.0, 12.0034, -29.8, 55.9, -36.2, 95.6, 88.6], [14.0, 20.6419, -29.2, 57.6, -26.0, 104.6, 78.3]]
CDL_E_2 = {
    'c_ASD_in':5,
    'c_ASA_in':11,
    'c_ZSD_in':3,
    'c_ZSA_in':7,
    'XPR_in':8
}




if __name__=='__main__':
    print('11111')
    read_docx()