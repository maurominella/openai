from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)
from semantic_kernel.orchestration.sk_context import SKContext

class mmMathPlugin:
    @sk_function(
        description="Calculates the result of <base> elevated to <power>",
        name="elevation_to_power",
        input_description="The base and the exponent",
    )    
    def elevation_to_power(self, base: str, power: str) -> str:
        """ Calculates the result of <base> elevated to <power> """
        import json
        elevation_to_power_result = {
            "result": float(base) ** float(power)
        }
        return json.dumps(elevation_to_power_result)