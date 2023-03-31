                                    Python - Variable Annotations
When writing code in Python, it's important to be clear about the data types and values that variables hold.
Python 3.5 introduced a new feature called variable annotations, which allows you to explicitly declare the data type of a variable.
This can help make your code more readable and reduce the risk of bugs.

                                    Syntax
The syntax for variable annotations is simple: you add a colon after the variable name and then specify the data type. Here's an example:
            x: int = 5
In this example, we've declared a variable named x and explicitly stated that it is an integer.
Note that we've also assigned it an initial value of 5. You can also declare multiple variables on a single line:

            x: int = 5
            y: str = "hello"
            z: bool = True

                                    Benefits
Variable annotations have several benefits:

Readability: By explicitly declaring the data type of a variable, you make it clear what kind of data it holds.
This can make your code easier to read and understand.

Reduced bugs: Declaring the data type of a variable can help prevent bugs caused by type mismatches.
For example, if you accidentally try to add a string and an integer, Python will raise a TypeError at runtime.
With variable annotations, you can catch this kind of error at compile time.



                                    Best practices
When using variable annotations, it's important to follow these best practices:

Use descriptive variable names: Make sure your variable names clearly indicate what the variable represents. For example, num_items is a better variable name than x.

Don't overuse annotations: While variable annotations can be useful, don't feel like you need to annotate every variable in your code. Use them where they provide the most benefit.

Be consistent: If you decide to use variable annotations in your code, be consistent in how you apply them. This will help make your code easier to read and understand.

