# U-django-nlp-ai

https://www.youtube.com/watch?v=_87RY9rb79I <br>
を見て写経


# 学んだこと
自然言語の扱い方


BOW
tfidf
Pipelineを使うと, 前処理 ~ 学習の処理をまとめられる

classification_report
混合行列を自動で返してくれる、使いやすい
↓
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
      System Firmware Version: 6723.120.36
      OS Loader Version: 6723.120.36
      Serial Number (system): FVFFX2QHQ6LT
      Hardware UUID: B167657C-B55D-5892-8E83-778F564A7C16
      Provisioning UDID: 00008103-000859980EF3001E
      Activation Lock Status: Disabled
      
 osをimportして, os.cpu_count()を使うと, パソコンで扱える最大のコア数で分散処理可能

