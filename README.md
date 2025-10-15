# Meningitis AI Workspace Setup

This guide helps you set up your development environment using the [uv](https://github.com/astral-sh/uv) package manager.

## Prerequisites

- [Python](https://www.python.org/) (version 3.8+ recommended)
- [uv](https://github.com/astral-sh/uv) installed  
    ```sh
    pip install uv
    ```

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone https://github.com/solomon344/mrc-hackathon.git

    cd mrc-hackathon
    ```

2. **Install dependencies and set up the environment**
    ```sh
    uv sync
    ```
    This command will automatically create a virtual environment (if one does not exist) and install all dependencies in `project.toml`

3. **Activate the virtual environment**

    - **Windows**
        ```sh
        .venv\Scripts\activate
        ```
    - **macOS/Linux**
        ```sh
        source .venv/bin/activate
        ```

4. **Run the project**
    - Open `test.ipynb` and run the cells

## Additional Commands

- **Add a new package**
    ```sh
    uv pip install <package-name>
    ```

- **Export dependencies**
    ```sh
    uv pip freeze > requirements.txt for pip users
    ```

---

For more details, see the [uv documentation](https://github.com/astral-sh/uv).
