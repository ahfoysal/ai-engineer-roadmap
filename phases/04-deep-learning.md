# Phase 4 — Deep Learning

**Goal:** Understand and build neural networks with PyTorch. Implement backprop once, then use the framework.
**Time:** 5–6 weeks.

---

## 🎯 Outcomes
You can build, train, and debug neural networks; understand what every layer does; and know how to fix a model that won't learn.

## ✅ Checklist

### Neural network fundamentals
- [ ] The perceptron & multilayer perceptron (MLP)
- [ ] Activation functions (ReLU, sigmoid, tanh, GELU, softmax) — and *why* non-linearity matters
- [ ] Forward pass & loss functions (cross-entropy, MSE)
- [ ] **Backpropagation & autograd** (implement once by hand)
- [ ] Optimizers: SGD, Momentum, **Adam / AdamW**
- [ ] Learning rate, batch size, epochs

### Training in practice
- [ ] Train/val/test split & the training loop
- [ ] Overfitting fixes: dropout, weight decay, early stopping
- [ ] Batch normalization & layer normalization
- [ ] Data augmentation
- [ ] Vanishing/exploding gradients
- [ ] GPU training & mixed precision (AMP)
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
- [ ] `model.train()` vs `model.eval()` and `torch.no_grad()`
- [ ] Saving/loading models, checkpoints
- [ ] (Optional) PyTorch Lightning to reduce boilerplate

---

## 🧠 Neural network fundamentals

**From perceptron to MLP.** A *perceptron* is just `output = activation(w · x + b)` — a weighted sum plus a bias, squashed by a non-linearity. Stack neurons side-by-side into a *layer*, stack layers front-to-back, and you have a **multilayer perceptron (MLP)**: input layer → hidden layers → output layer. Each layer is a matrix multiply (`Wx + b`) followed by an activation. That's the whole idea — the depth and the non-linearities are where the power comes from.

**Why non-linearity matters.** Without activation functions, stacking layers is pointless: `W₂(W₁x) = (W₂W₁)x` collapses into a single linear map no matter how many layers you add. The activation between layers is what lets the network bend and fold the input space to model curves, edges, and decision boundaries a straight line could never capture.

**Activation functions** — pick by role:
- **ReLU** `max(0, x)` — the default for hidden layers. Cheap, doesn't saturate for positive inputs, trains fast. Can "die" (stuck-at-zero neurons); variants like LeakyReLU help.
- **GELU** — smooth ReLU-ish curve; the modern default inside transformers.
- **sigmoid** `1/(1+e⁻ˣ)` — squashes to (0,1). Use for a **single** binary-probability output. Saturates and kills gradients if used in deep hidden layers.
- **tanh** — like sigmoid but (-1,1) and zero-centered; mostly historical / inside RNNs.
- **softmax** — turns a vector of logits into a probability distribution that sums to 1. Use it for the **final layer of multi-class classification** (or let the loss apply it for you — see below).

**Forward pass.** Push a batch of inputs through the layers, applying weights then activations, until you produce predictions. Compare predictions to targets with a **loss function**:
- **Cross-entropy** — classification. Measures how surprised the model is by the correct label.
- **MSE (mean squared error)** — regression. Average squared distance between prediction and target.

The loss is a single number summarizing how wrong the model is. Training = nudging the weights to make that number go down.

## 🔁 Backprop & autograd

**Backpropagation** is just the **chain rule** applied across the whole network. The forward pass builds a graph of operations; backprop walks that graph *backward*, multiplying local derivatives to compute how much each weight contributed to the loss — i.e. the **gradient** `∂loss/∂w` for every weight. The optimizer then steps each weight in the direction that reduces the loss.

**Autograd** (PyTorch's engine) records every tensor operation into a graph and computes all those gradients for you when you call `.backward()`. You almost never write backprop by hand in real work — *but you should implement it once* so it stops being magic.

> **Do this once:** build [Karpathy's micrograd](https://github.com/karpathy/micrograd) yourself. A scalar `Value` class that tracks `data`, `grad`, and a `_backward` closure, topologically sorted — ~150 lines that make autograd click permanently.

## ⚙️ Optimizers & the training loop

The optimizer decides *how* to use the gradients:
- **SGD** — step `w ← w − lr · grad`. Simple, noisy, needs tuning.
- **SGD + Momentum** — accumulates a velocity so it powers through flat regions and dampens oscillation. Faster, more stable.
- **Adam / AdamW** — adapts the step size per-parameter using running averages of the gradient and its square. **The default for most work.** Use **AdamW** (decoupled weight decay) when you want regularization — it's the standard for transformers.

**Learning rate** is the single most important knob. Too high → loss explodes or oscillates (NaNs). Too low → trains painfully slowly or stalls in a bad spot. Start around `1e-3` for Adam, `1e-1`–`1e-2` for SGD, then tune. A **learning-rate schedule** (warmup + cosine/step decay) usually beats a fixed rate.

**The training loop** (the heartbeat of all deep learning):
1. Get a batch from the `DataLoader`.
2. **`optimizer.zero_grad()`** — clear last step's gradients.
3. Forward pass → predictions.
4. Compute the loss.
5. **`loss.backward()`** — autograd fills in every `.grad`.
6. **`optimizer.step()`** — update the weights.
7. Repeat for all batches (one **epoch**), for many epochs.

## 🩺 Training in practice

**Overfitting** = great on training data, bad on validation data (the gap widens as you train). Fixes:
- **Dropout** — randomly zero out activations during training so the net can't rely on any single neuron.
- **Weight decay (L2)** — penalize large weights to keep the model simple.
- **Early stopping** — stop when validation loss stops improving; keep the best checkpoint.
- **More / augmented data** — the most reliable fix of all.

**Normalization layers** stabilize and speed up training:
- **BatchNorm** — normalize activations across the batch; great for CNNs. Behaves differently in train vs eval mode (uses running stats at eval).
- **LayerNorm** — normalize across features within each sample; the standard inside transformers and for variable-length sequences.

**Data augmentation** — generate new training examples on the fly (random crops, flips, rotations, color jitter for images). Free regularization and the cheapest accuracy boost you'll find.

**Vanishing / exploding gradients** — in deep nets, repeated multiplication of small (<1) or large (>1) derivatives makes gradients shrink to zero or blow up. Mitigations: ReLU/GELU activations, residual connections, normalization layers, careful weight init (He/Xavier), and **gradient clipping** for exploding gradients (common in RNNs).

**GPU & mixed precision.** Move model and batches to the GPU (`.to(device)`) — the same loop runs 10–100× faster. **Mixed precision (AMP)** runs most ops in fp16/bf16 for speed and memory savings while keeping a fp32 master copy for stability (`torch.cuda.amp.autocast` + `GradScaler`). Essential once models get large.

**Reading loss curves.** Plot train *and* validation loss every epoch:
- Both falling, val tracking train → healthy. Keep going.
- Train falls, val rises → **overfitting**. Regularize / get more data / stop earlier.
- Both flat and high → **underfitting** or a bug. More capacity, higher lr, or train longer.
- Loss spikes to NaN → lr too high, bad data, or numerical blowup.

### "Why won't it learn?" — debugging checklist
- [ ] **Overfit a single batch first.** If the model can't reach ~0 loss on 1 batch, you have a bug — not a tuning problem.
- [ ] Did you call `optimizer.zero_grad()` each step? (forgetting it accumulates gradients)
- [ ] Loss & final activation paired correctly? (see pitfalls below)
- [ ] Inputs normalized? Labels in the right shape/dtype?
- [ ] Is the lr sane? Try sweeping ×10 and ÷10.
- [ ] `model.train()` during training, `model.eval()` during validation?
- [ ] Is data actually on the same device as the model?
- [ ] Are gradients flowing? Check a few `.grad` norms aren't zero or NaN.

## 🏗️ Architectures

**CNNs (Convolutional Neural Networks)** — for images and grid-like data. A **convolution** slides small learnable filters over the image to detect local patterns (edges → textures → shapes → objects as you go deeper), sharing weights across positions so it's parameter-efficient and translation-invariant. **Pooling** (max/avg) downsamples to shrink spatial size and add robustness. Classic stack: conv → activation → pool, repeated, then a small MLP head.

**Transfer learning & fine-tuning** — don't train from scratch. Take a model pretrained on a huge dataset (e.g. ResNet on ImageNet), replace its final classification head with yours, and either **freeze** the backbone and train only the head, or **fine-tune** the whole thing at a low lr. This is how you get strong results with little data — and it will usually beat your from-scratch CNN.

**RNNs / LSTMs / GRUs** — for sequences (text, time series). They process one step at a time, carrying a hidden state. **LSTM/GRU** add gates to remember long-range info and fight vanishing gradients. They're now mostly historical: **transformers replaced them** because RNNs are sequential (slow, hard to parallelize) and still struggle with very long dependencies — attention sees the whole sequence at once. Learn the intuition; you'll spend your real time on transformers in Phase 5.

**Embeddings** — dense, learned vector representations of discrete things (words, users, items). Similar things land near each other in vector space. The foundational idea behind NLP and recommender systems.

**Autoencoders** — train a network to compress input to a small **latent** vector (encoder) and reconstruct it back (decoder). Forces it to learn the essential structure. Intuition-builder for representation learning, denoising, and the latent-space thinking behind modern generative models.

## 🔥 PyTorch essentials

- **Tensors** — NumPy-like arrays that live on CPU or GPU and track gradients. `requires_grad=True` opts a tensor into autograd.
- **Autograd** — `.backward()` computes gradients through the recorded graph; `.grad` holds them.
- **`nn.Module`** — base class for models. Define layers in `__init__`, the forward pass in `forward()`. Parameters register automatically.
- **`Dataset` / `DataLoader`** — `Dataset` yields one `(x, y)` example; `DataLoader` batches, shuffles, and parallelizes loading.
- **`model.train()` / `model.eval()`** — toggle training behavior of dropout & batchnorm. Wrap evaluation in `torch.no_grad()` to skip gradient tracking (faster, less memory).
- **Save/load** — save `model.state_dict()` (the weights), not the whole object: `torch.save(model.state_dict(), "m.pt")` then `model.load_state_dict(torch.load("m.pt"))`. Checkpoint optimizer state too for resuming.

### Minimal training loop

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

device = "cuda" if torch.cuda.is_available() else "cpu"

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10),          # raw logits; no softmax here
).to(device)

loss_fn = nn.CrossEntropyLoss()  # applies softmax internally
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)

for epoch in range(num_epochs):
    model.train()
    for xb, yb in train_loader:
        xb, yb = xb.to(device), yb.to(device)

        optimizer.zero_grad()        # 1. clear old gradients
        preds = model(xb)            # 2. forward pass
        loss = loss_fn(preds, yb)    # 3. compute loss
        loss.backward()              # 4. backprop -> fills .grad
        optimizer.step()             # 5. update weights

    # validation
    model.eval()
    with torch.no_grad():
        # ... compute val loss / accuracy on val_loader ...
        pass
```

## ⚠️ Pitfalls for SWEs
- **Forgetting `optimizer.zero_grad()`** — PyTorch *accumulates* gradients by default. Skip the reset and every step is corrupted by stale gradients.
- **Wrong loss/activation pairing** — `nn.CrossEntropyLoss` expects **raw logits** (it does softmax internally), so don't add a softmax layer. For binary, use `BCEWithLogitsLoss` (logits) not `BCELoss` after a sigmoid. Double-softmax silently wrecks training.
- **Not normalizing inputs** — feed raw pixel values 0–255 or unscaled features and training crawls or diverges. Normalize (e.g. mean/std).
- **Learning rate too high/low** — the #1 cause of "won't learn." Sweep it before touching anything else.
- **Forgetting `train()` / `eval()` mode** — leaving dropout/batchnorm in training mode during evaluation gives wrong, noisy metrics; leaving them in eval mode during training disables regularization.
- **Not using a GPU** — training MLPs/CNNs on CPU is needlessly 10–100× slower. Move model *and* data to the same device.
- **Tensor shape/dtype mismatches** — labels as float when CrossEntropy wants `long`, or a stray batch dimension. Print shapes early and often.

## 🔑 Key terms
- **Epoch** — one full pass over the training set. **Batch** — the subset processed per step. **Iteration** — one batch step.
- **Gradient** — derivative of the loss w.r.t. a parameter; the direction to move to reduce loss.
- **Logits** — raw, unnormalized model outputs before softmax/sigmoid.
- **Parameter** — a learnable weight or bias. **Hyperparameter** — a setting *you* choose (lr, batch size, layers).
- **Overfitting / Underfitting** — too tuned to training data / too weak to fit it at all.
- **Regularization** — anything that fights overfitting (dropout, weight decay, augmentation).
- **Backbone / Head** — the pretrained feature extractor / the task-specific final layers.
- **Latent vector** — a compressed internal representation (e.g. an autoencoder's bottleneck).
- **AMP** — automatic mixed precision (fp16/bf16 training for speed & memory).

## 📚 Best resources
- **Best intro** — [fast.ai: Practical Deep Learning for Coders (free)](https://course.fast.ai/) — *top-down, build first*
- **From scratch** — [Andrej Karpathy: Neural Networks Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) **(build [micrograd](https://github.com/karpathy/micrograd) & GPT by hand — essential)**
- **PyTorch** — [Official 60-min Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) · [Daniel Bourke: Learn PyTorch (free, 25h)](https://www.learnpytorch.io/)
- **Theory** — [DeepLearning.AI Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) · *Dive into Deep Learning* (free book, [d2l.ai](https://d2l.ai/))

## 🛠️ Phase project
**Two projects:**

**1. Image classifier — beat yourself with transfer learning.**
- Train a CNN from scratch on a real dataset (CIFAR-10, or a custom folder of images).
- Then fine-tune a pretrained ResNet on the same data.
- **Acceptance criteria:** custom training loop (no Lightning) with train/val split; loss & accuracy plotted per epoch; transfer-learning model **beats** your from-scratch CNN's validation accuracy; data augmentation applied; model saved/loaded from a `state_dict`; you can explain *why* the pretrained model won.

**2. Implement micrograd yourself.**
- Build [Karpathy's micrograd](https://github.com/karpathy/micrograd) — a tiny scalar autograd engine — from scratch.
- **Acceptance criteria:** a `Value` class supporting `+`, `*`, `tanh`/`relu`, with a working `.backward()`; train a tiny MLP on a toy dataset and watch the loss go down; verify your gradients match PyTorch's on the same expression. This *cements* backprop forever.

➡️ Next: [Phase 5 — NLP & Transformers](05-nlp-transformers.md)
