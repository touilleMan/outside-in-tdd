From:

- <https://www.youtube.com/watch?v=XHnuMjah6ps>

## Problem description - Bank kata

Create a simple bank application with the following fetaures:

- Deposit into an Account
- Withdraw from an Account
- Print a bank statement to the console

## Acceptance criteria

Statement should have transactions in the following format:

```
> DATE       | AMOUNT  | BALANCE
> 10/04/2014 | 500.00  | 1400.00
> 02/04/2014 | -100.00 | 900.00
> 01/04/2014 | 1000.00 | 1000.00
```

## Starting point and constraints

1. Start with a class with the following structure:

```
class Account:
    def deposit(self, amount):
        raise NotImplementedError()

    def withdraw(self, amount):
        raise NotImplementedError()

    def print_statement(self):
        raise NotImplementedError()

```

2. You are not allowed to add any other public method to this class.
3. Use Strings and Integers for dates and amounts (keep it simple)
4. Don't worry about spacing in the satement printed on the console

Note: the three public methods are commands, they don't return anything.

Note: I cannot add query methods, I cannot query for the state.

## Requirements

You need Python 3.4 or compatible. If you have pyenv installed, you can:

    $ make pyenv

Once you have a compatible version of Python installed, you can install the requirements:

    $ make requirements

## Running the tests

See the `Makefile`.
