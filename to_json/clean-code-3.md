---

mindmap-plugin: basic

---


[
  {
    "title": "Map 1",
    "topic": {
      "title": "3. Functions",
      "topics": [
        {
          "title": "switch statement",
          "topics": [
            {
              "title": "always big"
            },
            {
              "title": "Since we cannot always avoid switch statement, make sure that each switch statement is buried in a low-level class and is never repeated.",
              "topics": [
                {
                  "title": "Polymorphism"
                }
              ]
            }
          ]
        },
        {
          "title": "Small!",
          "topics": [
            {
              "title": "look",
              "topics": [
                {
                  "title": "blocks and indenting",
                  "topics": [
                    {
                      "title": "functions should not be large enough to hold nested structures"
                    },
                    {
                      "title": "the blocks within if, else, while statements and so on should be one line long. Probably that line should be a function call",
                      "topics": [
                        {
                          "title": "function called within the block can have a nicely descriptive name"
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "title": "meaning",
              "topics": [
                {
                  "title": "Do one thing",
                  "topics": [
                    {
                      "title": "how do we know function does one thing",
                      "topics": [
                        {
                          "title": "if a function does only steps that are one level below the stated name of the function, then the function is doing one thing"
                        },
                        {
                          "title": "if a function is divided into sections such as declarations, initializations, and sieve, then the function is doing more than one thing"
                        }
                      ]
                    },
                    {
                      "title": "one level of abstraction per function",
                      "topics": [
                        {
                          "title": "high level: \n  getHtml();\n\nintermediate level: \n  pathName = PathParser.render(pagePath);\n\nlow level:\n  .append(\"\\n\");"
                        },
                        {
                          "title": "mixing levels of abstraction within a function is always confusing"
                        }
                      ]
                    },
                    {
                      "title": "Do not have hidden things"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "title": "Arguments",
          "topics": [
            {
              "title": "ideal: 0\nprohibited: 3~"
            },
            {
              "title": "is hard",
              "topics": [
                {
                  "title": "to understand"
                },
                {
                  "title": "to test"
                }
              ]
            },
            {
              "title": "Do not use arguments like",
              "topics": [
                {
                  "title": "output"
                },
                {
                  "title": "boolean"
                }
              ]
            },
            {
              "title": "common monadic forms",
              "topics": [
                {
                  "title": "asking question about that argument",
                  "topics": [
                    {
                      "title": "fileExists(\"MyFile\")"
                    }
                  ]
                },
                {
                  "title": "operating on that argument, transforming it into something else and returning it",
                  "topics": [
                    {
                      "title": "fileOpen(\"MyFile\")"
                    }
                  ]
                },
                {
                  "title": "event: no output argument",
                  "topics": [
                    {
                      "title": "passwordAttemptFailedNTimes(attempt)"
                    }
                  ]
                }
              ]
            },
            {
              "title": "verb/noun pair of function and argument(monadic)"
            }
          ]
        },
        {
          "title": "Name",
          "topics": [
            {
              "title": "Use long descriptive name"
            },
            {
              "title": "the smaller and more focused a function is, the easier it is to choose a descriptive name"
            }
          ]
        },
        {
          "title": "Readability",
          "topics": [
            {
              "title": "Write code like a top-down narrative",
              "topics": [
                {
                  "title": "each of set is describing the current level of abstraction and referencing subsequent To paragraphs at the next level down"
                },
                {
                  "title": "very hard to learn but important for programmer"
                }
              ]
            }
          ]
        },
        {
          "title": "DRY"
        },
        {
          "title": "Command query seperation",
          "topics": [
            {
              "title": "Do something or answer something, but not both",
              "topics": [
                {
                  "title": "violation:\n\nif (set(\"username\",\"unclebob\"))"
                }
              ]
            },
            {
              "title": "Prefer exceptions to returning error codes",
              "topics": [
                {
                  "title": "violations:\n\nif (deletePage(page) == E_OK)"
                },
                {
                  "title": "this violation leads to deeply nested structures"
                },
                {
                  "title": "Extract try/catch blocks",
                  "topics": [
                    {
                      "title": "try/catch blocks confuse the structure of the code and mix error processing with normal processing"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "title": "Structured Programming",
          "topics": [
            {
              "title": "every function and every block within a function, should have one entry and one exit"
            },
            {
              "title": "benefits are very little when we keep our functions small"
            },
            {
              "title": "if we keep our functions small, the occasional multiple return, break or continue statement does no harm and can be expressive than single-entry, single-exit rule"
            }
          ]
        }
      ]
    },
    "structure": "org.xmind.ui.map.clockwise"
  }
]