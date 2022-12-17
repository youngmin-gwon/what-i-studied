[
  {
    "title": "Map 1",
    "topic": {
      "title": "9. Unit Tests",
      "topics": [
        {
          "title": "TDD",
          "topics": [
            {
              "title": "Laws",
              "topics": [
                {
                  "title": "1. You may not write production code until you have written a failing unit test"
                },
                {
                  "title": "2. You may not write more of a unit test than is sufficient to fail, and not compiling is failing"
                },
                {
                  "title": "You may not write more production code than is sufficient to pass the currently failing test"
                }
              ]
            },
            {
              "title": "These three laws lock you into 30 seconds-long cycle"
            }
          ]
        },
        {
          "title": "Keep tests clean",
          "topics": [
            {
              "title": "Test code is just as important as production code"
            },
            {
              "title": "Having dirty tests means having no tests"
            },
            {
              "title": "Tests must change as the production code evolves"
            },
            {
              "title": "The dirtier the tests, the harder they are to change"
            }
          ]
        },
        {
          "title": "Readability",
          "topics": [
            {
              "title": "principles",
              "topics": [
                {
                  "title": "clarity"
                },
                {
                  "title": "simplicity"
                },
                {
                  "title": "density of expression"
                }
              ]
            },
            {
              "title": "Build-Object-Check pattern is useful"
            },
            {
              "title": "Anyone should be able to work out very quickly, without being misled or overwhelmed by details"
            },
            {
              "title": "Domain-Specific Testing Language",
              "topics": [
                {
                  "title": "Rather than using the test APIs, we build up a set of functions that make use of test APIs more convenient to write and easier to read"
                },
                {
                  "title": "succinct and expressive forms"
                }
              ]
            }
          ]
        },
        {
          "title": "A dual standard",
          "topics": [
            {
              "title": "Test environment and production environment have very different needs"
            },
            {
              "title": "Test code must still be simple, succinct, and expressive but not as efficient as production code",
              "topics": [
                {
                  "title": "assertEquals(\"HBchL\", hw.getState());"
                }
              ]
            }
          ]
        },
        {
          "title": "Never make test as ad hoc code"
        },
        {
          "title": "Test suite",
          "topics": [
            {
              "title": "key to keep your design and architecture as clean as possible"
            },
            {
              "title": "The higher test coverage, the less your fear"
            }
          ]
        },
        {
          "title": "Test unit",
          "topics": [
            {
              "title": "one assert per test",
              "topics": [
                {
                  "title": "defects",
                  "topics": [
                    {
                      "title": "a lot of duplicate code"
                    }
                  ]
                },
                {
                  "title": "okay to put more than one assert in a test",
                  "topics": [
                    {
                      "title": "but, the number of asserts in a test should be minimized"
                    }
                  ]
                }
              ]
            },
            {
              "title": "single concept per test",
              "topics": [
                {
                  "title": "hard to figure out why section is there if more than one concept"
                },
                {
                  "title": "minimize the number of asserts per concept"
                }
              ]
            }
          ]
        },
        {
          "title": "Given-When-Then Convention"
        },
        {
          "title": "F.I.R.S.T.",
          "topics": [
            {
              "title": "1. Fast",
              "topics": [
                {
                  "title": "when test runs slow, you won't want to run test frequently"
                }
              ]
            },
            {
              "title": "2. Independent",
              "topics": [
                {
                  "title": "When tests depend on each other, then the first one to fail causes a cascade of downstream failures, making diagnosis difficult and hiding downstream defects"
                }
              ]
            },
            {
              "title": "3. Repeatable",
              "topics": [
                {
                  "title": "should be repeatable without network"
                },
                {
                  "title": "if your test aren't repeatable in any environment, then you'll always have an excuse for why they fail"
                }
              ]
            },
            {
              "title": "4. Self-validating",
              "topics": [
                {
                  "title": "If the test aren't self-validating, then failure can become subjective and running the tests can require a long manual evaluation"
                }
              ]
            },
            {
              "title": "5. Timely",
              "topics": [
                {
                  "title": "Unit tests should be written just before the production code that makes them pass"
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