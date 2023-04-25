#!/usr/local/bin/python3.11

import os, sys, configparser, argparse

config = configparser.ConfigParser()
config.read("secrets.config")

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--init", action="store_true")
arg_parser.add_argument("-r", "--repo")
args = arg_parser.parse_args()

os.environ["OPENAI_API_KEY"] = config["openai"]["apikey"]
os.environ["ACTIVELOOP_TOKEN"] = config["activeloop"]["token"]

def init():
  embeddings = OpenAIEmbeddings()
  docs = []

  for dirpath, dirnames, filenames in os.walk(args.repo):
    for file in filenames:
      try: 
        loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
        docs.extend(loader.load_and_split())
      except Exception as e:
        print(e, file)

  print(f"{len(docs)} docs collected")
  print("Next: Splitting text into chunks")

  text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
  texts = text_splitter.split_documents(docs)

  username = config["activeloop"]["user"]
  dataset = config["activeloop"]["dataset"]
  dataset_path = f"hub://{username}/{dataset}"

  print("Next: Performing the indexing process")

  db = DeepLake(
    dataset_path=dataset_path,
    embedding_function=embeddings)
  #  public=True)
  db.add_documents(texts)

def main():
  db = Dataset(path=dataset_path, read_only=True, tensors=["embedding", "ids", "metadata", "text"])
  print(db)

if __name__ == "__main__":
  if args.init:
    init()
  else:
    main()
