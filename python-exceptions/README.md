| File | Task Name | Description |
| :--- | :--- | :--- |
| `0-safe_print_list.py` | 0. Safe list printing | Prints `x` elements of a list without using `len()`. Gracefully handles index bounds using exceptions. |
| `1-safe_print_integer.py` | 1. Safe printing of an integers list | Prints an integer using `"{:d}".format()` format strings. Returns `True` if successful, otherwise `False` without using `type()`. |
| `2-safe_print_list_integers.py` | 2. Print and count integers | Prints the first `x` elements of a list, skipping non-integers in silence. Bubbles up an `IndexError` if `x` exceeds bounds. |
| `3-safe_print_division.py` | 3. Integers division with debug | Divides two integers and prints the result inside a `finally:` block. Returns the outcome or `None`. |
| `4-list_division.py` | 4. Divide a list | Divides elements across two lists. Outputs standard error prompts for mismatched sizes, division by zero, or bad types. |
| `5-raise_exception.py` | 5. Raise exception | Intentionally triggers and raises a standard `TypeError` exception. |
| `6-raise_exception_msg.py` | 6. Raise a message | Intentionally raises a `NameError` exception containing a custom status string. |
