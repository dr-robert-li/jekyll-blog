---
layout: post
title: The Looming Crisis of AI Training Data and the Spectre of Model Collapse. What can we do about it?
date: 2024-04-29
categories: [AI, Research, Training, Data, Model Collapse]
---

![https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/model-collapse.jpeg](https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/model-collapse.jpeg)

In recent years, as LLMs have moved from having millions of parameters to billions of parameters, from GPT to Claude 3 one of the more surprising developments has been the emergent capabilities in natural language understanding and generation this models have started to provide, and now power experiences through applications from search engines to coding assistants to chatbots, that mirror our own behaviours and tendencies remarkably well. The recipe for this meteoric progress has relied on three key ingredients - more efficient algorithms and architectures, most influentially the invention of transformer architecture, a massive increase in compute driven by the raw firepower of GPUs first and now the proliferation of specialized AI chipsets and cloud hyperscalers using them, and the actual trigger of this acceleration in LLM development, (basically) OpenAI's, Ilya Sutskever's, choice to improve LLM performance by scaling data to ever larger training datasets scraped from (mainly) the Internet and other sources.

But, what happens when we run out of... the Internet?

A growing body of research and analysis has predicted that we may soon hit a wall when it comes to the availability of the high-quality human generated training data that has fueled the rise of LLMs. Even more concerning, the widespread deployment of AI systems themselves is starting to pollute and contaminate the very data sources they rely on, leading to a phenomenon called "model collapse." Like a snake eating its own tail, AI that trains on AI-generated data could ultimately devolve into incoherence and nonsense.

In this post, we'll take a deep dive into the looming crisis of AI training data and what it means for the future development of the technology. We'll examine the evidence and projections around the exhaustion of data sources, the threat of model collapse, and potential paths forward for the field. As we'll see, while there are no easy answers, grappling with this challenge will be essential if we want to realize the full transformative potential of artificial intelligence in the years and decades to come.

## The Voracious Appetite of LLMs

To understand the impending data crunch, we first need to wrap our heads around the truly staggering scale of the datasets used to train modern LLMs. Let's look at some key numbers:

- GPT-3, was released by OpenAI in 2020, was trained on 45 terabytes of text data. By some estimates, this represents nearly a trillion words of text. This was 100x the size of the entire English language corpus used to train GPT-2, released in 2019. GPT-2 was itself trained on 170 terabytes of data. By some estimates GPT-4 has over 1.76 trillion tokens of text data. If we take the rule of thumb of 4 tokens per 3 words, this would mean GPT-4 has just over 1.32 trillion words of text data.

- Chinchilla, the compute-optimal model debuted by DeepMind in 2022, was trained on 1.4 trillion tokens, although it has far fewer parameters than GPT-3 or PaLM.

- Although the details of their training data are not fully public, more recent models like Claude 3 likely utilize corpora larger than even these predecessors.

To put these numbers in perspective, the entire works of Shakespeare clock in at around 900,000 words. The English Wikipedia contains just over 3.5 billion words as of 2022. So training a single state-of-the-art LLM today requires text data equivalent to hundreds of Wikipedias or millions of Shakespeares. 

This exponential growth shows no signs of slowing down. Gavin Uberti of Etched.ai (a startup building a new generation of AI focused chipsets) estimates that GPT-5, which is set to release imminently is ~10x the size of GPT-4, which would mean ~12-18 trillion tokens of text data. 

## The Dwindling Supply of Quality Data

So where does all this training data come from? The bulk of it is sourced from the public internet - websites, articles, social media posts, databases and so on. A commonly used resource is Common Crawl, a repository of web page data collected by crawling the internet monthly. As of 2022, Common Crawl contained over 300 TBs of compressed data.

However, a closer look reveals that this data is not an infinite resource that will scale to meet the needs of ever-hungrier AI models. A 2022 paper by Pablo Villalobos and colleagues analyzed the current availability and growth of language data on the internet and came to some startling conclusions:

- The total stock of language data on the internet is currently estimated to be between 1e14 and 1e15 words (100-1000 trillion). This sounds like a lot, but it's only 1-2 orders of magnitude larger than the datasets already used to train the largest LLMs and could be fully consumed by the time we reach LLMs that are generational peers of GPT-6 or GPT-7.

- The growth rate of online data has slowed significantly since the days of the early internet. From 2010-2018, the amount of data grew around 20% per year, but more recently this has declined to around 7% annually. By 2100, the growth rate may be as low as 1% per year.

- Crucially, when it comes to the high quality data most useful for training LLMs - books, articles, websites, databases etc. - the total stock is estimated at only 1e13 to 1e14 tokens (10-100 trillion). As a reminder ***this is the expected size of GPT-5***. This means that as the growth rate of online data continues to slow, we will still run out of high quality data to train LLMs by 2026. Far faster than the prediction of Pablo Villalobos just 2 years ago.

- We will essentially run out of high quality language data to train LLMs by 2026, and lower quality data between 2030-2050.

- For image and video data used to train AI models like DALL-E, Midjourney and Stable Diffusion, a similar dynamic of slowing growth and potential exhaustion in the 2030-2060 timeframe is predicted by the same paper.

This "peak data" scenario should be extremely concerning for anyone banking on the continued exponential progress of AI models. While there are always uncertainties in such long-range forecasts, it's clear that data availability will act as a constraint on future model development, absent a major change in approach.

## The Curse of Model Collapse

However, hitting peak data is a (near) future problem, there's an even more immediate brake to AI progress: the pollution of the data supply by AI itself. With LLMs and other models now widely deployed in real-world applications from search engines to chatbots to writing tools, an ever-increasing share of the content being published online is itself generated by AI (in fact, full disclosure, this article too, was generated with the assistance of generative AI). And when that synthetic, AI-generated data is then fed back into the training sets for future models, it can lead to a feedback loop known as "model collapse".

You can think of model collapse as the AI equivalent of inbreeding. When a model is trained on lower and lower quality data generated by other AI models, it loses coherence and any connection to external reality. It may spit out content that superficially looks okay, but is full of nonsense, falsehoods and contradictions. We got a sneak preview of this recently when Anthropic's Claude model, prompted by a user to describe itself, confidently declared "I am Ernie Bot from Baidu" - likely because that's what it had seen other AI models say in its training data.

The risks of model collapse get even worse when you consider that today's LLMs are not just stochastic parrots mindlessly regurgitating their training data, but are imbued with some ability to reason, infer and generate novel content - including potentially generating training data for future models in a hypothetical AI recursive self-improvement scenario. An AI that trains on the not-quite-coherent outputs of a previous generation of AI, which trained on the outputs of the generation before that, is a recipe for an accelerating lurch into incoherence and detachment from reality - a hyperreality, so to speak.

So model collapse is not some distant, theoretical concern - it's likely already happening to some degree in currently deployed models. Absent a major effort to filter, fact-check and curate training data, or a shift away from models that simply ingest and regurgitate internet data in a wholly unsupervised manner, we may soon be facing a crisis of AI models that are superficially fluent but have no real understanding.

## Potential Paths Forward

So what can be done to avert the looming crisis of peak data and model collapse? There are no easy answers, but here are a few potential directions the field may take:

- We can explore novel architectures, selective data usage, hardware optimization, and improved embedding techniques to make AI models more data-efficient and capable of handling complex tasks with limited resources:

    - Designing architectures that can dynamically expand their learning capacity as needed is a promising direction for data efficiency. For example, the mixed expert architecture has been used to great effect with Mistral's Mixtral LLM recently, is parameter-efficient and can grow its learning capacity to better balance the stability-plasticity tradeoff in lifelong learning scenarios with limited data. For example as proposed in:

        - **Hypermixer**  (https://arxiv.org/abs/2203.03691): An MLP-based low-cost alternative to transformers that forms token mixing MLPs dynamically using hypernetworks.

        - **MLP-Mixer**  (https://openreview.net/pdf?id=r8h2uUX22d): An all-MLP architecture for vision tasks that mixes per-location features and spatial information via MLPs instead of convolutions or self-attention.

    Other novel approaches showing promise include:

    - **H3**  (https://arize.com/blog/hungry-hungry-hippos-h3-state-space-models/): A state-space model that performs comparably to transformers while admitting much longer context lengths, scaling as n log(n) rather than n^2 with sequence length.  

    - **Hyena**  (https://hazyresearch.stanford.edu/blog/2023-03-07-hyena): Builds on H3 using gated convolutions, showing promising results on language modeling at scale.

    - **The SwiftLearn approach** (https://hazyresearch.stanford.edu/blog/2023-03-07-hyena) accelerates training by using only a subset of the most important data samples selected during initial warm-up stages. This subset is chosen based on an importance criteria measured over the entire dataset, with the aim of preserving model performance while using fewer examples for the remaining training. The importance measure can be updated during training to allow previously excluded samples back into the training loop if they become more important.

    - **EVA**  (https://web.eecs.umich.edu/~taustin/papers/CASES2013-eva.pdf): An efficient vision architecture using custom accelerators and a 2D-aware cache for mobile systems.  

    - **RoFormer**  (https://arxiv.org/abs/2104.09864): Leverages rotary position embeddings to improve transformers' ability to model long sequences.

    - **Dynamic Convolutions**  (https://arxiv.org/abs/1912.03458): Instead of using a single convolution kernel per layer as in standard CNNs, dynamic convolution aggregates multiple parallel convolution kernels dynamically based upon their attentions, which are input dependent. Assembling multiple kernels is not only computationally efficient due to the small kernel size, but also has more representation power since these kernels are aggregated in a non-linear way via attention. It showed image classification is boosted by 2.9% with only 4% additional FLOPs.

- **Specialised Models**: A shift away from huge, generic models trained on raw internet data to more specialized models trained on carefully curated, domain-specific datasets. For many applications, a smaller model with deep knowledge of a particular area like law, medicine, science etc. may be more useful than a jack-of-all-trades mega-model. 

- **Model-based training simulators for large language models (LLMs)** (https://arxiv.org/html/2312.00678v2) offer a cost-effective way to estimate model perplexity before extensive computational resources are used. These simulators mimic the real training environment using simpler, less resource-intensive models to predict how well LLMs will perform. By enabling researchers to test various configurations and training strategies, these tools help optimize resource allocation and accelerate model development. However, ensuring the accuracy and calibration of these simulators is essential for them to be truly effective in advancing AI efficiency and capabilities.

- **Modular training strategies** (https://arxiv.org/pdf/2312.03863.pdf) to enhance training speed and reduce resource consumption in LLMs, which can be split into three non-exclusive approaches:
    - Distributed Training involves partitioning the training process across multiple devices or machines to accelerate the training. 
    - Mixed Precision Training uses varying precision levels for different parts of the model to optimize memory and computational resources. 
    - GPU to CPU Offloading involves transferring certain computations from GPUs to CPUs to further optimize memory usage and computational efficiency. 
    
- **Using Stratified Cluster Sampling**: careful data curation via stratified cluster sampling aims to make the most effective use of available data by selecting representative and high-quality samples. This data-efficient approach can yield better-performing models without requiring as much data scaling, bypassing some of the limitations of the power-law scaling bottleneck. A very good recent paper surveying the current efficiency of LLMs by Ding et al. can be found here: https://arxiv.org/html/2312.00678v2

- **Self Questioning and Data Density Evaluation**: The paper "How to Train Data-Efficient LLMs" introduces methods like Ask-LLM and Density sampling (https://arxiv.org/html/2402.09668v1). These methods significantly reduce the data needed for training without compromising model performance, potentially speeding up convergence and outperforming models trained on full datasets.
    - Ask-LLM is a method for optimizing data efficiency during LLM training by leveraging the model's own capabilities to generate questions based on the training data it has already seen. This helps in focusing the training on data areas that are less understood by the model, thereby improving its learning efficiency. 
    - Density sampling, on the other hand, involves selecting training data based on the density of information it contains. This method prioritizes diverse and information-rich examples to ensure broad coverage and effective learning. 

- **Increased use of human feedback and oversight in the training process** to catch model errors and instill more coherent behavior. Techniques like reinforcement learning from human feedback (RLHF), debate and iterated amplification show promise here. The goal is to rely more on human knowledge and less on brute force data ingestion.

- **Expanding the data supply through generating synthetic data**: This is already a common approach in fields like robotics and autonomous driving where sim-to-real approaches are used that mimics the structure of the real world. Some approaches have been explored with large language models several papers including "Best Practices and Lessons Learned on Synthetic Data for Language Models" (https://arxiv.org/html/2404.07503v1) where the following approaches are discussed allowing for increased data privacy and expanded training datasets, although it was noted that some challenges included maintaining data quality and the ethical issues of potentially magnifying biases in the existing dataset:
    - Generative Adversarial Networks (GANs): These involve training two neural networks, a generator and a discriminator, that compete against each other to produce increasingly realistic data.
    - Variational Autoencoders (VAEs): VAEs generate new data points by learning to encode inputs into a low-dimensional space and then decoding from this space.

- **Grappling with the societal impacts of widespread AI-generated content online**: This may require developing robust watermarking techniques to tag synthetic content, as well as norms and regulations around disclosure of AI authorship. Platforms may need to more aggressively filter and fact-check AI outputs before dissemination.

In the longer run, fundamental advances in our understanding of intelligence and reasoning might be able to yield more data-efficient and generalizable models. Today's language models operate by pattern matching and information retrieval - they have no real understanding of the world, but incoming, larger and more advanced models (perhaps GPT-5, as OpenAI's CEO, Sam Altman, fondly refers to the current top performing model in many benchmarks, their own GPT-4, as [the dumbest model you will ever use](https://www.msn.com/en-us/news/technology/openai-ceo-sam-altman-promises-with-a-high-degree-of-scientific-certainty-that-gpt-5-will-be-smarter-than-the-mildly-embarrassing-at-best-gpt-4/ar-AA1o5JAT)) may implement cognitive architectures that can learn causal models from less data, or that incorporate techniques like analogical reasoning, abstraction and compositionality, which are necessary to transcend the current limits that brute force scaling necessarily leads to.

None of these paths are easy or guaranteed to succeed. But the AI field will need to grapple with them if we want to sustain progress. 
It is widely acknowledged that the value of data exceeds even the value of oil, and the demand created by training models has made this more and more concrete. The era of cheap and easily accessible data is coming to an end. What comes next will require more than just scaling up, but a fundamental rethinking of how we build and train AI systems.

## The Specter of Hyperreality

It's worth stepping back to consider the deeper implications of a world increasingly saturated with AI-generated content and interaction. As alluded to earlier, we may be entering an era of hyperreality, where the distinction between the "real" and the "simulated" becomes increasingly blurred.

This is not a new idea - philosophers like Jean Baudrillard have been grappling with the concept of simulation and hyperreality for decades. But the rise of large language models and generative AI puts these abstract musings within the grasp of our lived realities. When the news articles we read, the social media posts we scroll, and the chatbot conversations we have are increasingly generated by AI models trained on AI-generated content, reality itself starts to feel unmoored.

In some ways, this is the culmination of trends that have been building for a long time. We already live in a world saturated with media representations and constructed narratives. The difference is that now, those representations are being generated not just by human culture industries, but by AI systems with their own emergent goals and dynamics. This is reality Ouroboros.

Of course, AI models are not conscious agents with true understanding - they are simply very sophisticated pattern matchers and information retrievers, operating in the narrow domains of language and images. But as they get better and better at imitating human behavior and reasoning, the experiential distinction may start to erode. Contemporary human-generated reality is already grappling with instability. Adding an AI generated feedback loop without intervention may only accelerate this trend. 

So the challenges of peak data and model collapse are not just technical problems for AI researchers to grapple with - they have profound implications for the fabric of our shared reality and sense-making. In a hyperreal world, where truth and authenticity are increasingly elusive, we'll need to find new ways to anchor ourselves and navigate the blurry boundaries between the real and the simulated.

This is a daunting prospect, but also an opportunity for growth and exploration. Just as the rise of the internet and social media forced us to grapple with new challenges around information overload, filter bubbles, and digital manipulation, the rise of AI will require us to develop new cognitive and cultural tools for making sense of a world where the line between human and machine, real and simulated, is increasingly porous.

We'll need to cultivate a new kind of critical literacy - an ability to discern the provenance and reliability of the information we encounter, and to reason about the goals and limitations of the AI systems we interact with. We'll need to find ways to anchor our sense of reality and meaning in the face of a rising tide of synthetic content and interaction. And we'll need to grapple with the philosophical and ethical implications of living in a world where the distinction between human and artificial intelligence is increasingly blurred.

The rise of large language models and generative AI is not just a technical development, but a cultural and epistemological shift that will reshape our relationship to reality itself. Navigating this new landscape will require not just better AI architectures and training paradigms, but a different, perhaps more thorough understanding and definition of the nature of intelligence, meaning, and truth in an age of hyperreality.