from llm import ManufacturingCopilot

copilot = ManufacturingCopilot()

answer = copilot.ask(
    "Explain how to assemble a dashboard."
)

print(answer)