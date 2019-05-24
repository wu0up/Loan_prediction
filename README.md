<H2>金融商品交易預測-信貸(Loan)</H2>
https://tbrain.trendmicro.com.tw/Competitions/Details/5

<H4>目標：</H4>
提供顧客在玉山官網上120天的瀏覽行為、客戶基本資料及交易(/申請，預測顧客在之後的30天與玉山有哪些金融商品的往來。
在此只展示信貸商品的預測
由於此資料是使用前120天的行為去預測後30天的行為, 週期不長, 因此打算透過先使用90天及後30天的資料去訓練model,再去進行預測


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
<li>資料正規劃(Normalization)</li>
<li>資料探勘(EDA)</li>
<li>使用模型進行預測</li>
<li>結論</li>
</ol>

<H4>1. 資料清洗：</H4>
   日期顯示調整：因為9xxx不容易判斷, 將其調整為個位數
<H4>1. 特徵產生(Feature Generation):</H4>
  Train_set_y: 

<H4>3. 資料探勘(EDA):</H4>

1. 各產品的次數與週期

2. user behavior的分析-產品類別和popular的url關聯

2. 缺失值

3. 相關


<H4>4. 使用模型進行預測：</H4>
處理缺失值-> 產生特徵 ->使用方法

<H4>5.結論：</H4>

1. 為什麼選擇這個方法？
2. 待加強的部分
