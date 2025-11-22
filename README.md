# Simple Streamlit Calculator

A simple web-based calculator built with Python and the Streamlit library.

## Features

*   Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
*   Simple and intuitive user interface.
*   Includes error handling for division by zero.

## Project Structure

```
.
├── app.py           # The main Streamlit application
├── calculator.py    # Core calculator logic
├── pyproject.toml   # Project dependencies
├── README.md        # This file
...
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ABIHAAHEMD4262/GEMINI_CLI_CALCULATOR.git
    cd GEMINI_CLI_CALCULATOR
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    The project uses `uv` to manage dependencies.
    ```bash
    pip install uv
    uv pip install -r requirements.txt 
    ```
    *(Note: If `requirements.txt` does not exist, you can create it from `pyproject.toml` or install dependencies manually)*
    ```bash
    pip install streamlit
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

3.  Enter two numbers, select an operation, and click the "Calculate" button to see the result.
