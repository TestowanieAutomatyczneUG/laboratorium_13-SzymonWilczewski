from behave import *
from assertpy import *
from src.zad02.roman import Roman


@given('instance of Roman')
def step_impl(context):
    context.r = Roman()


@when('we input number 1')
def step_impl(context):
    context.result = context.r.number(1)


@then('game will return "I"')
def step_impl(context):
    assert_that(context.result).is_equal_to("I")


@when('we input number 2')
def step_impl(context):
    context.result = context.r.number(2)


@then('game will return "II"')
def step_impl(context):
    assert_that(context.result).is_equal_to("II")


@when('we input number 3')
def step_impl(context):
    context.result = context.r.number(3)


@then('game will return "III"')
def step_impl(context):
    assert_that(context.result).is_equal_to("III")


@when('we input number 4')
def step_impl(context):
    context.result = context.r.number(4)


@then('game will return "IV"')
def step_impl(context):
    assert_that(context.result).is_equal_to("IV")


@when('we input number 5')
def step_impl(context):
    context.result = context.r.number(5)


@then('game will return "V"')
def step_impl(context):
    assert_that(context.result).is_equal_to("V")


@when('we input number 6')
def step_impl(context):
    context.result = context.r.number(6)


@then('game will return "VI"')
def step_impl(context):
    assert_that(context.result).is_equal_to("VI")


@when('we input number 9')
def step_impl(context):
    context.result = context.r.number(9)


@then('game will return "IX"')
def step_impl(context):
    assert_that(context.result).is_equal_to("IX")


@when('we input number 27')
def step_impl(context):
    context.result = context.r.number(27)


@then('game will return "XXVII"')
def step_impl(context):
    assert_that(context.result).is_equal_to("XXVII")


@when('we input number 48')
def step_impl(context):
    context.result = context.r.number(48)


@then('game will return "XLVIII"')
def step_impl(context):
    assert_that(context.result).is_equal_to("XLVIII")


@when('we input number 49')
def step_impl(context):
    context.result = context.r.number(49)


@then('game will return "XLIX"')
def step_impl(context):
    assert_that(context.result).is_equal_to("XLIX")


@when('we input number 59')
def step_impl(context):
    context.result = context.r.number(59)


@then('game will return "LIX"')
def step_impl(context):
    assert_that(context.result).is_equal_to("LIX")


@when('we input number 93')
def step_impl(context):
    context.result = context.r.number(93)


@then('game will return "XCIII"')
def step_impl(context):
    assert_that(context.result).is_equal_to("XCIII")


@when('we input number 141')
def step_impl(context):
    context.result = context.r.number(141)


@then('game will return "CXLI"')
def step_impl(context):
    assert_that(context.result).is_equal_to("CXLI")


@when('we input number 163')
def step_impl(context):
    context.result = context.r.number(163)


@then('game will return "CLXIII"')
def step_impl(context):
    assert_that(context.result).is_equal_to("CLXIII")


@when('we input number 402')
def step_impl(context):
    context.result = context.r.number(402)


@then('game will return "CDII"')
def step_impl(context):
    assert_that(context.result).is_equal_to("CDII")


@when('we input number 575')
def step_impl(context):
    context.result = context.r.number(575)


@then('game will return "DLXXV"')
def step_impl(context):
    assert_that(context.result).is_equal_to("DLXXV")


@when('we input number 911')
def step_impl(context):
    context.result = context.r.number(911)


@then('game will return "CMXI"')
def step_impl(context):
    assert_that(context.result).is_equal_to("CMXI")


@when('we input number 1024')
def step_impl(context):
    context.result = context.r.number(1024)


@then('game will return "MXXIV"')
def step_impl(context):
    assert_that(context.result).is_equal_to("MXXIV")


@when('we input number 3000')
def step_impl(context):
    context.result = context.r.number(3000)


@then('game will return "MMM"')
def step_impl(context):
    assert_that(context.result).is_equal_to("MMM")
