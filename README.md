# PyCoseQA Challenge
Automation script using Playwright and Pytest using the Page Object Model (POM) design pattern.

## User Story
As an online shopper, I want to search for a product on Amazon, add it to my basket, and update the quantity of the item to ensure a seamless shopping experience.

### Test Scenario 
Scenario: Search, add and update quantity of the product.
1. Given I am on the homepage 
2. When I type "laptop" on the search bar
3. And I click on the Search button or Enter
4. And I click on the first item that is displayed on the search list
5. And I add that product to my basket
6. And I update the quantity to 2
7. Then the quantity of the product should be updated to 2

## System requirements

-   Python 3.8 or higher.
-   Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL).
-   MacOS 12 Monterey, MacOS 13 Ventura, or MacOS 14 Sonoma.
-   Debian 11, Debian 12, Ubuntu 20.04 or Ubuntu 22.04.

## Getting started

(Optional) Firstly create a virtual environment by using the following command in your directory:

    python -m venv venv
    
   And activate it using this command:
   

    venv/Scripts/activate
   Note: Some code editors / IDEs activate the virtual enviroment automatically

---
Next up you will need to install project dependencies:

    pip install -r "requirements.txt"
   
   In order for playwright to install the web drivers you need to run this command:
   

    playwright install
   
   ---

#### Running the tests

To run your test suite, navigate to your tests directory and run the pytest command:

   

    cd tests
    pytest

Pytest will pick up files called test_* as a test, as seen on the pytest.ini file.

## Purposes
| Playwright | Pytest  |
|--|--|
| Access to the pages | Test Case assertion |

## Goal
This script opens up amazon, searches for a generic product, selects a product, updates the stock and evaluates if the stock has updated successfully after save.
