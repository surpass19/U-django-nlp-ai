# U-django-nlp-ai

* rakuma_NPL.ipynb:
【4時間でPython AIアプリ開発】Python Django scikit learnでAIアプリを開発 <br>
https://www.youtube.com/watch?v=_87RY9rb79I <br>
を見て写経

* rakuma_NPL_add_w2v_LGBM.ipynb:
【たった90分でAI開発】Python word2vec + LightGBMで多値分類に挑戦！ <br>
https://www.youtube.com/watch?v=wGCzd2k-0GU <br>
によってモデル改善


# 学んだこと
* 自然言語の扱い方
* 他クラス分類の流れ
* Djangoによるアプリ作成(AIのモデルを使った)
* GCEを使ったデプロイ ⇨ Herokuの方が楽

## 具体
* BOW
* tfidf
* Pipeline
前処理 ~ 学習の処理をまとめられる

* classification_report
混合行列を自動で返してくれる、使いやすい

```
from sklearn.metrics import classification_report
#配列を渡す
print(classification_report(y_test, prediction))

precision    recall  f1-score   support

           0       0.86      0.69      0.77       372
           1       0.96      0.96      0.96      1124
           2       0.87      0.86      0.86       382
           3       0.96      0.96      0.96       689
           4       0.80      0.90      0.84      3278
           5       0.70      0.38      0.50       395
           6       0.83      0.92      0.87      2000
           7       0.87      0.89      0.88       900
           8       0.99      0.98      0.98       393
           9       0.99      0.89      0.94       313
          10       0.99      0.96      0.97       685
          11       0.80      0.54      0.65       443
          12       0.89      0.80      0.84       456
          13       0.93      0.90      0.92       389
          14       0.98      0.97      0.97       487
          15       0.99      0.93      0.96       660
          16       0.99      0.95      0.97       372
          17       0.99      1.00      0.99      3435
          18       1.00      0.99      1.00       928
          19       0.96      0.93      0.94       677
          20       0.98      0.89      0.93       294
          21       0.90      0.83      0.86       332

    accuracy                           0.91     19004
   macro avg       0.92      0.87      0.89     19004
weighted avg       0.91      0.91      0.91     19004
```

* ↓
BOW・tfidfでは次元が多くなってしまうため, Word2vecを使った方が良い

「system_profiler SPHardwareDataType」
コマンドにこれを打つと, コア数がわかる
出力:
Hardware:

    Hardware Overview:

      Model Name: MacBook Air
      Model Identifier: MacBookAir10,1
      Chip: Apple M1
      Total Number of Cores: 8 (4 performance and 4 efficiency)
      Memory: 16 GB
      
 osをimportして, os.cpu_count()を使うと, パソコンで扱える最大のコア数で分散処理可能

# 次学びたいこと
* BERTの書籍 <br>
https://www.amazon.co.jp/BERTによる自然言語処理入門-Transformersを使った実践プログラミング-ストックマーク株式会社/dp/427422726X
