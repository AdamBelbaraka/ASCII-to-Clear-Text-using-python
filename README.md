# ASCII to Clear Text Converter

## Description

A simple Python script that converts ASCII numerical codes into readable text.

## Features

- **ASCII Conversion**: Converts numeric ASCII codes to characters
- **User Input**: Interactive command-line interface for easy use
- **Simple Implementation**: Clean, minimal code that's easy to understand and modify

## How It Works

The script takes a series of space-separated ASCII numeric codes as input and converts each code to its corresponding character using Python's `chr()` function. For example:

- Input: `65 100 97 109`
- Output: `Adam`

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. When prompted, enter your ASCII codes separated by spaces:
   ```
   ASCII text : 65 100 97 109
   ```

3. The script will output the converted text:
   ```
   Clear text : Adam
   ```

## Code Overview

The script contains a single main function:

- **`ascii_to_text(ascii_text)`**: Accepts a string of space-separated ASCII codes and returns the converted text

## Requirements

- Python 3.x

## Example

```python
# Input
ASCII text : 80 121 116 104 111 110

# Output
Clear text : Python
```

## License

This project is provided as-is for educational purposes.
