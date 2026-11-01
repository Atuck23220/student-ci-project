# Student CI Project

A small Python calculator used to demonstrate Continuous Integration with Jenkins and GitHub for CMSC 426 (In-Class Activity 3). Every push to `main` triggers a Jenkins build that runs the automated tests and fails the build if any test fails.

## Project Structure

```
student-ci-project/
├── calculator.py          # multiply() and subtract() functions
├── tests/
│   └── test_calculator.py # unittest tests for both functions
├── README.md
└── .gitignore
```

## Requirements

- Python 3 (tested with Python 3.9.4)
- No third-party packages. Tests use Python's built-in `unittest` module.

## Running the App

From the repository root:

```bash
python3 calculator.py
```

This prints a short demo of both functions, `multiply` and `subtract`:

```
Application started
2 * 4 = 8
10 - 4 = 6
```

## Running the Tests

From the repository root:

```bash
python3 -m unittest discover -s tests -v
```

- `-s tests` tells unittest to look for tests in the `tests` folder.
- `-v` prints each test by name.
- Run this from the repository root so `calculator.py` can be imported by the tests.

Expected result: all 6 tests pass and the output ends with `OK`.

## CI Pipeline

This repository is built by a Jenkins Freestyle job named `Student-CI-Project`.

**Flow:** Developer pushes to GitHub → GitHub webhook → Jenkins → build and tests → build result

**Job configuration:**

- **Source Code Management:** Git, this repository, branch `*/main`
- **Build Trigger:** GitHub hook trigger for GITScm polling
- **GitHub Webhook:** sends push events as `application/json` to Jenkins at `/github-webhook/`, signed with a shared secret
- **Build Step:** Execute shell:

```bash
echo "=== CI Build Started ==="

echo "Checking source files..."
ls -la

echo "Python version:"
python3 --version

echo "=== Running Application Tests ==="
python3 -m unittest discover -s tests -v || { echo "TESTS FAILED"; exit 1; }

echo "=== CI Build Completed Successfully ==="
```

If any test fails, the build step exits with a nonzero code and Jenkins marks the build as **FAILURE**.
