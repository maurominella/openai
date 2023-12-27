from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)
from semantic_kernel.orchestration.sk_context import SKContext


class TextPlugin:
    @sk_function(
        description="Calculates the uppercase value of a string",
        name="uppercase",
        input_description="The string to convert to uppercase",
    )
    def uppercase(self, s: str) -> str:
        return str(s.upper())
    
    
    @sk_function(
        description="Calculates the lowercase value of a string",
        name="lowercase",
        input_description="The string to convert to lowercase",
    )
    def lowercase(self, s: str) -> str:
        return str(s.lower())