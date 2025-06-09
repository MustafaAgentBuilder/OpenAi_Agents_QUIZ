# Fundamentals of Agentic AI Quiz
- **Total Questions**: 48 MCQs  
- **Duration**: 120 Minutes  
- **Difficulty Level**: Advanced (Stanford graduate-level equivalent)  
- **Passing Percentage**: 70%  

---

## Instructions  
- This quiz consists of 48 multiple-choice questions.  
- Each question has four options; select the most appropriate answer.  
- Some questions may involve code snippets or scenarios requiring analysis.  
- Ensure you read each question carefully, as the quiz is designed to be challenging and tests deep understanding.  

---

## Section 1: OpenAI Agents SDK (20 Questions)  
**1.** What is the primary purpose of the `Runner` class in the OpenAI Agents SDK?  
   a) To define the agent's tools and capabilities  
   b) To manage the execution of the agent loop and handle tool calls  
   c) To store the agent's context and state  
   d) To generate dynamic instructions for the agent  

**2.** In the OpenAI Agents SDK, what does the `@function_tool` decorator do?  
   a) It registers a function as a tool that the agent can call during execution.  
   b) It validates the input and output types using Pydantic models.  
   c) It enables asynchronous execution of the function.  
   d) It clones the agent for multi-agent collaboration.  

**3.** Which of the following is a key feature of the OpenAI Agents SDK's "Python-first" design?  
   a) It prioritizes natural language processing over code-based orchestration.  
   b) It allows developers to define agents and tools using Python code for precise control.  
   c) It restricts the use of external libraries to maintain simplicity.  
   d) It automatically generates Python code from natural language prompts.  

**4.** What is the role of `Pydantic` models in the OpenAI Agents SDK?  
   a) To manage the agent's memory and context  
   b) To define structured inputs and outputs for tools and agents  
   c) To handle asynchronous operations within the agent loop  
   d) To generate dynamic instructions for the agent  

**5.** Consider the following code snippet:  
```python  
from openai.agents import Agent, function_tool  
from pydantic import BaseModel  

class MyToolInput(BaseModel):  
    query: str  

@function_tool  
def my_tool(input: MyToolInput):  
    return f"Processed: {input.query}"  

agent = Agent(tools=[my_tool])  
```  
What will happen if the agent calls `my_tool` with an input that is not a string?  
   a) The tool will process the input as a string regardless.  
   b) Pydantic will raise a validation error due to type mismatch.  
   c) The agent will automatically convert the input to a string.  
   d) The tool will return an error message without processing.  

**6.** In the context of the OpenAI Agents SDK, what is a "Handoff"?  
   a) A mechanism to transfer control from one agent to another in a multi-agent workflow  
   b) A way to pause the agent's execution and resume it later  
   c) A method to clone an agent for parallel processing  
   d) A tool that allows the agent to hand off tasks to external APIs  

**7.** Which of the following best describes the `context` object in the OpenAI Agents SDK?  
   a) It stores the agent's tools and capabilities.  
   b) It manages the agent's state, including conversation history and intermediate results.  
   c) It defines the agent's personality and behavior.  
   d) It handles the execution of the agent loop.  

**8.** What is the difference between `Runner.run_sync()` and streaming in the OpenAI Agents SDK?  
   a) `Runner.run_sync()` executes the agent loop synchronously, while streaming allows for real-time output.  
   b) `Runner.run_sync()` is used for multi-agent workflows, while streaming is for single agents.  
   c) `Runner.run_sync()` handles asynchronous operations, while streaming is synchronous.  
   d) There is no difference; both terms refer to the same functionality.  

**9.** In a multi-agent workflow, how does the OpenAI Agents SDK facilitate collaboration between agents?  
   a) By using shared memory and context objects  
   b) Through the use of Handoffs and agent cloning  
   c) By automatically merging the outputs of multiple agents  
   d) By restricting agents to operate in isolation  

**10.** What is the purpose of dynamic instructions in the OpenAI Agents SDK?  
    a) To allow the agent to generate its own tools on the fly  
    b) To enable the agent to adapt its behavior based on the context and user input  
    c) To automatically optimize the agent's performance  
    d) To simplify the agent's configuration by reducing the need for predefined tools  

**11.** Consider the following code snippet:  
```python  
from openai.agents import Agent, Runner  
agent = Agent(tools=[])  
runner = Runner(agent)  
result = runner.run_sync("Hello, agent!")  
```  
What will be the output of this code?  
    a) The agent's response to "Hello, agent!"  
    b) An error, because no tools are defined  
    c) A default greeting message  
    d) Nothing, as the agent has no tools to process the input  

**12.** Which of the following is a best practice when defining tools in the OpenAI Agents SDK?  
    a) Use Pydantic models to strictly type the inputs and outputs.  
    b) Avoid using async functions to simplify the code.  
    c) Define tools without descriptions to reduce overhead.  
    d) Limit the number of tools to one per agent.  

**13.** In the OpenAI Agents SDK, what happens if a tool raises an exception during execution?  
    a) The agent loop terminates immediately.  
    b) The exception is caught, and the agent continues with the next tool call.  
    c) The agent retries the tool call up to three times.  
    d) The exception is propagated to the runner, which handles it based on the configuration.  

**14.** What is the purpose of agent cloning in the OpenAI Agents SDK?  
    a) To create a backup of the agent's state  
    b) To enable parallel processing of multiple tasks by the same agent  
    c) To facilitate handoffs in multi-agent workflows  
    d) To reset the agent's context and start a new conversation  

**15.** Which of the following is NOT a primitive in the OpenAI Agents SDK?  
    a) Agents  
    b) Tools  
    c) Handoffs  
    d) Prompts  

**16.** In the context of the OpenAI Agents SDK, what is the agent loop?  
    a) A loop that continuously trains the agent on new data  
    b) The process by which the agent repeatedly calls tools and processes responses until a task is complete  
    c) A mechanism for handling recursive function calls within tools  
    d) A loop that manages the agent's memory and context  

**17.** Consider the following Pydantic model:  
```python  
from pydantic import BaseModel, Field  
class UserInput(BaseModel):  
    name: str = Field(..., description="The user's name")  
    age: int = Field(..., gt=0, description="The user's age")  
```  
What does the `gt=0` constraint enforce?  
    a) The age must be greater than 0.  
    b) The age must be greater than or equal to 0.  
    c) The age must be less than 0.  
    d) The age must be a positive integer, but zero is allowed.  

**18.** Which of the following is a key benefit of using Pydantic models in the OpenAI Agents SDK?  
    a) They enable automatic code generation for tools.  
    b) They provide runtime validation of inputs and outputs, ensuring type safety.  
    c) They simplify the agent's configuration by reducing the need for documentation.  
    d) They allow for dynamic modification of the agent's behavior.  

**19.** In the OpenAI Agents SDK, how can you specify that a tool should only be called under certain conditions?  
    a) By using the `tool_choice` parameter in the runner  
    b) By defining conditional logic within the tool's function  
    c) By setting constraints in the Pydantic model for the tool's input  
    d) By configuring the agent's context to include conditional flags  

**20.** What is the role of the `system_message` in the OpenAI Agents SDK?  
    a) It defines the agent's personality and behavior.  
    b) It provides instructions to the user on how to interact with the agent.  
    c) It manages the agent's memory and context.  
    d) It specifies the tools available to the agent.  

---

## Section 2: Prompt Engineering (10 Questions)  
**21.** What is the primary goal of prompt engineering in the context of AI agents?  
    a) To optimize the agent's code for performance  
    b) To craft inputs that guide the agent to produce desired outputs  
    c) To automate the generation of tools and functions  
    d) To reduce the need for human intervention in agent workflows  

**22.** Which of the following is a technique used in prompt engineering to improve the agent's reasoning?  
    a) Chain-of-Thought prompting  
    b) Zero-shot learning  
    c) Transfer learning  
    d) Reinforcement learning  

**23.** Consider the following prompt: "You are a helpful assistant. Please respond in a friendly manner." What is the purpose of this prompt?  
    a) To define the agent's tools  
    b) To set the agent's persona and tone  
    c) To provide context for a specific task  
    d) To instruct the agent on how to handle errors  

**24.** In prompt engineering, what is the significance of including examples in the prompt?  
    a) To increase the length of the prompt  
    b) To provide the agent with a template for generating similar responses  
    c) To confuse the agent and test its robustness  
    d) To reduce the need for clear instructions  

**25.** Which of the following is a best practice for handling sensitive data in prompts?  
    a) Include sensitive data directly in the prompt for clarity.  
    b) Use placeholders or anonymize sensitive data to protect privacy.  
    c) Avoid mentioning sensitive data altogether.  
    d) Encrypt the prompt before sending it to the agent.  

**26.** What is the difference between a system message and a user message in the context of prompt engineering?  
    a) The system message defines the agent's behavior, while the user message provides the input for a specific task.  
    b) The system message is used for error handling, while the user message is for normal interactions.  
    c) The system message is generated by the agent, while the user message is provided by the user.  
    d) There is no difference; both terms are interchangeable.  

**27.** Consider the following prompt: "Think step by step before answering the question." What technique is being used here?  
    a) Chain-of-Thought prompting  
    b) Few-shot learning  
    c) Zero-shot learning  
    d) Transfer learning  

**28.** In prompt engineering, what is the purpose of specifying the desired output format?  
    a) To make the prompt longer and more detailed  
    b) To guide the agent in structuring its response correctly  
    c) To test the agent's ability to handle different formats  
    d) To reduce the computational load on the agent  

**29.** Which of the following is a common challenge in prompt engineering?  
    a) Ensuring the prompt is clear and unambiguous  
    b) Making the prompt as long as possible  
    c) Including as many tools as possible in the prompt  
    d) Avoiding the use of examples in the prompt  

**30.** What is the role of temperature in prompt engineering?  
    a) It controls the randomness of the agent's responses.  
    b) It determines the length of the agent's responses.  
    c) It specifies the number of tools the agent can use.  
    d) It manages the agent's memory and context.  

---

## Section 3: Markdown Basics (5 Questions)  
**31.** What is the correct Markdown syntax for creating a hyperlink?  
    a) `[link text](URL)`  
    b) `<a href="URL">link text</a>`  
    c) `[[link text]](URL)`  
    d) `{link text}(URL)`  

**32.** How do you create an unordered list in Markdown?  
    a) Using asterisks (*) or hyphens (-) before each item  
    b) Using numbers (1., 2., etc.) before each item  
    c) Using the `<ul>` and `<li>` tags  
    d) Using the `list:` keyword  

**33.** What is the Markdown syntax for inserting an image?  
    a) `![alt text](image URL)`  
    b) `<img src="image URL" alt="alt text">`  
    c) `[image: alt text](image URL)`  
    d) `{image}(image URL)`  

**34.** How do you create a level 2 heading in Markdown?  
    a) `## Heading 2`  
    b) `# Heading 2`  
    c) `**Heading 2**`  
    d) `<h2>Heading 2</h2>`  

**35.** What is the purpose of using backticks (`) in Markdown?  
    a) To create inline code snippets  
    b) To emphasize text  
    c) To create hyperlinks  
    d) To insert images  

---

## Section 4: General AI Concepts (5 Questions)  
**36.** What is the primary difference between supervised and unsupervised learning?  
    a) Supervised learning uses labeled data, while unsupervised learning does not.  
    b) Supervised learning is used for classification, while unsupervised learning is for regression.  
    c) Supervised learning requires more computational power than unsupervised learning.  
    d) Unsupervised learning is always more accurate than supervised learning.  

**37.** Which of the following is a key characteristic of agentic AI?  
    a) It operates without any human intervention.  
    b) It can autonomously make decisions and take actions to achieve goals.  
    c) It is limited to performing predefined tasks without adaptation.  
    d) It relies solely on rule-based systems.  

**38.** What is the role of reinforcement learning in AI agents?  
    a) To train agents to make decisions based on rewards and penalties  
    b) To classify data into predefined categories  
    c) To generate natural language responses  
    d) To optimize database queries  

**39.** Which of the following is a common application of natural language processing (NLP)?  
    a) Image recognition  
    b) Sentiment analysis  
    c) Pathfinding algorithms  
    d) Data encryption  

**40.** What is the purpose of transfer learning in AI?  
    a) To transfer data between different AI models  
    b) To apply knowledge gained from one task to improve performance on another task  
    c) To reduce the size of the AI model  
    d) To increase the computational speed of the AI model  

---

## Section 5: Code Analysis and Debugging (8 Questions)  
**41.** Consider the following code snippet:  
```python  
from openai.agents import Agent, function_tool  
from pydantic import BaseModel  

class CalculatorInput(BaseModel):  
    a: int  
    b: int  

@function_tool  
def add(input: CalculatorInput):  
    return input.a + input.b  

agent = Agent(tools=[add])  
result = agent.run("Add 5 and 3")  
```  
What will be the output of this code?  
    a) 8  
    b) "Add 5 and 3"  
    c) An error, because the input is not in the correct format  
    d) None  

**42.** In the OpenAI Agents SDK, what happens if a tool's function does not return a value?  
    a) The agent loop continues without any issues.  
    b) The agent raises an exception and stops execution.  
    c) The tool's output is assumed to be None.  
    d) The agent retries the tool call.  

**43.** Consider the following code snippet:  
```python  
from openai.agents import Agent, Runner  
agent = Agent(tools=[])  
runner = Runner(agent)  
try:  
    result = runner.run_sync("Hello")  
except Exception as e:  
    print(type(e))  
```  
What type of exception is likely to be printed?  
    a) `TypeError`  
    b) `ValueError`  
    c) `RuntimeError`  
    d) `AgentExecutionError`  

**44.** Which of the following is a common debugging technique for agentic AI systems?  
    a) Analyzing the agent's logs and tracing the execution path  
    b) Increasing the temperature parameter  
    c) Reducing the number of tools available to the agent  
    d) Disabling all error handling mechanisms  

**45.** In the context of async programming, what is the purpose of the `await` keyword?  
    a) To pause the execution of an async function until a promise is resolved  
    b) To define a new async function  
    c) To handle exceptions in async code  
    d) To run multiple async functions in parallel  

**46.** Consider the following code snippet:  
```python  
from openai.agents import Agent, function_tool  
from pydantic import BaseModel  

class GreetInput(BaseModel):  
    name: str  

@function_tool  
async def greet(input: GreetInput):  
    return f"Hello, {input.name}!"  

agent = Agent(tools=[greet])  
```  
What is the significance of the `async` keyword in the tool definition?  
    a) It allows the tool to run asynchronously, enabling non-blocking operations.  
    b) It makes the tool execute faster.  
    c) It restricts the tool to only handle synchronous inputs.  
    d) It automatically handles exceptions within the tool.  

**47.** Which of the following is a best practice for error handling in agentic AI systems?  
    a) Catch all exceptions and ignore them to prevent the agent from stopping.  
    b) Log detailed error messages and provide fallback mechanisms.  
    c) Avoid using try-except blocks to simplify the code.  
    d) Raise custom exceptions for every possible error condition.  

**48.** In the OpenAI Agents SDK, how can you inspect the agent's context during execution?  
    a) By accessing the `context` attribute of the agent object  
    b) By using the `Runner.get_context()` method  
    c) By analyzing the logs generated by the runner  
    d) It is not possible to inspect the context during execution.  

---

## Answer Key  
1. b  
2. a  
3. b  
4. b  
5. b  
6. a  
7. b  
8. a  
9. b  
10. b  
11. a  
12. a  
13. d  
14. c  
15. d  
16. b  
17. a  
18. b  
19. a  
20. a  
21. b  
22. a  
23. b  
24. b  
25. b  
26. a  
27. a  
28. b  
29. a  
30. a  
31. a  
32. a  
33. a  
34. a  
35. a  
36. a  
37. b  
38. a  
39. b  
40. b  
41. c  
42. c  
43. d  
44. a  
45. a  
46. a  
47. b  
48. a  

---

This quiz is designed to be highly challenging, requiring a deep understanding of the OpenAI Agents SDK, prompt engineering, and related concepts. It includes a mix of theoretical questions, code analysis, and practical scenarios to ensure a comprehensive assessment of the test-taker's skills. The questions are crafted to match the difficulty level of a Stanford graduate-level test, as specified by Mu Sir. Good luck!