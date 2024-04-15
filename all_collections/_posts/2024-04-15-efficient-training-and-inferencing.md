---
layout: post
title: Efficient Training and Inference - The future of Large Language Models at Scale.
date: 2024-04-15
categories: [AI, Research, Future]
---

News about Large Language Models (LLMs) breakthroughs is everywhere at the moment, showcasing remarkable capabilities in natural language understanding, generation, and reasoning. 

However, use of them in real world applications, isn't as pervasive. That is because as these models have grown in size and complexity, the computational resources required to train and deploy them have become a significant bottleneck. 

Here, we'll explore three recent research papers that tackle the challenge of improving training and inference efficiency for LLMs, and discuss how these advancements could pave the way for LLMs to move beyond hobbyist fascination to mainstream ubiquity by 2025.

## The Computational Bottleneck
Training state-of-the-art LLMs pre-2023 like GPT-3, PaLM, and Chinchilla required an enormous amount of computational resources. For example, training GPT-3 consumed an estimated 314 *Thousand Exaflops* of compute, and cost many millions of dollars, and it's expected that the training of the hypothetical GPT-6 and GPT-7 will be exponentially more expensive, potentially costing trillions. Inference is also expensive, with OpenAI reportedly spending tens of millions per month on API costs alone with each inference request reportedly costing ~3x more than is being charged and Microsoft supporting most of that bill.

This computational bottleneck poses a major challenge for organizations looking to develop and deploy LLMs in production-ready workloads. The physical limits of high-performance GPUs and the exorbitant costs associated with training and inference have meant that only the most well-funded tech giants and research labs have been able to push the boundaries of what's possible with LLMs.

However, a flurry of recent research is starting to chip away at this problem, offering new techniques to drastically improve the efficiency of LLMs without sacrificing performance. Let's dive into three promising approaches.

## LongRoPE: Extending LLM Context Windows
One key limitation of LLMs is the context window - the amount of text the model can attend to when generating a response. Most LLMs are constrained to context windows of a few thousand tokens, with the largest context window provided by Anthropic's Claude 3 of 1 Million tokens (to selected customers). This limits most model's ability to handle very long-form content or maintain coherence over extended interactions. Case in point, Anthropic's own research showed a novel jailbreaking technique that exploited these context window limitations ([https://www.anthropic.com/research/many-shot-jailbreaking](https://www.anthropic.com/research/many-shot-jailbreaking)).

In the paper "LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens" ([https://arxiv.org/html/2402.13753v1](https://arxiv.org/html/2402.13753v1)), Ding et al. from Microsoft's AI Research team introduce a new technique called LongRoPE that allows LLMs to efficiently attend to context windows of over 2 million tokens - an improvement by a factor of many multiples over the status quo. LongRoPE achieves this by exploiting non-uniformities in the positional embeddings used by the model's attention mechanism. By carefully interpolating these embeddings, the approach minimizes information loss while enabling massive context window extension.

The results are impressive - LongRoPE-equipped models match the perplexity of standard models on short context windows, while vastly outperforming them on longer contexts. Importantly, LongRoPE introduces minimal overhead in terms of parameters and computation. This makes it an appealing plug-and-play upgrade for existing LLMs looking to expand their context windows without breaking the bank. This was also conducted on mid-tier performing models LLaMA2 and Mistral-7B with no loss in perplexity even at the context window length of over 2 Million tokens, so we can expect that there is *more juice to squeeze out of this approach* and that further finetuning could yield ever larger context windows.

## Tokenizer-Free LLMs
Another active area of research is on the efficacy of LLM tokenizers themselves. Tokenizers are responsible for splitting raw text into discrete tokens that can be processed by the model. Standard tokenizers encode and decode text, which requires computationally expensive string manipulations that can bottleneck inference speed.

The paper "Training LLMs over Neurally Compressed Text" ([https://arxiv.org/html/2404.03626v1](https://arxiv.org/html/2404.03626v1)) by Lester et al. proposes a radically different approach - training LLMs directly on compressed representations of text. The key insight is to use a small neural compressor model to tokenize raw text into a compressed bit stream, and then train a larger LLM to model this bit stream directly. This has the dual benefit of reducing sequence lengths (allowing more text to be packed into a fixed context window) and enabling faster tokenization.

The authors from Anthropic and Deep Mind show that LLMs trained on neurally compressed text can match the perplexity of standard LLMs while using up to 23% less compute. The approach also unlocks very large vocabulary sizes of up to 65K tokens, without the usual inference-time costs, since the vocabulary is neurally compressed. While there are still challenges around the stability of the neural compression, this is a promising direction and the use of tokenizer-free inferencing in combination with other novel approaches could both dramatically increase context window and vocabulary sizes, while simultaneously increasing inference speed and reducing cost.

## Efficient Infinite Context Transformers
A third novel research direction combines ideas from long-range attention and compressed memory to enable LLMs that can efficiently process arbitrary-length context windows. The paper "Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention" ([https://arxiv.org/html/2404.07143v1](https://arxiv.org/html/2404.07143v1)) from the team at Google DeepMind introduces the Infini-attention mechanism, which augments the standard attention layer in Transformers with a compressed memory store.

Infini-attention reuses the key and value states from the local attention window to incrementally update a fixed-size compressed memory. This memory can then be queried efficiently to retrieve relevant information from the entire preceding context, no matter how long. Importantly, the time and memory complexity of Infini-attention is constant with respect to sequence length, making it radically more efficient than standard attention.

The authors demonstrate that Transformer LLMs equipped with Infini-attention can match or outperform standard models on language modeling and summarization tasks, while using up to 100x less memory. An Infini-attention model trained on only 5K token contexts can extrapolate to solving tasks with 1 million token contexts - an unheard of level of length generalization. 

While this wasn't benchmarked against the most modern LLMs performance, this is a promising avenue developing much more efficient and extremely scalable LLMs that can handle arbitrary-length contexts and also consume very little resource.

## The Road to Everyday Ubiquity
The very recent research covered, has me convinced that 2025 will be the year when *LLMs will finally operate at scale*.

By improving the efficiency of training and inference across multiple fronts - context window extension, tokenizer-free modeling, infinite context attention - these techniques promise to drastically reduce the computational burden of LLMs while expanding their capabilities.

This is a crucial step towards making LLMs practical and cost-effective for a much wider range of applications beyond the current "hobbyist" phase. As training and inference efficiency continues to improve, we can expect to see LLMs deployed in more production-ready workloads on a global scale.

2024 is shaping up to be the year of multi-modal LLMs. Rapid progress in text-to-image models like DALL-E, Midjourney and Stable Diffusion, music generation technologies like the recently released Suno.ai, and text-to-video models like the incoming Sora are expanding the creative capabilities of AI. As these models grow in scale and fidelity, the compute requirements will once again become a limiting factor.

This is where the efficiency techniques being pioneered for language-only LLMs at the moment, will likely play a key role when their use becomes adapted. Approaches like compressed attention, hybrid sparse architectures, and neural compression will be essential for scaling multi-modal models to the next level. With the rate at which research is being commercialized we can expect this to be within the next 12-18 months.

All of this points to 2025 being an inflection point for LLMs and AI more broadly. As the technology matures and the cost curve bends towards affordability, we will likely see LLMs transition from objects of mainstream curiosity to everyday ubiquity. LLMs will become a pervasive part of the technology landscape. 

Where mobile phones gave us access to the world's information in the palm of our hands, AI driven assistance will curate that information to be contextually relevant. 

It won't just be about knowing everything anymore. It will be all about knowing *the right things*.