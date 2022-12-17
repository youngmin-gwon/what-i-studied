[
  {
    "title": "Map 1",
    "topic": {
      "title": "7. Error Handling",
      "topics": [
        {
          "title": "Exception",
          "topics": [
            {
              "title": "clean and robust way to handle errors with grace and style"
            },
            {
              "title": "displines",
              "topics": [
                {
                  "title": "Use exception rather than return codes",
                  "topics": [
                    {
                      "title": "easy to forget return values"
                    },
                    {
                      "title": "throwing exception is cleaner"
                    },
                    {
                      "title": "better not because it is cleaner, but because two concerns, logic and error handling, are separated"
                    }
                  ]
                },
                {
                  "title": "try-catch-finally first",
                  "topics": [
                    {
                      "title": "good starting point, and can narrow down next"
                    },
                    {
                      "title": "follow TDD process"
                    }
                  ]
                },
                {
                  "title": "Use unchecked exception",
                  "topics": [
                    {
                      "title": "Checked exceptions are not necessary for the production of robust software"
                    },
                    {
                      "title": "The cost of checked exceptions is an OCP violation: checked exceptions break encapsulation"
                    }
                  ]
                },
                {
                  "title": "Provide context with Exception",
                  "topics": [
                    {
                      "title": "Descriptive and informative error messages always help"
                    }
                  ]
                },
                {
                  "title": "Define Exception Classes in Terms of a Caller's Needs",
                  "topics": [
                    {
                      "title": "Wrappers for 3rd-party libraries are best practices"
                    },
                    {
                      "title": "Wrappers make you untied to a particular vendor's API design choices"
                    },
                    {
                      "title": "The information sent with user-defined exception can distinguish the errors"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "title": "Define Normal Flow",
          "topics": [
            {
              "title": "Normal Flow: default work flow when nothing is got"
            },
            {
              "title": "Wrap external APIs so that you can throw your own exceptions"
            },
            {
              "title": "Use Special Case(=Null Object) pattern"
            }
          ]
        },
        {
          "title": "Null",
          "topics": [
            {
              "title": "Don't pass null"
            },
            {
              "title": "Don't return null",
              "topics": [
                {
                  "title": "If you are tempted to return null from a method, consider throwing an exception or returning a \"Special Case\" object"
                },
                {
                  "title": "If you are calling a null-returning method from a third-party API, consier wrapping that method with a method that either throws an exception or returns a \"Special Case\" object"
                }
              ]
            }
          ]
        },
        {
          "title": "Logic first",
          "topics": [
            {
              "title": "if error handling obscures logic, it's wrong"
            }
          ]
        }
      ]
    },
    "structure": "org.xmind.ui.map.clockwise"
  }
]