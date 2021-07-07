###LINEBOT機器人快速開發工具，ImageMap轉換多尺寸圖片

LINE的聊天機器人提供了許多模板給開發者使用，有一種很熱門應用叫做imagemap，他可以上傳最高1040x1040的圖片，並讓你設定最多20個觸控點，可以隨機放在圖上任意地點。在使用圖片的時候，為了要讓各個裝置有最佳體驗，他會根據尺寸在圖片後面加上/700 /240。

舉例來說，我今天有一張台灣的圖片(taiwan.jpg)，我將他上傳到雲端後，應該會是https://雲端/taiwan.jpg。

假設今天有個使用者使用700px寬度的裝置，呼叫這張圖出來，LINE去抓這張圖的時候會在後面加上/700，變成https://雲端/taiwan.jpg/700，這樣也就造成圖片路徑不對，而變成404not found。解決方法是開一個雲端資料夾，檔名叫做taiwan，然後將官方提供的五種尺寸分別輸出，並將副檔名刪掉，此時圖片名稱就是700，再上傳到雲端（我上傳的是AWS的S3），如果你跟我一樣上傳到S3，要記得修改TAG，改成content/jpg。然後後台設定的時候，只要設定https://雲端/taiwan就好，剩下的讓LINE抓取圖片的時候自動生成。

這一段有一個很麻煩的點，就是「官方提供的五種尺寸分別輸出」。於是寫了這支程式幫助圖片快速產出，我使用的是PILLOW及OS。使用方法如下：

1.開啟Terminal，建立環境

$ Conda create convert_img

$ Source activate convert_img

$ pip install pillow

2.設定檔案參數

開啟檔案，在multi_resize後面加上自己要的參數，中間用,分隔

#resize.py

multi_resize()

3.將要壓縮的圖片放在resize.py的檔案夾裡面，並在啟動resize.py

$ python resize.py

