import deeplake
import pandas as pd

df = pd.read_csv("file.csv")
deeplake_path = "hub://ahape/example"

ds = deeplake.ingest_dataframe(df, deeplake_path, token = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTY4MjM5Njg2MCwiZXhwIjoxNjg4MTg1NjE5fQ.eyJpZCI6ImFoYXBlIn0.2jk8Y6e8GqTQ2wbJ0H6--JIuQQfxmLX_E9Iagj3ik7lzeDwNSP_QuOgLWN161ZH-dau_t4ufukDRDwRVFVAHAA")
