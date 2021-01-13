from behave import *
from assertpy import *
from src.zad01.fizzbuzz import FizzBuzz


@given('instance of FizzBuzz')
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when('we input number 15')
def step_impl(context):
    context.result = context.fizzbuzz.game(15)


@then('game will return FizzBuzz')
def step_impl(context):
    assert_that(context.result).is_equal_to("FizzBuzz")


@when('we input number 3')
def step_impl(context):
    context.result = context.fizzbuzz.game(3)


@then('game will return Fizz')
def step_impl(context):
    assert_that(context.result).is_equal_to("Fizz")


@when('we input number 5')
def step_impl(context):
    context.result = context.fizzbuzz.game(5)


@then('game will return Buzz')
def step_impl(context):
    assert_that(context.result).is_equal_to("Buzz")


@when('we input number 1')
def step_impl(context):
    context.result = context.fizzbuzz.game(1)


@then('game will return 1')
def step_impl(context):
    assert_that(context.result).is_equal_to(1)


@when('we input string "text"')
def step_impl(context):
    context.result = context.fizzbuzz.game("text")


@then('game will return "Wrong type!"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Wrong type!")
