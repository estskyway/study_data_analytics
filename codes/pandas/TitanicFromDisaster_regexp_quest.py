import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font',family='Malgun Gothic')
import seaborn as sns
import pandas as pd
import scipy.stats as stats

# quest
# - Name 변수에서 성씨와 결혼 유무 컬럼 생성
# - hint : 성씨 컬럼에 Nan 없어야 함.

df_TFD = pd.read_csv('datasets/TitanicFromDIsaster_train.csv')
# print(df_TFD)

# Name 변수에서 성씨 가져오기
df_TFD_NS = df_TFD[['Name', 'SibSp']]
pattern = r'^([A-z]*)'
df_Name_extract = df_TFD_NS['Name'].str.extract(pattern)
# print(df_Name_extract)

# 결혼 유무 표시 뽑기
pattern1 = r'(Mr\w|Mr|Miss|Ms)'
df_Name_extract1 = df_TFD_NS['Name'].str.extract(pattern1)
# print(df_Name_extract1) 

df_Name_extract1_drop = df_Name_extract1.dropna().copy()
df_isnull = df_Name_extract1_drop.isnull().sum()
# print(df_isnull)
# 0    0
# dtype: int64

# 컬럼만들어서 때려넣기
# print(df_TFD['SibSp'])
df_TFD_NS['LastName'] = df_Name_extract
df_TFD_NS['Married'] = df_Name_extract1_drop
print(df_TFD_NS[['LastName','Married']])


#       LastName Married
# 0       Braund      Mr
# 1      Cumings     Mrs
# 2    Heikkinen    Miss
# 3     Futrelle     Mrs
# 4        Allen      Mr
# ..         ...     ...
# 886   Montvila     NaN
# 887     Graham    Miss
# 888   Johnston    Miss
# 889       Behr      Mr
# 890     Dooley      Mr
# [891 rows x 2 columns]