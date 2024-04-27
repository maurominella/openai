# Configuration File

An overview of all configurations available in the config file, which is located at `project/taskweaver_config.json`.
You can edit this file to configure TaskWeaver.
:::tip
The configuration file is in JSON format. So for boolean values, use `true` or `false` instead of `True` or `False`.
For null values, use `null` instead of `None` or `"null"`. All other values should be strings in double quotes.
:::
The following table lists the parameters in the configuration file:

| Parameter                                     | Description                                                                            | Default Value                                                                                                                               |
|-----------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `llm.model`                                   | The model name used by the language model.                                             | gpt-4                                                                                                                                       |
| `llm.api_base`                                | The base URL of the OpenAI API.                                                        | `https://api.openai.com/v1`                                                                                                                 |
| `llm.api_key`                                 | The API key of the OpenAI API.                                                         | `null`                                                                                                                                      |
| `llm.api_type`                                | The type of the OpenAI API, could be `openai` or `azure`.                              | `openai`                                                                                                                                    |
| `llm.api_version`                             | The version of the OpenAI API.                                                         | `2023-07-01-preview`                                                                                                                        |
| `llm.response_format`                         | The response format of the OpenAI API, could be `json_object`, `text` or `null`.       | `json_object`                                                                                                                               |
| `llm.embedding_api_type`                      | The type of the embedding API                                                          | `sentence_transformers`                                                                                                                     |
| `llm.embedding_model`                         | The name of the embedding model                                                        | `all-mpnet-base-v2`                                                                                                                         |
| `code_interpreter.code_verification_on`       | Whether to enable code verification.                                                   | `false`                                                                                                                                     |
| `code_interpreter.allowed_modules`            | The list of allowed modules to import in code generation.                              | `["pandas", "matplotlib", "numpy", "sklearn", "scipy", "seaborn", "datetime", "typing"]`, if the list is empty, no modules would be allowed |
| `code_interpreter.blocked_functions`          | The list of functions to block from code generation.                                   | `["__import__", "eval", "exec", "execfile", "compile", "open", "input", "raw_input", "reload"]`                                             |
| `logging.log_file`                            | The name of the log file.                                                              | `taskweaver.log`                                                                                                                            |
| `logging.log_folder`                          | The folder to store the log file.                                                      | `logs`                                                                                                                                      |
| `plugin.base_path`                            | The folder to store plugins.                                                           | `${AppBaseDir}/plugins`                                                                                                                     |
| `planner.example_base_path`                   | The folder to store planner examples.                                                  | `${AppBaseDir}/planner_examples`                                                                                                            |
| `planner.prompt_compression`                  | Whether to compress the chat history for planner.                                      | `false`                                                                                                                                     | 
| `planner.use_experience`                      | Whether to use experience summarized from the previous chat history in planner.        | `false`                                                                                                                                     |
| `code_generator.example_base_path`            | The folder to store code interpreter examples.                                         | `${AppBaseDir}/codeinterpreter_examples`                                                                                                    |
| `code_generator.prompt_compression`           | Whether to compress the chat history for code interpreter.                             | `false`                                                                                                                                     |
| `code_generator.enable_auto_plugin_selection` | Whether to enable auto plugin selection.                                               | `false`                                                                                                                                     |
| `code_generator.use_experience`               | Whether to use experience summarized from the previous chat history in code generator. | `false`                                                                                                                                     |                      
| `code_generator.auto_plugin_selection_topk`   | The number of auto selected plugins in each round.                                     | `3`                                                                                                                                         |
| `session.max_internal_chat_round_num`         | The maximum number of internal chat rounds between Planner and Code Interpreter.       | `10`                                                                                                                                        |
| `session.roles`                               | The roles included for the conversation.                                               | ["planner", "code_interpreter"]                                                                                                             |
| `round_compressor.rounds_to_compress`         | The number of rounds to compress.                                                      | `2`                                                                                                                                         |
| `round_compressor.rounds_to_retain`           | The number of rounds to retain.                                                        | `3`                                                                                                                                         |
| `execution_service.kernel_mode`               | The mode of the code executor, could be `local` or `container`.                        | `local`                                                                                                                                     |

:::tip
$\{AppBaseDir\} is the project directory.
:::

:::tip
Up to 11/30/2023, the `json_object` and `text` options of `llm.response_format` is only supported by the OpenAI
models later than 1106. If you are using an older version of OpenAI model, you need to set the `llm.response_format`
to `null`.
:::

:::tip
Read [this](../advanced/compression.md) for more information for `planner.prompt_compression` and `code_generator.prompt_compression`.
:::

:::tip
We support to set configurations via environment variables. You need to transform the configuration key to uppercase and replace the dot with underscore. 
For example, `llm.model` should be set as `LLM_MODEL`, `llm.api_base` should be set as `LLM_API_BASE`, etc.
:::

