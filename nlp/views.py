from typing import Iterator
from django.shortcuts import render
# from django.http import HttpResponse
import pandas as pd
import pickle

from pandas.core.reshape import tile

categorydata = pd.read_csv("idx2category.csv")
index2category = {row.k: row.v for idx, row in categorydata.iterrows()}

with open("rdmf.pickle", mode="rb") as f:
  model = pickle.load(f)


def index(request):
  if request.method == "GET":
    return render(
      request,
      "nlp/home.html"
    )
  else:
    title = [request.POST["title"]]
    print("title:", title)
    result = model.predict(title)[0]
    print("result:", result)
    pred = index2category[result]
    print("pred:", pred)
    return render(
        request,
        "nlp/home.html",
        {"title":pred}
      )
