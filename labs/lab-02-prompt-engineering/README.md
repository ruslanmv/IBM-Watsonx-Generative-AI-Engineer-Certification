# Lab 02: Mastering Prompt Engineering

**Duration:** 45-60 minutes  
**Difficulty:** Beginner to Intermediate  
**Prerequisites:** Lab 01 completed, watsonx.ai account active

## Learning Objectives

By the end of this lab, you will be able to:
- ✅ Construct effective zero-shot and few-shot prompts
- ✅ Adjust model parameters for different tasks
- ✅ Use prompt templates and variables in watsonx.ai
- ✅ Evaluate and iterate on prompt quality
- ✅ Understand common prompt engineering pitfalls

## Lab Overview

This hands-on lab guides you through practical prompt engineering techniques using IBM watsonx.ai's Prompt Lab. You'll experiment with different prompting strategies, parameter settings, and learn to optimize prompts for various use cases.

---

## Part 1: Zero-Shot Prompting (15 minutes)

### Objective
Learn to create effective prompts without providing examples.

### Exercise 1.1: Basic Instruction Prompt

1. **Open watsonx.ai Prompt Lab**
   - Navigate to https://dataplatform.cloud.ibm.com
   - Click on "Prompt Lab" in the left sidebar

2. **Select Model**
   - Choose `meta-llama/llama-2-70b-chat`
   - This is a good general-purpose model for learning

3. **Write Your First Prompt**
   ```
   Summarize the following text in 3 bullet points:
   
   Artificial intelligence is transforming how businesses operate. 
   Companies are using AI for customer service automation, predictive 
   analytics, and process optimization. However, implementing AI 
   successfully requires careful planning, quality data, and ongoing 
   monitoring to ensure accuracy and fairness.
   
   Summary:
   ```

4. **Set Parameters**
   - Temperature: `0.3` (lower for factual tasks)
   - Max tokens: `150`
   - Top-p: `0.9`

5. **Generate and Observe**
   - Click "Generate"
   - Note how the model responds

### Exercise 1.2: Improving the Prompt

Now let's improve the prompt with better structure:

```
Task: Summarize the following text
Format: Exactly 3 bullet points
Style: Professional and concise

Text:
Artificial intelligence is transforming how businesses operate. 
Companies are using AI for customer service automation, predictive 
analytics, and process optimization. However, implementing AI 
successfully requires careful planning, quality data, and ongoing 
monitoring to ensure accuracy and fairness.

Summary:
-
```

**Question:** How did the output quality change? Write your observation:

```
Your observation:
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```

### Exercise 1.3: Temperature Experiment

Try the same prompt with different temperatures:

| Temperature | Output Quality | Notes |
|-------------|----------------|-------|
| 0.1 | | |
| 0.5 | | |
| 0.9 | | |

**Key Insight:** Lower temperature = more focused and consistent. Higher temperature = more creative and varied.

---

## Part 2: Few-Shot Prompting (20 minutes)

### Objective
Provide examples to guide the model's output format and style.

### Exercise 2.1: Basic Few-Shot

Create a product categorization prompt:

```
Categorize the following products into: Electronics, Clothing, or Home & Garden.

Examples:
Product: iPhone 14 Pro
Category: Electronics

Product: Cotton T-Shirt
Category: Clothing

Product: Garden Hose
Category: Home & Garden

Now categorize this product:
Product: Wireless Mouse
Category:
```

**Expected Output:** Electronics

### Exercise 2.2: Few-Shot for Style Transfer

Transform technical language into simple explanations:

```
Transform technical jargon into simple language that a 12-year-old can understand.

Example 1:
Technical: "The algorithm utilizes machine learning to optimize query performance."
Simple: "The program learns patterns to make searches faster."

Example 2:
Technical: "We implement end-to-end encryption for data security."
Simple: "We scramble your data so only you can read it."

Example 3:
Technical: "The system employs natural language processing for sentiment analysis."
Simple: "The computer reads text to figure out if people are happy or sad."

Now transform this:
Technical: "The neural network processes embeddings through attention layers."
Simple:
```

### Exercise 2.3: Creating Your Own Few-Shot Prompt

**Task:** Create a few-shot prompt for classifying customer emails by urgency (High, Medium, Low).

1. Write 3 example classifications
2. Test with a new email
3. Evaluate accuracy

```python
# Your prompt here:
prompt = """
Classify customer emails by urgency: High, Medium, Low

Example 1:
Email: "URGENT: System is down, all users affected, production stopped"
Urgency: High

Example 2:
Email: "Question about invoice date, can you clarify when we'll be charged?"
Urgency: Medium

Example 3:
Email: "Interested in learning more about your premium features"
Urgency: Low

Now classify:
Email: "Critical security vulnerability discovered, needs immediate patch"
Urgency:
"""
```

**Expected Output:** High

---

## Part 3: Parameter Tuning (15 minutes)

### Objective
Master the key parameters that control LLM behavior.

### Exercise 3.1: Temperature Deep Dive

**Scenario:** Generate marketing taglines for a coffee shop.

**Prompt:**
```
Generate 3 creative taglines for "Joe's Coffee House," a cozy neighborhood 
cafe known for artisanal roasts and friendly service.

Taglines:
1.
```

**Experiment:** Test with temperatures: 0.3, 0.7, 1.0

| Temperature | Tagline 1 | Tagline 2 | Tagline 3 | Creativity Rating (1-10) |
|-------------|-----------|-----------|-----------|--------------------------|
| 0.3 | | | | |
| 0.7 | | | | |
| 1.0 | | | | |

**Question:** Which temperature gave the best results for this creative task? Why?

```
Your answer:
_____________________________________________________________
_____________________________________________________________
```

### Exercise 3.2: Max Tokens Control

**Scenario:** Answer a customer question concisely.

**Prompt:**
```
Answer this customer question in 1-2 sentences:

Question: "How do I reset my password?"

Answer:
```

**Experiment:** Test with max tokens: 20, 50, 100

| Max Tokens | Output | Was it sufficient? |
|------------|--------|-------------------|
| 20 | | |
| 50 | | |
| 100 | | |

**Insight:** Set max tokens based on expected answer length. Too few = cut off. Too many = wasteful and potentially verbose.

### Exercise 3.3: Top-p (Nucleus Sampling)

**Scenario:** Generate code comments.

**Prompt:**
```python
# Function to calculate compound interest
def compound_interest(principal, rate, time, n):
    """
    
```

**Experiment:** Test top-p values: 0.5, 0.9, 1.0 with temperature fixed at 0.3

**Question:** How did top-p affect the diversity of the generated docstring?

```
Your observation:
_____________________________________________________________
_____________________________________________________________
```

---

## Part 4: Prompt Templates and Variables (10 minutes)

### Objective
Create reusable prompt templates with variables.

### Exercise 4.1: Email Template

**Template Structure:**
```
Write a {tone} email to {recipient} about {topic}.

Email format:
- Subject line
- Greeting
- Body (2-3 paragraphs)
- Closing

Email:
```

**Test Cases:**

1. **Test 1:**
   - tone: "professional"
   - recipient: "a client"
   - topic: "project deadline extension request"

2. **Test 2:**
   - tone: "friendly"
   - recipient: "team members"
   - topic: "celebrating a successful product launch"

**Your Results:**
```
Test 1 Subject Line: _________________________________________
Test 2 Subject Line: _________________________________________
```

### Exercise 4.2: Product Description Generator

Create a template for generating product descriptions:

```
Product Name: {{product_name}}
Category: {{category}}
Key Features: {{features}}

Generate a compelling 3-paragraph product description:

Paragraph 1: Hook the customer with the main benefit
Paragraph 2: Highlight 2-3 key features
Paragraph 3: Call to action

Description:
```

**Test with:**
- Product: "CloudSync Pro"
- Category: "Cloud Storage"
- Features: "Unlimited storage, AES-256 encryption, cross-platform sync"

---

## Part 5: Advanced Techniques (15 minutes)

### Exercise 5.1: Chain-of-Thought Prompting

**Scenario:** Solve a word problem step-by-step.

**Prompt:**
```
Solve this problem step by step:

Problem: A store is having a 25% off sale. If a jacket originally 
costs $80, and there's an additional 10% discount for loyalty members, 
what is the final price for a loyalty member?

Let's solve this step by step:
Step 1:
```

**Expected Process:**
1. Calculate 25% discount
2. Calculate new price after first discount
3. Calculate 10% loyalty discount on new price
4. Calculate final price

### Exercise 5.2: Self-Consistency

**Scenario:** Get multiple reasoning paths for better accuracy.

**Prompt:** (Run 3 times with temperature 0.7)
```
Question: If you're running a race and you pass the person in second 
place, what place are you in?

Think through this carefully:
```

**Results:**
- Attempt 1: _______________
- Attempt 2: _______________
- Attempt 3: _______________

**Most common answer:** _______________

---

## Part 6: Common Pitfalls and Solutions (10 minutes)

### Pitfall 1: Vague Instructions

**❌ Bad Prompt:**
```
Tell me about AI.
```

**✅ Good Prompt:**
```
Explain artificial intelligence in 3 paragraphs:
1. Definition and core concepts
2. Real-world applications
3. Current limitations

Target audience: Business executives with no technical background
```

### Pitfall 2: Assuming Context

**❌ Bad Prompt:**
```
What are the benefits?
```

**✅ Good Prompt:**
```
What are the benefits of implementing Retrieval-Augmented Generation 
(RAG) for enterprise chatbots compared to fine-tuning alone?

Focus on:
- Cost efficiency
- Maintenance overhead
- Accuracy and source attribution
```

### Pitfall 3: Not Specifying Format

**❌ Bad Prompt:**
```
List programming languages.
```

**✅ Good Prompt:**
```
List 5 popular programming languages for web development.

Format as a numbered list with:
- Language name
- Primary use case (1 sentence)
- Example company using it

Example:
1. JavaScript - Client-side web interactivity - Facebook
```

---

## Challenge Exercise (Optional)

Create a comprehensive prompt for a **Customer Service Email Response Generator** that:

1. Takes customer email as input
2. Analyzes sentiment and urgency
3. Generates an appropriate response
4. Includes a subject line
5. Maintains professional tone
6. Suggests next steps

**Constraints:**
- Response must be 3-4 paragraphs
- Include empathy statement
- Provide actionable solution
- End with clear next steps

**Test with this customer email:**
```
Subject: VERY FRUSTRATED - Package not delivered

I ordered a birthday gift for my daughter 2 weeks ago with expedited 
shipping. The tracking shows it's been sitting in a warehouse for 5 days. 
Her birthday is tomorrow and now I have nothing to give her. This is 
completely unacceptable and I want a full refund plus compensation for 
the inconvenience.
```

---

## Lab Deliverables

Submit the following:

1. ✅ Screenshot of your best zero-shot prompt and output
2. ✅ Your few-shot customer email urgency classifier
3. ✅ Temperature experiment results table (filled out)
4. ✅ One reusable prompt template you created
5. ✅ Answer to the challenge exercise

---

## Key Takeaways

- 🎯 **Clear instructions** are crucial - be specific about format, tone, and constraints
- 🌡️ **Temperature** controls creativity: 0.1-0.3 (factual), 0.7-1.0 (creative)
- 📊 **Few-shot examples** dramatically improve output quality and consistency
- 🔧 **Max tokens** should match expected output length
- 🎨 **Prompt templates** enable reusability and consistency
- 🧠 **Chain-of-thought** improves reasoning on complex problems

---

## Next Steps

- 📘 Complete Lab 03: Advanced Prompt Engineering
- 📚 Read: [IBM Prompt Lab Documentation](https://www.ibm.com/docs/en/watsonx)
- 🎥 Watch: Module 3 Videos on Advanced Techniques
- 💬 Join Discord: Share your best prompts with the community

---

## Additional Resources

- [watsonx.ai Prompt Lab Guide](https://www.ibm.com/docs/en/watsonx/prompt-lab)
- [Prompt Engineering Best Practices](https://github.com/your-repo/resources)
- [Parameter Tuning Cheat Sheet](./resources/parameter-guide.pdf)
- [100+ Example Prompts Library](./resources/prompt-library.md)

---

**Lab Version:** 1.0  
**Last Updated:** 2024  
**Estimated Completion Time:** 60 minutes

**Questions or issues?** Contact the instructor or post in the Discord #labs channel.
