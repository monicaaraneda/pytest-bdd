Feature: Payment Token Generation
  Scenario Outline: Request a payment token with different users
    Given I am a "<user_type>"
    When I request a payment token for "<user_id>" with an amount of "<amount>"
    Then I should get a successful response

    Examples:
      | user_type  | user_id          | amount |
      | collector  | 3Bx8IW9lxOEnjitb | 4000   |
      | collector  | lyET3ZX2YUVwOdAB | 7000   |
      | payer      | tbOnpmf67kIuJStB | 5000   |
