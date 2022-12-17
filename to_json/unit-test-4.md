[
  {
    "title": "Map 1",
    "topic": {
      "title": "4. Test Smells: Readability",
      "topics": [
        {
          "title": "Test smells around assertions",
          "topics": [
            {
              "title": "Primitive Assertions",
              "topics": [
                {
                  "title": "assertion should express an assumption or intent"
                },
                {
                  "title": "level of abstraction is too low when it comes to asserting stuff"
                },
                {
                  "title": "Ask yourself whether the level of abstraction is right whenever seeing comparisons such as != or ==, especially to magic numbers like -1 or 0"
                }
              ]
            },
            {
              "title": "Hyperassertions",
              "topics": [
                {
                  "title": "it's hard to say what exactly it's supposed to check, and when you step back to observe, the test is probably breaking far more frequently than the average."
                },
                {
                  "title": "this test is too broad",
                  "topics": [
                    {
                      "title": "it fails too easily, making it brittle and fragile"
                    }
                  ]
                },
                {
                  "title": "this test violate a fundamental guiding principle for what constitutes a good test:",
                  "topics": [
                    {
                      "title": "A test should have only one reason to fail (test version of SRP)"
                    }
                  ]
                },
                {
                  "title": "Make test more focused and easier to grasp"
                }
              ]
            },
            {
              "title": "Bitwise Assertions",
              "topics": [
                {
                  "title": "Bit operation is powerful feature but too abstract to understand"
                },
                {
                  "title": "we are not in the domain of bits and bytes"
                },
                {
                  "title": "Replace the bit operator with one or more boolean operators, expressing the expectations clearly one by one"
                }
              ]
            }
          ]
        },
        {
          "title": "Test smells around information scatter within the code base",
          "topics": [
            {
              "title": "Split Logic",
              "topics": [
                {
                  "title": "tests that span several screenfuls of code"
                },
                {
                  "title": "Chunk test code into smaller pieces"
                },
                {
                  "title": "a heuristic for quickly determining what you should pull into the test and what to push out to the sidelines",
                  "topics": [
                    {
                      "title": "1. if it's short, inline it"
                    },
                    {
                      "title": "2. if it's too long to keep inlined, stash it behind a factory method or a test data builder"
                    },
                    {
                      "title": "3. if that feels inconvenient, pull it out into a separate file",
                      "topics": [
                        {
                          "title": "Trim your data to bare essentials"
                        },
                        {
                          "title": "Place such data files in the same folder as the tests that use them"
                        },
                        {
                          "title": "Whatever structure you end up with, make it a convention with your team and stick to it"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "title": "Test smells around excess or irrelevant detail",
          "topics": [
            {
              "title": "Incidental Details",
              "topics": [
                {
                  "title": "test has too much details"
                },
                {
                  "title": "how to express core assertion",
                  "topics": [
                    {
                      "title": "1. Extract the non-essential setup into private method or the setup"
                    },
                    {
                      "title": "2. Give things appropriate, descriptive names"
                    },
                    {
                      "title": "3. Strive for a single level of abstraction in a method"
                    }
                  ]
                }
              ]
            },
            {
              "title": "Split Personality",
              "topics": [
                {
                  "title": "A test should only check one thing and check it well"
                }
              ]
            },
            {
              "title": "Magic Numbers",
              "topics": [
                {
                  "title": "Replace them with constants or variables that give the number that much-desired meaning"
                }
              ]
            },
            {
              "title": "Setup Sermon",
              "topics": [
                {
                  "title": "messy setup code looks complicated"
                },
                {
                  "title": "how to set up",
                  "topics": [
                    {
                      "title": "1. Extract the nonessential details from the setup into private methods"
                    },
                    {
                      "title": "2. Give things appropriate, descriptive name"
                    },
                    {
                      "title": "3. Strive for a single level of abstraction in the setup"
                    }
                  ]
                }
              ]
            },
            {
              "title": "Overprotective Tests",
              "topics": [
                {
                  "title": "this assertion is superfluous"
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