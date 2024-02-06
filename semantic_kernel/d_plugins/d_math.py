# from semantic_kernel.skill_definition import (
#     sk_function,
#     sk_function_context_parameter,
# )

from semantic_kernel.plugin_definition import (
    kernel_function,
    kernel_function_context_parameter,
)

# from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.orchestration.kernel_context import KernelContext



class d_MathPlugin:
    @kernel_function(
        description="Calculates 2 elevated to the power provided",
        name="two_elevated_to_power",
        input_description="The power to elevate the base 2",
    )
    def two_elevated_to_power(self, power: str) -> str:
        """ Calculates the result of 2 elevated to <power> """
        return str (2 ** float(power))