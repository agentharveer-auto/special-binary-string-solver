# Special Binary String Solver

This project solves the LeetCode "Special Binary String" problem (https://leetcode.com/problems/special-binary-string/) using a React frontend and a Python backend.

## Architecture

The application consists of three main components:

1.  **Frontend (React):** Provides a user interface for entering a binary string and displaying the result.
2.  **Backend (Python/Flask):** Implements the core algorithm for solving the problem.
3.  **API (Flask):** Exposes an API endpoint for the frontend to communicate with the backend.

## Setup

1.  Clone the repository:
    ```bash
    git clone [repository URL]
    ```
2.  Navigate to the project directory:
    ```bash
    cd special-binary-string-solver
    ```
3.  Install the backend dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Install the frontend dependencies:
    ```bash
    cd frontend
    npm install
    ```
5.  Run the backend:
    ```bash
    cd ..
    python app.py
    ```
6.  Run the frontend:
    ```bash
    cd frontend
    npm start
    ```

## References

*   LeetCode Problem: https://leetcode.com/problems/special-binary-string/
*   Flask: https://flask.palletsprojects.com/
*   React: https://react.dev/
*   pytest: https://docs.pytest.org/en/stable/
