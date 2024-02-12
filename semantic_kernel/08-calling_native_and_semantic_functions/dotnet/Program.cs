// This example shows how to use OpenAI's tool calling capability via the chat completions interface.

using Xunit; // requires "dotnet add package xunit". Tt contains the [Fact] definition
using Microsoft.SemanticKernel; // requires "dotnet add package Microsoft.SemanticKernel"
using Microsoft.SemanticKernel.Connectors.OpenAI; // requires "dotnet add package Microsoft.SemanticKernel"
using Microsoft.SemanticKernel.ChatCompletion;
using Azure.AI.OpenAI; // used for ChatCompletionsFunctionToolCall
using DotNetEnv; // requires "dotnet add package DotNetEnv"
using System.Text.Json;

// Console.WriteLine();

public class Example59_OpenAIFunctionCalling  
{  
    [Fact]   
    public async Task RunAsync()  
    {  
        // Create kernel  
        IKernelBuilder builder = Kernel.CreateBuilder();
        
        Env.Load();
        #pragma warning disable CS8600 // Converting null literal or possible null value to non-nullable type.
        string AZURE_OPENAI_DEPLOYMENT_NAME = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME");
        string AZURE_OPENAI_ENDPOINT = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
        string AZURE_OPENAI_API_KEY = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");

        #pragma warning disable CS8604  // Possible null reference argument for parameter 'deploymentName'
        builder.AddAzureOpenAIChatCompletion(  
            AZURE_OPENAI_DEPLOYMENT_NAME, // Azure OpenAI Deployment Name
            AZURE_OPENAI_ENDPOINT,        // Azure OpenAI Endpoint
            AZURE_OPENAI_API_KEY);        // Azure OpenAI Key

        Kernel kernel = builder.Build();

        // Add a plugin with some helper functions we want to allow the model to utilize.
        kernel.ImportPluginFromFunctions("HelperFunctions", new[]
        {
            kernel.CreateFunctionFromMethod(() => DateTime.UtcNow.ToString("R"), "GetCurrentUtcTime", "Retrieves the current time in UTC."),
            kernel.CreateFunctionFromMethod((string cityName) =>
                cityName switch
                {
                    "Boston"   => "61 and rainy",
                    "London"   => "55 and cloudy",
                    "Miami"    => "80 and sunny",
                    "Paris"    => "60 and rainy",
                    "Tokyo"    => "50 and sunny",
                    "Sydney"   => "75 and sunny",
                    "Tel Aviv" => "80 and sunny",
                    _          => "31 and snowing",
                },  "Get_Weather_For_City", "Gets the current weather for the specified city"),
        });

        Console.WriteLine("======== Example 1: Use automated function calling with a non-streaming prompt ========");
        {
            OpenAIPromptExecutionSettings settings = new() { ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions };
            Console.WriteLine(await kernel.InvokePromptAsync("Given the current time of day and weather, what is the likely color of the sky in Boston?", new(settings)));
            Console.WriteLine();
        }


        Console.WriteLine("======== Example 2: Use automated function calling with a streaming prompt ========");
        {
            OpenAIPromptExecutionSettings settings = new() { ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions };
            await foreach (var update in kernel.InvokePromptStreamingAsync("Given the current time of day and weather, what is the likely color of the sky in Boston?", new(settings)))
            {
                Console.Write(update);
                Console.Write("-");
            }
            Console.WriteLine();
            Console.WriteLine();
        }

        Console.WriteLine("======== Example 3: Use manual function calling with a non-streaming prompt ========");
        {
            var chat = kernel.GetRequiredService<IChatCompletionService>();
            var chatHistory = new ChatHistory();

            OpenAIPromptExecutionSettings settings = new() { ToolCallBehavior = ToolCallBehavior.EnableKernelFunctions };
            chatHistory.AddUserMessage("Given the current time of day and weather, what is the likely color of the sky in Boston?");
            while (true)
            {
                var result = (OpenAIChatMessageContent)await chat.GetChatMessageContentAsync(chatHistory, settings, kernel);

                if (result.Content is not null)
                {
                    Console.Write(result.Content);
                }

                List<ChatCompletionsFunctionToolCall> toolCalls = result.ToolCalls.OfType<ChatCompletionsFunctionToolCall>().ToList();
                if (toolCalls.Count == 0)
                {
                    break;
                }

                chatHistory.Add(result);
                foreach (var toolCall in toolCalls)
                {
                    string content = kernel.Plugins.TryGetFunctionAndArguments(toolCall, out KernelFunction? function, out KernelArguments? arguments) ?
                        JsonSerializer.Serialize((await function.InvokeAsync(kernel, arguments)).GetValue<object>()) :
                        "Unable to find function. Please try again!";

                    chatHistory.Add(new ChatMessageContent(
                        AuthorRole.Tool,
                        content,
                        metadata: new Dictionary<string, object?>(1) { { OpenAIChatMessageContent.ToolIdProperty, toolCall.Id } }));
                }
            }

            Console.WriteLine();
        }
    }    
}


public partial class Program  
{  
    public static async Task Main(string[] args)  
    {  
        // Create an instance of the class  
        var example = new Example59_OpenAIFunctionCalling();  
  
        // Call the RunAsync method  
        await example.RunAsync();  
    }  
}  