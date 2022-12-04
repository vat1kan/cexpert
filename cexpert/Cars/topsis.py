import numpy as np
import pandas as pd

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:0.4f}'.format})

# def Grading (df):
#     df = df.drop(df.columns[[0, 1]], axis=1)
#     df[4] = df[4].replace(['Manual', 'Auto',], [1, 2])
#     df[5] = df[5].replace(['Gas', 'Diesel'], [2, 1])
#     return df

def Normalization(df):
    #df = Grading(df)
    w = np.zeros(df.shape[1])
    arr = np.array(df)
    for i in range(len(w)):
        w[i] = np.power(np.sum(np.square(np.array(df[i+2].values))),0.5)
    for j in range(arr.shape[1]):
        for i in range(arr.shape[0]):
            arr[i,j] = arr[i,j]/w[j] 
    return arr

def R_Max_Min(df):
    arr = Normalization(df)
    r_max = np.amax(arr,axis = 0)
    r_min = np.amin(arr,axis = 0)
    return arr, r_max, r_min

def Distances(df):
    arr, r_max, r_min = R_Max_Min(df)
    S_plus = np.zeros(arr.shape[0])
    S_min = np.zeros(arr.shape[0])
    for i in range(arr.shape[0]):
        S_plus[i] = np.power(np.sum(np.square(arr[i,:] - r_max)),0.5)
        S_min[i] = np.power(np.sum(np.square(arr[i,:] - r_min)),0.5)
    return S_plus, S_min


def Closeness(df):
    s_plus, s_min = Distances(df)
    k = np.zeros(s_plus.shape)
    for i in range(len(k)):
        k[i] = s_min[i]/(s_plus[i]+s_min[i])
    return k

# def Result1(data):
#     dataFrame = pd.DataFrame(data)
#     df = dataFrame.drop(dataFrame.columns[[0, 1,2,5]], axis=1)
#     sorted_list = np.array(dataFrame)
#     k = Closeness(df)
#     sort = np.argsort(k)
#     return sorted_list[~sort]



# data = [[1,'Name1',26000,2,'Manual','Gas',2006,3],
#         [2,'Name2',19300,1.8,'Auto','Gas',2001,3],
#         [3,'Name3',14490,1.8,'Manual','Diesel',2003,1],
#         [4,'Name4',19900,2.4,'Auto','Gas',2007,2]]

# dataFrame = pd.DataFrame(data)

# res = Result(data,dataFrame)

def dataFrame(data):
    dataFrame = pd.DataFrame(data)
    #df = np.array(dataFrame)
    df = dataFrame.drop(['id','name','carmod','picture'],axis = 1)
    return df