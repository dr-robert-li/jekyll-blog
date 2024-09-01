---
layout: post
title: Compute-Efficient Frontier, the limits of current generation LLMs and is that really a bad thing?
date: 2024-08-27
categories: [AI, Research, Development, Scalability, Future Trends, Internet of Things, Spatial Computing]
---

![https://github.com/dr-robert-li/jekyll-blog/blob/main/images/sad-investor-hdr.jpeg](https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/sad-investor-hdr.jpeg)

Recently private investment in AI technologies and companies has hit a bit of a snag. This can largely be attributed to unmet expectations from private investors and has led to a wholesale reassessment of their potential (many "I told you so's" and "I saw this coming's" pundits are having their 15 minutes of fame).

But it's crucial to recognize that this slowdown is not indicative of a failure in AI and generative AI itself. Instead we're simply going through a commonly observed pattern in the adoption of paradigm-shifting technologies. Initial hubris often gives way to a period of disillusionment before more realistic, sustainable progress resumes.

## We are heading into the Trough of Disillusionment

For those of you unfamiliar, Gartner's Hype Cycle describes the normal progression of adoption of new technologies in five phases:

![](https://media.licdn.com/dms/image/D5612AQEGbAWj-dTgVg/article-cover_image-shrink_720_1280/0/1718762258257?e=2147483647&v=beta&t=u_c3mmUQEY0jStKmOgJjrBq9wDRfjhBdPhMGYivNaXI)

* Innovation Trigger: A breakthrough or a new technology generates initial excitement and attracts attention.
* Peak of Inflated Expectations: Early success stories and media attention lead to overhyped expectations. During this phase, investments soar as businesses and investors anticipate rapid, transformative changes.
* Trough of Disillusionment: Reality sets in as the technology fails to meet the exaggerated expectations. Investment slows, and some projects may be abandoned as they struggle to deliver immediate returns.
* Slope of Enlightenment: As the technology matures, its real capabilities and limitations become clearer. Practical applications emerge, and adoption increases steadily.
* Plateau of Productivity: The technology achieves mainstream adoption and starts delivering tangible benefits at scale.

Where AI investors are at right now is tumbling down the very steep slope after hype enticed them to the top of the Peak of Inflated Expectations to the Trough of Disillusionment. 

During the peak, the excitement around AI, especially generative AI, led to massive investments with the expectation that these technologies would quickly revolutionize industries and disrupt whole parts of our lives. This might still come to pass in time, however, as current technologies have taken a lot more effort to implement, have experienced resistance to adoption, and produced lower than expected returns, that initial enthusiasm has cooled.

However, this view overlooks the fact that AI development has always been characterized by cycles of rapid progress followed by periods of adjustment where research is slower.

Historically, AI research has experienced several "AI winters/ice ages" where progress slowed due to overpromised results and underdelivered outcomes. Each time, the field eventually rebounded, often with new approaches and technologies that laid the groundwork for future breakthroughs. 

In fact, transformer architecture was the underlying technological shift that catapulted the current class of LLMs out of the previous AI winter.

Now that I've primed you, the reader, let me introduce you to a paper that I recently got around to reading (alas, it's not new) from John's Hopkins and OpenAI and released pre-ChatGPT in January 2020. 

## The Compute-Efficient Frontier Reality Check

*[Scaling Laws for Neural Language Models](https://arxiv.org/pdf/2001.08361)* by Kaplan, McCandlish et. al. was a seminal paper at the time, but as we reach the threshold of all the data on the Internet being consumed (for further reading: [The Looming Crisis of AI Training Data and the Spectre of Model Collapse. What can we do about it?](https://drli.blog/posts/ai-training-data-model-collapse/)) it bears revisiting.

![](https://miro.medium.com/v2/resize:fit:1400/1*jpJpml0yk4AitDBIcCCwag.png)

Briefly, it investigates the empirical scaling laws for LLM performance, using cross-entropy loss to measure accuracy (one *could* argue this is an imperfect measure) and found that models followed a predictable power-law trend across several factors: model size, dataset size, and the amount of compute used for training. Significant that these trends were mirrored over seven orders of magnitude, showing that larger models, proportionally large training data and compute, significantly improved performance and efficiency (i.e. fewer shots were required for the same output quality). This is the ***Compute-Efficient Frontier***. Additionally, the paper discusses the minimal effects of architectural details such as network width or depth within a certain range, emphasizing that scaling the three key factors—model size, dataset size, and compute—simultaneously is crucial for optimal performance. 

One way to read this is that you could, in theory, scale model sizes predictably forever as long as there is enough data and compute, and it's an interpretation that many have taken and run with (it's what Ilya Sutskever and OpenAI had the funding and, let's be honest, *brass balls*, to do).

But we are human and the resources within our grasp right now are finite. And so, another way to interpret the Compute-Efficient Frontier is that there will be a point, and, arguably, we are nearing it, where, because we haven't and aren't able to build anything more meaningful than elaborate chatbots (even GraphRAG is a bit of this, I have to admit, as compelling in performance as it is), the value of these incremental improvements, as frontier-breaking as they are for research and development, are not worth the time, energy nor cost (until we can figure out a better way of using them - or more dramatic and disruptive use cases emerge). That there is a practical limit to what can be achieved by simply scaling up current architectures and beyond this point, further improvements in model fidelity or performance would require novel architectures or techniques, rather than merely increasing scale.

Hm. Sounds sobering.

## It's not sexy, but it's got teeth

However, as a Solutions Architect myself, I've always been more comfortable with defined constraints than unbounded potential. Not only is it the mother of invention, but it also sets the correct expectations for what can be achieved with what we have, and might get.

Current-generation LLMs are well-suited for tasks that require processing and generating human-like text, but the diminishing returns of scaling suggest that they might not yet be ready to revolutionize human interaction with technology on their own. 

We've already seen use cases where they can enhance existing systems incrementally by improving natural language understanding, customer support, and automating routine communication tasks.

But, in the context of emerging computing paradigms, unbounded by screens, such as spatial computing and IoT, LLMs could potentially play a more significant role in measurably improving quality of life. 

For instance, there are early examples of LLMs being integrated into smart devices and environments to interpret user commands, provide contextual information, and automate tasks based on natural language input (although, like the Rabbit R1 or the Humane Pin, these are still not yet ready for general use, and arguably decrease a user's quality of life right now).

![](https://global.discourse-cdn.com/openai1/original/4X/7/1/1/711acdef4b262a57b8769c86fd8d43e866444224.jpeg)

LLMs could also enhance spatial computing systems by providing contextual awareness through natural language processing. For example, by interpreting user commands or questions in real-time, adjusting the environment or providing relevant information based on the user's location, preferences, previous interactions, or what might be happening in the vicinity with instructions for reacting to them. It would be the cybernetic human made real (for reading on where this reference comes from, see my own work in [Reconceptualizing MMORPG Play - A Study On Actor-Network Theory In Practice](https://www.academia.edu/43769178/Reconceptualizing_MMORPG_Play_A_Study_On_Actor_Network_Theory_In_Practice)) and it would forever change the way we perceive reality.

Finally, for agentic AI, which is already emerging as a new method in AI engineering for enabling AI to solve more complex tasks, it can be reasonably assumed that it's only a matter of time before IoT ecosystems are also being operated by agentic AI, not only translating user intents into actions that can be understood and executed by various devices in the network, but also facilitating interoperability between devices themselves. When taken to it's Nth degree these are the baby steps that lead to smart homes, then smart neighbourhoods and finally smart cities.

## Enjoy the ride. We're all in this together.

When you take AI efforts grounded in reality to their logical conclusions, they still lead to profound changes in human computer interaction. There is no need to worry about fantastical end-games such as AGI, singularities or the end of humanity. As engineers, and architects, there is still a great amount of real-world value can still be reaped by understanding the current limitations of LLMs and practically applying them to real-world problems.

We can leave the research to the researchers.

It's worth remembering that since the Dartmouth Workshop in 1956, AI research has been characterized by a cycles of "ice ages" sandwiched between "golden ages" with several "winters" in the middle. A rollercoaster of sorts owing to the fact that AI research frequently hit the economic and technological limits of their times.

The first ice age was primarily driven by the gap between high expectations and the actual capabilities of AI technologies at the time. It followed a boom in investment in the 1960s and early 70s when there was significant optimism about the potential of AI, fueled by early successes in areas like problem-solving and symbolic reasoning. However, several factors contributed to the decline:

* Technical Limitations: Early AI systems were limited by the computational power available at the time and the complexity of real-world problems.
* Funding Cuts: As AI projects failed to deliver on their promises, funding agencies, particularly in the United States and the United Kingdom, began to reduce their support. 
* Economic Factors: The oil crisis and global recession during the 1970s led to global cuts in speculative research areas of which AI was one.

![](https://museum.ipsj.or.jp/computer/other/images/0008_01_l.jpg)

The second ice age happened in the late 1980s and was capped off by the dotcom bubble bursting in 2000.

* Commercial Failures: Many AI companies, particularly those involved in expert systems and Lisp machines, faced commercial failures after failing to deliver on the marketing hype. Many expert systems, which were rules-based, were abandoned due to maintenance difficulties and limits with which you can really scale such a system.
* Failure of Lisp Machines: Lisp machines, which were specialized computers for running AI applications, but became obsolete with the rise of general-purpose computers (which eventually did fulfil the goal of the Japanese project of fifth generation computing, although it failed at this time).
* Reduced Funding: Funding was again cut, this time by the US government, which had been a major source of funding for AI research.

Several other spasms included:

* 1969: Criticism of Perceptrons: Marvin Minsky and Seymour Papert published a book criticizing perceptrons, an early form of neural networks, for their inability to solve certain types of problems. This led to a decline in neural network research until the mid-1980s.
* 1971-75: Speech Understanding Research: The DARPA-funded Speech Understanding Research program aimed to develop systems that could understand spoken language. However, the project faced numerous technical challenges and was eventually deemed a failure.
* 1973: Lighthill Report: This report, commissioned by the British government, criticized the progress and potential of AI research. It led to a major and permanent reduction in funding, and the UK no longer being a peer to the US in research.
* 1988: Strategic Computing Initiative: The U.S. Department of Defense's Strategic Computing Initiative, which had been a significant source of funding for AI research, reduced its spending on AI projects due to unmet expectations.

## Waiting for the One

While the development of AGI or Artificial General Intelligence within my lifetime is a distinct possibility, it is important to recognize that this will emerge from deep, fundamental research - perhaps at the end of another "AI Winter", not from the efforts to implement and commercial the current generation of AI.

And, AGI, should it ever be realized, may not immediately have commercial applications. It's nature could be so different from our current understanding of intelligence that it might not behave in ways we can easily comprehend. The anthropomorphization of AI—projecting human traits onto machines—can lead to misguided expectations and fears. An AGI might exhibit forms of intelligence that do not align with human notions of consciousness or self-awareness.

Finally, if an AGI were to emerge, its impact on society, economy, and even its very announcement would probably be governed by its own understanding and objectives, which could be vastly different from what we might comprehend. 

![](https://global.discourse-cdn.com/openai1/optimized/4X/f/f/1/ff1e39451197c7850794bab266bbb9b613ed731e_2_500x500.jpeg)

So, if we don't know that we'd recognize it's emergence, is it worth worrying about just yet?

## What now?

In the end, the current stall in AI investment is a typical and expected phase in the technology adoption cycle. It is a necessary and welcomed (from my perspective as an engineer and technologist) recalibration of expectations after a period of overhype. 

What this means is that rather than seeing this as a failure of generative AI or AI research in general, we should be viewing this as an opportunity to focus on realistic, practical applications that can deliver real-world value today. Understanding the efficient computing frontier and the limitations of current LLMs will be crucial in driving meaningful progress in AI, without succumbing to the worries that come from thinking about speculative end-states.

So, what now? Get building!
