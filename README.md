# U-django-nlp-ai

* rakuma_NPL.ipynb:
https://www.youtube.com/watch?v=_87RY9rb79I <br>
を見て写経

* rakuma_NPL_add_w2v_LGBM.ipynb:
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
* BERTの書籍
