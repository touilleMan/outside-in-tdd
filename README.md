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

Once you have a compatible version of Python installed, you can install the
requirements:

    $ make requirements

## Running the tests

See the `Makefile`.

## Notes

- deposit = dépôt, versement
- withdrawal = retrait
- balance = solde

### Présentation

- Bien expliquer la fonctionnalité au départ (souligner le mot de transaction,
  montrer l'ordre chronologique inverse)
- Commencer par écrire le feature test
- We need to identify the side effects, what are we testing in this acceptance
  test? print this ordered transaction statements to the console. So that's
  what we should be testing for.
- Bien insister : on traite la console comme un système extérieur, comme on
  traiterait une base de données.
- External system ⇒ interface to isolate my application from the external
  world.

- Now that I know what the side effect is, I need to identify the trigger of
  the side effect.

### Account

- why two methods: "I don't deposit -100, that doesn't make sense. Paying
  attention to that semantic is very important."
- before I move on, I want to see my acceptance test fail for the right reason
  ⇒ remove NotImplementedError
- acceptance test fails for the right reason ⇒ time to park acceptance test
  (double loop of TDD)
- why not inject console into account? I'm not quite sure that the account
  should call the console. I don't know how many abstractions will be between
  the account and the console.

### Go to unit level

- Simplest test I could possibly find. The deposit is an interesting candidate.
- All the methods in the account class are commands according to the initial
  constraints. I cannot change this interface.
- problems with classic TDD : expose query methods for the purpose of testing.
- storing total balance in account is not necessary for this feature.
- What is the side effect of a deposit? What do I want to happent when a
  deposit is made?
- I need to bind an amount to a date ⇒ transaction (montrer le README)
- si date + amount + balance dans le même objet, si on reçoit les transactions
  dans le désordre (batches), il faut recalculer le solde
- Design = trade-off
- deposit = a lot of stuff: somehow get the current date, create transaction,
  store it... Defer some of it?
- the account itself shoud not know how the transaction is stored ⇒ repository
  pattern
- Dans le TU on mocke le TransactionRepository, pas dans l'acceptance test.

### Print statement


