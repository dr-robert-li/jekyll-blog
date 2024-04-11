# 12 Simple Techniques to Improve Your Prompts

As someone who is deep into AI engineering, reading research and learning about novel implementations, I often find myself drawn to the bleeding edge, and that's what I end up sharing.

By my partner recently asked me, 

> "Who actually reads that stuff?"

And, to be honest, not a whole lot of people. 

Many of us are new to AI and simply want to get their hands dirty in a way that's easy to understand. 

So let's take a step back. 

I know interacting with chatbots can sometimes be a frustrating experience, especially when you ask a question and receive a response that, while technically correct, completely misses the mark in terms of what you were actually looking for. This can happen when the chatbot fails to grasp the context, nuance, or intent behind your question and, why would it? Unlike a human, it isn't reading your body language, your facial expressions, nor does it understand you as a person.

So, it's important to remember that chatbots, while powerful tools, are not perfect and may require additional guidance and refinement through the use of effective prompting techniques to better understand and address your unique needs.

Crafting effective prompts is essential to getting the most out of these conversations. 

By employing a few simple techniques, you can significantly improve the quality and accuracy of the responses you receive from the chatbot. Below, we'll explore 12 easy-to-implement strategies to help you create better prompts and enhance your overall chatbot experience.

### One-shot prompting: 
Provide a clear and specific prompt with all the necessary information for the model to generate an accurate response in a single attempt. By including all relevant details upfront, you minimize the need for back-and-forth clarification, enabling the chatbot to deliver a more precise and comprehensive answer. For example, instead of asking, "What's the weather like today?" you could say, "What's the weather forecast for New York City on April 15, 2023?"

### Few-shot prompting: 
Include a few examples in the prompt to demonstrate the desired output format, structure, or style, enabling the model to better understand the task. By providing concrete examples, you help the chatbot grasp the context and expectations more effectively. For instance, if you want the chatbot to generate a haiku, you could include a couple of haiku examples in your prompt to illustrate the desired format and style.

### Decomposition: 
Break down complex tasks into smaller, more manageable sub-tasks to facilitate more accurate and focused responses from the model. By dividing a complicated request into a series of simpler, sequential steps, you allow the chatbot to tackle each component individually, leading to more precise and coherent overall results. For example, instead of asking the chatbot to "Write a 1000-word essay on the impact of social media on mental health," you could break it down into smaller tasks like "Outline the main points for an essay on the impact of social media on mental health" followed by "Expand on each outline point with supporting details and examples."

### Output format specification: 
Clearly state the desired output format (e.g., list, table, or specific file type) in the prompt to guide the model's response. By explicitly communicating your expectations, you help the chatbot structure its response in a way that best suits your needs. For instance, you could say, "Please provide a list of the top 5 tourist attractions in Paris" or "Generate a Markdown table comparing the features of three popular smartphones."

### System messages: 
Provide relevant context or background information in the system message to help the model generate more contextually appropriate responses. The system message acts as a primer, setting the stage for the conversation and guiding the chatbot's behavior. For example, you could start with a system message like, "You are an expert in medieval European history. Please answer the following questions as if you were a scholar from that era."

### Role-playing: 
Assign a specific role or persona to the model using the system message to guide its responses and behavior. By placing the chatbot in a particular role, you can elicit responses that are more aligned with the desired perspective or expertise. For instance, you could say, "Act as a professional chef and provide advice on creating a three-course meal for a dinner party."

### Iterative refinement: 
If the model's initial response doesn't meet the requirements, engage in a multi-turn conversation by rephrasing the prompt or providing additional information to refine the output. Iterative refinement allows you to collaboratively shape the chatbot's responses until you achieve the desired result. For example, if the chatbot's initial answer is too broad, you could follow up with, "Thanks for the overview. Can you now provide more specific examples to illustrate each point?"

### Tone specification: 
Use the system message to specify the desired tone (e.g., formal, casual, humorous) for the model's responses. By clearly communicating the intended tone, you help the chatbot adapt its language and style to better suit the context of the conversation. For instance, you could say, "Please respond to the following questions in a friendly, conversational tone as if you were explaining the concepts to a 10-year-old."

### Constraint specification: 
Include any specific constraints or limitations (e.g., word count, topic avoidance) in the system message to ensure the model adheres to them. By setting clear boundaries, you can keep the chatbot's responses focused and relevant to your needs. For example, you could say "Please provide a summary of the article in about 100 words, avoiding any mention of political figures or events."

### Experimentation and fine-tuning: 
Engage in iterative experimentation with different prompting techniques and fine-tune the prompts based on the model's responses to improve performance over time. As you interact with the chatbot, pay attention to which prompting strategies yield the best results and adapt your approach accordingly. Keep refining your prompts based on the chatbot's responses, and don't be afraid to try new techniques to see how they impact the conversation.

### Chain of thought reasoning: 
Encourage the model to provide step-by-step reasoning or a sequence of intermediate results that lead to the final answer, enabling better understanding of the model's thought process and potentially more accurate responses. By prompting the chatbot to walk you through its reasoning, you can gain insights into how it arrives at its conclusions and identify any potential gaps or errors in its logic. For instance, you could say, "Please solve this mathematical problem and explain each step of your solution process."

### Feigned catastrophization: 
Inject catastrophizing statements. These, for some reason, appear to make models more likely to respond with an accurate response. This also relates to Many Shot Jailbreaking, which Anthropic researchers recently described and, apparently, is most applicable to very large models with large context windows (https://www.anthropic.com/research/many-shot-jailbreaking) as it appears to induce catastrophic forgetting of a model's internal filters. By introducing hypothetical worst-case scenarios or extreme consequences, you may be able to elicit more accurate or unfiltered responses from the chatbot. However, it's essential to use this technique judiciously and ethically, as it can potentially lead to unintended or undesirable outcomes.

## Summing it up...
Improving your prompts is a powerful way to enhance your interactions with chatbots like ChatGPT. By employing techniques such as the ones described above you can elicit more accurate, relevant, and engaging responses from the chatbot.

Remember that effective prompting is an iterative process, and it may take some practice to find the right combination of techniques that work best for your specific needs and unlock their full potential as valuable tools for learning, problem-solving, and creative exploration.