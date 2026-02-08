# The Agentic Disaggregation: A Research Brief for Follow-Up to "The Evolution of Human-Internet Interaction"

---

## Preamble: Connecting to the Original Thesis

The original article, *The Evolution of Human-Internet Interaction* (June 2025), established a core thesis: we are witnessing a fundamental shift from browser-based internet use to AI agent-mediated digital interaction, creating a "New Information Architecture" where information is stored in semantic databases, transported via AI agents, and delivered through conversation rather than traditional websites[^1]. The article traced the arc from ARPANET's document-centric model through the browser era, the app era, and voice/ambient computing, arriving at a post-browser world where AI agents handle our information needs invisibly.

Eight months later, the thesis has not only held—it has accelerated beyond most predictions. On February 3, 2026, Anthropic announced a single AI-powered legal plugin for Claude Cowork. Within hours, $285 billion in market value evaporated across the software sector. Traders called it the "SaaSpocalypse"[^95]. Software stocks have lost over $1 trillion in 2026, dropping approximately 20%[^35][^92]. Forbes declared: "Intelligence becomes mobile, data becomes interpretable, and workflows become replicable. Software is increasingly viewed as a vessel, with intelligence emerging as the actual product"[^92].

This is the landscape against which the three hypotheses should be evaluated. What follows is an exhaustive research brief organized by near-term (2025–2027), mid-term (2027–2030), and long-term (2030–2035) horizons across each hypothesis, culminating in a fourth section on cognitive adaptation and macro-evolutionary trajectory.

---

## Hypothesis 1: Software Disaggregation — From Monolithic Platforms to Personal Micro-Applications Over Shared Semantic Data

### The Core Claim

Software functionality is being drawn inward to individual users and teams, disaggregated from large enterprise platforms (ERPs, CRMs), and reconstituted as small, personalized, disposable, self-made applications. The enduring substrate is not the application layer but the data layer—data lakes, warehouses, and semantic databases—which is what all SaaS platforms ultimately reduce to.

### The Nadella Doctrine

Microsoft CEO Satya Nadella articulated this most bluntly in December 2024: "The notion that business applications exist—that's probably where they'll all collapse, right, in the agent era. They are essentially CRUD databases with business logic. The business logic is all going to these agents, and these agents are going to be multi-repo CRUD. They're going to update multiple databases, and all the logic will be in the AI tier"[^66][^67][^72]. Bill McDermott, CEO of ServiceNow, echoed this at Knowledge 25: "In the era of agentic AI, a traditional application stack will collapse. The number of apps that customers use will be greatly reduced, and traditional applications will become databases"[^70].

This is not speculative positioning. It is the stated strategic direction of two of the world's largest enterprise software companies.

### Near-Term (2025–2027): The Unbundling Begins

**Evidence of disaggregation in progress:**

- Gartner predicts 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from less than 5% in 2025[^68].
- Deloitte's 2025 Tech Value survey found 57% of respondents were putting 21–50% of annual digital transformation budgets into AI automation, with 20% investing over 50%[^23]. Deloitte predicts up to half of organizations will exceed 50% AI automation budgets in 2026[^23].
- Bain identifies five strategic scenarios for SaaS workflows: AI enhances SaaS, spending compresses, AI outshines SaaS, and AI cannibalizes SaaS—with "easier" business processes like customer service being disrupted first[^17].
- SaaS annual recurring revenue dropped 29%; growth forecasts revised downward from 14% to 10.5%[^101]. Seat-based pricing dropped from 21% to 15% of SaaS companies in 12 months, while hybrid pricing models surged from 27% to 41%[^68].

**The rise of vibe coding and disposable software:**

"Vibe coding"—the practice of prompting AI tools to generate working software from natural language—has made disposable micro-applications a reality. Tools like Bolt.new and Cursor enable anyone to spin up custom micro-apps in minutes[^40][^43]. In 2021, an MVP took three months and cost $50,000. In 2026, you can build and deploy a SaaS over a weekend[^46]. Bain Capital Ventures describes these micro-apps as filling "the gap between the spreadsheet and a full-fledged product"[^43]. Users create restaurant-picking apps, health symptom trackers, holiday family games, and podcast translation tools—applications that "disappear when the need is no longer present"[^43].

**But ERPs are being wrapped, not dismantled:**

McKinsey's January 2026 analysis is clear: "While it is unlikely that AI agents will replace the ERP in the near or medium term because of system complexity, companies should consider not only how AI agents will disrupt ERP operations but also how they provide a powerful capability for evolving and modernizing ERP itself"[^37]. The recommended approach is embedding agentic capabilities inside workflows—placing AI directly inside the steps where work gets done (approvals, planning, recommendations, forecasting, exception handling)[^37]. Bain's analysis of nearly 500 IT leaders found that 78% expect at least some ERP functionality to be replaced or augmented by agentic AI over three years, but only 16% expect AI to affect more than 25% of ERP functionality[^44].

**The three-layer stack is emerging:**

Bain describes the rebundling architecture as three layers: **Systems of record** (source of truth, storing core business data), **Agent operating systems** (orchestrating work—Microsoft Azure AI Foundry, Google Vertex AI Agent Builder, Amazon Bedrock Agents), and **Outcome interfaces** (translating plain-language requests into agent actions via Teams, Slack, or custom apps)[^17]. The application layer is being squeezed between the data substrate below and the intelligence/agent layer above.

### Mid-Term (2027–2030): The Semantic Data Substrate Becomes the Competitive Moat

**Gartner's five-stage trajectory:**

| Stage | Year | Capability | Enterprise Impact |
|-------|------|-----------|-------------------|
| 1 | 2025 | AI Assistants Everywhere | Nearly all enterprise apps embed AI assistants requiring human input |
| 2 | 2026 | Task-Specific Agents | 40% of enterprise applications integrate agents acting independently |
| 3 | 2027 | Collaborative Agents Within Apps | One-third of implementations combine agents with different skills |
| 4 | 2028 | Cross-App Agent Ecosystems | 15% of daily work decisions made autonomously; agents collaborate across business functions |
| 5 | 2029 | The New Normal | 50% of knowledge workers develop skills to create AI agents on demand |

Source: Gartner, compiled in Business 2.0 Channel[^68].

**By 2030:** Gartner projects 35% of point-product SaaS tools will be absorbed into larger agent ecosystems or replaced entirely by AI agents[^23][^68]. At least 40% of enterprise SaaS spend will shift toward usage-, agent-, or outcome-based pricing[^23]. The agentic AI market is projected to grow from $8.5 billion in 2026 to $42–52 billion by 2030 (43%+ CAGR)[^68].

**The semantic layer becomes the control plane:**

AtScale's 2025 review concluded: "The Universal Semantic Layer has evolved beyond accelerating business intelligence. It's become the control plane for enterprise AI"[^99]. Three architectural patterns are emerging for 2026 and beyond: **Semantic-First AI Agents** (LLMs reasoning directly over governed models), **Semantic Observability** (monitoring how AI interprets business logic, detecting drift and bias), and **Composable Governance** (treating semantic models as version-controlled shared code)[^99].

Bain identifies the semantic gap as the critical bottleneck: "The first semantic layer that creates an industry-wide standard to enable an invoice.bot to talk to a payment.bot will reshape the AI ecosystem and direct a large next wave of value"[^17]. MCP and A2A standardize how agents package tool calls and results, but they don't provide shared vocabulary or show how business concepts map to APIs and tables[^17].

**Validation of the "SaaS becomes semantic database" claim:**

Glean's analysis frames this as the "evolution from database-centric to intelligence-centric architecture"—agents interact directly with APIs and databases without requiring graphical interfaces, orchestrating actions across multiple systems simultaneously[^26]. The Kindo.AI CEO predicts: "Soon, AIs will hold the entire business logic layer of a SaaS like Salesforce in memory. AI will only need access to the data"[^98].

### Long-Term (2030–2035): Full Disaggregation of Logic from Data

**Projected state:**

- By 2035, agentic AI could drive approximately 30% of enterprise application software revenue, surpassing $450 billion[^68].
- By 2030, 90% of B2B buying will be AI agent intermediated, pushing over $15 trillion of B2B spend through AI agent exchanges[^68].
- The surviving platforms will function as orchestration layers, "managing fleets of specialised agents rather than serving as destinations for human interaction"[^68].

**Assessment:** Hypothesis 1 is **strongly validated** for point-solution SaaS and workflow tools, and **directionally validated** for ERP/CRM systems with a longer timeline. The claim that SaaS platforms ultimately reduce to semantic databases is exactly the trajectory described by Nadella, Bain, and the emerging semantic layer architecture. The nuance is that core systems of record will persist as governed data substrates while the application/logic layer migrates to agents.

---

## Hypothesis 2: The Three Attendant Challenges — Siloing, Insecurity, and Coordination Failure

### The Core Claim

The inward pull of software functionality to individuals creates three interlocking problems: (a) data silos and fragmented organizational truth because data is consumed and generated at the individual level; (b) proliferation of insecure, unsafe, and biased micro-applications; and (c) difficulty coordinating organization-wide transformation due to barely understood micro-application sprawl.

### Near-Term (2025–2027): Shadow AI and the Governance Vacuum

**Data silos and truth fragmentation:**

Equinix's January 2026 analysis identifies data coherence as the central challenge: "As data proliferates across systems, clouds and formats, it's increasingly difficult to connect the right information... Lacking context for data, an agent might misinterpret, use stale data and/or take inappropriate actions"[^58]. InformationWeek reports that "the poor quality of unstructured data is data noise from too many copies, irrelevant, outdated versions and conflicting versions"[^55]. AtScale found that "the tolerance businesses had for semantic drift—conflicting definitions, inconsistent metrics, and undocumented logic—ran out the moment AI agents started consuming that data"[^105].

**Shadow AI as the mechanism of fragmentation:**

ISACA defines Shadow AI as using AI solutions—chatbots, code assistants, LLMs—without approval from IT or compliance teams[^39]. Unlike shadow IT, which was mostly limited to technically oriented teams, Shadow AI adoption spans every role: engineering, marketing, finance, HR[^45]. The Cyber Institute frames the core challenge: "Models ingest and learn from sensitive inputs, generate outputs that can influence decisions, and often leave no clear audit trail"[^48].

IBM's 2025 Cost of Data Breach Report found AI-associated breaches cost organizations more than $650,000 per breach[^39]. Unauthorized AI tools create silos that are "often dangerous for enterprise risk management"—employees may inadvertently create unmonitored information flows and compliance vulnerabilities despite improving productivity[^39].

**Insecure and biased micro-applications:**

The vibe-coded micro-apps present specific risks. Ruth Suehle, president of the Apache Software Foundation, cautioned that inexperienced developers "only know whether the output works or doesn't"[^43]. David Heinemeier Hansson (creator of Ruby on Rails, CTO of 37signals) described AI as "a flickering light bulb," pointing out it still oscillates between helpful and useless[^43]. Invicti's analysis warns that shadow AI applications can produce "misleading information (model hallucinations) and biased outcomes, resulting in poor-quality decisions and diminished organizational trust"[^45]. Developers may "integrate LLMs into applications or workflows without security review, embedding unsanctioned APIs, model calls, or cloud-hosted AI services directly into code"[^45].

**Coordination failure is already visible:**

Gartner warns that over 40% of agentic AI projects will be cancelled by the end of 2027 due to "escalating costs, unclear business value, or inadequate risk controls"[^68]. Only approximately 130 of the thousands of agentic AI vendors are considered legitimate, with most engaging in "agent washing"—rebranding existing products without substantial agentic capabilities[^68]. InformationWeek reports that 10–20% of leading firms are building internal "agent platforms" because off-the-shelf copilots don't yet provide the reliability, auditability, and policy control needed[^55].

### Mid-Term (2027–2030): Governance Frameworks Emerge Under Pressure

**The governance response crystallizes:**

Enterprise governance is moving from policy documents to infrastructure. The semantic layer becomes the enforcement mechanism—policies are declared once and applied everywhere, across BI dashboards, AI agents, and custom applications[^102]. Fine-grained controls include row-level filters, column-level restrictions, and feature-level permissions[^102]. Oracle Database 26ai exemplifies this approach: row-level policies, masking rules, and audit logging uniformly applicable to both human users and AI agents[^61].

**Predicted challenges during this period:**

- Data quality issues will increasingly stall agentic AI initiatives. "As we move toward ambient agents that are autonomous, this will introduce significant risk due to data quality leading to poor decisions"[^55].
- Privacy-preserving techniques (federated learning, secure enclaves, homomorphic encryption) will mature as enterprises need to train on sensitive data without centralizing it[^55].
- Regulatory frameworks will expand. The pattern mirrors factory regulation: EU AI Act already in force, with more jurisdictions following.

### Long-Term (2030–2035): Standards and Governance Mature

The long-term trajectory points toward comprehensive governance frameworks analogous to the factory safety codes that took decades to develop in the industrial era. The organizations that succeed "won't be those deploying the most AI models. They'll be the ones whose models operate from a common, open, governed semantic foundation"[^99].

**Assessment:** Hypothesis 2 is **strongly validated** across all three dimensions. Data siloing through shadow AI is already documented and costing organizations significantly. Insecurity and bias in micro-applications are acknowledged by industry leaders (Apache Foundation president, 37signals CTO). Coordination failure is reflected in Gartner's prediction of 40%+ agentic project cancellations. The key insight is that these are not hypothetical future risks—they are present realities accelerating with adoption.

---

## Hypothesis 3: The Cognitive Industrial Revolution — Parallels to Pre-Standardization Chaos

### The Core Claim

The current period of agentic proliferation mirrors the chaotic early phase of the industrial revolution before standardization coalesced—but as a cognitive and logical revolution rather than a physical and mechanistic one.

### The Cottage Industry Phase (Pre-Factory / Pre-Standard): Where We Are Now

The pre-industrial "putting-out system" bears striking resemblance to the current state of AI-assisted work. Under the putting-out system, merchants provided raw materials to rural workers who produced goods in their homes. Quality was inconsistent. Embezzlement of supplies was common. Logistics were inefficient. There was no standardization—"no two exactly alike"[^31][^54][^60].

| Putting-Out System (Pre-Industrial) | Current Agentic Micro-App Proliferation |
|---|----|
| Workers produced goods at home with merchant-supplied materials | Workers generate micro-apps/workflows at their desks with AI-supplied capabilities |
| No standardization of outputs; quality inconsistent | No standardization of agent outputs; hallucination and bias |
| Embezzlement of supplies, poor quality control | Data leakage, IP exposure, shadow AI governance gaps |
| Logistical effort in procuring/distributing raw materials | Integration effort in connecting agents to data sources and each other |
| Each product unique, no interchangeable parts | Each micro-app unique, no interoperability or shared governance |
| Merchant capitalists provided raw materials, paid by piece | AI vendors provide foundation models, charging by token/usage |

### The Interchangeable Parts Moment: Standardization as the Pivotal Shift

Eli Whitney's concept of interchangeable parts (c. 1800) transformed manufacturing: "Rather than creating unique parts for each item, parts would be standardized and produced in large quantities so they could fit into any assembly"[^69][^74]. Before this, gun-making was handcraft—"no two exactly alike"[^74]. Whitney's vision required precision that the technology of his time couldn't deliver, but it "inspired a wave of innovation that would steadily improve machine tools and manufacturing processes"[^69].

The current analog is the emergence of MCP (Model Context Protocol, developed by Anthropic, adopted by OpenAI March 2025, Google April 2025) and A2A (Google's Agent2Agent protocol)[^17]. These standardize how agents communicate, but—critically—they don't yet provide the shared vocabulary, semantic definitions, or policy frameworks needed for true interoperability[^17]. Bain notes that "the emergence of these standards has shown strong network-effect dynamics—lightning-fast tipping points, winner takes most"[^17].

This is the equivalent of Whitney demonstrating the concept while the machine tools to achieve it are still being built. The vision is clear; the implementation infrastructure is catching up.

### The Factory Acts: Regulation Following Chaos

The industrial revolution's regulatory response followed a predictable pattern: chaos → incidents → incremental regulation → comprehensive frameworks:

| Year | Regulation | What It Addressed |
|------|-----------|-------------------|
| 1833 | Factory Act 1833 | First effective enforcement: inspectors for textile factories |
| 1844 | Factories Act 1844 | Required safeguarding of mill gearing, prohibited cleaning machinery in motion |
| 1844–1856 | Seven successive factory statutes | Safety of children, young persons, women; fencing of machinery |
| 1878 | Factory and Workshop Act | Extended regulation to practically all workplaces |
| 1937 | Factories Act 1937 | First comprehensive code for safety, health and welfare applicable to all factories |

Source: History of Occupational Safety and Health[^86][^89].

The parallel timeline for AI/agentic regulation:

| Year | Development | Analog |
|------|-----------|--------|
| 2023–2024 | EU AI Act passed and entering force | First comprehensive AI safety framework |
| 2025 | Shadow AI governance becomes urgent; enterprise policies inadequate | Early Factory Acts—piecemeal, inconsistent |
| 2025–2026 | MCP/A2A protocols adopted | Interchangeable parts concept demonstrated |
| 2026–2028 | Semantic layers, agent platforms, governance infrastructure | Standardized machine tools, measurement systems |
| 2030+ | Comprehensive agent governance frameworks | Full factory safety codes |

### What Maps Well and What Requires Nuance

The analogy is strongest at the structural level: a technological discontinuity creates rapid, uneven adoption; organizations improvise locally; quality and safety suffer; only later do standards, safety practices, and interoperable components crystallize.

The analogy requires careful framing in three areas:

1. **Speed**: The industrial revolution's standardization arc played out over roughly 100 years (1750s–1850s for interchangeable parts; 1833–1937 for comprehensive factory regulation). The cognitive/logical revolution will compress this dramatically—possibly into 10–15 years—because information-based systems can be reconfigured far faster than physical infrastructure[^31].

2. **Locus**: The industrial revolution was anchored in physical capital, energy, and labor relations. The current shift is about information flows, cognition, and coordination. The "raw materials" being distributed to "cottage workers" are not cotton and wool but foundation model capabilities and data access[^54][^60].

3. **Governance structure**: Industrial standardization was tightly coupled to nation-state and military needs (Whitney's interchangeable parts were commissioned by the U.S. government for muskets)[^69][^71]. Today's standards are emerging from private consortia (Anthropic, Google, OpenAI) and platform vendors, with regulators following rather than leading[^17].

**Assessment:** Hypothesis 3 is **validated as a structural analogy** with the essential qualification that this is a cognitive and logical revolution operating at information-age speed. The cottage industry → factory system → standardization arc provides a useful narrative framework for the article, provided the reader understands the locus has shifted from physical production to cognitive production, and the timeline is compressed by an order of magnitude.

---

## Section 4: Cognitive Adaptation — How to Think Differently, and Where This Goes

### The Cognitive Challenge: Why This Transition Is Harder Than It Looks

The shift from monolithic SaaS to agent-mediated, individually-generated workflows does not merely change what tools people use. It changes what cognitive demands are placed on them. This is the dimension most analyses miss.

**Cognitive Load Theory** (John Sweller, 1988) identifies three types of mental load: intrinsic (the inherent difficulty of the task), extraneous (how information is presented), and germane (the effort required to build understanding)[^81][^87]. AI agents initially reduce extraneous load by simplifying interfaces. But they simultaneously create new intrinsic load: understanding what the agent did, whether it did it correctly, how its outputs relate to organizational truth, and when to override it.

A 2025 study in *PMC* found a paradox: "AI can concurrently function as an efficiency facilitator while also contributing to cognitive debilitation, thereby supporting hypotheses regarding learned powerlessness and the erosion of intrinsic decision-making autonomy"[^84]. The study found strong correlations between AI's propensity to overwhelm users with choices and lower attention capacity (r = 0.908) and information overload (r = 0.920)[^84]. An April 2025 paper reframed the AI safety debate to center on cognitive overload as "a bridge between near-term harms and long-term risks"[^90].

This is the cognitive equivalent of the factory worker who could operate one machine but couldn't understand the system. In the agentic era, individuals can prompt one agent but may not understand the data it drew from, the biases it encoded, or the organizational implications of its output.

### Near-Term Cognitive Adaptation (2025–2027): From Consumer to Orchestrator

**The shift in mental model:**

The fundamental cognitive adaptation required is a shift from **application user** (I use tools that have been designed, tested, and maintained by professionals) to **system orchestrator** (I compose capabilities from agents, models, and data sources, and I am responsible for evaluating the outputs). This is a qualitatively different cognitive posture.

**Specific adaptation requirements:**

- **Developing "negative capability"**: The ability to remain comfortable with uncertainty and incomplete information. Organizational research shows that leaders who frame challenges as hypotheses to test rather than problems to solve demonstrate significantly better adaptation outcomes. Microsoft's cultural transformation under Nadella—from "know-it-all" to "learn-it-all"—is the enterprise-scale example[^50].

- **Embracing "provisional knowing"**: Organizations that adopt language acknowledging the temporary nature of current understanding—"based on what we know now," "our current best thinking suggests"—create cultures where updating beliefs in response to new evidence becomes normal rather than threatening[^50].

- **Building evaluation literacy**: The critical near-term skill is not prompt engineering but output evaluation. Can you assess whether an agent's output is accurate? Complete? Biased? Consistent with organizational data? This is a form of cognitive literacy that most knowledge workers do not currently possess.

- **Understanding the data substrate**: Just as factory workers eventually needed to understand not just their machine but the production system, knowledge workers need to understand not just their agent but the data it operates on—its provenance, freshness, governance, and limitations.

### Mid-Term Cognitive Adaptation (2027–2030): From T-Shaped to V-Shaped Professionals

IBM Research has advocated for T-shaped professionals who "uniquely combine specialization (critical thinking and problem-solving depth) and flexibility (empathy, breadth of knowledge, skills, experience, and complex communication abilities) and who also use smart machines as assistants"[^97]. But the agentic era may require something further: **V-shaped professionals** who develop "graduated depth across adjacent domains, creating a more fluid transition between specialization and generalization"[^103].

The difference matters. T-shaped professionals have deep expertise in one area and broad awareness across others. V-shaped professionals develop working depth in multiple adjacent areas—enough to evaluate agent outputs across domains, identify when agents are crossing domain boundaries poorly, and synthesize insights that require understanding of multiple fields simultaneously[^103].

Adobe's "T to V" initiative systematically reshaped its engineering culture: expertise expansion opportunities, cross-functional problem-solving forums, redesigned performance evaluations rewarding knowledge versatility[^103]. IBM redesigned its technical learning ecosystem around "knowledge constellations" rather than isolated competencies[^103].

**Organizational sensemaking becomes critical:**

The law of requisite variety (Ashby) states that an organization's internal diversity must match the complexity of its environment. As agents proliferate and generate diverse, potentially conflicting outputs, organizations need distributed sensemaking capabilities—regular forums for collective interpretation across hierarchical levels that develop "richer, more nuanced understanding that informs better adaptation"[^82][^50].

Structured practices include:

- **Weekly learning cycles**: Dedicated time for reflection, sense-making, and knowledge consolidation. Research indicates teams with structured weekly retrospectives demonstrate 36% faster adaptation cycles and 43% lower error rates during change implementation[^50].
- **Monthly strategic conversations**: Regular forums for discussing emerging patterns, testing strategic assumptions, and recalibrating priorities—transforming strategy from an annual event into an ongoing capability[^50].
- **Reflection prompts in workflow**: A financial services firm that embedded five-minute reflection prompts into its project management workflow reported 29% improvement in lessons-learned capture and 35% reduction in repeated errors[^50].

### Long-Term Cognitive Adaptation (2030–2035): Building Change Fitness as Core Capability

The long-term requirement is not managing discrete changes but building **change fitness**—"the organizational capacity to continuously adapt without depleting human resources"[^50]. Change fitness differs from change management: it treats adaptation as ongoing rather than episodic, focuses on capability development rather than process compliance, and distributes adaptive responsibility rather than concentrating it in specialized roles[^50].

Organizations that identify and develop specific capabilities—sense-making, experimentation, learning agility, tolerance for ambiguity, collaborative problem-solving—demonstrate 46% higher change success rates than those relying on general leadership development[^50].

The cognitive model shifts from:

- **Pre-agentic**: "I am skilled at using specific tools" → 
- **Early agentic**: "I am skilled at prompting and evaluating agents" → 
- **Mature agentic**: "I am skilled at understanding systems of agents, data, and humans, and navigating their interactions"

### Macro-Evolutionary Trajectory: Tying Back to the Original Thesis

The original article described the New Information Architecture as: semantic databases → agent transport → LLM aggregation → conversational/immersive delivery[^1]. The evidence gathered for this follow-up suggests the macro trajectory can now be refined into three concurrent evolutionary arcs:

**Arc 1: The Infrastructure Arc (Data and Standards)**

The enduring substrate is the semantic data layer. SaaS applications are being reduced to their essential function—governed data repositories. The competitive moat moves from application features to data quality, semantic richness, and governance rigor. The standardization pathway follows: MCP/A2A (transport protocols, already adopted) → semantic vocabularies (industry-specific ontologies, emerging) → comprehensive governance frameworks (composable, auditable, version-controlled, still nascent)[^17][^99][^105].

**Arc 2: The Interaction Arc (Agents and Interfaces)**

The agent layer replaces the application layer as the primary locus of business logic and user interaction. This is the "collapse" Nadella described—CRUD databases persist, but the logic, the interface, and the value migrate to agents[^66][^67]. The interaction modality shifts from visual/click-based to conversational/ambient, exactly as the original article predicted[^1]. By 2029, Gartner expects 50% of knowledge workers to create AI agents on demand[^68].

**Arc 3: The Cognitive Arc (Human Adaptation)**

This is the arc missing from most analyses and represents the article's distinctive contribution. As software functionality disaggregates to the individual level, the cognitive demands on individuals *increase* even as the mechanical demands decrease. The paradox of cognitive offloading—AI reduces effort on individual tasks while increasing the systemic complexity the individual must navigate—creates a new form of professional capability requirement[^84][^87][^90].

The macro movement evolves through these phases:

| Phase | Infrastructure | Interaction | Cognition |
|-------|---------------|------------|-----------|
| **Current (2025–2027)** | Data sprawl; semantic drift exposed; early protocol standards | AI assistants → task-specific agents; vibe-coded micro-apps proliferate | Application user → system evaluator; negative capability required |
| **Consolidation (2027–2030)** | Semantic layers as enterprise control plane; governed ontologies | Cross-app agent ecosystems; 15% daily decisions autonomous | T-shaped → V-shaped professionals; distributed sensemaking |
| **Maturation (2030–2035)** | Universal semantic standards; composable governance | Agent fleets managed as infrastructure; 30% revenue from agentic AI | Change fitness as core capability; cognitive literacy as professional baseline |

### The Key Insight for the Article

The original thesis described the shift from "search and browse" to "ask and receive." The follow-up article should extend this to a deeper claim: **the shift from "use applications" to "orchestrate intelligence" is not merely a technological transition but a cognitive one, and the primary bottleneck to realizing the agentic web's potential is not infrastructure or standards (those are converging) but the human capacity to operate effectively in a world where the individual is the integration point.**

The industrial revolution analogy works precisely because it captures this dynamic: the transition from cottage industry to factory system was not primarily about machines. It was about reorganizing human work, cognition, and coordination around a new technological capability. The machines came first; the standards, regulations, skills, and organizational forms that made them safe and productive took decades to follow. We are in the cottage industry phase of the cognitive revolution, and the factory acts—the semantic layers, governance frameworks, and professional competency models—are only beginning to be written.

---

## Suggested Article Structure

For Claude to write the follow-up article based on this research:

1. **Opening**: The SaaSpocalypse as the inflection point that validates the original thesis—$285B erased by a single AI product announcement, confirming that intelligence is displacing application as the value layer.

2. **Hypothesis 1 (The Disaggregation)**: Software functionality migrating from monolithic platforms to personalized micro-applications over shared semantic data substrates. Near/mid/long-term evidence. The Nadella doctrine. Vibe coding and disposable software. The three-layer stack.

3. **Hypothesis 2 (The Three Challenges)**: Data siloing and truth fragmentation. Shadow AI and insecurity. Coordination failure. Each mapped across time horizons with evidence of current severity and projected evolution.

4. **Hypothesis 3 (The Cognitive Industrial Revolution)**: The cottage industry parallel—but cognitive, not physical. The interchangeable parts moment (MCP/A2A). The factory acts trajectory. What maps well and what requires careful framing.

5. **The Cognitive Adaptation Imperative (The Distinctive Contribution)**: Why this is harder than it looks. Cognitive load paradox. Negative capability and provisional knowing. T-shaped to V-shaped professionals. Distributed sensemaking. Change fitness. This should be the section that distinguishes the article from the dozens of "AI eats SaaS" takes currently circulating.

6. **Macro Trajectory**: The three concurrent arcs (infrastructure, interaction, cognition) and how they converge toward the mature agentic web described in the original article, with the cognitive arc as the binding constraint.

---

## Source Summary

| Source Category | Key Sources | Primary Use |
|----------------|-------------|-------------|
| Original thesis | drli.blog Agentic Web Evolution (June 2025) | Foundation; predictions to validate |
| Enterprise analysis | Bain Technology Report 2025; Deloitte TMT Predictions 2026; McKinsey ERP/AI 2026 | Hypothesis 1 (disaggregation evidence, timelines) |
| Market events | Forbes SaaSpocalypse; Anthropic Claude Cowork trigger; $285B selloff | Opening narrative, urgency |
| Industry leadership | Nadella CRUD doctrine; McDermott Knowledge 25 | Strategic direction validation |
| Adoption data | Gartner 5-stage timeline; Bain 500 IT leaders survey | Quantitative milestones |
| Micro-apps/vibe coding | TechCrunch; DailyAIWorld; YouTube vibe coding analysis | Hypothesis 1 (disposable software evidence) |
| Shadow AI/governance | ISACA; Invicti; Cyber Institute; IBM breach data | Hypothesis 2 (insecurity, siloing) |
| Data infrastructure | AtScale; Equinix; Oracle 26ai; InformationWeek | Hypothesis 1–2 (semantic layer, data quality) |
| Historical parallel | Wikipedia Industrial Revolution; HistoryCrunch; Historycentral; Factory Acts timeline | Hypothesis 3 |
| Cognitive frameworks | PMC cognitive overload studies; Innovative Human Capital change fatigue; IBM T-shaped research | Section 4 |
| Professional development | V-shaped talent evolution research; Adobe/IBM case studies | Section 4 (mid/long-term adaptation) |


---

## References

1. [interests.writing_blog](interests.writing_blog) - The user publishes essays on AI, societal implications, and technological evolution—including a June...

17. [Will Agentic AI Disrupt SaaS? | Bain & Company](https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/) - Will AI and agents disrupt SaaS? Yes. In some cases, that disruption will grow the market; in others...

23. [SaaS meets AI agents | Deloitte Insights](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html) - AI agents could drive a gradual transformation of SaaS markets starting in 2026. To put things in pe...

26. [Will AI agents replace SaaS? Key insights for 2025](https://www.glean.com/perspectives/will-ai-agents-replace-saas-tools-as-the-new-operating-layer-of-work) - The Glean Team | Will AI Agents Replace SaaS? Key Insights for 2025: Learn how AI agents may reshape...

31. [Industrial Revolution](https://en.wikipedia.org/wiki/Industrial_Revolution) - On the eve of the Industrial Revolution, spinning and weaving were done in households, for domestic ...

35. [SaaSpocalypse Now? AI Is Disrupting SaaS — But Not All Software ...](https://www.forbes.com/sites/petercohan/2026/02/06/saaspocalypse-now-heres-why-ai-will-not-kill-all-software/) - Software stocks have lost over $1 trillion in 2026 due to slowing revenue, enterprise SaaS cuts, and...

37. [Bridging the great AI agent and ERP divide to unlock value at scale](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/bridging-the-great-ai-agent-and-erp-divide-to-unlock-value-at-scale) - While it is unlikely that AI agents will replace the ERP in the near or medium term because of syste...

39. [The Rise of Shadow AI: Auditing Unauthorized AI Tools in ...](https://www.isaca.org/resources/news-and-trends/industry-news/2025/the-rise-of-shadow-ai-auditing-unauthorized-ai-tools-in-the-enterprise) - Shadow AI resembles shadow IT, a problem associated with unauthorized technological innovations circ...

40. [Disposable Software & Vibe Coding 2026 | The End of SaaS, The ...](https://dailyaiworld.com/post/disposable-software-vibe-coding-2026-the-end-of-saas-the-rise-of-software-on-demand) - Disposable Software is replacing long-term SaaS subscriptions for many niche, short-lived use cases;...

43. [Micro-app boom: AI “vibe coding” lets non-programmers ...](https://www.bez-kabli.pl/micro-app-boom-ai-vibe-coding-lets-non-programmers-build-apps-instead-of-buying-them/) - Micro-app boom: AI “vibe coding” lets non-programmers build apps instead of buying them - Bez Kabli

44. [How Soon Will Agentic AI Redefine Enterprise Resource ...](https://www.bain.com/insights/how-soon-will-agentic-ai-redefine-enterprise-resource-planning-snap-chart/) - Bain’s latest survey reveals a divide: tech leaders find ERP enables AI adoption, while laggards say...

45. [Shadow AI: Risks, Challenges, and Solutions in 2025](https://www.invicti.com/blog/web-security/shadow-ai-risks-challenges-solutions-for-2025) - Shadow AI introduces hidden risks across enterprises. Learn what it is, why it matters, and how lead...

46. [This vibe coding trend will DOMINATE 2026 - YouTube](https://www.youtube.com/watch?v=rlVUKdQZM6Y) - Vibe coding is evolving fast. 2026 is the year AI agents start ... Top Agentic Coding Tools 05:27 Di...

48. [Shadow AI and the Governance Vacuum - The Cyber Institute](https://www.cyber-institute.org/post/shadow-ai-and-the-governance-vacuum-confronting-the-next-phase-of-digital-trust-risk) - Shadow AI is the use of AI tools, often public generative apps without an organization’s approval or...

50. [Organizational Change Fatigue: Building Adaptive Capacity in an ...](https://www.innovativehumancapital.com/article/organizational-change-fatigue-building-adaptive-capacity-in-an-era-of-permanent-disruption) - The article concludes with frameworks for long-term organizational resilience that treat adaptabilit...

54. [History of Methods of Production before Industrial Revolution](https://edukemy.com/free-resources-for-upsc/prelims-notes/industrial-revolution/history-of-methods-of-production-before-industrial-revolution/97375) - Industrial Revolution - Industrial Revolution - History of Methods of Production before Industrial R...

55. [2026 enterprise AI predictions -- what's facing CIOs](https://www.informationweek.com/machine-learning-ai/2026-enterprise-ai-predictions-fragmentation-commodification-and-the-agent-push-facing-cios) - In 2026, enterprise AI is shaped by competing agent-based approaches, commoditized agent tooling and...

58. [The Data Problem Behind Agentic AI, and What You Can ...](https://blog.equinix.com/blog/2026/01/29/the-data-problem-behind-agentic-ai-and-what-you-can-do-about-it/?country_selector=Global+%28EN%29) - With agentic AI gaining traction, enterprises need to modernize how they manage, govern and intercon...

60. [Cottage Industry vs. Factory System - HISTORY CRUNCH](https://www.historycrunch.com/cottage-industry-vs-factory-system.html) - Cottage Industry vs. Factory System - A central change in the Industrial Revolution was the shift fr...

61. [How Oracle AI Database 26ai Addresses The Enterprise AI ...](https://www.forbes.com/sites/stevemcdowell/2026/01/27/how-oracle-database-26ai-addresses-enterprise-ai-data-paradox/) - Oracle AI Database 26ai addresses the AI paradox by bringing AI to the data, rather than moving data...

66. [Related transcript from Microsoft CEO Satya Nadella: "This is a very ...](https://x.com/convequity/status/1868893301732262075) - For Dynamics, our approach is that business applications will collapse in the AI era. They are essen...

67. [Is SaaS dead? Microsoft CEO makes bold Agentic AI prediction](https://www.windowscentral.com/microsoft/hey-why-do-i-need-excel-microsoft-ceo-satya-nadella-foresees-a-disruptive-agentic-ai-era-that-could-aggressively-collapse-saas-apps) - Microsoft CEO Satya Nadella predicts the Agentic AI era might lead to the collapse of traditional So...

68. [How Agentic AI Will Disrupt the SaaS Industry from 2026 to 2030](https://business20channel.tv/how-agentic-ai-will-disrupt-saas-industry-2026-2030-31-january-2026) - By 2030, Gartner projects that 35% of point-product SaaS tools will be absorbed into larger agent ec...

69. [1800 Manufacture with Interchangeable Parts - Historycentral](https://www.historycentral.com/WH1400-1900/Tech/InterchangeableParts.html) - 1800 Manufacture with Interchangeable Parts

70. [Bill McDermott Channels Satya Nadella: AI Agents Will Turn Apps ...](https://cloudwars.com/cloud-wars-minute/bill-mcdermott-channels-satya-nadella-ai-agents-will-turn-apps-into-crud/) - On this specifically, McDermott commented that in the era of agentic AI, a traditional application s...

71. [Interchangeable parts](https://en.wikipedia.org/wiki/Interchangeable_parts) - Eli Whitney and an early attempt​​ The Congress was captivated and ordered a standard for all United...

72. [Microsoft CEO: AI Agents Will Transform SaaS as We Know It](https://www.cxtoday.com/customer-analytics-intelligence/microsoft-ceo-ai-agents-will-transform-saas-as-we-know-it/) - CX Today covers Customer Analytics & Intelligence news including Artificial Intelligence, Automation...

74. [Eli Whitney and the Whitney Armory](https://www.eliwhitney.org/eli-whitney-and-whitney-armory) - This concept was known as “interchangeable parts.” Each part would be manufactured to a precise stan...

81. [Cognitive Load & Decision Making | Smarter Choices with AI](https://www.ronlabs.ai/blog/cognitive-load-on-delayed-decision-making/) - Explore the impact of cognitive load on decision-making.

82. [Advanced AI-Enhanced Knowledge Management Strategy: Embracing Sensemaking, Uncertainty, Requisite Variety, and AI Technologies](https://www.linkedin.com/pulse/advanced-ai-enhanced-knowledge-management-strategy-ai-david) - A few people have asked how I approach incorporating AI into a KM strategy; this is a generic versio...

84. [Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC12367725/) - Artificial intelligence (AI) is increasingly shaping daily decision-making by enhancing efficiency a...

86. [Timeline - History of Occupational Safety and Health](https://www.historyofosh.org.uk/timeline.html) - Between 1844 and 1856 a succession of seven factory statues and subordinate regulations provided for...

87. [Cognitive offloading or cognitive overload? How AI alters the ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC12678390/)

89. [Factory Acts | Timeline, Features, Impact | History Worksheets](https://schoolhistory.co.uk/industrial/factory-acts/) - The Factory Acts were a series of labour legislation in Britain enacted from the early 19th to mid-2...

90. [3 Ai As Catalyst...](https://arxiv.org/html/2504.19990v1)

92. [$300 Billion Evaporated. The SaaS -Pocalypse Has Begun. - Forbes](https://www.forbes.com/sites/donmuir/2026/02/04/300-billion-evaporated-the-saaspocalypse-has-begun/) - AI didn't kill software. It broke the SaaS growth story. $300B vanished as markets repriced legacy m...

95. [Anthropic's AI Legal Tool Triggers $285 Billion 'SaaSpocalypse'](https://www.codercops.com/blog/anthropic-legal-ai-saaspocalypse-2026/) - Anthropic launched an AI legal plugin for Claude Cowork and software stocks crashed. Thomson Reuters...

97. [Cultivating T-shaped professionals in the era of digital transformation](https://research.ibm.com/publications/cultivating-t-shaped-professionals-in-the-era-of-digital-transformation) - In this commentary, we make the case for an education system that encourages the development of T-sh...

98. [How AI Is Disrupting The SaaS Landscape And Reshaping The Future](https://www.forbes.com/councils/forbestechcouncil/2025/02/19/how-ai-is-disrupting-the-saas-landscape-and-reshaping-the-future/) - I expect to see a potential 15%-20% reduction in most SaaS software seats by 2026. This reduction wi...

99. [The State of the Semantic Layer: 2025 in Review - AtScale](https://www.atscale.com/blog/semantic-layer-2025-in-review/) - A look back at how 2025 made open, governed semantics essential infrastructure for enterprise AI. Ex...

101. [SaaSpocalypse Now? AI Is Disrupting SaaS — But Not All Software Is Doomed](https://www.forbes.com/sites/petercohan/2026/02/06/saaspocalypse-now-ai-is-disrupting-saas---but-not-all-software-is-doomed/) - Software stocks have plunged some 20% this year. AI is considered a driving force as hedge funds hav...

102. [How enterprises scale secure, governed AI with a universal ...](https://www.strategysoftware.com/blog/how-enterprises-scale-secure-governed-ai-with-a-universal-semantic-layer) - See how enterprises scale secure, governed AI with Strategy Mosaic—the universal semantic layer that...

103. [The Evolution of Professional Versatility: From T-Shaped to V ...](https://www.innovativehumancapital.com/article/the-evolution-of-professional-versatility-from-t-shaped-to-v-shaped-talent) - This article examines the evolution from T-shaped to V-shaped professional competency models in resp...

105. [Why 2025 Redefined the Semantic Layer](https://www.atscale.com/blog/why-ai-redefined-the-semantic-layer/) - Why 2025 exposed semantic drift, forced governance into infrastructure, and made open semantic layer...

