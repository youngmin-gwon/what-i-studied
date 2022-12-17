[
  {
    "title": "Map 1",
    "topic": {
      "title": "3. Test doubles",
      "topics": [
        {
          "title": "The power of a test double",
          "topics": [
            {
              "title": "Isolate the code under test",
              "topics": [
                {
                  "title": "we can substitute collaborators with test double"
                }
              ]
            },
            {
              "title": "Speed up test execution",
              "topics": [
                {
                  "title": "test double's implementation is often faster than real one"
                }
              ]
            },
            {
              "title": "Make execution deterministic",
              "topics": [
                {
                  "title": "test double can make tests get same results"
                }
              ]
            },
            {
              "title": "Simulate special conditions",
              "topics": [
                {
                  "title": "test double can throw an exception to test failed case"
                }
              ]
            },
            {
              "title": "Gain access to hidden information",
              "topics": [
                {
                  "title": "we can add for-testing-only method to test code"
                }
              ]
            }
          ]
        },
        {
          "title": "What kind of test doubles",
          "topics": [
            {
              "title": "Test stub",
              "topics": [
                {
                  "title": "a short thing"
                },
                {
                  "title": "it stands in for the real implementation with the simplest possible implementation"
                },
                {
                  "title": "a typical example of what a stub does - nothing"
                }
              ]
            },
            {
              "title": "Fake object",
              "topics": [
                {
                  "title": "a replicated, but thinned-down version of the real thing"
                },
                {
                  "title": "usually faster than real one"
                },
                {
                  "title": "good example: persistence test"
                }
              ]
            },
            {
              "title": "Test spy",
              "topics": [
                {
                  "title": "like a cop going undercover and reporting afterward what he observed"
                },
                {
                  "title": "useful in a case where there is no return value to assert against"
                },
                {
                  "title": "it gains access to hidden information",
                  "topics": [
                    {
                      "title": "by inheriting original object and add for-test-only methods to gain information"
                    }
                  ]
                }
              ]
            },
            {
              "title": "Mock object",
              "topics": [
                {
                  "title": "a special kind of test spy"
                },
                {
                  "title": "an object that's configured to behave in a certain way under certain circumstances"
                }
              ]
            }
          ]
        },
        {
          "title": "Guidelines for using test doubles",
          "topics": [
            {
              "title": "Pick the right double for the test",
              "topics": [
                {
                  "title": "There is no hard and fast rule for much of this, but we should probably mix and match a little"
                },
                {
                  "title": "heuristics when to use which",
                  "topics": [
                    {
                      "title": "simple version: stub queries; mock actions."
                    },
                    {
                      "title": "details version",
                      "topics": [
                        {
                          "title": "you care about a certain interaction taking place in the form of method calls between two objects:\n\nmock object"
                        },
                        {
                          "title": "you decided to go with a mock object but your test code ends up looking less pretty than you’d like:\n\ntest spy"
                        },
                        {
                          "title": "you only care about the collaborator objects being there:\n\nstub"
                        },
                        {
                          "title": "you want to run a complex scenario that relies on a service or component that’s unavailable or unusable for your test’s purposes, and your quick attempt at stubbing all of those interactions grinds to a halt or results in messy test code that’s going to be a pain to maintain:\n\nfake object"
                        },
                        {
                          "title": "none of the above sufficiently describes your particular situation at hand:\n\ntoss a coin—heads is a mock, tails is a stub, and if the coin is standing on its side, you have my permission to whip up a fake."
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "title": "Arrange, Act, Assert",
              "topics": [
                {
                  "title": "Follow this order of test and add whitespace between the three blocks of code"
                },
                {
                  "title": "\"given, when, then\" in BDD term"
                }
              ]
            },
            {
              "title": "Check for behavior, not implementation",
              "topics": [
                {
                  "title": "Such failure comes from lack of focus"
                },
                {
                  "title": "A test should test just one thing and test it well while communicating its intent clearly"
                }
              ]
            },
            {
              "title": "Choose your tools",
              "topics": [
                {
                  "title": "Mock Library"
                }
              ]
            },
            {
              "title": "Inject your dependencies",
              "topics": [
                {
                  "title": "Collaborator objects you'd like to replace for the purposes of testing should not be instantiated in the same place they are used",
                  "topics": [
                    {
                      "title": "Store objects as private member or acquire them, for example, through factory method"
                    }
                  ]
                },
                {
                  "title": "Employ dependency injection and pass dependencies into the object from outside, typically using constructor injection"
                }
              ]
            }
          ]
        },
        {
          "title": "Reason for creating",
          "topics": [
            {
              "title": "to serve as a placeholder until the real thing becomes available",
              "topics": [
                {
                  "title": "to allow you to compile and execute one piece of code before its surrounding pieces were in place"
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