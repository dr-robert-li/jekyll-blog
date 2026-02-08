## Section 4 Amendment (drop-in text)

**Instruction:** Insert the following subsection into Section 4 (Cognitive Adaptation) immediately after the paragraph that introduces the “cognitive paradox / cognitive offloading” idea, while keeping the rest of Section 4 unchanged.

---

### Evidence from software engineering: cognition shifts from design to verification

This cognitive reconfiguration is already observable in modern software engineering workflows, where generative AI shifts effort away from up-front design/architecture and toward *verification*, integration, and constraint management (reviewing generated code, debugging, testing, and preventing uncontrolled feature sprawl). A randomized controlled trial by METR studying experienced open-source developers working on tasks in their own repositories found that allowing AI tools **increased completion time by 19%**, despite developers believing they were faster; the reported gap highlights how AI can introduce substantial overhead in prompt iteration, integration, and review, as well as miscalibrated confidence about actual productivity.[^121][^122]

A systematic literature review synthesizing **37 peer-reviewed studies (2014–2024)** on LLM assistants and developer productivity concludes that while LLM tools can reduce task initiation overhead and accelerate some code-adjacent tasks, the literature repeatedly reports risks consistent with “effort transplant”: cognitive offloading, disrupted flow, and inconsistent effects on code quality and maintainability (which then pushes effort downstream into review, repair, and governance rather than up-front planning).[^115][^137]

Security evidence points in the same direction: Perry et al. conducted a large-scale user study (“Do Users Write More Insecure Code with AI Assistants?”) and found that participants with access to an AI assistant wrote **significantly less secure code** than those without, while also being more likely to believe they had written secure code—an overconfidence dynamic that increases the need for disciplined review and security gates.[^145][^146][^147]

Finally, large-scale engineering telemetry is consistent with feature sprawl and downstream cognitive burden. GitClear analyzed ~**153 million changed lines of code** across four years (2020–2023) and reported rising code churn (lines reverted or updated within two weeks) projected to double compared to the pre-AI baseline, along with increasing “added” and “copy/pasted” code and declining “moved” (refactoring/reuse) code—patterns aligned with faster scaffolding, more duplication, and a larger long-term review/maintenance load.[^132][^142]

**Implication for the broader thesis:** as agentic systems and AI coding tools expand “local software creation capacity,” the individual’s role shifts from careful construction to *governed orchestration*—allocating attention to verification, narrowing scope, and preventing accidental complexity. The core competency becomes disciplined constraint-setting (security boundaries, architectural invariants, test coverage, performance budgets, dependency control) so that speed does not collapse into brittleness, vulnerability, and unmaintainable feature sprawl.[^145][^132][^115]

---

## Optional: one-sentence bridge back to the original Agentic Web Evolution thesis

If you want a tight connective sentence to the original thesis (place immediately after the subsection above):

> In the agentic web stack described in the original article (semantic data substrate → agent transport → model inference → conversational delivery), software engineering becomes the earliest “microcosm” of the broader transition: humans increasingly specify intent and constraints while machines generate the intermediate artifacts—forcing the human cognitive burden to concentrate in verification, governance, and coordination rather than direct construction.[^1][^115][^121]


---

## References

1. [interests.writing_blog](interests.writing_blog) - The user publishes essays on AI, societal implications, and technological evolution—including a June...

115. [The Impact of LLM-Assistants on Software Developer ...](https://arxiv.org/html/2507.03156v1) - In this paper, we present a systematic literature review of 37 peer-reviewed studies published betwe...

121. [Measuring the Impact of Early-2025 AI on Experienced ...](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) - We conduct a randomized controlled trial (RCT) to understand how early-2025 AI tools affect the prod...

122. [[2507.09089] Measuring the Impact of Early-2025 AI on ...](https://arxiv.org/abs/2507.09089) - by J Becker · 2025 · Cited by 70 — Surprisingly, we find that allowing AI actually increases complet...

132. [Coding on Copilot: 2023 Data Suggests Downward ... - GitClear](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality)

137. [The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Literature Review](https://arxiv.org/pdf/2507.03156.pdf)

142. [Coding on Copilot: 2023 Data Shows Downward Pressure on Code ...](https://jeremypeckham.com/wp-content/uploads/2024/03/Coding-on-Copilot-2024-Developer-Research.pdf)

145. [Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622) - by N Perry · 2022 · Cited by 379 — We find that participants who had access to an AI assistant based...

146. [Do Users Write More Insecure Code with AI Assistants?](https://dl.acm.org/doi/abs/10.1145/3576915.3623157) - by N Perry · 2023 · Cited by 379 — Overall, we find that participants who had access to an AI assist...

147. [Do Users Write More Insecure Code with AI Assistants?](https://www.veracode.com/wp-content/uploads/2024/07/2211.03622v3.pdf) - by N Perry · 2023 · Cited by 371 — In this paper, we conduct a user study to examine how users inter...

