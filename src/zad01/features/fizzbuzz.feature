Feature: FizzBuzz

  Scenario: FizzBuzz with number 15
    Given instance of FizzBuzz
    When we input number 15
    Then game will return FizzBuzz

  Scenario: FizzBuzz with number 3
    Given instance of FizzBuzz
    When we input number 3
    Then game will return Fizz

  Scenario: FizzBuzz with number 5
    Given instance of FizzBuzz
    When we input number 5
    Then game will return Buzz

  Scenario: FizzBuzz with number 1
    Given instance of FizzBuzz
    When we input number 1
    Then game will return 1

  Scenario: FizzBuzz with wrong type
    Given instance of FizzBuzz
    When we input string "text"
    Then game will return "Wrong type!"
