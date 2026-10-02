# Nano GPT – Shakespeare

A character-level GPT language model implemented using PyTorch, inspired by Andrej Karpathy's GPT tutorial.

## Overview

This project implements a decoder-only Transformer trained on the Tiny Shakespeare dataset to generate Shakespeare-style text.

## Architecture

* Character-level tokenization
* Token and positional embeddings
* Masked self-attention
* Multi-head self-attention
* Feed-forward neural networks
* Layer normalization
* Residual connections
* AdamW optimizer

## Configuration

| Hyperparameter      |  Value |
| ------------------- | -----: |
| Batch size          |     64 |
| Context length      |    256 |
| Embedding dimension |    384 |
| Attention heads     |      6 |
| Transformer layers  |      6 |
| Dropout             |    0.2 |
| Training iterations |  5,000 |
| Learning rate       | 0.0003 |

## Installation

```bash
git clone YOUR_REPOSITORY_URL
cd nano-gpt-shakespeare

pip install -r requirements.txt
```

## Dataset

The model uses the Tiny Shakespeare dataset.

Place the dataset at:

`data/input.txt`

## Training

```bash
python train.py
```

The trained model is saved as `shakespeare_gpt.pth` after training.

## Text Generation

The script generates Shakespeare-style text after training.

## Technologies

* Python
* PyTorch
* Transformer Architecture
* Deep Learning

## Acknowledgements

Inspired by Andrej Karpathy's educational GPT implementation and tutorial.

https://github.com/karpathy/nanoGPT
