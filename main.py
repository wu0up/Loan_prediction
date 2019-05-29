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
train_set = pd.concat([cif, test], sort = False) #將test和cif整合成一個train_set
train_set = train_set.drop_duplicates(subset='CUST_NO', keep = False)
train_set = train_set.drop(['CC_IND','FX_IND', 'LN_IND', 'WM_IND'], axis =1)
ln_r_train = pd.merge(train_set, ln_data_3, on ='CUST_NO', how = 'left')  #將Train_set和信貸資料整合
cc_ln_r_train = pd.merge(ln_r_train, cc_number_2, on = 'CUST_NO', how = 'left') #將Train_set和信用卡資料整合
fx_cc_ln_r_train = pd.merge(cc_ln_r_train, fx_txn_f_2, on = 'CUST_NO', how= 'left') #將Train_set和外匯資料整合
ln_cc_fx_wm_r_train=pd.merge(fx_cc_ln_r_train, wm_txn_unique_id_2, on = 'CUST_NO', how = 'left') #將Train_set和信託類產品資料整合
ln_cc_fx_wm_page_r_train=pd.merge(ln_cc_fx_wm_r_train, viewing_page_1, on = 'CUST_NO', how = 'left') #將train_set將瀏覽網頁資料整合
#test_set
ln_r=pd.merge(test, ln_data_3, on ='CUST_NO', how = 'left') #只有test only的資料
ln_r=ln_r.drop(['CC_IND', 'FX_IND', 'LN_IND', 'WM_IND'], axis =1)
cc_ln_r = pd.merge(ln_r, cc_number_2, on = 'CUST_NO', how = 'left')
fx_cc_ln_r = pd.merge(cc_ln_r, fx_txn_f_2, on = 'CUST_NO', how= 'left')
ln_cc_fx_wm_r=pd.merge(fx_cc_ln_r, wm_txn_unique_id_2, on = 'CUST_NO', how = 'left')
ln_cc_fx_wm_page_r=pd.merge(ln_cc_fx_wm_r, viewing_page_1, on = 'CUST_NO', how = 'left')
ln_cc_fx_wm_page_cif_r=pd.merge(ln_cc_fx_wm_page_r, cif_d, on = 'CUST_NO', how = 'left')
ln_cc_fx_wm_page_cif_r['CUST_START_DT']=ln_cc_fx_wm_page_cif_r['CUST_START_DT']-9447
ln_cc_fx_wm_page_cif_r.head()

#填補缺失值
values = {'target_60':0, 'target_90': 0,'target_120': 0,'AGE':-999, 'CHILDREN_CNT': -999,'CUST_START_DT':0, 'EDU_CODE': -999, 'INCOME_RANGE_CODE': -999, 'WORK_MTHS': -999,
          'cc_apply_c': 0, 'FX_TXN_AMT': 0, 'fx_apply_c': 0, 'CUST_RISK_CODE':0, 'INVEST_TYPE_CODE':0, 'WM_TXN_AMT':0, 
          'WM_txn_c':0, 'PAGE':0, 'Target':0,'LN_AMT':0}
#test_set
result_cif = ln_cc_fx_wm_page_cif_r.fillna(value=values)
result_cif_1 = result_cif.drop(['GENDER_CODE', 'ln_apply_date','VISITDATE'], axis = 1)
#train_set
result_cif_train = ln_cc_fx_wm_page_r_train.fillna(value = values)
result_cif_train_1 = result_cif_train.drop(['GENDER_CODE', 'ln_apply_date','VISITDATE'], axis = 1)

#設定X和y
#用未來當y, 現在當x
test_set = result_cif_1.drop(['CUST_NO','target_60', 'target_90','target_120'], axis =1)
train_set = result_cif_train_1.drop(['CUST_NO','target_60', 'target_90','target_120'], axis =1)
train_y = result_cif_train_1.target_120

df = test_set.iloc[:,:9]
df.head()
df.shape
test_set_1 = test_set.drop(test_set.iloc[:,:9], axis=1)
test_set_1.head()
test_set_1.shape
test_set_2 = pd.concat([test_set_1, df], axis =1)
test_set_2.shape

#使用model
model = XGBClassifier()
X_train, X_test, y_train, y_test = train_test_split(train_set, train_y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)

#進行Validation
y_val = model.predict(X_test)
accuracy_score(y_test, y_val)

#進行Prediction
model.fit(train_set, train_y)
y_pred = model.predict(test_set_2)
df_predict = pd.DataFrame(y_pred, columns=['LN_IND'])
