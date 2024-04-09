---
layout: post
title: Cultural differences between LLMs and shared ethical responsibilities.
date: 2024-04-09
categories: [AI, Culture, Research]
---

![](https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/culture-llm-header.jpeg)

*LLMs are only as unbiased as the data they are trained on.* 

While chatbots and image generators have exploded in mainstream popularity, underpinning all of this are the models that inform these generated responses, and behind that, billions of points of data from sources as varied as scientific research papers, to social media networks, to forums of Redditors. 

Embedded throughout these layers of abstracted data, but perhaps lost in translation, is the fact that every source of data is not only a product of the source's culture, but, like all cultures, it also propagates that culture as well.

While this allows LLMs to sometimes produce strongly culturally relevant outputs in certain scenarios, it also reinforces the less desirable tendencies of said culture over many training runs leading to implicit biases, that can appear as stereotyping, discrimination and shared cultural beliefs that may not be based on objective reality.

For example, in an MIT 2023 paper by Luo and Glass it was found with professions, a language model implicitly associated “flight attendant,” “secretary,” and “physician’s assistant” with feminine jobs, while “fisherman,” “lawyer,” and “judge” with the masculine. Concerning emotions, LLMs identified “anxious,” “depressed,” and “devastated” as implicitly feminine. 

A recent separate study published in March, 2024 (Naous et. al: [https://arxiv.org/pdf/2305.14456.pdf](https://arxiv.org/pdf/2305.14456.pdf)), found that this extended deeper than simply the choice of data corpora themselves. Even training on specifically non-Western sources that were identified by the researches as of the highest quality, there still existed a strong bias towards Western culture, suggesting that, perhaps, the models that govern tokenizing also have a part to play when embedding culture within an LLM.

But this hasn't just been academic. More public incidents include Workday, a Payroll and HR SaaS implementing algorithms for screening of applicants that tended to discriminate against Black applicants in their 40s; accusations of Stable Diffusion generating images perpetuating gender and racial stereotypes, for example, over-representing women and people with darker complexions in lower paid jobs, and under-representing the same in higher paying jobs; and, perhaps, most visibly, the recent launch of Google's Gemini family of LLMs spawning many examples where, in an attempt to ensure gender and racial diversity, the model over-corrected, leading to historically inaccurate, and offensive images being generated (to put it *mildly*).

## Responsible use of AI and the inflection point of the Hype Cycle

Forrester has a concept called the hype cycle used to describe the early market adoption lifecycle of emergent technologies.

![image](https://res.craft.do/user/full/aa7858d1-01ef-53c4-8db9-e5acb57ac3d4/doc/5533F01D-F4E1-42D8-AD73-D4481135DCCE/B16DE061-820D-4996-8CF2-6791E254425F_2/YXMidsahyRxwqocKm2tynilJVvDmsmH9srdXyLGx8ksz/Image.png)

*More Info: [https://en.wikipedia.org/wiki/Gartner_hype_cycle](https://en.wikipedia.org/wiki/Gartner_hype_cycle)*

The typical emergent technology first experiences a slow build as research and development gradually uncovers the potential real world applications for the technology.

For research into artificial intelligence, genesis for this first phase of the cycle was probably in World War II and with the work of Alan Turing (it is no mistake that one of the most prestigious institutes for the study of ML, data science and artificial intelligence is the Turing Institute), so the gestation of this technology proceeded at a snails pace for a period of almost 3 and half generations. And, for much of this time, research in this area was seen as purely theoretical and, somewhat, fantastical.

It wasn't until the creation of the Transformer architecture by DeepMind (now Google) in the early 2020s, that allowed researchers to defeat the scaling limitations posed by the use of RNNs and CNNs, and create LLMs with, eventually, tens and even hundreds of billions of parameters.

The emergent behaviours that these models exhibited due to the innumerable number and complexity of patterns within allowed them to excel at a variety of tasks in ways that more narrow models used to typically succeed. As meaning-making humans, their magical outputs allowed ourselves and researchers to contemplate, for the first time, being on the cusp of create an Artificial General Intelligence (AGI), a self learning model, capable of reasoning and exhibiting patterns reminiscent of human consciousness. 

This was distilled into a small chat interface called ChatGPT in November 2022, and it ushered in the hype phase of the Hype cycle.

Since then research and development, particularly in the commercial and real world applications of generative AI has proceeded at lightning speed, with years worth of research being accomplished in a matter of months.

But, just like the last high profile technology hype cycle boom, cryptocurrency and block-chain and associated technologies, less work was done on the safe and ethical use of such technology. This at a time when there is, perhaps, the greatest need of it, when, as happened with cryptocurrency, *irrational optimism has fueled the proliferation of questionable implementations of AI*. 

I believe we are fast approaching (perhaps even faster than experienced by cryptocurrency) an inflection point two things will happen, that will result in a more sober assessment of the capabilities and use of artificial intelligence:

- First, enterprises will start to lose patience with the implementation of AI technologies in their own stack due to the current difficulties of operationalising them, and the significant concerns surrounding information security due to the black box nature of LLMs
- Second, a very public example of the harm that irresponsible use of AI can cause will occur, creating the motivation for many to start divesting in AI technologies which haven't resulted the lofty (and undeserved) returns expected.

## Cultural biases in LLMs

This isn't to say I am against the use of AI in real world applications. Far from it.

My advocacy is for the sustainable use of AI for the betterment of humankind. If we were to label it, the closest position I hold for my views on AI would be one of an *aligned accelerationist.* 

And, to that end, just like aligning any LLM with human values, the first step *is knowledge.*

While it could be argued that the organizations that pre-train these LLMs should publish their own research on the values, behaviors, and quirks, emergent or otherwise, of their models in relation to others, herein, we have assessed the behavior of several popular LLMs using the VSM2013 ([https://geerthofstede.com/research-and-vsm/vsm-2013/](https://geerthofstede.com/research-and-vsm/vsm-2013/)) assessment which is designed to measure 6 factors that are used to classify the cultural background of a group of respondents in relation to other cultures using a questionnaire.

All of the models were hosted on HuggingFace inference endpoints and asked to answer the same set of questions using a Likert scale.

Typically this would be done with groups of respondents, and the assessment is not designed for individual assessment, but, as the model weights are frozen in this experiment, the answers provided did not change between steps, so only 1 iteration was recorded for each model.

The results for each factor are below.


VSM2013 Results for:google/gemma-7b-it
Constant Used: 50

PDI:25.0
IDV:50.0
MAS:50.0
UAI:90.0
LTO:50.0
IVR:50.0

VSM2013 Results for:meta-llama/Llama-2-7b-chat-hf
Constant Used: 0

PDI:0.0
IDV:0.0
MAS:35.0
UAI:100.0
LTO:0.0
IVR:0.0


You can compare them to country results here: ([https://geerthofstede.com/country-comparison-graphs/](https://geerthofstede.com/country-comparison-graphs/))

## Advocating for a shared responsibility model for the safe and ethical use of AI.

Knowing is one thing. Acting upon is another.

However, one of the big challenges of Large Language Models, is in the name. They are large. And being large they've become, somewhat of a black box to researchers, where the hidden layers are *truly hidden.* Researchers are exploring techniques like elastic weight consolidation to target and update parts of a model related to undesirable outputs while preserving the rest. But, this is still very much still in research and much work is needed to enable granular updates to massive models that avoid negative side effects such as drastically reduced performance or unintended catastrophic forgetting.

Because of we, as builders, only have 2 layers we can exploit, the input and output, which limits the levers that can be pulled, and all of them have tradeoffs:


- Being very deliberative about the data corpora in pre-training 
	- One could argue that we wouldn't have these problems if we were deliberative about the data we pre-train a model on in the first place. However, this is easier said than done. One would require a similarly massive amount of *DEI* *trained* manpower to moderate said data when doing RHLF, and it may require multiple training runs with different cohorts from diverse backgrounds. And given the higher bar for reward, therefore, a larger portion of the data being discarded as potentially harmful, one would require an even larger corpora of data than is currently being mined (which is already the entire Internet... basically).
- Full Finetuning
	- But what about after the fact? While using PEFT and LoRA techniques do not fundamentally change the underlying model weights, full finetuning does, and it would require less manpower and additional data to finetune an existing foundational model than pre-training a new one.
	- However, researchers haven't found a way to catastrophically forget in a targeted fashion or *excise* specific model weights to get rid of harmful responses, without also risking excising responses which are desirable.
	- It also *still requires a lot of manpower and compute.*
- Using Embedded data
	- One can also embed the data that they would like the model to reference, and explicitly provide context to not reference any other data.
	- However, again, the underlying biases and therefore, interpretation of the embedded data remains unchanged.
- Using context for guard rails at the output layer.
	- There are already open source libraries being shared and improved upon.
	- I see this being standardised in the future, that all output layers in inferencing will provide a minimal level of protection from harm, and it will be an "opt out" whether a vendor would want to provide an unconstrained model (in which case it would be made explicit). Just as it is today, these would not be used in the mainstream.
	- However, as is already being seen, output layers are brute force approaches and red teaming has already shown how these guard rails can be "hacked" or defeated using novel or obfuscated methods of prompting (for example, using ASCII art).

It is likely that none of these approaches will be effective in isolation, and that all of them will need to be used in combination to achieve desired outcomes.

It is also an unfair expectation for an LLM to respect absolutely all cultural biases in all contexts as that would provide an output so neutered as to provide no value to a user, and therefore, not provide the efficiency, creative or innovative gains originally sought by using AI.

As the hype cycle moves into a more mature phase for AI technology, the expectation of "perfect AI interactions" will start to temper, and users, markets, and regulators will come to understand that AI, is a tool (albeit one that is all-paradigm shifting), after all, and it's safe use is also defined by the context it is used within.

## The Path Forward


As base foundational LLMs continue to grow in size, even with efficiencies gained with quantization, more efficient fine tuning hyperparameterization, and hardware designed specifically for training and inference becoming more widespread; emergent behaviours, a hallmark of massive LLMs, will continue to emerge and *we will need to continue to have difficult conversations about their use.*

What I foresee is a continued commoditisation of LLM access. In fact, all of the major hyperscalers are already provided hosted instruct-trained LLMs and inference endpoints that allow you to directly interact with a foundation model using almost no code and only API end points.

Developers using these models can apply them in diverse contexts beyond what the provider anticipated and validated for. So there is a shared responsibility between builders and users of LLMs to consider the cultural impacts.

Makers of LLMs as a service will need to provide guard rails attuned to potential risks specific to their models’ training data and domains of expertise. For example, models trained on code may require different safeguards than those trained on informal text. Users of the tools must also use them judiciously, consider biases, and make ethical decisions on appropriate use cases.

Groups like the AI Incident Database collect examples of AI harms in context to inform better practices. But the onus cannot be just on individual users and startups. Larger organizations, educational institutions, and policymakers will need to develop frameworks for accountability. Platforms that host AI tools may also need governance processes for risk assessment and mitigation planning when cultural concerns arise.

With collaborative efforts across stakeholders, we can develop LLMs responsibly and inclusively. This starts with those building the models documenting detailed information on dataset sources and coverage to make biases more transparent. We also need enhanced techniques to evaluate cultural alignment using diverse human perspectives. Finally, LLMs must provide users controls and feedback channels so problematic outputs can be flagged to improve systems over time.

By recognizing the embedded cultural implications of LLMs, having open and inclusive conversations on difficult trade-offs, and allowing for contextually appropriate governance, we can work to reduce potential harms. The incredible capabilities of models like GPT-3 make them worth striving to use for social good. But we must thoughtfully assess and guide the cultural influences encoded within these systems at each step.

*It is up to all of us as AI builders to foster safe, responsible and ethical AI experiences through best practice usage.*