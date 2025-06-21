---

# 🔐 Quiz: OpenAI Agents SDK, Prompting & Markdown

📚 **Level**: Expert | 📈 **Questions**: 20 of 48 | 🧠 **Topics**: Agents SDK, Prompt Engineering, Markdown

---

### **Q1. In the OpenAI Agents SDK, what is the primary role of `AgentAction`?**

**Tag**: `agents-sdk`

* A. It handles tool return values
* B. It tracks user feedback
* C. It represents a tool call step during the run
* D. It validates the final agent response

---

### **Q2. What is the effect of omitting `output_type` in a custom agent definition?**

**Tag**: `agents-sdk`, `output_type`

* A. The agent will fail to respond
* B. The output will always be a JSON object
* C. The output will be returned as raw string
* D. The run will timeout

---

### **Q3. In markdown, how would you represent inline code inside a sentence?**

**Tag**: `markdown`

* A. \[code]
* B. \`code\`
* C. code
* D. (code)

---

### **Q4. When using `handoff()` in an OpenAI agent, what is its core purpose?**

**Tag**: `agents-sdk`, `handoff`

* A. Passing control to another agent
* B. Ending the conversation
* C. Saving context permanently
* D. Returning tool metadata

---

### **Q5. Which prompt is more likely to yield structured output using GPT-4-Turbo?**

**Tag**: `prompting`, `structured-output`

* A. "Tell me something about Paris"
* B. "Output a JSON with name and population of Paris"
* C. "Explain Paris"
* D. "Return a markdown list about Paris"

---

### **Q6. What will happen if a Pydantic model is passed as `output_type`, but the returned data lacks a required field?**

**Tag**: `agents-sdk`, `output_type`

* A. It is auto-filled
* B. It is ignored
* C. It raises a validation error
* D. It falls back to string output

---

### **Q7. What markdown syntax creates a level 2 heading?**

**Tag**: `markdown`

* A. == Heading ==
* B. -- Heading --
* C. ## Heading
* D. Heading

---

### **Q8. In the OpenAI SDK, what does `DynamicInstructions` enable?**

**Tag**: `agents-sdk`, `dynamic-instructions`

* A. Live tool updates
* B. User-specific context injection
* C. Embedding search
* D. Markdown formatting enforcement

---

### **Q9. What happens if you return a dictionary from an agent with `output_type` set to a Pydantic model, but the keys don’t match the model's fields?**

**Tag**: `agents-sdk`, `code-trap`

* A. It returns as-is
* B. SDK attempts best-fit mapping
* C. A validation error occurs
* D. Only matching fields are used

---

### **Q10. Which markdown symbol creates an unordered list?**

**Tag**: `markdown`

* A. -
* B. 1.
* C. #
* D. =

---

### **Q11. What is the effect of using a `TypedDict` in the `output_type` parameter of an agent?**

**Tag**: `agents-sdk`, `output_type`

* A. It disables structured output parsing
* B. It adds runtime type checking
* C. It allows structured output without needing external libraries
* D. It turns response into a dataclass

---

### **Q12. What does `tool_call()` represent in a multi-step agent run?**

**Tag**: `agents-sdk`, `tool_call`

* A. The final agent return value
* B. An intermediate system function to load state
* C. A call to a registered tool with specified arguments
* D. A placeholder until user confirms the next step

---

### **Q13. Which of the following best helps control hallucination in prompts?**

**Tag**: `prompting`

* A. Asking model to explain
* B. Prompting for JSON output
* C. Giving step-by-step examples
* D. Including URLs in prompt

---

### **Q14. What markdown symbol is used to create a blockquote?**

**Tag**: `markdown`

* A. &
* B. >
* C. @
* D. //

---

### **Q15. What does `RunContextWrapper` enable in agent creation?**

**Tag**: `agents-sdk`, `context`

* A. Adds typing to async calls
* B. Captures the SDK logs
* C. Accesses the tools, user input, and metadata dynamically
* D. Embeds Markdown directly in tool input

---

### **Q16. Which method allows for switching control to another agent during runtime?**

**Tag**: `agents-sdk`, `handoff`

* A. transfer\_to()
* B. switch\_agent()
* C. handoff()
* D. yield\_agent()

---

### **Q17. What would this Markdown render? `**Note:** *italicized text*`**

**Tag**: `markdown`

* A. **Note:** *italicized text*
* B. Note: italicized text
* C. Note: italicized text
* D. Note: italicized text

---

### **Q18. Which part of the OpenAI SDK enables chaining previous agent responses?**

**Tag**: `agents-sdk`, `context`

* A. ConversationSummaryTool
* B. DynamicInstructions
* C. Context history object
* D. AgentMemoryWrapper

---

### **Q19. In prompt engineering, what does the "few-shot" approach refer to?**

**Tag**: `prompting`

* A. Prompting with only system instructions
* B. Using API tools instead of natural language
* C. Including examples in prompt
* D. Chaining multiple models

---

### **Q20. What result does `\n` produce inside a markdown response?**

**Tag**: `markdown`

* A. Tab space
* B. Code block
* C. New line
* D. Bolded line

### **Q21.** In the OpenAI Agents SDK, what happens if a tool registered with `tool_call()` raises an exception but no error handler is defined?

**Tag**: `agents-sdk`, `error-handling`

* A. The agent logs it and continues
* B. The run fails and bubble-up the error
* C. The exception is silently ignored
* D. A default `ToolError` wrapper is returned

---

### **Q22.** When prompting GPT-4 with multiple few‑shot examples, what common trap can reduce performance?

**Tag**: `prompting`, `code-trap`

* A. Using too many examples (>10)
* B. Mixing formats between examples
* C. Providing system message inside examples
* D. Using numbered bullets instead of JSON

---

### **Q23.** In Markdown responses from agents, how can you force a literal backtick (`` ` ``) to appear?

**Tag**: `markdown`, `code-trap`

* A. Use triple backticks: \`\`\`\`\`
* B. Escape with backslash: ``\` ``
* C. Surround with single quotes: ``'`'``
* D. Use HTML entity: `&#96;`

---

### **Q24.** What is a key benefit of using a `TypedDict` over `Pydantic` for `output_type`?

**Tag**: `agents-sdk`, `structured-output`

* A. Faster runtime performance
* B. Runtime validation built-in
* C. More verbose error messages
* D. Supports nested schema structures

---

### **Q25.** In `DynamicInstructions`, using variables from the run context incorrectly can cause?

**Tag**: `agents-sdk`, `dynamic-instructions`, `code-trap`

* A. Early template rendering error
* B. Infinite instruction loops
* C. Tool registration failure
* D. Silent fallback to default instructions

---

### **Q26.** Which approach helps ensure JSON output without the agent adding extraneous fields?

**Tag**: `prompting`, `structured-output`

* A. Provide an explicit schema in the prompt
* B. Use few-shot examples in plain text
* C. Ask the agent to “think step by step”
* D. Insert an emoji before JSON

---

### **Q27.** If you define `output_type` as a dataclass, what happens when unknown extra keys are returned?

**Tag**: `agents-sdk`, `code-trap`, `structured-output`

* A. They’re dropped silently
* B. A validation exception is thrown
* C. They’re added as new attributes
* D. They’re stored in `.extra`

---

### **Q28.** In Markdown, how do you create a nested unordered list?

**Tag**: `markdown`

* A. Use four spaces before hyphen
* B. Use two tabs before hyphen
* C. Use dash then asterisks: `-*`
* D. Use `>- -` sequence

---

### **Q29.** What side effect can using `handoff()` inside `DynamicInstructions` cause?

**Tag**: `agents-sdk`, `handoff`, `dynamic-instructions`

* A. Instructions ignored in downstream agent
* B. Tool set reset to default
* C. Context history wiped
* D. Nested JSON overflow

---

### **Q30.** When defining a custom tool, why include `description` metadata?

**Tag**: `agents-sdk`, `tool-definition`

* A. Enables better auto‑documentation
* B. Prevents missing return types
* C. Forces sync execution
* D. Required by the SDK or run fails

---

### **Q31.** A prompt instructs "Return an array of strings", but agent returns objects. This is likely caused by?

**Tag**: `prompting`, `code-trap`

* A. Model misunderstanding instructions
* B. Hidden default format in system prompt
* C. Lack of example outputs
* D. Using `\n` instead of comma

---

### **Q32.** In Markdown, how do you insert an HTML comment that won’t display?

**Tag**: `markdown`

* A. `<!-- comment -->`
* B. `[* comment *]`
* C. `[//]: # (comment)`
* D. `\\<!-- comment -->`

---

### **Q33.** What is the risk of enabling logging of full tool inputs/outputs in production?

**Tag**: `agents-sdk`, `privacy`, `security`

* A. Memory leak risk
* B. Exposing sensitive user data
* C. Increased latent runtime errors
* D. Overriding tokenizer length

---

### **Q34.** Which method ensures an agent continues running if a circuit breaker trips?

**Tag**: `agents-sdk`, `error-handling`, `code-trap`

* A. Use `try_tool=True` in `tool_call()`
* B. Wrap tool\_call in `retry()` decorator
* C. Catch `ToolError` inside tool definition
* D. Set `safe_mode=True` on agent

---

### **Q35.** How can you prevent a Markdown hyphen at line-start from converting to list?

**Tag**: `markdown`, `code-trap`

* A. Escape it: `\- text`
* B. Wrap line in backticks
* C. Prefix with + instead
* D. Use HTML `<span>text</span>`

---

### **Q36.** What behavior does `RunContextWrapper.state` usually expose?

**Tag**: `agents-sdk`, `context`

* A. The entire LM call input
* B. Active tool definitions
* C. Historical user-tool messages
* D. Memory footprint metrics

---

### **Q37.** In structured prompting, why include a JSON schema in the prompt?

**Tag**: `prompting`, `structured-output`

* A. To normalize date formatting
* B. To enforce key ordering
* C. To guide models to expected types
* D. To avoid proper nouns

---

### **Q38.** What is MarkDown’s way to escape asterisks so they aren’t italic?

**Tag**: `markdown`

* A. `\* literal *`
* B. `**literal**`
* C. `\*\*literal\*\*`
* D. `*literal*`

---

### **Q39.** In the SDK, what happens if you send a large context causing truncation?

**Tag**: `agents-sdk`, `context`, `code-trap`

* A. SDK auto-splits payload
* B. Run errors out immediately
* C. Truncation via LLM silently
* D. Only latest messages kept

---

### **Q40.** Why use `handshake()` vs `handoff()` when chaining agents?

**Tag**: `agents-sdk`, `handoff`

* A. `handshake()` preserves context buffer
* B. `handoff()` automatically ends run
* C. `handshake()` logs agent metadata
* D. They are identical

---

### **Q41.** Prompt asks “List 3 facts” but answer has 4. What trap caused this?

**Tag**: `prompting`, `code-trap`

* A. No stop sequence defined
* B. Model exceeded token quota
* C. Incomplete schema enforcement
* D. Too many few‑shot examples

---

### **Q42.** To render fenced code block with language highlighting, what syntax?

**Tag**: `markdown`

* A. ` ```python\n…``` `
* B. `~~~python\n…~~~`
* C. `---python\n…---`
* D. `>>> python\n…`

---

### **Q43.** What trap occurs when using `DynamicInstructions` with mutable defaults?

**Tag**: `agents-sdk`, `context`, `code-trap`

* A. Shared memory across runs
* B. `NoneType` conversion errors
* C. Nested instructions drop out
* D. Overwriting built‑in methods

---

### **Q44.** In Markdown, how to prevent a URL from auto-linking?

**Tag**: `markdown`, `code-trap`

* A. Wrap in `< >`
* B. Escape dots: `example\.com`
* C. Surround URL with backticks
* D. Use HTML `<a>` tag

---

### **Q45.** What’s a limitation of using dataclasses with `output_type`?

**Tag**: `agents-sdk`, `structured-output`, `code-trap`

* A. No runtime validation
* B. Cannot be nested
* C. Slower than TypedDict
* D. Always JSON-serialized

---

### **Q46.** Using nested Markdown lists and code fences, what can break parsing?

**Tag**: `markdown`, `code-trap`

* A. Mixing tabs and spaces
* B. Using \`’\` inside code fence
* C. Having blank line before fence
* D. Using >blockquote inside code

---

### **Q47.** Why might GPT‑4 forget earlier prompts in a large chain?

**Tag**: `prompting`, `context`, `code-trap`

* A. System message limits
* B. Context window exceeded
* C. DynamicInstructions override memory
* D. Running in streaming mode

---

### **Q48.** How can an agent output both Markdown and raw JSON without formatting issues?

**Tag**: `agents-sdk`, `markdown`, `structured-output`

* A. Wrap JSON in triple backticks
* B. Return JSON via `tool_call()` only
* C. Escape quotes in JSON
* D. Use separate agent branches

---

---


---

## ✅ **Answer Key with Explanations (1–48)**

1. **C** – `AgentAction` captures execution of a tool call.

2. **C** – No `output_type` means the agent returns raw string output.

3. **B** – Inline code in markdown uses backticks: `` `code` ``.

4. **A** – `handoff()` delegates the conversation to another agent/tool.

5. **B** – Prompting for a JSON with specific fields enables structured output.

6. **C** – A required field missing from a Pydantic model causes a validation error.

7. **C** – `##` in markdown denotes a level 2 heading.

8. **B** – `DynamicInstructions` allow injecting user-specific or runtime context.

9. **C** – A mismatch between dictionary keys and model fields leads to a validation error.

10. **A** – `-` denotes an unordered list in markdown.

11. **C** – `TypedDict` allows structured output parsing without extra libraries.

12. **C** – `tool_call()` is used to call a registered tool with provided arguments.

13. **C** – Few-shot prompting reduces hallucination by guiding model behavior.

14. **B** – `>` is used for blockquotes in markdown.

15. **C** – `RunContextWrapper` provides access to tools, inputs, and metadata.

16. **C** – `handoff()` switches control to another agent.

17. **A** – It renders **bold** and *italic* together in markdown.

18. **C** – Context object retains previous agent outputs for chaining.

19. **C** – Few-shot prompting means including structured examples in the prompt.

20. **C** – `\n` adds a new line in markdown.

21. **B** – An unhandled exception in a tool fails the run unless explicitly caught.

22. **B** – Mixing output formats leads to inconsistent structured results.

23. **A** – Use triple backticks inside triple backticks with different language specifiers.

24. **A** – `TypedDict` provides static typing with less runtime overhead than Pydantic.

25. **A** – Template errors arise when variables are undefined in structured prompts.

26. **A** – Using schema in prompts encourages correct data types and structure.

27. **A** – `@dataclass` silently drops extra fields not defined in the class.

28. **A** – Four spaces are required for nested bullet lists in markdown.

29. **A** – Using `handoff()` inside dynamic instructions breaks continuity.

30. **A** – Tool descriptions improve auto-generated docs and agent clarity.

31. **B** – System prompts override user instructions if not explicitly controlled.

32. **C** – `[//]: # (This is a comment)` is a valid markdown comment.

33. **B** – Logging inputs/outputs without sanitization can leak PII or secrets.

34. **C** – Catching `ToolError` allows continuing execution gracefully.

35. **A** – Escaping hyphens (`\-`) prevents auto-list rendering.

36. **C** – `.state` object stores interaction history between agent and tool.

37. **C** – Including schema in instructions improves model output alignment.

38. **A** – Escaping `*` as `\*` is necessary to avoid italic formatting.

39. **D** – The SDK truncates long histories to fit the context window.

40. **A** – `handshake()` maintains shared context between agents unlike `handoff()`.

41. **A** – Without a stop-sequence, the model continues beyond expected output.

42. **A** – Use \`\`\`json to highlight code blocks with JSON formatting.

43. **A** – Mutable defaults in functions persist across runs and can cause bugs.

44. **C** – Wrapping links in backticks avoids automatic link rendering.

45. **A** – `dataclass` does not enforce runtime field validation like Pydantic.

46. **A** – Mixing tabs and spaces in Python causes `IndentationError`.

47. **B** – Too much historical context exceeds model token limit.

48. **A** – Wrapping JSON in backticks helps preserve structure in markdown.

---
