# Assignment 3: Symbol Table Simulation

## 📌 Overview
**Course:** Advanced Programming (CO2039)  
**Semester:** HK242 - HCMUT  
**Project:** Implementing a Symbol Table using Functional Programming

## 📂 Files Structure
```plaintext
├── Symbol.py # Symbol class definition
├── SymbolTable.py # Main implementation file (student modifies this)
├── TestSuite.py # Test cases (student writes ≥50 tests)
├── TestUtils.py # Testing utilities
├── main.py # Entry point
└── README.md
```

## 🎯 Objectives
- Simulate compiler symbol table operations
- Master functional programming techniques:
  - Higher-order functions
  - Immutable data structures
  - List operations without loops

## ⚙️ Core Operations
| Command | Format | Description |
|---------|--------|-------------|
| INSERT | `INSERT <id> <type>` | Add new identifier |
| ASSIGN | `ASSIGN <id> <value>` | Type-checked assignment |
| BEGIN/END | `BEGIN`/`END` | Manage scoping blocks |
| LOOKUP | `LOOKUP <id>` | Find identifier's scope level |
| PRINT/RPRINT | `PRINT`/`RPRINT` | Display active identifiers |

## 🚨 Error Handling
```python
Redeclared("INSERT x number")  # Duplicate declaration
Undeclared("ASSIGN y 10")      # Unknown identifier 
TypeMismatch("ASSIGN str '123'") # Invalid type assignment
UnclosedBlock(1)               # Missing END for level 1 block

## 🚀 How to Run the Program
```bash
python main.py
