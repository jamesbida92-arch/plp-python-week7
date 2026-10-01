# PLP Python Week 7

## Files

- `list_warmup.py` - Demonstrates list indexing, append, remove, and len.
- `shopping_list.py` - A menu-driven shopping list manager using add, remove, show, and done.
- `list_report.py` - Prints a numbered list, counts item names with more than 4 letters, and finds the longest item.
- `screenshots/` - Contains screenshots showing each program running.

## Why check `in` before `.remove()`?

It is safer to check whether an item is in the list before calling `.remove()`. If the item does not exist, `.remove()` raises a `ValueError` and can stop the program. Using `in` first allows the program to display a helpful message instead of crashing.