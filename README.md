<H2>金融商品交易預測-信貸(Loan)</H2>
https://tbrain.trendmicro.com.tw/Competitions/Details/5

<H4>目標：</H4>
提供顧客在玉山官網上120天的瀏覽行為、客戶基本資料及交易(信貸申請, 信用卡申請, 外匯交易, 信託類產品交易)，預測顧客在之後的30天與玉山的信貸往來狀況。


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
<li>使用模型進行預測</li>
<li>結論</li>
</ol>

<H4>1. 特徵產生(Feature Generation):</H4>
  信用卡/外匯/信託類產品: 有進行交易的設為1;
  

<H4>2. 資料探勘(EDA):</H4>

<H6>a. 信貸申請次數 VS.天數</H6>
透過趨勢圖, 可看出在月初和月底貸款申請人數較高;

![image](https://github.com/wu0up/github_test/blob/master/Picture/Loan.png)

<H6>b. 信貸申請和可能的url關聯</H6>

![image](https://github.com/wu0up/github_test/blob/master/Picture/URL%20vs%20Loan.png)

<H6>c. 缺失值</H6>

![image]()


<H6>d. 個特徵之間的相關性</H6>

![image]()



<H4>4. 使用模型進行預測：</H4>
處理缺失值-> 產生特徵 ->使用方法

<H4>5.結論：</H4>
