# Mauro Minella repository for storing samples about Open AI technologies

# Environment preparation

## 1. Install Git from its [WEB site](https://git-scm.com/downloads), choosing your operating system

## 2. Open a git/bash command prompt, or make sure that git executable is in the path

## 3. ***CD*** into the base folder for your git repositories
If you do not have one, you may create a folder called `git_repos`

## 4. Use `git` to clone this repo locally
```git clone https://github.com/maurominella/openai.git```

## 5. Create a sub-folder of the base `git_repos` called `config`
**Before** moving into this folder, just copy the file `credentials_my(template).env` of the cloned repo into it:
- ```cp "./openai/credentials_my(template).env" ./config```

The file `./config/credentials_my.env` -without the final `(template)` in the name- will have to be updated with your own credentials in order to be shared among all repositories.

## 6. ***CD*** into `openai` folder of the cloned repository
```cd openai```

## 7. Install Miniconda from its [WEB site](https://www.anaconda.com/docs/getting-started/miniconda/install), choosing your operating system

## 8. Open Miniconda bash / prompt, or make sure that conda executable is in the path

## 9. Environment provisioning for Azure AI Agent Service (`openai`)

### 9.1 Remove the pre-existing conda `openai` environment (if exists)
```conda env remove -n openai -y```

### 9.2 Create new Conda Environment `openai` with Python 3.13
```conda create -n openai python=3.13 -y```

### 9.3 Activate the `openai` environment
```conda activate openai```

### 9.4 Install libraries and dependencies
```pip install -r requirements_openai.txt```

### 9.5 Remove `openai` kernel (if exists)
```jupyter kernelspec uninstall openai -y```

### 9.6 Create `openai` kernel 
```python -m ipykernel install --name openai --user```

### 9.7 Check kernels list to make sure that `openai` exists
```jupyter kernelspec list```
