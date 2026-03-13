# Response APIs

## UV Installation
- On Linux / macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- On Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Setup Steps
- **CD** into the folder
- Create the environment: `uv init . --python 3.13`
- Create the local virtual environment: `uv venv`
- Activate the environment:
  - On Linux/macOS: `source .venv/bin/activate`
  - On Windows: `.\.venv\Scripts\activate.ps1`
- Add libraries (it's KEY to use `--active`):
  - Automatically: `uv add --active $(cat requirements.txt) --prerelease=allow`
  - Manually: `uv add --active <package-name> --prerelease=allow`
- Check that the packges are installed: `uv pip list`
- Synchronize to create the file structure: `uv sync --active --prerelease=allow`
- To deactivate: `deactivate`
- Create kernel for the jupyter notebook: ```python -m ipykernel install --name responses --use```
- Test Python:
```
python - << 'EOF'
import agent_framework
print("OK:", agent_framework)
EOF
```
