<H2>信貸(Loan)交易預測</H2>
https://tbrain.trendmicro.com.tw/Competitions/Details/5

<H4>目標：</H4>
透過玉山提供官網上120天的瀏覽行為、客戶基本資料及交易(信貸申請, 信用卡申請, 外匯交易, 信託類產品交易)，預測顧客在之後的30天與玉山的信貸往來狀況。


<H4>本次使用的資料集：</H4>
<table border=1 cellpadding=10>
  <tr>
    <th>資料名稱</th> <th>資料內容</th> <th>資料筆數</th>
  </tr>
  <tr>
    <th>TBN_CUST_BEHAVIOR.csv</th> <td>顧客網頁瀏覽行為</td> <td>2,209,864筆</td>
  </tr>
  <tr>
    <th>TBN_CIF.csv</th> <td>顧客基本資料</td> <td>187,679筆</td>
  </tr>
  <tr>
    <th>TBN_CC_APPLY.csv</th> <td>顧客信用卡核卡資料</td> <td>54,393筆</td>
  </tr>
  <tr>
    <th>TBN_FX_TXN.csv</th> <td>顧客外匯交易資料</td> <td>507,185筆</td>
  </tr>
  <tr>
    <th>TBN_LN_APPLY.csv</th> <td>顧客信貸申請資料</td> <td>6,741筆</td>
  </tr>
  <tr>
    <th>TBN_WM_TXN.csv</th> <td>顧客信託類產品交易資料</td> <td>195,000筆</td>
  </tr>
 </table>

<H4>技巧：</H4>
<ol>
<li>特徵產生(Feature Generation)</li>
<li>資料探勘(EDA)</li>
<li>資料前處理</li>
<li>使用模型進行預測</li>
<li>結論</li>
</ol>

<H4>1. 特徵產生(Feature Generation):</H4>
本次的資料集除了信貸資料外，共有5個表格，分別描述其他產品及使用者行為；為了探討其他特徵和信貸的關係，以使用者(Cust_NO)作為Primary Key，針對有發生信用卡/外匯/信託類產品/使用者行為的動作設為1，並合併成1個Train_Set.

<H4>2. 資料探勘(EDA):</H4>

<H5>a. 信貸申請次數 VS.天數</H5>
透過趨勢圖, 可看出前兩個月的貸款申請人數在月初和月底較高，但第三個月的狀況不明顯。

![image](https://github.com/wu0up/github_test/blob/master/Picture/Loan.png)

<H5>b. 信貸申請和可能的url關聯</H5>
為了探討使用者行為和信貸申請的關係，觀察編碼後的URL，篩選出包含和信貸相關關鍵字-qodr的URL，再繪製每一天的URL拜訪數量，並和信貸申請人數比較；
雖然有些趨勢類似，但兩者的相關係數為-0.3，並非正相關。

![image](https://github.com/wu0up/github_test/blob/master/Picture/URL%20vs%20Loan.png)

<H5>c. 缺失值</H5>
合併整理後的Train_Set，資料筆數為157971筆；然而，下方圖表為缺失值的數目，可以發現信貸的數據缺失值很多，這是這次信貸預測最難進行的一個原因。

![image](https://github.com/wu0up/github_test/blob/master/Picture/Missing_value.png)


<H5>d. 各特徵之間的相關性</H5>

![image](https://github.com/wu0up/github_test/blob/master/Picture/feature.png)


<H4>3. 資料前處理：</H4>
a. 使用

<H4>4. 使用模型進行預測：</H4>
參考其它文獻及Kaggle競賽，因此使用XGBoost作為訓練模型；並利用Train_set的前90天資料作為X， 後30天資料作為y; 其中30%的資料集做為Validation set。

<H4>5.結論：</H4>
本次預測在信貸部分得到Validation set的Accuracy為
