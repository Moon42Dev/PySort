
```markdown
# Contributing to Sorting Algorithms Package

We welcome contributions to the sorting_algorithms package. Here are some guidelines to get you started.

## Reporting Issues

If you encounter any issues, please report them on the GitHub issue tracker.

## Development Setup

To set up the development environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sorting_algorithms.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sorting_algorithms
    ```
3. Install the package in editable mode along with the development dependencies:
    ```bash
    pip install -e .[dev]
    ```

## Running Tests

We use `unittest` for testing. You can run the tests with the following command:

```bash
python -m unittest discover
