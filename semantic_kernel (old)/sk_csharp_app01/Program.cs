using Microsoft.SemanticKernel; // dotnet add package Microsoft.SemanticKernel
using Microsoft.SemanticKernel.Connectors.OpenAI;
using DotNetEnv; // dotnet add package DotNetEnv

Env.Load();
#pragma warning disable CS8600 // Converting null literal or possible null value to non-nullable type.
string AZURE_OPENAI_DEPLOYMENT_NAME = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME");
string AZURE_OPENAI_ENDPOINT = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
string AZURE_OPENAI_API_KEY = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");


#pragma warning disable CS8604 // Possible null reference argument.
var builder = Kernel.CreateBuilder();
builder.AddAzureOpenAIChatCompletion(
         AZURE_OPENAI_DEPLOYMENT_NAME, // Azure OpenAI Deployment Name
         AZURE_OPENAI_ENDPOINT,        // Azure OpenAI Endpoint
         AZURE_OPENAI_API_KEY);        // Azure OpenAI Key
#pragma warning restore CS8604 // Possible null reference argument.

var kernel = builder.Build();

var prompt = @"{{$input}}
One line TLDR with the fewest words.";

var summarize_semantic_function = kernel.CreateFunctionFromPrompt(prompt, executionSettings: new OpenAIPromptExecutionSettings { MaxTokens = 100 });

string text1 = @"
1) A robot may not injure a human being or, through inaction,
allow a human being to come to harm.
2) A robot must obey orders given it by human beings except where
such orders would conflict with the First Law.
3) A robot must protect its own existence as long as such protection
does not conflict with the First or Second Law.
Give me the TLDR in exactly 5 words.";

string text2 = @"
    1st Law of Thermodynamics - Energy cannot be created or destroyed.
    2nd Law of Thermodynamics - For a spontaneous process, the entropy of the universe increases.
    3rd Law of Thermodynamics - A perfect crystal at zero Kelvin has zero entropy.";

string text3 = @"
    1. An object at rest remains at rest, and an object in motion remains in motion at constant speed and in a straight line unless acted on by an unbalanced force.
    2. The acceleration of an object depends on the mass of the object and the amount of force applied.
    3. Whenever one object exerts a force on another object, the second object exerts an equal and opposite on the first.";

string text4 = @"
    Every point mass attracts every single other point mass by a force acting along the line intersecting both points.
    The force is proportional to the product of the two masses and inversely proportional to the square of the distance between them.";


Console.WriteLine(await kernel.InvokeAsync(summarize_semantic_function, new() { ["input"] = text1 }));

Console.WriteLine(await kernel.InvokeAsync(summarize_semantic_function, new() { ["input"] = text2 }));

Console.WriteLine(await kernel.InvokeAsync(summarize_semantic_function, new() { ["input"] = text3 }));

Console.WriteLine(await kernel.InvokeAsync(summarize_semantic_function, new() { ["input"] = text4 }));