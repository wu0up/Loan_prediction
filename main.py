#載入套件
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
% pylab inline

# 載入資料
# 一併處理特徵工程，將dataset: **test** 附加於 **train** 後方，成為另一個dataset: **x_train**。

customer_behavior= pd.read_csv('TBN_CUST_BEHAVIOR.csv')
cc_apply = pd.read_csv('TBN_CC_APPLY.csv')
cif= pd.read_csv('TBN_CIF.csv')
fx_txn = pd.read_csv('TBN_FX_TXN.csv')
ln_apply = pd.read_csv('TBN_LN_APPLY.csv')
recent_dt = pd.read_csv('TBN_RECENT_DT.csv')
wm_txn = pd.read_csv('TBN_WM_TXN.csv')
test = pd.read_csv('TBN_Y_ZERO.csv')

#1. 特徵值產生-信貸
ln_apply_c =ln_apply.copy()

#1-1. 日期調整
ln_apply_c['ln_apply_date']=ln_apply_c['TXN_DT']-9447
ln_apply_c = ln_apply_c.drop(['TXN_DT'], axis=1)

sp1 = ln_apply_c['ln_apply_date']                               #將ln_apply_date欄位移到第一個
ln_apply_c.drop(labels=['ln_apply_date'], axis=1, inplace=True)
ln_apply_c.insert(1, 'ln_apply_date', sp1)

ln_apply_c = ln_apply_c.sort_values(by=['ln_apply_date'])

#1-2. 生成特徵值
ln_apply_c['target_60']=0
ln_apply_c['target_60'][(ln_apply_c['ln_apply_date'] > 30) & (ln_apply_c['ln_apply_date'] <= 60)] = 1
ln_apply_c['target_90']=0
ln_apply_c['target_90'][(ln_apply_c['ln_apply_date'] > 60) & (ln_apply_c['ln_apply_date'] <= 90)] = 1
ln_apply_c['target_120']=0
ln_apply_c['target_120'][(ln_apply_c['ln_apply_date'] > 90) & (ln_apply_c['ln_apply_date'] <= 120)] = 1

ln_data_3 = ln_apply_c.groupby('CUST_NO').agg('sum') #將同Cust_no的天數合併
ln_data_3.reset_index()

#特徵生成-信用卡申請
cc_number = cc_apply.copy()
cc_number = cc_number.drop(['TXN_DT'], axis=1) 將其他不要的欄位刪除

cc_number.info()
cc_number['cc_apply_c']=1
cc_number_2 = cc_number.groupby('CUST_NO').agg('sum') #已經將各天相加
cc_number_2.reset_index()

#特徵生成-外匯
fx_txn_f=fx_txn.copy()
fx_txn_f = fx_txn_f.drop(['TXN_DT'], axis=1)
fx_txn_f.head()
fx_txn_f['fx_apply_c']=1

fx_txn_f_2 = fx_txn_f.groupby('CUST_NO').agg('sum') 
fx_txn_f_2.reset_index()

#特徵生成-信託類產品交易
wm_txn_unique_id=wm_txn.copy()
wm_txn_unique_id = wm_txn_unique_id.drop(['TXN_DT'], axis=1)
wm_txn_unique_id.info()
wm_txn_unique_id['WM_txn_c']=1

wm_txn_unique_id_2 = wm_txn_unique_id.groupby('CUST_NO').agg('sum') 
wm_txn_unique_id_2.reset_index()

#特徵生成-瀏覽網頁資料
viewing_page = customer_behavior.copy()
viewing_page['PAGE']=viewing_page.groupby(['CUST_NO']).transform('count')
viewing_page = viewing_page.drop_duplicates(subset = 'CUST_NO', keep ='first')

#將資料合併成Train_set 和test_set
#train_set
train_set = pd.concat([cif, test], sort = False)
train_set = train_set.drop_duplicates(subset='CUST_NO', keep = False)
train_set = train_set.drop(['CC_IND','FX_IND', 'LN_IND', 'WM_IND'], axis =1)
ln_r_train = pd.merge(train_set, ln_data_3, on ='CUST_NO', how = 'left')  #將Train_set和信貸資料整合
cc_ln_r = pd.merge(ln_r, cc_number_2, on = 'CUST_NO', how = 'left') #將Train_set和信用卡資料整合


