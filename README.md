# Get started

# Features
- [x] User registration
- [x] User login
- [x] User logout
- [x] User profile
- [x] User profile update




Ensure you have nodejs `node -v` and python 3.12 `python -V` installed.

If not install via:

- [pyenv](https://github.com/pyenv/pyenv-installer)

- [node version manager](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)

1. Clone the repo
    ```
    git clone --depth 1 && cd twix_api
    ```
2. Activate a virtual environment and install python dependencies
    ```
    python -m venv .venv
    ```
    ```
    source .venv/bin/activate
    ```
    ```
    pip install -r requirements.txt
    ```
    <!-- ```
    cd backend
    ```
    cd frontend
    ``` -->
3. Split the terminal and cd into the frontend
    ```
    cd frontend && npm install
    ```
4. Start the frontend
    ```
    npm run dev
    ```
