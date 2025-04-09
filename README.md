# bulk-chain-shell 0.25.0

This project is a bash-shell client for bulk-chain no-string framework for reasoning over your data using predefined CoT prompt schema.

<p align="center">
    <img src="https://github.com/user-attachments/assets/0cc8fdcb-6ddb-44a3-8f05-d76250ae6423" width="380" height="auto"/>
</p>

> 📺 This video showcase application of the [↗️ Sentiment Analysis Schema](https://github.com/nicolay-r/bulk-chain/blob/master/test/schema/thor_cot_schema.json) towards [LLaMA-3-70B-Instruct](https://replicate.com/meta/meta-llama-3-70b-instruct) hosted by Replicate for reasoning over submitted texts

### Extra Features
* ✅ **Progress caching [for remote LLMs]**: withstanding exception during LLM calls by using `sqlite3` engine for caching LLM answers;

# Installation

```bash
pip install git+https://github.com/nicolay-r/bulk-chain-shell@master
```

# Usage

To interact with LLM via command line with LLM output streaming support.
The video below illustrates an example of application for sentiment analysis on author opinion extraction towards mentioned object in text.

## Interactive Mode

Quick start :
1. ⬇️ Download [replicate](https://replicate.com/) provider for `bulk-chain`:
2. 📜 Setup your reasoning `thor_cot_schema.json` according to the [following example ↗️](test/schema/thor_cot_schema.json)
3. 🚀 Launch `demo.py` as follows:
```bash
python3 -m bulk_chain_shell.demo \
    --schema "test/schema/thor_cot_schema.json" \
    --adapter "dynamic:replicate_104.py:Replicate" \
    %%m \
    --model_name "meta/meta-llama-3-70b-instruct" \
    --api_token "<REPLICATE-API-TOKEN>" \
    --stream
```

## Inference Mode

> **NOTE:** You have to install `source-iter` and `tqdm` packages that actual [dependencies](dependencies.txt) of this project

1. ⬇️ Download [replicate](https://replicate.com/) provider for `bulk-chain`:
```bash
wget https://raw.githubusercontent.com/nicolay-r/nlp-thirdgate/refs/heads/master/llm/replicate_104.py
```
2. 📜 Setup your reasoning `schema.json` according to the [following example ↗️](test/schema/default.json)
3. 🚀 Launch inference using `DeepSeek-R1`:
```bash
python3 -m bulk_chain_shell.infer \
    --src "<PATH-TO-YOUR-CSV-or-JSONL>" \
    --schema "test/schema/default.json" \
    --adapter "replicate_104.py:Replicate" \
    %%m \
    --model_name "deepseek-ai/deepseek-r1" \
    --api_token "<REPLICATE-API-TOKEN>"
```

# Embed your LLM

All you have to do is to implement `BaseLM` class, that includes:
* `__init__` -- for setting up *batching mode support* and (optional) *model name*;
* `ask(prompt)` -- infer your model with the given `prompt`.

See examples with models [at nlp-thirdgate 🌌](https://github.com/nicolay-r/nlp-thirdgate?tab=readme-ov-file#llm).

# References

> TODO.