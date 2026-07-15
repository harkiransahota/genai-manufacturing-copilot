from pydantic import BaseModel

class AssemblyInstructions(BaseModel):

    assembly: str

    required_tools: list[str]

    operations: list[str]

    warnings: list[str]