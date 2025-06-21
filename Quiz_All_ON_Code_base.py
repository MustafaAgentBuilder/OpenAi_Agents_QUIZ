# Question 1
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="SimpleAgent", instructions="Repeat the input")
result = Runner.run_sync(agent, "Test")
print(result.final_output)
# Question: What will be the output?
# A) "Test"
# B) "Repeat the input"
# C) None
# D) An error message
None: 

# Question 2
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def multiply(a: int, b: int):
    return a * b
agent = Agent(name="MathAgent", tools=[multiply])
result = Runner.run_sync(agent, "Multiply 4 by 5")
print(result.final_output)
# Question: What will be the output?
# A) "20"
# B) "Multiply 4 by 5"
# C) 20
# D) An error message
None: 

# Question 3
# Code Snippet:
from agents import Agent, Runner
agent1 = Agent(name="Agent1", instructions="Handoff to Agent2")
agent2 = Agent(name="Agent2", instructions="Say 'Done'")
agent1.handoffs = [agent2]
result = Runner.run_sync(agent1, "Go")
print(result.final_output)
# Question: What will be the output?
# A) "Go"
# B) "Done"
# C) "Handoff to Agent2"
# D) An error message
None: B


# Question 4
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
@function_tool
def store_data(key: str, value: int, context: Context):
    context[key] = value
agent = Agent(name="StoreAgent", tools=[store_data])
Runner.run_sync(agent, "Store 'count' as 10", context=context)
print(context.get("count"))
# Question: What will be the output?
# A) 10
# B) "count"
# C) None
# D) An error message
None: 

# Question 5
# Code Snippet:
import asyncio
from agents import Agent, Runner
agent = Agent(name="AsyncAgent", instructions="Say 'Hi'")
async def run():
    result = await Runner.run(agent, "Start")
    print(result.final_output)
asyncio.run(run())
# Question: What will be the output?
# A) "Start"
# B) "Hi"
# C) An error message
# D) None
None: 

# Question 6
# Code Snippet:
from agents import Agent, Runner
from pydantic import BaseModel
class Number(BaseModel):
    value: int
agent = Agent(name="TypedAgent", output_type=Number)
result = Runner.run_sync(agent, "Return 42")
print(result.final_output.value)
# Question: What will be the output?
# A) "42"
# B) 42
# C) An error message
# D) None
None: 

# Question 7
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="LimitedAgent", instructions="Echo input")
result = Runner.run_sync(agent, "Hello", max_turns=0)
print(result.final_output)
# Question: What will be the output?
# A) "Hello"
# B) An error message
# C) None
# D) "Echo input"
None: 

# Question 8
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def crash():
    raise Exception("Crash")
agent = Agent(name="CrashAgent", tools=[crash])
result = Runner.run_sync(agent, "Use crash tool")
print(result.final_output)
# Question: What will be the output?
# A) "Crash"
# B) An error message
# C) None
# D) "Use crash tool"
None: 

# Question 9
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="NoToolAgent", tools=[])
result = Runner.run_sync(agent, "Calculate 2 + 3")
print(result.final_output)
# Question: What will be the output?
# A) 5
# B) "Calculate 2 + 3"
# C) "I can't calculate"
# D) An error message
None: 

# Question 10
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
agent1 = Agent(name="SetAgent", instructions="Set 'x' to 5 in context")
agent2 = Agent(name="GetAgent", instructions="Get 'x' from context")
agent1.handoffs = [agent2]
Runner.run_sync(agent1, "Begin", context=context)
print(context.get("x"))
# Question: What will be the output?
# A) 5
# B) "x"
# C) None
# D) An error message
None: 

# Question 11
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="DynamicAgent", instructions=lambda: "Echo input")
result = Runner.run_sync(agent, "Test")
print(result.final_output)
# Question: What will be the output?
# A) "Test"
# B) "Echo input"
# C) An error message
# D) None
None: 

# Question 12
# Code Snippet:
from agents import Agent, Runner, Prompt
prompt = Prompt(system="Say 'Yes'", user="Input")
agent = Agent(name="PromptAgent", prompt=prompt)
result = Runner.run_sync(agent, "Anything")
print(result.final_output)
# Question: What will be the output?
# A) "Anything"
# B) "Yes"
# C) "Input"
# D) An error message
None: 

# Question 13
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def add(a: int, b: int):
    return a + b
agent = Agent(name="ForcedToolAgent", tools=[add], tool_choice="add")
result = Runner.run_sync(agent, "Add 2 and 3")
print(result.final_output)
# Question: What will be the output?
# A) 5
# B) "Add 2 and 3"
# C) "I don’t know"
# D) An error message
None: 

# Question 14
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def subtract(a: int, b: int):
    return a - b
agent = Agent(name="NoToolAgent", tools=[subtract], tool_choice="none")
result = Runner.run_sync(agent, "Subtract 5 from 8")
print(result.final_output)
# Question: What will be the output?
# A) 3
# B) "Subtract 5 from 8"
# C) "I can’t subtract"
# D) An error message
None: 

# Question 15
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="OriginalAgent", instructions="Say 'Original'")
clone = agent.clone()
result = Runner.run_sync(clone, "Run")
print(result.final_output)
# Question: What will be the output?
# A) "Run"
# B) "Original"
# C) An error message
# D) None
None: 

# Question 16
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
async def async_task():
    return "Done"
agent = Agent(name="AsyncToolAgent", tools=[async_task])
result = Runner.run_sync(agent, "Use async task")
print(result.final_output)
# Question: What will be the output?
# A) "Done"
# B) An error message
# C) None
# D) "Use async task"
None: 

# Question 17
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
@function_tool
def get_data(context: Context):
    return context.get("data")
agent = Agent(name="ContextAgent", tools=[get_data])
result = Runner.run_sync(agent, "Get data", context=context)
print(result.final_output)
# Question: What will be the output?
# A) "data"
# B) None
# C) An error message
# D) "Get data"
None: 

# Question 18
# Code Snippet:
from agents import Agent, Runner, InputGuardrail
def check(input: str):
    if "error" in input:
        return GuardrailFunctionOutput(tripwire_triggered=True, message="Error detected")
    return GuardrailFunctionOutput(tripwire_triggered=False)
guardrail = InputGuardrail(check)
agent = Agent(name="GuardedAgent", input_guardrails=[guardrail])
result = Runner.run_sync(agent, "Trigger error")
print(result.final_output)
# Question: What will be the output?
# A) "Trigger error"
# B) An error message
# C) "Error detected"
# D) None
None: 

# Question 19
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="MultiTurnAgent", instructions="Echo twice")
result = Runner.run_sync(agent, "Hi", max_turns=2)
print(result.final_output)
# Question: What will be the output?
# A) "Hi"
# B) "Hi Hi"
# C) An error message
# D) None
None: 

# Question 20
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def divide(a: int, b: int):
    return a / b
agent = Agent(name="DivideAgent", tools=[divide])
result = Runner.run_sync(agent, "Divide 10 by 0")
print(result.final_output)
# Question: What will be the output?
# A) "Infinity"
# B) An error message
# C) 0
# D) None
None: 

# Question 21
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="IntAgent", instructions="Return integer", output_type=int)
result = Runner.run_sync(agent, "Return 100")
print(result.final_output)
# Question: What will be the output?
# A) "100"
# B) 100
# C) An error message
# D) None
None: 

# Question 22
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="NullAgent", instructions=None)
result = Runner.run_sync(agent, "Test")
print(result.final_output)
# Question: What will be the output?
# A) "Test"
# B) An error message
# C) None
# D) "No instructions"
None: 

# Question 23
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def greet(name: str):
    return f"Hello, {name}"
agent = Agent(name="GreetAgent", tools=[greet])
result = Runner.run_sync(agent, "Greet 'Alice'")
print(result.final_output)
# Question: What will be the output?
# A) "Hello, Alice"
# B) "Greet 'Alice'"
# C) An error message
# D) None
None: 

# Question 24
# Code Snippet:
from agents import Agent, Runner
agent1 = Agent(name="FirstAgent", instructions="Pass to next")
agent2 = Agent(name="SecondAgent", instructions="Say 'End'")
agent1.handoffs = [agent2]
result = Runner.run_sync(agent1, "Start")
print(result.final_output)
# Question: What will be the output?
# A) "Start"
# B) "End"
# C) "Pass to next"
# D) An error message
None: 

# Question 25
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
agent = Agent(name="ContextSetter", instructions="Set 'flag' to True")
Runner.run_sync(agent, "Set flag", context=context)
print(context.get("flag"))
# Question: What will be the output?
# A) True
# B) "flag"
# C) None
# D) An error message
None: 

# Question 26
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="TraceAgent", instructions="Say 'Trace'")
result = Runner.run_sync(agent, "Go", tracing=True)
print(result.tracing_data)
# Question: What will be the output?
# A) "Go"
# B) "Trace"
# C) Tracing data
# D) An error message
None: 

# Question 27
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="ModelAgent", model="gpt-4", instructions="Say 'Hi'")
result = Runner.run_sync(agent, "Run")
print(result.final_output)
# Question: What will be the output?
# A) "Run"
# B) "Hi"
# C) An error message
# D) None
None: 

# Question 28
# Code Snippet:
import asyncio
from agents import Agent, Runner, function_tool
@function_tool
async def async_sum(a: int, b: int):
    return a + b
agent = Agent(name="AsyncSumAgent", tools=[async_sum])
result = await Runner.run(agent, "Sum 3 and 4")
print(result.final_output)
# Question: What will be the output?
# A) 7
# B) "Sum 3 and 4"
# C) An error message
# D) None
None: 

# Question 29
# Code Snippet:
from agents import Agent, Runner
agent1 = Agent(name="LoopAgent1", instructions="Handoff to Agent2")
agent2 = Agent(name="LoopAgent2", instructions="Handoff to Agent1")
agent1.handoffs = [agent2]
agent2.handoffs = [agent1]
result = Runner.run_sync(agent1, "Loop", max_turns=2)
print(result.final_output)
# Question: What will be the output?
# A) "Loop"
# B) An error message
# C) None
# D) "Handoff to Agent1"
None: 

# Question 30
# Code Snippet:
from agents import Agent, Runner, OutputGuardrail
def validate(output):
    if "fail" in output:
        return GuardrailFunctionOutput(tripwire_triggered=True, message="Fail detected")
    return GuardrailFunctionOutput(tripwire_triggered=False)
guardrail = OutputGuardrail(validate)
agent = Agent(name="OutputAgent", output_guardrails=[guardrail])
result = Runner.run_sync(agent, "Say 'fail'")
print(result.final_output)
# Question: What will be the output?
# A) "fail"
# B) An error message
# C) "Fail detected"
# D) None
None: 

# Question 31
# Code Snippet:
from agents import Agent, Runner, Context
context = Context({"id": 123})
@function_tool
def fetch_id(context: Context):
    return context.get("id")
agent = Agent(name="IdAgent", tools=[fetch_id])
result = Runner.run_sync(agent, "Fetch ID", context=context)
print(result.final_output)
# Question: What will be the output?
# A) 123
# B) "id"
# C) An error message
# D) None
None: 

# Question 32
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="TypeAgent", instructions="Return number")
result = Runner.run_sync(agent, "Return 50")
print(type(result.final_output))
# Question: What will be the output?
# A) <class 'int'>
# B) <class 'str'>
# C) An error message
# D) None
None: 

# Question 33
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="InvalidAgent", instructions=42)
result = Runner.run_sync(agent, "Run")
print(result.final_output)
# Question: What will be the output?
# A) "Run"
# B) An error message
# C) 42
# D) None
None: 

# Question 34
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def echo(value: str):
    return value
agent = Agent(name="EchoAgent", tools=[echo])
result = Runner.run_sync(agent, "Echo 'Test'")
print(result.final_output)
# Question: What will be the output?
# A) "Test"
# B) "Echo 'Test'"
# C) An error message
# D) None
None: 

# Question 35
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="RunnerAgent", instructions="Say 'Done'")
runner = Runner()
result = runner.run_sync(agent, "Go")
print(result.final_output)
# Question: What will be the output?
# A) "Go"
# B) "Done"
# C) An error message
# D) None
None: 

# Question 36
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
agent = Agent(name="UpdateAgent", instructions="Set 'state' to 'active'")
Runner.run_sync(agent, "Update", context=context)
print(context.get("state"))
# Question: What will be the output?
# A) "active"
# B) "state"
# C) None
# D) An error message
None

# Question 37
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="SlowAgent", instructions="Say 'Slow'")
result = Runner.run_sync(agent, "Run", timeout=0.001)
print(result.final_output)
# Question: What will be the output if the agent takes longer than 0.001 seconds?
# A) "Slow"
# B) An error message
# C) None
# D) "Run"
None: 

# Question 38
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def fail():
    return 1 / 0
agent = Agent(name="FailAgent", tools=[fail])
result = Runner.run_sync(agent, "Use fail")
print(result.final_output)
# Question: What will be the output?
# A) "Infinity"
# B) An error message
# C) 0
# D) None
None: 

# Question 39
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="BadModelAgent", model="invalid-model", instructions="Say 'Hi'")
result = Runner.run_sync(agent, "Run")
print(result.final_output)
# Question: What will be the output?
# A) "Hi"
# B) An error message
# C) None
# D) "Run"
None: 

# Question 40
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def async_wrong():
    async def inner():
        return "Wrong"
    return inner()
agent = Agent(name="WrongAgent", tools=[async_wrong])
result = Runner.run_sync(agent, "Use tool")
print(result.final_output)
# Question: What will be the output?
# A) "Wrong"
# B) An error message
# C) None
# D) "Use tool"
None: 

# Question 41
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
agent1 = Agent(name="A1", instructions="Set 'val' to 99")
agent2 = Agent(name="A2", instructions="Get 'val'")
Runner.run_sync(agent1, "Set", context=context)
result = Runner.run_sync(agent2, "Get", context=context)
print(result.final_output)
# Question: What will be the output?
# A) 99
# B) "val"
# C) None
# D) An error message
None: 

# Question 42
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="ZeroTurnAgent", instructions="Echo")
result = Runner.run_sync(agent, "Hi", max_turns=0)
print(result.final_output)
# Question: What will be the output?
# A) "Hi"
# B) An error message
# C) None
# D) "Echo"
None: 

# Question 43
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def sum_nums(a: int, b: int):
    return a + b
agent = Agent(name="SumAgent", tools=[sum_nums])
result = Runner.run_sync(agent, "Sum 7 and 8")
print(result.final_output)
# Question: What will be the output?
# A) 15
# B) "Sum 7 and 8"
# C) An error message
# D) None
None: 

# Question 44
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="NoHandoffAgent", instructions="Handoff to next")
result = Runner.run_sync(agent, "Start")
print(result.final_output)
# Question: What will be the output?
# A) "Start"
# B) An error message
# C) "Handoff to next"
# D) None
None: 

# Question 45
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
@function_tool
def update_context(context: Context):
    context["status"] = "ok"
agent = Agent(name="UpdaterAgent", tools=[update_context])
Runner.run_sync(agent, "Update", context=context)
print(context.get("status"))
# Question: What will be the output?
# A) "ok"
# B) "status"
# C) None
# D) An error message
None: 

# Question 46
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="NoTraceAgent", instructions="Say 'No'")
result = Runner.run_sync(agent, "Run", tracing=False)
print(result.tracing_data)
# Question: What will be the output?
# A) "No"
# B) None
# C) An error message
# D) "Run"
None: 

# Question 47
# Code Snippet:
import asyncio
from agents import Agent, Runner
agent = Agent(name="AsyncEchoAgent", instructions="Echo input")
async def execute():
    result = await Runner.run(agent, "Async")
    print(result.final_output)
asyncio.run(execute())
# Question: What will be the output?
# A) "Async"
# B) An error message
# C) None
# D) "Echo input"
None: 

# Question 48
# Code Snippet:
from agents import Agent, Runner, function_tool
@function_tool
def process():
    return "Processed"
agent = Agent(name="ProcessAgent", tools=[process])
result = Runner.run_sync(agent, "Run process")
print(result.final_output)
# Question: What will be the output?
# A) "Processed"
# B) "Run process"
# C) An error message
# D) None
None: 

# Question 49
# Code Snippet:
from agents import Agent, Runner
agent = Agent(name="SingleTurnAgent", instructions="Echo once")
result = Runner.run_sync(agent, "Once", max_turns=1)
print(result.final_output)
# Question: What will be the output?
# A) "Once"
# B) "Echo once"
# C) An error message
# D) None
None: 

# Question 50
# Code Snippet:
from agents import Agent, Runner, Context
context = Context()
agent1 = Agent(name="Setter", instructions="Set 'count' to 1")
agent2 = Agent(name="Getter", instructions="Get 'count'")
Runner.run_sync(agent1, "Set", context=context)
result = Runner.run_sync(agent2, "Get", context=context)
print(result.final_output)
# Question: What will be the output?
# A) 1
# B) "count"
# C) None
# D) An error message
None: 

# Answer Key:
# 1:A, 2:C, 3:B, 4:A, 5:B, 6:B, 7:B, 8:B, 9:C, 10:A,
# 11:A, 12:B, 13:A, 14:C, 15:B, 16:B, 17:B, 18:B, 19:B, 20:B,
# 21:B, 22:B, 23:A, 24:B, 25:A, 26:C, 27:B, 28:A, 29:B, 30:B,
# 31:A, 32:B, 33:B, 34:A, 35:B, 36:A, 37:B, 38:B, 39:B, 40:B,
# 41:A, 42:B, 43:A, 44:B, 45:A, 46:B, 47:A, 48:A, 49:A, 50:A