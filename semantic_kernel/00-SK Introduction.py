import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

kernel = sk.Kernel()

# Set the current working directory to the folder where the Python file is located
import os
current_file_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file_path)
os.chdir(current_directory)

# Prepare Azure OpenAI service using credentials stored in the `.env` file
deployment_name, api_key, endpoint  = sk.azure_openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", AzureChatCompletion(deployment_name=deployment_name, endpoint=endpoint, api_key= api_key))

# Wrap your prompt in a function
prompt_without_input_params = kernel.create_semantic_function("""
1) A robot may not injure a human being or, through inaction,
allow a human being to come to harm.
2) A robot must obey orders given it by human beings except where
such orders would conflict with the First Law.
3) A robot must protect its own existence as long as such protection
does not conflict with the First or Second Law.
Give me the TLDR in exactly 5 words.""")


# Create a reusable function with one input parameter
prompt_with_input_params = kernel.create_semantic_function("{{$input}}\n\nOne line TLDR with the fewest words.")


# Run your prompt
# Note: functions are run asynchronously
async def main():
    print(await prompt_without_input_params()) # => Robots must not harm humans.
    
    # Summarize the laws of thermodynamics
    print(await prompt_with_input_params("""
    1st Law of Thermodynamics - Energy cannot be created or destroyed.
    2nd Law of Thermodynamics - For a spontaneous process, the entropy of the universe increases.
    3rd Law of Thermodynamics - A perfect crystal at zero Kelvin has zero entropy."""))

    # Summarize the laws of motion
    print(await prompt_with_input_params("""
    1. An object at rest remains at rest, and an object in motion remains in motion at constant speed and in a straight line unless acted on by an unbalanced force.
    2. The acceleration of an object depends on the mass of the object and the amount of force applied.
    3. Whenever one object exerts a force on another object, the second object exerts an equal and opposite on the first."""))

    # Summarize the law of universal gravitation
    print(await prompt_with_input_params("""
    Every point mass attracts every single other point mass by a force acting along the line intersecting both points.
    The force is proportional to the product of the two masses and inversely proportional to the square of the distance between them."""))

if __name__ == "__main__":
    asyncio.run(main())