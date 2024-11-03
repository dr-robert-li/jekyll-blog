---
layout: post
title: OpenDiLoCo and Distributed Training
date: 2024-10-28
categories: [AI, Research, Model Development, Scalability, Future Trends, Distributed Training, Training Methodology]
---

![https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/refs/heads/main/images/opendiloco.jpg](https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/refs/heads/main/images/opendiloco.jpg)

### Introduction

The evolution of large language models (LLMs) has brought significant challenges regarding their training, primarily due to the extensive computational resources required and the need for efficient parallelization across multiple devices. Amidst all the furtive whispers of Chinese researchers and Microsoft finding a way to train models in a distributed manner across disparate hardware, there was a silently released paper on **OpenDiLoCo**, an open-source framework designed to implement the **Distributed Low-Communication (DiLoCo)** training method, you can read here: [arXiv paper](https://arxiv.org/abs/2407.07852). This innovative approach allows for efficient training across poorly connected devices by drastically reducing communication overhead, thus enabling global-scale training without the constraints typically imposed by bandwidth limitations.

### Key Themes and Concepts

#### Local Stochastic Gradient Descent (SGD) Algorithm

At the heart of DiLoCo is a local SGD algorithm that employs two optimizers:

- **Inner Optimizer**: **AdamW** (Adaptive Moment Estimation with Weight Decay) is utilized for local updates on individual workers. AdamW enhances the Adam optimizer by decoupling weight decay from optimization steps, facilitating better generalization in models.

- **Outer Optimizer**: **SGD with Nesterov Momentum** is employed to synchronize updates across workers. Nesterov momentum improves convergence speed by considering future parameter positions during updates.

The mathematical formulation for these optimizers can be summarized as follows:

- For the inner optimizer (AdamW):

$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t
$$

$$
v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2
$$

$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{v_t} + \epsilon} m_t
$$

- For the outer optimizer (SGD with Nesterov):

$$
v_t = \mu v_{t-1} + g_t
$$

$$
\theta_{t+1} = \theta_t - \eta g_t + \mu(\theta_t - \theta_{t-1})
$$

This dual optimization approach allows DiLoCo to reduce communication requirements by up to **500 times**, which is crucial for distributed training in environments with limited bandwidth.

#### Implementation Details

The implementation of DiLoCo consists of two main frameworks:

- **Torch.distributed**: This implementation utilizes PyTorch's distributed package with NCCL as the communication backend. It requires custom training code and is not compatible with standard libraries like Hugging Face or PyTorch Lightning.

```python
for batch, step in enumerate(train_loader):
    ... # loss calculation
    inner_optimizer.step()
    if real_step % local_steps == 0:
        for old_param, param in zip(original_params, model.parameters()):
            param.grad = old_param - param.data
            dist.all_reduce(tensor=param.grad, op=dist.ReduceOp.AVG)
            param.data = old_param
        outer_optimizer.step()
        original_params = [p.detach().clone() for p in model.parameters()]
```

- **Hivemind**: A more practical decentralized training framework that uses a distributed hash table for peer-to-peer communication. This implementation simplifies integration and allows for dynamic resource allocation and fault tolerance.

Here’s a code snippet illustrating how the Hivemind implementation works:

```python
from hivemind.dht.dht import DHT
from open_diloco import DiLoCoOptimizer

optimizer = DiLoCoOptimizer(
    bs,  # batch size
    ls,  # learning rate scheduler
    DHT(),  # distributed hash table for coordination
    i_opt,  # inner optimizer
    o_opt,  # outer optimizer
    m.params()  # model parameters
)

for batch in train_dataloader:
    model(batch).loss.backward()
    optimizer.step()  # outer step triggered automatically after local steps
    optimizer.zero_grad()
```

### Experimental Setup and Results

The authors replicated experiments using a model with **150 million parameters** on a language modeling task utilizing the C4 dataset. They also scaled their experiments to models with **1.1 billion parameters**, demonstrating that DiLoCo is effective even at larger scales.

#### Main Findings

- DiLoCo outperformed a baseline without replicas and matched the performance of a stronger baseline while communicating significantly less.
  
- The experiments showed that using eight workers yielded comparable perplexity to Distributed Data Parallel (DDP) training after sufficient steps but was less efficient in shorter runs.

#### Performance Metrics

| Model                       | Communication | Time | Compute & Data | Perplexity |
|-----------------------------|---------------|------|----------------|------------|
| Baseline, no replica        | 0             | 1×   | 1×             | 16.17      |
| Baseline, 8× batch size     | $$8 × N$$     | 1×   | $$8 ×$$       | 13.68      |
| DiLoCo, 8 replicas          | $$8 × N/H$$   | 1×   | $$8 ×$$       | **13.73**  |

### Conclusions and Ramifications

The authors conclude that OpenDiLoCo successfully reproduces and scales the original DiLoCo method while achieving high compute utilization across globally distributed settings. The implications of this methodology are significant for future LLM training, as it allows researchers to leverage decentralized resources effectively without being constrained by bandwidth limitations.

#### Future Directions

Future research will focus on:

- Enhancing compute efficiency for decentralized training.
  
- Developing asynchronous communication methods to reduce idle time during training.
  
- Scaling OpenDiLoCo further to accommodate even larger model sizes and more complex architectures.

### Relation to Large Language Models Training Methodologies

As LLMs continue to grow in size and complexity, methodologies like OpenDiLoCo provide essential frameworks for efficient training across diverse environments. By minimizing communication overhead while maintaining high compute utilization, this approach paves the way for more accessible and scalable AI development practices.

### Supporting Research

Third-party studies support these findings by demonstrating similar trends in decentralized training efficiency and optimization strategies that enhance model performance while reducing resource consumption.

---

## Detailed Analysis of OpenDiLoCo and the Prime Codebase

### Overview of the Prime Codebase

In conjunction with OpenDiLoCo, the **Prime** codebase serves as a practical implementation framework designed specifically for scaling distributed training over the internet. Below are key features and functionalities that enhance its utility:

#### Key Features of Prime

1. **ElasticDeviceMesh**: A dynamic process group management system that handles node join/leave events without requiring a restart. It uses heartbeat mechanisms to maintain group integrity.

2. **Asynchronous Distributed Checkpointing**: Minimizes blocking during checkpoint creation by first saving checkpoints in RAM (`/dev/shm`) before transferring them to disk asynchronously.

3. **Live Checkpoint Recovery**: Allows new nodes to quickly join ongoing training sessions by fetching the latest model state from peers without stalling the training process.

4. **Custom Int8 All-Reduce Kernel**: Implements efficient quantization of pseudo-gradients to reduce communication payloads significantly while maintaining performance.

5. **Maximized Bandwidth Utilization**: Implements techniques to optimize peer-to-peer connections and improve data transfer speeds between nodes.

6. **Integration with PyTorch FSDP2 / DTensor ZeRO-3**: Enables sharding of model weights and gradients across multiple GPUs, allowing larger models to be trained efficiently.

### Getting Started with Prime

To start using the Prime codebase for distributed training:

1. **Install Dependencies**:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

2. **Set Up Environment**:

```bash
uv venv
source .venv/bin/activate
uv sync --extra all
uv pip install flash-attn --no-build-isolation
git submodule update --init --recursive
```

3. **Log into Hugging Face** (for model access):

```bash
huggingface-cli login
```

4. **Run DiLoCo Locally**:

Use helper scripts provided in the repository to simulate multi-node setups.

```bash
ZERO_BAND_LOG_LEVEL=DEBUG ./scripts/simulate_multi_node_diloco.sh 2 2 src/zeroband/train.py @configs/debug/diloco.toml
```

### Importance of OpenDiLoCo and Prime Codebase

The significance of OpenDiLoCo and its implementation through Prime lies in their potential to revolutionize distributed training methodologies for LLMs:

- **Scalability**: Enables efficient training of models that exceed traditional hardware limitations by leveraging decentralized resources.
  
- **Reduced Communication Costs**: The architecture minimizes bandwidth requirements, making it feasible to train models across geographically dispersed nodes without high latency or costs.
  
- **Fault Tolerance and Flexibility**: The design allows for dynamic adjustments in resource availability, accommodating real-world conditions where nodes may join or leave unexpectedly.
  
- **Future Research Directions**: The framework opens avenues for further exploration into asynchronous training methods and improved convergence techniques that can enhance performance even as model sizes continue to grow.

In summary, both OpenDiLoCo and the Prime codebase represent significant advancements in distributed machine learning that could facilitate more accessible and efficient training of increasingly complex AI models.

##### Citations:
* [1] https://arxiv.org/abs/2407.07852
* [2] https://www.aimodels.fyi/papers/arxiv/diloco-distributed-low-communication-training-language-models
* [3] https://openreview.net/forum?id=pICSfWkJIk
* [4] https://www.restack.io/p/distributed-ai-training-answer-llm-ai-ml-cat-ai
* [5] https://openreview.net/pdf/OM0jvwB8jIp57ZJjtNEZ.pdf
* [6] https://en.wikipedia.org/wiki/Stochastic_gradient_descent
* [7] http://arxiv.org/pdf/2407.07852v1.pdf
