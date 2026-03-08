# Response APIs

## UV Installation
- On Linux / macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- On Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Setup Steps
- **CD** into the folder
- Create the environment: `uv init . --python 3.13`
- Add libraries:
  - Automatically: `uv add $(cat requirements.txt) --prerelease=allow`
  - Manually: `uv add <package-name> --prerelease=allow`
- Synchronize to create the file structure: `uv sync --prerelease=allow`
- Activate the environment:
  - On Linux/macOS: `source .venv/bin/activate`
  - On Windows: `.\.venv\Scripts\activate.ps1`
- To deactivate: `deactivate`
- Create kernel for the jupyter notebook: ```python -m ipykernel install --name responses --use```