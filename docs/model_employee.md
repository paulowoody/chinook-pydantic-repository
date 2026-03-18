[Back to Index](../README.md)

---

# Employee Model & Repository

This document details the `Employee` Pydantic model and its corresponding `EmployeeRepository`.

## Pydantic Model: Employee

The `Employee` model represents an employee in the music database.

- **`employee_id`**: The unique identifier for the employee.
- **`last_name`**: The last name of the employee (max length 20).
- **`first_name`**: The first name of the employee (max length 20).
- **`title`**: The job title of the employee (max length 30).
- **`reports_to`**: The employee ID of this person's manager.
- **`birth_date`**: The employee's birth date (datetime).
- **`hire_date`**: The date the employee was hired (datetime).
- **`address`**: The employee's street address (max length 70).
- **`city`**: The city where the employee resides (max length 40).
- **`state`**: The state or province where the employee resides (max length 40).
- **`country`**: The country where the employee resides (max length 40).
- **`postal_code`**: The postal code for the employee's address (max length 10).
- **`phone`**: The employee's phone number (max length 24).
- **`fax`**: The employee's fax number (max length 24).
- **`email`**: The employee's email address (max length 60).

## Repository: EmployeeRepository

`EmployeeRepository` provides access to the `employee` table.

### Example Usage

```python
from chinook_pydantic_repository.database import DatabasePoolManager
from chinook_pydantic_repository.repository import EmployeeRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = EmployeeRepository(pool)

# Get an employee by ID
employee = repo.get_by_id(1)
print(f"Employee: {employee.first_name} {employee.last_name}, Title: {employee.title}")
```
