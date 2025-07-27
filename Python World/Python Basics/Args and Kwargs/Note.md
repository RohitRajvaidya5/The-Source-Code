# Args :

- `args` is used in Python functions when you want to allow the function to accept **more than one positional argument**, or when you **don’t know in advance how many arguments** will be passed.
- When a function uses `*args`, all additional positional arguments passed to the function are **collected into a tuple** named `args`. This makes it possible to **handle a dynamic number of arguments**.

## Example :

```python
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

```

### Output :

```text
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```
<br>

---

# Kwargs :

`**kwargs` is similar to *args, but it allows a function to accept any number of keyword arguments (i.e., arguments passed with a key=value pair).

All these keyword arguments are collected into a dictionary named kwargs.

Inside the function, you can use kwargs like any normal dictionary (using loops, .items(), .keys(), etc.).

## Example :

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Alice", age=30, country="India")
```

### Output 

```text
name = Alice
age = 30
country = India
```

---

### Real Life Examples :

1. Scenario: A Restaurant Billing System
You don’t know how many items a customer will order, so you can use `*args` to calculate the total bill dynamically. 

2. Scenario: User Profile Creation
You don’t know in advance what details a user might provide (e.g., name, age, email, address), so use `**kwargs`.
3. Scenario: Send Customized Email to Multiple Recipients



