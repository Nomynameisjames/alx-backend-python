                             Python - Async
Asyncio is a module in Python's standard library that provides tools for writing asynchronous code.
Asynchronous code is code that does not execute sequentially, but rather allows multiple tasks to run concurrently.

With asyncio, you can write code that performs input/output (I/O) operations without blocking the execution of other code.
This is particularly useful for network programming and web development, where I/O operations such as making requests to a server can take a long time.

Asyncio is built on coroutines, which are functions that can be paused and resumed. 
Coroutines can be created using the async keyword, and are run using the asyncio event loop.

The event loop is responsible for scheduling and running coroutines. When a coroutine makes an I/O operation, it is paused and added to a queue.
The event loop then continues running other coroutines until the I/O operation completes, at which point the original coroutine is resumed.

To create a coroutine, you define a function using the async def syntax. Within the function,
you can use the await keyword to pause the coroutine until an I/O operation completes.
For example, you might use await to make an HTTP request to a remote server.

Asyncio provides a number of tools for working with coroutines, including Futures, Tasks, and Streams.
Futures represent the result of a computation that has not yet completed.
Tasks are used to run coroutines concurrently, and Streams provide a way to work with data in a streaming fashion.

                            Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
0. async and await syntax
1. How to execute an async program with asyncio
2. How to run concurrent coroutines
3. How to create asyncio tasks
4. How to use the random module

