# AI BuildCamp - Foundation

This repository contains the homework and exercises for the AI Engineering BuildCamp.

## Prerequisites

- **Python 3.12+**
- **[uv](https://github.com/astral-sh/uv)**: A fast Python package installer and project manager.
- **[dirdotenv](https://github.com/what/dirdotenv)** (Optional but recommended): Automatically loads environment variables from `.env` files.

## Project Initialization Reference

This project was initialized using `uv`:

```bash
# Initialize a new project
uv init
# Add dependencies
uv add jupyter openai python-dotenv
```

## Installation

1.  **Install `uv`**:
    ```bash
    pip install uv
    ```

2.  **Install `dirdotenv`** (optional):
    ```bash
    pip install dirdotenv
    # Add hook to your shell configuration (e.g., ~/.zshrc or ~/.bashrc)
    echo 'eval "$(dirdotenv hook zsh)"' >> ~/.zshrc
    source ~/.zshrc
    ```

3.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd ai-buildcamp
    ```

4.  **Install dependencies**:
    Initialize the environment and install dependencies using `uv`:
    ```bash
    uv sync
    ```

## Configuration

1.  **Create `.env` file**:
    Copy the example configuration file:
    ```bash
    cp .env.example .env
    ```

2.  **Add API Keys**:
    Open `.env` and add your API keys:
    ```bash
    OPENAI_API_KEY='your-key-here'
    # Add other keys as needed
    ```

## Usage

### Running Jupyter Notebooks

This project uses `uv` to manage the virtual environment. To run Jupyter Notebook:

```bash
uv run jupyter notebook
```

This will start the Jupyter server. You can then open `01-foundation-hw/hw1.ipynb` to run the homework assignment.

### Homework 1: Download Books

The notebook `01-foundation-hw/hw1.ipynb` contains the logic to:
1.  Fetch the list of books from a remote CSV.
2.  Download the PDFs to a local `books/` directory (ignored by git).
3.  Skip files that have already been downloaded.