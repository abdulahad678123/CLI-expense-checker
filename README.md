# CLI Expense Tracker

A command-line application built with Python.

## Features

- Add expenses
- List expenses
- Delete expenses
- Summarize expenses
- Store expenses in JSON
- Custom exception handling
- Command-line interface using argparse

## Requirements

Python 3.12+

## Usage

Add an expense:

python -m expense_tracker.main add --title "Lunch" --amount 500 --category "Food"

List expenses:

python -m expense_tracker.main list

Delete an expense:

python -m expense_tracker.main delete --id 1

Summarize expenses:

python -m expense_tracker.main summary