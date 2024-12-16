---

mindmap-plugin: basic

---

# 3. Functions
## switch statement
- always big
- Since we cannot always avoid switch statement, make sure that each switch statement is buried in a low-level class and is never repeated.
- Polymorphism

## Small!
- look
  - blocks and indenting
    - functions should not be large enough to hold nested structures
    - the blocks within if, else, while statements and so on should be one line long. Probably that line should be a function call
    - function called within the block can have a nicely descriptive name
  - meaning
    - Do one thing
      - how do we know function does one thing
        - if a function does only steps that are one level below the stated name of the function, then the function is doing one thing
        - if a function is divided into sections such as declarations, initializations, and sieve, then the function is doing more than one thing
      - one level of abstraction per function
        - high level: <br/>  getHtml();<br/><br/> intermediate level:<br/>  pathName = PathParser.render(pagePath);<br/><br/>low level:<br/>  .append("\n");
        - mixing levels of abstraction within a function is always confusing
      - Do not have hidden things

## Arguments
  - ideal: 0<br/> prohibited: 3~
  - is hard
    - to understand
    - to test
  - Do not use arguments like
    - output
    - boolean
  - common monadic forms
    - asking question about that argument
      - fileExists("MyFile")
    - operating on that argument, transforming it into something else and returning it
      - fileOpen("MyFile")
    - event: no output argument
      - passwordAttemptFailedNTimes(attempt)
  - verb/noun pair of function and argument(monadic)

## Name
- Use long descriptive name
- the smaller and more focused a function is, the easier it is to choose a descriptive name

## Readability
- Write code like a top-down narrative
  - each of set is describing the current level of abstraction and referencing subsequent To paragraphs at the next level down
  - very hard to learn but important for programmer

## DRY

## Command query seperation
- Do something or answer something, but not both
  - violation:<br/><br/>if (set("username","unclebob"))
- Prefer exceptions to returning error codes
  - violations:<br/><br/>if (deletePage(page) == E_OK)
  - this violation leads to deeply nested structures
  - Extract try/catch blocks
    - try/catch blocks confuse the structure of the code and mix error processing with normal processing

## Structured Programming
- every function and every block within a function, should have one entry and one exit
- benefits are very little when we keep our functions small
- if we keep our functions small, the occasional multiple return, break or continue statement does no harm and can be expressive than single-entry, single-exit rule