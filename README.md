# Holberton School – ChatGPT Introduction
[![Language](https://img.shields.io/badge/language-Python%203.x-blue)](https://python.org)
[![Web](https://img.shields.io/badge/web-HTML%2FCSS%2FJS-orange)](debugging/change_background.html)

## Description

This repository contains programming exercises demonstrating how to use ChatGPT for debugging and automation in Python and web development. The focus is on:

- **AI-assisted error identification and resolution**
- **Automated code and documentation generation**
- **Testing and code style enforcement**

All programs are designed to be robust, with error handling and clear user interaction. This project is part of the Holberton School curriculum to help you integrate AI into your coding workflow and improve your productivity.

---

## Repository Structure

```
├── factorial.py             # Iterative factorial calculation
├── factorial_recursive.py   # Recursive factorial calculation with documentation
├── print_arguments.py       # Command-line argument processing utility
├── checkbook.py             # Banking system simulation with deposit/withdrawal operations
├── mines.py                 # Complete Minesweeper game implementation
├── tic.py                   # Interactive Tic-Tac-Toe game
├── change_background.html   # Interactive web page with color changing functionality

```

## Programs Overview

### Web Development
- **`change_background.html`**
  - Interactive HTML page with JavaScript functionality
  - Click button to randomly change background color
  - Demonstrates DOM manipulation and event handling

### Python Applications

#### Mathematical Utilities
- **`factorial.py`**
  - Calculates factorial using iterative approach
  - Usage: `./factorial.py <number>`
  - Example: `./factorial.py 5` outputs `120`

- **`factorial_recursive.py`**
  - Recursive factorial implementation with comprehensive documentation
  - Includes function docstring and error handling
  - Usage: `./factorial_recursive.py <number>`

#### Games
- **`mines.py`**
  - Full-featured Minesweeper game
  - Customizable board size and mine count
  - Features: auto-reveal, win/lose detection, clear interface
  - Run: `./mines.py`

- **`tic.py`**
  - Interactive Tic-Tac-Toe game
  - Two-player gameplay with input validation
  - Win condition detection and board display
  - Run: `./tic.py`

#### System Utilities
- **`checkbook.py`**
  - Banking simulation with deposit/withdrawal functionality
  - Balance tracking and insufficient funds protection
  - Interactive menu system
  - Run: `./checkbook.py`

- **`print_arguments.py`**
  - Utility to display command-line arguments
  - Usage: `./print_arguments.py arg1 arg2 arg3`
  - Demonstrates sys.argv handling


## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/adi-mart/holbertonschool-chatgpt-introduction.git
cd debugging
```

2. **Make Python scripts executable:**
```bash
chmod +x *.py
```

3. **Verify Python installation:**
```bash
python3 --version
```

## Requirements

- **Python**: Version 3.x
- **Web Browser**: Any modern browser for HTML file
- **Operating System**: Cross-platform compatible

## Learning Objectives

This collection demonstrates:
- AI-assisted debugging techniques
- Code optimization and enhancement
- Error handling implementation
- User input validation
- Game logic development
- Web development fundamentals
- Documentation best practices

## License

This project was realized as part of the Holberton School curriculum.
