Feature: Single Sign On

Scenario: Successful SSO
    Given An user is not authenticated
    When he enters the web application
    Then he gets authenticated
