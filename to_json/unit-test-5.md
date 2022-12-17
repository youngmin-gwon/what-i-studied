[
  {
    "title": "Map 1",
    "topic": {
      "title": "5. Test Smells:\nMaintainability",
      "topics": [
        {
          "title": "Test smells that add to your cognitive load",
          "topics": [
            {
              "title": "Conditional logic",
              "topics": [
                {
                  "title": "it is difficult to parse and understand, even though it is testing a fairly trivial behavior"
                },
                {
                  "title": "Avoid conditional execution such as if, else, for, while, and switch in your test methods"
                }
              ]
            },
            {
              "title": "Parameterized mess",
              "topics": [
                {
                  "title": "a parameterized test is a good pattern, but when used too much and in wrong context, it becomes code smell"
                },
                {
                  "title": "difficult",
                  "topics": [
                    {
                      "title": "to understand"
                    },
                    {
                      "title": "to pinpoint the actual failure when one of the tests fails"
                    }
                  ]
                },
                {
                  "title": "Distinguish the individual data sets",
                  "topics": [
                    {
                      "title": "wrap each set into a method call"
                    },
                    {
                      "title": "indentation"
                    }
                  ]
                },
                {
                  "title": "Add failure message thrown from a failing assertion"
                }
              ]
            },
            {
              "title": "Lack of cohesion in methods",
              "topics": [
                {
                  "title": "some fields(or fixture) of a class are not used by every method"
                },
                {
                  "title": "these fields usually have bad names"
                },
                {
                  "title": "Coerce the tests to use the same fixture objects"
                }
              ]
            }
          ]
        },
        {
          "title": "Test smells that make for a maintenance nightmare",
          "topics": [
            {
              "title": "Duplication",
              "topics": [
                {
                  "title": "= needless repetition"
                },
                {
                  "title": "Category",
                  "topics": [
                    {
                      "title": "literal duplication"
                    },
                    {
                      "title": "structural duplication"
                    }
                  ]
                },
                {
                  "title": "it makes the code base more opaque and difficult to understand as concepts and logic are scattered among multiple places"
                },
                {
                  "title": "it increases the chance of a bug slipping in as we forget to make a change in all necessary places"
                },
                {
                  "title": "Get rid of it",
                  "topics": [
                    {
                      "title": "but primary interest is readability"
                    }
                  ]
                }
              ]
            },
            {
              "title": "Sleeping snail",
              "topics": [
                {
                  "title": "slow tests due to drags from File I/O, sleep"
                },
                {
                  "title": "Make test thread notified when each worker thread actually completes; await, etc"
                }
              ]
            },
            {
              "title": "Pixel perfection",
              "topics": [
                {
                  "title": "a special case of primitive assertion and magic number"
                },
                {
                  "title": "brittle and difficult to understand because of hard-coded and low-level code"
                },
                {
                  "title": "Replace code with a custom assertion that reads like plain english"
                },
                {
                  "title": "Express intent at the appropriate level of abstraction"
                }
              ]
            }
          ]
        },
        {
          "title": "Test smells that cause failures",
          "topics": [
            {
              "title": "Flaky test",
              "topics": [
                {
                  "title": "tests that fail intermittently"
                },
                {
                  "title": "threads, race conditions, current date or time, computer's performance, I/O speed or the CPU load, network"
                },
                {
                  "title": "Solution",
                  "topics": [
                    {
                      "title": "1. Avoid it",
                      "topics": [
                        {
                          "title": "replace nondeterministic code"
                        }
                      ]
                    },
                    {
                      "title": "2. Control it",
                      "topics": [
                        {
                          "title": "using test doubles"
                        }
                      ]
                    },
                    {
                      "title": "3. Isolate it",
                      "topics": [
                        {
                          "title": "into a small place"
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "title": "Crippling file path",
              "topics": [
                {
                  "title": "it causes failure depending on file system"
                },
                {
                  "title": "it forces developers to place their workspace in the same physical location"
                },
                {
                  "title": "Avoid absolute paths, and use relative paths whenever possible"
                },
                {
                  "title": "Try to put all project resources under the project's root directory"
                }
              ]
            },
            {
              "title": "Persistent temp files",
              "topics": [
                {
                  "title": "when the temporary file isn't that temporary but rather persistent, to the extent that it won't be deleted before the next test runs"
                },
                {
                  "title": "Avoid using files altogether where they are not essential to the objects you're testing"
                },
                {
                  "title": "Keep the use of physical files to a minimum"
                },
                {
                  "title": "Delete the file before next test"
                },
                {
                  "title": "Use unique names for temporary files if possible"
                },
                {
                  "title": "Be explicit about whether or not a file should exist"
                }
              ]
            }
          ]
        }
      ]
    },
    "structure": "org.xmind.ui.map.clockwise"
  }
]