# Sample Selenium pytest project using POM design pattern

## Things to remember in Applying Pytest Framework with Selenium
	
- utilize fixtures from pytest (conftest)
	
- able to run as a test (better analysis)
    - this allows to schedule (locally, Jenkins)
    - you can add pytest plugins to run as xml, html
		
- parametrize scenarios using yml
    - flexible in using the input data
    - allows to reuse the code for different data set and change the scenario
		
- enable logging (no print in the project)
    - prints are used for debugging purposes

- enhance the framework for reusable components
    - build more components
    - Page Object Modeling Pattern (OOP concepts)

- Page Object Modeling (POM)
	- to handle frequent changes in HTML locators and methods on the application page.
	
----
## Logging in python 
Documentation of the python logging [here](https://docs.python.org/3/library/logging.html)

- why logging is important
- timestamp for unique filename
	
	
    Logging Levels (types of message):
    Level 		Numeric value 
    CRITICAL    50
    ERROR  		40
    WARNING		30
    INFO		20
    DEBUG		10
    NOTSET		0

---
## Software Engineering


### Software development principles
There are many software development principles, though they are not backed by some scientific experiments, they greatly help to develop software. This week’s class will try to cover some of these principles.

Some of the popular terms:
- SOLID: Mnemonic for a set of 5 different patterns
- DRY: Don’t Repeat Yourself
- YAGNI: You Ain’t Gonna Need It
- KISS: Keep It Stupid Simple

### SOLID principles
- **Single responsibility principle**
A class should have only a single responsibility, that is, only changes to one part of the software's specification should be able to affect the specification of the class.

- **Open–closed principle**
"Software entities ... should be open for extension, but closed for modification."

- **Liskov substitution principle**
"Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program."

- **Interface segregation principle**
"Many client-specific interfaces are better than one general-purpose interface."

- **Dependency inversion principle**
One should "depend upon abstractions, [not] concretions."


### Design patterns
Design patterns usually mean best practices of software development. They are specialized in solving common problems.

**Examples:** 
- Façade pattern: Provide a common interface that can abstract complex set of actions
- Chain of responsibility: Instead of bundling everything into one place, build a pipeline that handles specific actions

### Page modeling pattern
In this pattern you try to model the given web page in Python objects. For example, Amazon’s homepage. We can observe that the page has a search input, a left sidebar and recommended/advertised items. Based on that we can create a Python class:

```python
class AmazonHomePage():
    def search(self, query):
        pass

    def toggle_sidebar(self):
        pass

    @property
    def items(self):
        pass
```

### Page modeling pattern: advantages

- **Separation of concerns**: the pattern will let you separate your browser related code from your validation/testing logic.
- **Reusability**: Since the browser related code is separate, it can be reused by many other validation pieces.
- **Isolation**: We can swap browser related code when necessary.

### Page modeling pattern: disadvantages

- Slightly more code
- Can lead to overengineering


### Maintainable code
You will hear a lot about maintainable code at work. People use the word in quite broad contexts. Usually they mean:
- The code is clean
- The code is extendable
- The code is well-written/well-designed/taken care well
- The code can be reused
- The code does not require a lot of brain processing power to understand
- The code is written by me (replace with “authority”)
- The code is does not require rewrite, because it is not full of hacks
- The code is/was written by a large team
- Do not touch/change the code


### Maintainable code: should we care?
Usually, software automation projects are not written in a well-maintainable way. But be sure when to follow design patterns/principles even when you write small scripts. You will never know if the script gets used more than once. Automation scripts are also considered software projects, they suffer from the same issues like other software projects.

**How do we achieve maintainable code?**
- Clean coding, with necessary comments
- Carefully applying design patterns/principles
- Consistency
- Modular/isolated blocks, &etc.

### Unix philosophy
In short, the main takeaway from this is:
- A tool (script) should do one job and should do it well
- A tool (script) should be able to work together with other tools

----
## Project structure: 

    README.md
        description of the project
        Instructions
        requirements 
        
    data (input)
    screenshots
    logs
    src (source code in this package)
        - features (enhancement with bdd)
        - pages (enhancement with POM)
        - steps (enhancement with POM)
    
        - tests (package)
            <login_to_automation_practice>
        - conftest.py
        - utilities.py (commonly used functions not from selenium)
            loading yml
            save root dir
            take screenshots
            create logging 	
            
        - Import all files and import one file for all tests
            all_imports.py
                import yaml
                from os.path import dirname, abspath
    
                from selenium.webdriver import ActionChains
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                
            login.py
                from src.all_imports import *
                
      requirements.txt - list of all required libraries for the project

## References: 
1. link to help you with identifying the locators [check here.](https://www.red-gate.com/simple-talk/dotnet/.net-framework/xpath,-css,-dom-and-selenium-the-rosetta-stone/)