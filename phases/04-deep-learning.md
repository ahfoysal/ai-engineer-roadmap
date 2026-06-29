# Phase 4 — Deep Learning

**Goal:** Understand and build neural networks with PyTorch. Implement backprop once, then use the framework.
**Time:** 5–6 weeks.

---

## 🎯 Outcomes
You can build, train, and debug neural networks; understand what every layer does; and know how to fix a model that won't learn.

## ✅ Checklist

### Neural network fundamentals
- [ ] The perceptron & multilayer perceptron (MLP)
- [ ] Activation functions (ReLU, sigmoid, tanh, GELU, softmax)
- [ ] Forward pass & loss functions (cross-entropy, MSE)
- [ ] **Backpropagation & autograd** (implement once by hand)
- [ ] Optimizers: SGD, Momentum, **Adam / AdamW**
- [ ] Learning rate, batch size, epochs

### Training in practice
- [ ] Train/val/test, the training loop
- [ ] Overfitting fixes: dropout, weight decay, early stopping
- [ ] Batch normalization & layer normalization
- [ ] Data augmentation
- [ ] Vanishing/exploding gradients
- [ ] GPU training, mixed precision
- [ ] Reading loss curves & debugging ("why won't it learn?")

### Architectures
- [ ] CNNs (convolution, pooling) — for images
- [ ] Transfer learning & fine-tuning pretrained models
- [ ] RNNs / LSTMs / GRUs — for sequences (then mostly replaced by transformers)
- [ ] Embeddings (dense vector representations)
- [ ] Autoencoders (intuition)

### Framework: PyTorch
- [ ] Tensors & autograd
- [ ] `nn.Module`, `Dataset`, `DataLoader`
- [ ] Writing a custom training loop
- [ ] Saving/loading models, checkpoints
- [ ] (Optional) PyTorch Lightning to reduce boilerplate

## 📚 Best resources
- **Best intro** — [fast.ai: Practical Deep Learning for Coders (free)](https://course.fast.ai/) — *top-down, build first*
- **From scratch** — [Andrej Karpathy: Neural Networks Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) **(build micrograd & GPT by hand — essential)**
- **PyTorch** — [Official 60-min Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) · [Daniel Bourke: Learn PyTorch (free, 25h)](https://www.learnpytorch.io/)
- **Theory** — [DeepLearning.AI Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) · *Dive into Deep Learning* (free book, [d2l.ai](https://d2l.ai/))

## 🛠️ Phase project
**Two projects:**
1. Build & train an image classifier (CNN) on a real dataset — then beat your score with transfer learning (ResNet).
2. Implement [Karpathy's micrograd](https://github.com/karpathy/micrograd) — a tiny autograd engine — yourself. This *cements* backprop forever.

➡️ Next: [Phase 5 — NLP & Transformers](05-nlp-transformers.md)
