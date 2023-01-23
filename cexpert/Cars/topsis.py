import numpy as np
import pandas as pd

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:0.4f}'.format})

def Initialization(data):
    dataFrame = pd.DataFrame(data)
    data_array = dataFrame.drop(['name__brand','carmod','picture'],axis = 1)
    for i in range(len(data_array['cost'])):
        data_array['cost'][i] = data_array['cost'][i]/10000
    return data_array

def Grading(data, search_value):
    Cars = Initialization(data)
    if str(search_value) == "Город":
        Cars['trans__trans'] = Cars['trans__trans'].replace(['Ручная','Автоматическая'],['10','100'])
        Cars['drive__drive'] = Cars['drive__drive'].replace(['Передний','Задний','Полный'],['100','50','10'])
        Cars['fuel__fuel'] = Cars['fuel__fuel'].replace(['Электро','Бензин','Газ','Дизель'],['100','70','40','10'])
        Cars['type__type'] = Cars['type__type'].replace(['Внедорожник','Купе','Седан','Кабриолет'],['1','50','100','20'])
    if str(search_value) == "Пригород":
        Cars['trans__trans'] = Cars['trans__trans'].replace(['Ручная','Автоматическая'],['10','100'])
        Cars['drive__drive'] = Cars['drive__drive'].replace(['Передний','Задний','Полный'],['60','100','10'])
        Cars['fuel__fuel'] = Cars['fuel__fuel'].replace(['Электро','Бензин','Газ','Дизель'],['30','100','70','10'])
        Cars['type__type'] = Cars['type__type'].replace(['Внедорожник','Купе','Седан','Кабриолет'],['20','40','100','1'])
    if str(search_value) == "Бездорожье":
        Cars['trans__trans'] = Cars['trans__trans'].replace(['Ручная','Автоматическая'],['1000','10'])
        Cars['drive__drive'] = Cars['drive__drive'].replace(['Передний','Задний','Полный'],['1','30','10000'])
        Cars['fuel__fuel'] = Cars['fuel__fuel'].replace(['Электро','Бензин','Газ','Дизель'],['1','1000','40','70'])
        Cars['type__type'] = Cars['type__type'].replace(['Внедорожник','Купе','Седан','Кабриолет'],['100000','1','1','1'])
    if str(search_value) == "Шоссе":
        Cars['trans__trans'] = Cars['trans__trans'].replace(['Ручная','Автоматическая'],['10','100'])
        Cars['drive__drive'] = Cars['drive__drive'].replace(['Передний','Задний','Полный'],['10','100','60'])
        Cars['fuel__fuel'] = Cars['fuel__fuel'].replace(['Электро','Бензин','Газ','Дизель'],['1','30','70','100'])
        Cars['type__type'] = Cars['type__type'].replace(['Внедорожник','Купе','Седан','Кабриолет'],['20','10','100','10'])
    return Cars


def Normalization(data,search_value):
    Cars = Grading(data,search_value)
    R = Cars.to_numpy().astype(float)
    w = np.zeros(Cars.shape[1])
    for i in range(len(w)):
        w[i] = np.power(np.sum(np.square(R[:,i])),0.5)
    for j in range(R.shape[1]):
        for i in range(R.shape[0]):
            R[i,j] = R[i,j]/w[j]
    return R

def R_Max_Min(data,search_value):
    arr = Normalization(data,search_value)
    r_max = np.amax(arr,axis = 0)
    r_min = np.amin(arr,axis = 0)
    return arr, r_max, r_min

def Distances(data,search_value):
    arr, r_max, r_min = R_Max_Min(data,search_value)
    S_plus = np.zeros(arr.shape[0])
    S_min = np.zeros(arr.shape[0])
    for i in range(arr.shape[0]):
        S_plus[i] = np.power(np.sum(np.square(arr[i,:] - r_max)),0.5)
        S_min[i] = np.power(np.sum(np.square(arr[i,:] - r_min)),0.5)
    return S_plus, S_min


def Closeness(data,search_value):
    s_plus, s_min = Distances(data,search_value)
    k = np.zeros(s_plus.shape)
    for i in range(len(k)):
        k[i] = s_min[i]/(s_plus[i]+s_min[i])
    return k

def Topsis(data,search_value):
    dataFrame = pd.DataFrame(data)
    sorted_list = np.array(dataFrame)
    k = Closeness(data, search_value)
    sort = np.argsort(k)
    return sorted_list[~sort][0]