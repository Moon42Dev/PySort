# PySort

## Overview

PySort is a comprehensive Python package that provides a collection of popular sorting algorithms. It is designed for easy integration and use, making it suitable for both educational purposes and practical applications. Each sorting function prints the step-by-step process of the sorting, allowing users to understand how the algorithms work internally.

## Features

- Collection of various sorting algorithms
- Step-by-step printing of the sorting process for educational purposes
- Suitable for practical applications and learning

## Installation

You can install PySort via pip:

```bash
pip install PySort
```
If you prefer to install from the source, you can clone the repository and use the setup script:
```bash
git clone https://github.com/yourusername/PySort.git
cd PySort
pip install
```
## Usage
Here is a basic example of how to use PySort:

### Example: Bubble Sort
```python
from PySort.bubble_sort import bubble_sort

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

```
### Example: Counting Sort
```python
from PySort.counting_sort import counting_sort

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
```

## Contributing
We welcome contributions to PySort! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Ensure all tests pass.
5. Commit your changes and push to your fork.
6. Create a pull request on the main repository.
Please see the contributing guide in the docs directory for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to reach out:

- **Author**: Maemoun
- **Email**: moontouzil@example.com
- **GitHub**: [Moon42Dev](https://github.com/Moon42Dev)

