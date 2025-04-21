---
layout: post
title: So You Wanna Vibe Code?
date: 2025-04-21
categories: ["Vibe Coding", "Software Architecture", "AI-Assisted Development", "Software Engineering", "SDLC", "Prompt Engineering", "Best Practices", "Code Quality", "AI", "LLM", "Secure Coding", "DevOps", "Developer Productivity", "Software Lifecycle"]
---

![https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/refs/heads/main/images/swe.png](https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/refs/heads/main/images/swe.png)

As promised to my partner, for each impenetrably esoteric blog post, I am to write a more accessible and practical one. 

So, here we go.

***Vibe coding.***

If you are an experienced, traditionalist software engineer, mention of this Karpathyan term probably leads to uncontrollable twitching and a momentary loss of motor skills.

Sorry.

The reality though, is, what originally began as a near-meme, has become an accepted, albeit underground, method of software development. In fact, as of April 9, 2025, Shopify has mandated AI proficiency as a baseline skill all employees must master. 

But because it is still somewhat an underground practice, there is precious little practical guidance. Much of the debate has either been derision or giddy excitement. The hype is overpowering.

Nevertheless, it's become too late to shove it back into the pandora's box from whence it came, and so, I'd like to, in this post, accept that it has become a normal method of software development, and provide some guidance on how to use it responsibly. 

Again. Here we go.

## What is Vibe Coding Anyway?

Rather than butcher its description, here's a quote from Andrej Karpathy himself:

>
> There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper so I barely even touch the keyboard. I ask for the dumbest things like "decrease the padding on the sidebar by half" because I'm too lazy to find it. I "Accept All" always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I'd have to really read through it for a while. Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away. It's not too bad for throwaway weekend projects, but still quite amusing. I'm building a project or webapp, but it's not really coding - I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works. 
>
> Andrej Karpathy (Feb 3, 2025)
>

The very serious members of our profession probably furrowed their brows and profusely mouthed wordless expletives at the very flippant manner in which Karpathy describes his approach to software development. This is an approach to a career that many of us spent not only years studying and getting certified in, but probably spent even more years honing our expertise through late nights of crunch and gnashing of teeth finding improbable bugs.

But, part of the problem with our profession, is that it *is* this impenetrable, and suffers from the cultural reputation of being a job with a steep and continuous learning curve, along with a punishing, and often unrewarding work schedule. It is not by chance that the Stack Overflow 2024 Developer Survey found a narrow demographic bulge between 18-44 years old with particular concentration between 25-34 years old, and a sharp drop off in respondents below and above this age bracket.

Like elite athletes, we burn bright, but we burn out.

So, from a different perspective, maybe we can see that the approach of Karpathy and others is a way to make software development more accessible to a wider range of people, to make it easier to live with, and, for some of us, to regain the love of it.

## Why Some Are Concerned

Let's be clear - the resistance isn't about assisted programming practices itself. Most of us already use linters, IDEs, extensions in VS Code, and even tools like Copilot and Cursor. As we say, *we software engineers are lazy, therefore we are efficient.*

The concern arises from *how laissez faire* we are with these tools. For example, if I was building something that I knew needed to progress to production, I might not be as nonchalant as Karpathy.

Similarly, if I was new to software development, I might want to be a bit more self-aware of this (there's nothing wrong with this and if you're fiddling around on your own local maching, no harm, no foul), and spend more time canvassing best practices (even if you don't know specifically what something like the Well-Architected Framework is - generative AI is fantastic at explaining things).

For example, you might want to think about:

1. **Scalability**: AI models optimize for correctness, not efficiency, often leading to performance bottlenecks as applications grow.
2. **Security**: AI doesn't always think about adversaries, and convenience often introduces serious vulnerabilities
3. **Readability**: AI-generated code is usually pretty good with commenting and documentation if properly prompted
4. **Performance**: Vibe coding frequently results in code bloat and inefficient implementations
5. **Maintainability**: Without careful planning, being able to quickly spit out thousands of lines of code means projects can easily and quickly get out of hand with "spaghetti code" that's difficult to parse, trace, debug and update

Don't be a `@leojr94_`:

> guys I'm under attack. 
>
> ever since I started to share how I built my SaaS using cursor, random things are happening, maxed out usage on api keys, people bypassing the subscription, creating random shit on db
>
> as you know, I'm not technical so this is taking me longer that usual to figure out
>
> for now, I will stop sharing what I do publicly on X
>
> there are just some wierd ppl out there

## Frameworks to Vibe Code to

So, if you're going to be vibe coding safely, let's remind ourselves of some of the easy to remember principles that should govern our approach.

### KISS (Keep It Simple, Stupid):
If any of you have read completely AI generated content you know it has a tendency to get... just a bit verbose. The same applies when generating code. 

Contrary to the acronym, you should actually be very specific when prompting to adhere to the KISS principle. What this means is that you are providing the logic, rather than allowing the AI to make broad assumptions (narrow, bounded assumptions are generally OK, and much more manageable).

So, for example, instead of prompting with the phrase “Build a user system,” try “Create a signup flow with email validation using OTP, 3 retries max, and rate-limiting.” 

### DRY (Don’t Repeat Yourself):
Any generative AI is going to create text based on what it already knows. This is the very definition of repeating. Plan for this as part of your vibe coding process. Ask it to “centralize API calls in a reusable module” or “generate utility functions for date formatting”, and review generated code blocks for duplication.

### YAGNI (You Aren’t Gonna Need It):
Because a LLM has the benefit of having trained on much larger code bases, it has *all* of the "just in case" features in it's dataset. This means that it will often suggest features that you don't need. It's going to be really tempting to accept that these suggested features are a good idea. Be disciplined in your consideration of these suggestions - are they *really* a good idea?

Without thoughtful consideration, vibe coding can lead to feature creep and, eventually, a codebase that strays far from the project's initial objectives. Start by asking yourself (or the team) “What’s the MVP?” and prompt accordingly. Example: “Add a password reset. Do not add 2FA yet.”

### Separation of Concerns & Modularity
This is kind of a subset of KISS and adjacent to DRY, but it bears keeping in mind when vibe coding. To ensure readability, testability and maintainability, break down your code into smaller, more manageable units. This is especially important when working with large codebases. When building new, generate features as standalone modules first, for example: "Build a payment processing class with no UI dependencies.” You can always integrate later.

### Single Responsibility Principle (SRP)
As we've all discovered, generative AI models typically perform worse when they are given a one shot prompt, that is broad and there is no opportunity for reflection. This is why Chain of Thought (CoT) was such a powerful innovation. When vibe coding, you should take advantage of this quirk of LLM inferencing. It's not much different to Agile.

Break down your task down into micro-prompts, reflect, and chain or build upon the results. For example: instead of “Build a user dashboard,” you can chain prompts:

“Create a function to fetch user data”

“Now, design a component to display data as a table”

“Add error handling for failed fetches”

## Planning for Vibe Coding Success

Vibes without a blueprint = chaos. 

>
> "Sure, Gen AI supercharges development, but it also supercharges risk. Two engineers can now churn out the same amount of insecure, unmaintainable code as 50 engineers."
>
> Willem Delbare, founder and CTO of Aikido
>

Like any good MOAB, an AI coding assistant is a powerful tool, and whether it triggers armageddon or clears the way for more productive activities, depends on how you use it. 

So, before generating a single line of code:

### Architect First, Code Later

Vibe coding’s greatest strength—speed—is also its Achilles’ heel. Without a clear architecture, you’ll end up with the digital equivalent of a hoarder’s garage: piles of functional but incoherent code.

Decide on your patterns (MVC, microservices, etc.) and document exactly how modules should interact. 

### Create a Best Practice Template

Before prompting your AI, build a "code DNA" template. Define:

- Standardized module structures (e.g., “All API routes must validate inputs before processing”)
- Naming conventions (e.g., “fetchUserData() not getStuff()”)
- Documentation requirements (e.g., “Every function gets a one-line purpose statement”)

This template becomes your AI’s playbook, ensuring generated code adheres to your standards, not just correctness.

For example:

```text
- **Functions**: <50 lines, JSDoc comments, error handling  
- **Classes**: Single responsibility, typed properties  
- **Modules**: API calls in `/services`, UI components in `/views`  
```

Cursor already has this as a function within their IDE under `.cursor/rules`:

>
> Think of them as a persistent way to encode context, preferences, or workflows for your projects or for yourself.
> Use project rules to:
>
> - Encode domain-specific knowledge about your codebase
> - Automate project-specific workflows or templates
> - Standardize style or architecture decisions
>

### GitHub's Golden Rule

Because generating code with AI tools is so rapid, it becomes even more important to review the ground covered at each milestone. You might ask yourselves:

- “Does this align with our ‘code DNA’?” (Consistency)
- “Could a new engineer understand this?” (Readability)
- “What happens if we scale to 100k users?” (Scalability)

In GitHub's own studies, one team reported catching 60% of premature abstractions in these reviews—saving months of refactoring. Refactoring 10 files at a time, beats refacting 100 all at once.

## Where Vibe Coding Shines (and Where It Doesn’t)

Like any method, there's going to be times when vibe coding is the best tool for the job. And there will be times when it's not.

In these situations vibe coding can get you running quickly:

✅ Generating Boilerplate Code: “Generate a REST API with Express.js CRUD endpoints for a ‘Products’ model.”

✅ Prototyping and POCs: “Mock a login screen with React, Tailwind, and hover effects.”

✅ Tedious Tasks: “Write SQL migration scripts for these schema changes.”

And then there are the situations where additional human oversight is required:

🚩 Security: For “Create a payment gateway”, you are going to want a security expert reviewing every line to ensure PII is not exposed. The same can be said about any code that is going to be referencing any secrets or authentication keys.

🚩 Complex Logic: Without thoroughly breaking down the logic into more manageable chunks, asking your AI companion to build a complex system based on a simple abstract prompt such as "Create a program that continuously sorts these orders by X, Y and Z" will result in code that fails at scale.

🚩 Large Legacy Systems: “Integrate this AI-generated module into our 10-year-old monolithic applicaiton with a 500,000 line code base” = 💥. 

## The Human-in-the-Loop

Finally, and most importantly, with any use of AI, but especially in the case of software development, it is critical to remember that, even if the grunt work is being automated, you are still the one who is ultimately responsible for reviewing and knowing the code generated. It is the reason why this is a force multiplier that becomes more powerful the more experienced you are, and it's the reason why software engineering as a career isn't going away anytime soon.

### Understand the fundamentals before "surrendering to the vibes..."

Even when using AI to generate code, you still need to maintain a mental model of what the code is doing. Take the time to understand the programming concepts, data structures, and software architecture in use. This knowledge will help you evaluate AI-generated solutions and make informed decisions.

### Bake reviewing and testing into your workflow

Never trust AI-generated code blindly. Review every line meticulously. Ask yourself:
- Does this make sense?
- Are there security vulnerabilities?
- Is this the most efficient approach?
- Will this code scale as the application grows?

### You are the police

Enforce the frameworks and standards you've set. Like any rule in real life, they need to be enforced to be effective. 

AI-generated code may not interpret the rules you've set in the way you might invision it should be adhered to. 

If it is repeatedly non-compliant, in a way that demonstrates a pattern, it may be time to revisit your rules.

Be explicit when observing security best practice, as the impact of a security risk can be magnified when vibe coding. 

Implement proper input validation, avoid hardcoding secrets, use secure authentication methods, and regularly scan for vulnerabilities. Run security testing tools like SonarQube, Snyk Code, or OWASP ZAP to identify potential issues before deployment.

### QA is not someone else’s problem

AI-generated code often contains logical errors that may not be immediately apparent. Just because it “works on my machine” doesn't mean you are accounting for edge cases.  Implement thorough testing practices including unit tests, integration tests, and performance tests to catch these issues early.

Thankfully, your AI coding assistant can help you with this. Write unit tests with it: “Generate Jest tests for this Express endpoint.”

### Learn from the code generated

If any of us have use any number of the chat interfaces that have proliferated (including ChatGPT and DeepSeek), you know that these models have tremendous explanatory capabilities.

Vibe coding may bring up concepts that you may not have discovered before. Get it to explain how the generated code works and the underlying principles and patterns it is attempting to adhere to.

It is a powerful method for learning and understanding, not just getting faster.

## Finding Balance

Vibe coding represents a significant shift in how software is created. It's not inherently good or bad - it's like any other powerful tool. It requires informed use.

For newcomers to software development: recognize that while AI can help you build functioning applications quickly, there's immense value in understanding software engineering principles. Don't just surrender to the vibes - invest time in learning fundamentals.

For experienced engineers: instead of dismissing vibe coding outright, use it as a force multiplier. Your hand is still on the wheel. Share your knowledge with the less experienced, about security, scalability, and maintainability to help propogate time honored best practices with this new method of software development.

I see the future of software development likely involving a hybrid approach - leveraging AI assistance while applying human expertise to ensure the resulting code meets professional standards. By combining the accessibility of vibe coding with sound engineering principles, we can create better software more efficiently than ever before.

Who knows. Software engineering might not end up being such a slog after all.