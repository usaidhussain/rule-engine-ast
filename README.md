**Overview**
This project implements a rule engine that determines user eligibility based on attributes like age, department, salary, and experience. The engine uses an Abstract Syntax Tree (AST) to represent and evaluate complex conditional rules. The rules can be created, combined, and evaluated dynamically using a simple API.

**Features**
Rule Creation: Define conditional rules using a string-based syntax (e.g., age > 30 AND department = 'Sales').
Rule Combination: Combine multiple rules into a single AST for efficient evaluation.
Rule Evaluation: Evaluate user attributes against the rules to determine eligibility.
Dynamic Rule Modification: The rules can be modified dynamically at runtime.

**Tech Stack**
Backend: Python (Flask)
Database: MySQL
API: RESTful APIs for rule creation, combination, and evaluation
