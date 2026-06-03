---
layout: post
title: "GTM Is a Systems Problem Now: What 'Engineering' Actually Means in GTM Engineering"
date: 2026-06-01
categories: [GTM Engineering, Revenue Operations, Enterprise AI, B2B SaaS, Sales Strategy, AI Agents, Systems Design, Marketing Technology, Top of Funnel, Go-to-Market]
---

![Example of n8n](https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/n8n-example.jpeg)


---

### ***TL;DR***

* *The word "engineering" in "GTM engineering" marks a shift from a craft run on instinct to a discipline with architecture, data pipelines, feedback loops, and observable outputs.*

* *ICONIQ's 2026 data shows high AI adopters run roughly 24% leaner go-to-market headcount at the same revenue scale (ICONIQ, 2026).*

* *The top of the funnel concentrates the hardest problems — the messiest data, the least technical people, and the weakest governance — which is exactly why AI both helps most and amplifies mistakes fastest there.*

* *AI is a volume and qualification multiplier, not a closing accelerant. The ICONIQ funnel data shows large AI lift top of funnel (lead-to-MQL, MQL-to-SQL) and almost none at point of sale. Human relational sales persists at the bottom because that is where trust currently sits (ICONIQ, 2026; Dorfman, 2026).*

* *The martech explosion produced a decade of fragmentation. The AI tooling explosion looks similar, with one structural difference: frontier models are generalizable and can be designed to replace most point solutions.*

* *The companies building durable leverage are not the ones with the most tools. They are the ones with the cleanest data foundations and the governance maturity to deploy AI at top-of-funnel speed without amplifying bad decisions at the same rate.*

---

The word "engineering" did something to "go-to-market." Two years ago, revenue leaders talked about plays, motions, and quota coverage. Today a growing number of them talk about pipelines, signal routing, and observability. Clay coined "GTM engineer" in 2023, and the role has since spread to high-growth software companies including Cursor, Lovable, and Webflow (Clay, 2025) and reflects a structural change in where go-to-market leverage comes from.

GTM's new competitive moat is not headcount, channel mix, or even product quality on its own. It is the quality of the systems underneath the motion: data architecture, signal routing, workflow orchestration, and the ability to compound improvements over time. ICONIQ's 2026 research makes the point bluntly. High AI adopters in go-to-market run about 24% leaner headcount at the same revenue scale and hit materially higher quota attainment, with adopter teams reaching 67% average AE attainment versus 59% (ICONIQ, 2026). So what does "engineering" actually mean in this context, and why did go-to-market need it now?

## Why "Engineering" 

Traditional go-to-market thinking is linear and sequential: market, prospect, pitch, close, renew. Engineering thinking is recursive. It asks about inputs, outputs, feedback loops, failure modes, observability, and graceful degradation. When you apply that type of system design lens, different questions surface. Instead of asking "how many calls should our AEs make?" or "how do we build a better proposal deck?", you need to ask questions like "what is the signal-to-noise ratio in our inbound flow, and what is the latency between a signal arriving and an action firing?" or "what does the system need to know to route this prospect to the right motion at the right moment?"

Data architecture therefore becomes foundational here. Clay's framework for GTM engineering describes three progressive rungs — data foundation, data modelling, data activation — and you and I already know that the first rung is often the hardest to climb (Clay, 2025). The similarities to software are self evident: a corrupted state cannot support a reliable outcome.

There is a velocity argument underneath all of this. AI collapsed the gap between idea and execution from months to hours. What took a developer and a data team two years ago is now an afternoon's work. The value of a well-designed system therefore compounds faster than it ever has and that means the cost of a badly designed one amplifies faster too. That is why "engineering" concepts are required. The discipline of building reversible, testable, observable systems, with explicit failure modes and governance constraints, now also applies directly to revenue workflows. The people doing this work need to think like engineers, not only operators.

And here we expose a talent paradox. The people who understand sales and marketing motions deeply are rarely also competent engineers, and the people trained as engineers often find go-to-market motions, culture, and practices incredibly uncomfortable. Engineers are taught to advocate for minimal, elegant solutions. Go-to-market teams tend toward data maximalism — more signals, sprawling toolsets, attempts to personalize at speed and at scale. 

It is the inherent difficulty of aligning messy and human ways of working with systematic, procedural and programmatic system design. Right now, I am yet to see that friction be solved widely. 

## The Martech Parallel

We have seen the explosion in tooling before. The 2024 Marketing Technology Landscape counted 14,106 distinct martech products, and a 28% increase year over year (Brinker, 2024). At its peak, the martech explosion mirrored the current AI tooling explosion almost exactly: thousands of point solutions, each solving one narrow problem, almost none integrating cleanly, and a CMO or CIO making increasingly arbitrary stack decisions.

The early martech era had a characteristic failure mode. Integration cost consumed return. Companies spent more time connecting tools and trying to rationalize their outputs, than the tools saved. The combinatorial explosion of API dependencies made stacks brittle, data lived in dozens of silos, and "single source of truth" became a recurring board slide that never quite resolved.

The AI-native era differs in one structural way. The generalisation capability of frontier language models has the potential to remove most of the glue-code problem. If a task involves connecting data and generating synthesised output, or simple routing and execution, there is little point acquiring a dedicated tool — that is precisely what current AI systems do. The rational threshold for additional point-solutions has narrowed sharply.

I therefore, propose the following principle: the only go-to-market tool worth adding to a stack in 2026 are ones required by policy, compliance, or governance constraints; or the gap between a frontier model's capability, tool use and its harness for a specific use case is large enough that a purpose-built solution meaningfully outperforms. Everything else is a 2022 point solution with a shiny sticker stating "AI" or "agentic" pasted onto it. 

## Reminder of the Solow Paradox

There is a recurring objection at this point: if AI is so transformative, where is the step change in ROI? Leaders deploy dozens of AI tools and the productivity stubbornly refuses to arrive. This happened last time AI reached commercial relevance with LISP machines in the 1980s and 1990s before the most recent AI ice age. In 1987 Robert Solow observed that "you can see the computer age everywhere but in the productivity statistics" (Solow, 1987). 

The cause was organisational, not technical. Brynjolfsson and colleagues later formalised this as the productivity J-curve: general-purpose technologies depress measured productivity before they lift it, because the gains require large, unmeasured investments in intangible capital: new processes, new workflows, new ways of organising work that take time to build (Brynjolfsson, Rock, & Syverson, 2021). The technology is only the first and fastest moving part of that equation. Firms that bolted computers onto existing paper-era processes saw no positive gains. Firms that redesigned the work around computers saw them, eventually.

Sounds familiar? Because we're seeing this in the current iteration of AI adoption and the thousands of point solutions that have popped up. Each point solution, by design, accelerates an existing way of working. It makes the current step faster, cheaper, or slightly better, but the surrounding process untouched and it inherits all of that world's structural constraints. You get a local optimization and no change in the aggregate, hence the Solow paradox.

The step change comes only when the business is organized around AI rather than having AI grafted onto it. That means changing the ways of working themselves: who does what, where decisions sit, how data flows, what the human is for. It is the difference between hiring an SDR a faster dialler and rebuilding the top of the funnel so that qualification, routing, and enrichment are AI-native by default and the human only enters where oversight requires it, or it's where ownership of trust is required. Only the second escapes the paradox.

Secondly, and more broadly humanity is reliably slow to trust any new technology, and AI hands the sceptics plenty of ammunition — hallucinations, baked-in biases, guardrails that break under pressure, and plenty of instances of oppositional messaging. It does not help that the frontier is ruled by a handful of opaque, polarizing, and heavily financialised labs, a structure partly forced by market dynamics: input costs have climbed so high that staying at the frontier means absorbing a huge share of the world's available capital. 

Trust in the technology arrives only when two things become widespread — robust methods for guarding against these limitations, and enough literacy among users to recognize the limitations in the first place. Both necessarily lag the adoption curve. People adopt before the safeguards and the skills exist, because safeguards and skills are forged during the act of adoption when it is realised they are necessary. That is why laggards exist. They are not irrational; they are waiting for normalisation (if it ever arrives). And whether it arrives matters far beyond any single company's ROI. The last time AI reached commercial relevance it collapsed into an ice age. Building the guards and the literacy fast enough to outrun disillusionment is what will prevent the regression this time around. And so it becomes an imperative of all practitioners including GTM Engineers to recognize these responsibilities.

That responsibility has to land somewhere concrete. If escaping the paradox means reorganising the business around AI, and doing it under a trust constraint that is still being earned, then where does a GTM Engineer begin?

## The Top of the Funnel Is the Hard Problem

The top of the funnel concentrates all the hardest problems at once, and it does so along three axes.

**The data problem.** Top-of-funnel data is the least structured, most heterogeneous, and most rapidly decaying data in any go-to-market system. It spans firmographic enrichment (often contradictory across vendors), third-party intent signals (often noisy), first-party behavioural signals (often thin in APAC where the TAM is small), and unstructured signals from sales conversations (often unrecorded and unlabelled). The ICONIQ study confirms companies with more than half of pipeline influenced by AI show an 11-percentage-point improvement in lead-to-MQL conversion. But this only applies if the underlying data is clean enough to reliably use (ICONIQ, 2026). Garbage in, amplified out.

**The skills mismatch.** Top-of-funnel professionals — SDRs, BDRs, sales execs — are typically among the least technical people in any revenue organisation. RevOps, sitting adjacent, is usually operational rather than engineering-minded. Martech teams, where they exist, are often siloed from sales and often optimise for marketing metrics rather than pipeline quality (the core of most marketing/sales disagreements). Finding someone who can design the system *and* understands the commercial dynamics of top-of-funnel selling is genuinely rare.

**The governance vacuum.** Revenue teams are, statistically, among the least likely functions to observe data governance, privacy, and risk frameworks. The prevailing instinct is to collect everything, enrich everything, personalise everything. That instinct runs against how engineers approach system design, and it creates a field that technically disciplined leaders are often reluctant to enter.

AI is exceptionally well suited to the top-of-funnel problem. It tolerates messy, heterogeneous inputs, synthesises across sources no human would have the bandwidth to reconcile, and operates at scale. Across the strategic segment, ICONIQ reports cost per lead falling year over year from roughly $1,300 to $800 and cost per opportunity from about $15,900 to $11,200. This gain scales with how mature an AI-assisted motion is (ICONIQ, 2026). 

Acceleration cuts both ways, though, and this is where it pays to think of AI systems not as magic black boxes, but just like any other system or tool. AI amplifies poor decisions faster and at greater scale. A poorly designed routing workflow can misdirects thousands of leads before anyone notices. A badly calibrated lead score can cut out entire ICP segments. Integrated speed pointed in the wrong direction is worse than no integration at all, and it's why undirected adoption is leading to no movement in ROI because there are as many pointed in the wrong direction as the right one.

This is why architectural judgement, not raw technical execution, is so important right now. The question is rarely "can AI do this?" It almost always can. The real question is "should it, and if yes, how should it, under what evaluation criteria, under what governance constraints, and with what observability?"

### The funnel asymmetry: why humans persist at the bottom

As complexity and deal size grow, AI's role shifts from primary actor to supporting infrastructure. While AI influence improves new-lead-to-MQL by 11 points and MQL-to-SQL by 8 points, it only SQL-to-closed-won by only 1 point (ICONIQ, 2026). Right now it is a volume and qualification multiplier. It doesn't help in closing.

Anthropic's own deployment mirrors this shape. After demand surged following the launch of Claude Opus 4.6 in February 2026, CRO Eleanor Dorfman's team built an AI-native sales organisation in which enterprise self-service accounted for 54% of new enterprise logos in 2026 — a company-reported figure shared at SaaStr AI 2026 — while human AEs continued to run the complex, high-touch deal cycles at the bottom of the funnel (Dorfman, 2026; SaaStr, 2026). Claude handled enrichment, routing, call coaching, proposal generation, and forecasting. Humans continued to handle trust, negotiation, and relationship building.

Why this division of labour? Dorfman said enterprise buyers do not yet trust autonomous agents to make decisions that carry organisational risk. So, relational selling at the bottom of the funnel is a rational response to where trust currently sits. The boundary will move, eventually, but trust needs to first.

## What Frontier GTM Engineering Actually Looks Like

I've seen the Winning by Design maturity model floating around LinkedIn and X/Twitter by this point. It describes four states — Assistive, then Agentic, then Orchestrative, then Autonomous — across dimensions of data architecture, workflow, and decision science (Winning by Design, 2025). The trap is to read the four states as evenly spaced. They are not. The jump from State 1 to State 3 is largely a workflow and integration problem. The jump from State 3 to State 4 is a different discipline altogether.

By State 4, the hard problems are no longer go-to-market problems wearing an engineering costume. They are actual engineering problems:

1. **Multi-agent orchestration.** Designing systems where multiple agents handle distinct steps, pass state cleanly, and degrade gracefully when one fails. This draws directly on agent-computer interface design, tool documentation standards, and failure-mode design — the orchestrator-workers pattern and related principles in Anthropic's guidance on building effective agents (Schluntz & Zhang, 2024).
2. **Observability and evals.** Knowing whether an agentic system performs correctly while it runs at high volume and low human oversight. That means building evaluation frameworks, defining success criteria in advance, and instrumenting for ground-truth feedback. Agents still have issues handling long context horizon, multi-turn workflows leading to low rates of success and token burning.
3. **Governance and trust architecture.** At State 4 the system modifies its own behaviour as new data arrives (this used to be the red line of RSI), which demands explicit human-in-the-loop checkpoints, rollback mechanisms, and audit trails. None of this has ever been done before for revenue teams, but all of which enterprise customers increasingly require.
4. **Context management at scale.** Frontier models inside multi-agent systems need carefully designed context windows, memory architectures, and tool interfaces. Anthropic frames the agent-computer interface investment as the equivalent of the human-computer interface investment made for human-facing software (Schluntz & Zhang, 2024), in other words, equivalent to software engineering now.

While agentic mesh architectures may become the norm in the future, is this all actually necessary to have a functioning AI assisted GTM org right now?

The most instructive live example of what "good" looks like today is Anthropic's own build. Dorfman's team did not build a bespoke platform. They worked from existing tools — Salesforce, Jira, Slack, Gong, Ironclad, Clay — and used Claude as the connective tissue between them (Dorfman, 2026). In that system Claude enriches and routes every lead before human touch, generates morning briefings that prioritise each AE's day, drafts proposals within policy guardrails rather than freestyle, runs forecasts that managers inspect rather than originate, and surfaces a handful of coaching moments per rep each week. Best practices from top reps are encoded as reusable Skills — executable workflows any rep can invoke, not documentation that sits unread.

Claude became a powerful integration and assistive layer. The tools have not changed. The logic connecting them did. 

## Where the ROI Is: Start at the Top

The temptation is to start where the tools are most mature — call intelligence, proposal generation, contract management. Those sit mid-to-late funnel and look attractive because the data is cleaner and the workflows more constrained. The stronger case is to start at the top of the funnel, for four reasons.

1. **Widest aperture, biggest leverage.** Almost every downstream inefficiency traces back to an upstream data or qualification problem. Fixing ICP scoring, enrichment quality, and signal routing multiplies through every stage below it.
2. **Lowest trust barrier.** A misdirected cold sequence is recoverable. A misdirected contract workflow is not. The top of the funnel lets teams build competence in agentic system design where failure is cheap and iteration is fast.
3. **Fastest time to measurable signal.** ICONIQ's funnel data shows the largest year-over-year improvement anywhere in the B2B funnel was Free Trial/POC-to-Paid, up 14 points to 50%, driven partly by AI-qualified pipeline arriving at those trials with better fit (ICONIQ, 2026). The upstream investment pays out downstream.
4. **The data-foundation principle.** Clay's three-rung model is right: the data spine must hold before anything compounds (Clay, 2025). Top-of-funnel engineering is largely data-foundation work — the least exciting and the most consequential.

We usually advocate the work starts with a foundational choice: the AI operating system the stack will run on. The options fall into three camps — a proprietary platform, one of the frontier ecosystems (OpenAI, Anthropic, or Google), or a DIY build on Google Vertex, AWS Bedrock, or open-source models. That decision determines what you no longer need to buy. The mid-to-late-funnel capabilities this section opened with — call intelligence, proposal generation, and the broader class of aggregating and synthesising activities — can likely be absorbed by the AI OS of choice rather than procured as separate point solutions, with more capable platforms absorbing more of that workload.

The constraint continues to be, though, that this work is hard to buy off the shelf. It needs someone who understands the commercial dynamics well enough to know which signal matters, is technically capable enough to design the system correctly, and is disciplined enough to resist the maximalism instinct. That combination is rare, which is exactly why getting it right pays so asymmetrically.

## The Discipline Is Young, the Stakes Are Not

GTM engineering is not a tool category or a job title. It is a way of thinking about commercial systems with the rigour, testability, and long-horizon architecture that "engineering" implies. The martech explosion produced a decade of fragmentation and integration debt that enterprise teams are still unwinding. The AI tooling explosion of 2023 through 2026 is following a suspiciously similar pattern, but this time the consolidation mechanism *is AI itself*. Frontier models are general enough to replace most point solutions when the underlying system is designed well enough to use them.

The companies building durable leverage right now are not the ones with the most tools. They are the ones with the cleanest data foundations, the most disciplined signal-to-action architecture, and the governance maturity to deploy AI at top-of-funnel speed without amplifying bad decisions at the same rate. 

---

## References

Brinker, S. (2024, May). 2024 marketing technology landscape supergraphic: 14,106 martech products, 28% growth. *Chief Martec*. https://chiefmartec.com/2024/05/2024-marketing-technology-landscape-supergraphic/

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics*, 13(1), 333–372. https://doi.org/10.1257/mac.20180386

Clay. (2025). *The GTM engineering guide: Building the modern go-to-market data stack*. Clay. https://www.clay.com/blog/gtm-engineering

Dorfman, E. (2026). *How Anthropic's head of industries built an AI-native sales org from scratch* [Talk transcript]. Otter.ai. https://otter.ai/u/jvoLU-X6yu-TKtlWUi-8H2qgAP8?view=summary

ICONIQ. (2026). *The state of GTM in 2026*. ICONIQ Analytics. https://cdn.prod.website-files.com/65d0d38fc4ec8ce8a8921654/69c36701128b86b93599945d_ICONIQ_Analytics%20_The_State_of_GTM_in_2026.pdf

SaaStr. (2026). *How Anthropic rebuilt its sales org from scratch when demand went vertical: 54% of new enterprise logos now come self-serve*. SaaStr. https://www.saastr.com/how-anthropic-rebuilt-its-sales-org-from-scratch-when-demand-went-vertical-54-of-new-enterprise-logos-now-come-self-serve/

Schluntz, E., & Zhang, B. (2024, December 19). Building effective agents. *Anthropic Research*. https://www.anthropic.com/research/building-effective-agents

Solow, R. M. (1987, July 12). We'd better watch out. *The New York Times Book Review*, p. 36.

Winning by Design. (2025). *GTM AI archetypes: From assistive to autonomous*. Winning by Design. https://winningbydesign.com/resources/blueprints/gtm-ai-archetypes/
