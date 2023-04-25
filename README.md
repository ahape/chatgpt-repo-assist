Script for having ChatGPT analyze and answer questions about your codebase

How to use
---

First make sure you have python and pip installed.

Then follow the steps in this [how to article](https://www.activeloop.ai/resources/lang-chain-gpt-4-for-code-understanding-twitter-algorithm/) around creating a activeloop account and whatnot.

Then clone and install all the dependencies for this repo
```sh
git clone https://github.com/ahape/chatgpt-repo-assist.git
cd chatgpt-repo-assist
pip install -r requirements.txt
```

Then create your `secrets.config` file. It should look like this:
```gitconfig
[openai]
  apikey = <api-key>

[activeloop]
  token = <token>
  user = <username>
  dataset = <name-for-your-dataset>
```

Then, finally, initialize a dataset with a code repository you want scanned, run the following command:
```sh
python main.py --init --repo /path/to/your/codebase
```
