Feature: Roman

  Scenario: Roman with number 1
    Given instance of Roman
    When we input number 1
    Then game will return "I"

  Scenario: Roman with number 2
    Given instance of Roman
    When we input number 2
    Then game will return "II"

  Scenario: Roman with number 3
    Given instance of Roman
    When we input number 3
    Then game will return "III"

  Scenario: Roman with number 4
    Given instance of Roman
    When we input number 4
    Then game will return "IV"

  Scenario: Roman with number 5
    Given instance of Roman
    When we input number 5
    Then game will return "V"

  Scenario: Roman with number 6
    Given instance of Roman
    When we input number 6
    Then game will return "VI"

  Scenario: Roman with number 9
    Given instance of Roman
    When we input number 9
    Then game will return "IX"

  Scenario: Roman with number 27
    Given instance of Roman
    When we input number 27
    Then game will return "XXVII"

  Scenario: Roman with number 48
    Given instance of Roman
    When we input number 48
    Then game will return "XLVIII"

  Scenario: Roman with number 49
    Given instance of Roman
    When we input number 49
    Then game will return "XLIX"

  Scenario: Roman with number 59
    Given instance of Roman
    When we input number 59
    Then game will return "LIX"

  Scenario: Roman with number 93
    Given instance of Roman
    When we input number 93
    Then game will return "XCIII"

  Scenario: Roman with number 141
    Given instance of Roman
    When we input number 141
    Then game will return "CXLI"

  Scenario: Roman with number 163
    Given instance of Roman
    When we input number 163
    Then game will return "CLXIII"

  Scenario: Roman with number 402
    Given instance of Roman
    When we input number 402
    Then game will return "CDII"

  Scenario: Roman with number 575
    Given instance of Roman
    When we input number 575
    Then game will return "DLXXV"

  Scenario: Roman with number 911
    Given instance of Roman
    When we input number 911
    Then game will return "CMXI"

  Scenario: Roman with number 1024
    Given instance of Roman
    When we input number 1024
    Then game will return "MXXIV"

  Scenario: Roman with number 3000
    Given instance of Roman
    When we input number 3000
    Then game will return "MMM"
