# **Rule Engine with Abstract Syntax Tree (AST)**

## **Overview**
This project implements a rule engine that determines user eligibility based on attributes like age, department, salary, and experience. The engine uses an Abstract Syntax Tree (AST) to represent and evaluate complex conditional rules. The rules can be created, combined, and evaluated dynamically using a simple API.

## **Features**
- **Rule Creation**: Define conditional rules using a string-based syntax (e.g., `age > 30 AND department = 'Sales'`).
- **Rule Combination**: Combine multiple rules into a single AST for efficient evaluation.
- **Rule Evaluation**: Evaluate user attributes against the rules to determine eligibility.
- **Dynamic Rule Modification**: The rules can be modified dynamically at runtime.

---

## **Tech Stack**
- **Backend**: Python (Flask)
- **Database**: MySQL
- **API**: RESTful APIs for rule creation, combination, and evaluation
- **UI**: Simple frontend (if applicable)
  
---

## **Installation**

### **1. Prerequisites**
- **Python**: Version 3.8 or higher
- **MySQL**: Installed and running
- **Flask**: Python web framework
- **Git**: If cloning the repository

### **2. Clone the Repository**
   ```bash
   git clone https://github.com/your-username/rule-engine-ast.git
   cd rule-engine-ast

