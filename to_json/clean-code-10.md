[
  {
    "title": "Map 1",
    "topic": {
      "title": "10. Classes",
      "topics": [
        {
          "title": "Class organization",
          "topics": [
            {
              "title": "orders",
              "topics": [
                {
                  "title": "1. a list of variables",
                  "topics": [
                    {
                      "title": "static constants"
                    },
                    {
                      "title": "private static variables"
                    },
                    {
                      "title": "private instance variables"
                    }
                  ]
                },
                {
                  "title": "2. public functions"
                },
                {
                  "title": "3. private utilities"
                }
              ]
            },
            {
              "title": "Encapsulation",
              "topics": [
                {
                  "title": "no good reason to have a public variable"
                }
              ]
            }
          ]
        },
        {
          "title": "Class should be small",
          "topics": [
            {
              "title": "How small?",
              "topics": [
                {
                  "title": "small to have one responsibility",
                  "topics": [
                    {
                      "title": "SRP",
                      "topics": [
                        {
                          "title": "helps us recognize and create better abstractions in our code"
                        },
                        {
                          "title": "a large number of small, single-purpose classes makes it more difficult to understand the bigger picture?",
                          "topics": [
                            {
                              "title": "a system with many small classes has no more moving parts than a system with a few large classes"
                            },
                            {
                              "title": "The primary goal in managing such complexity is to organize it so that a developer knows where to look to find things and need only understand the directly affected complexity at any given time"
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
              "title": "Cohesion",
              "topics": [
                {
                  "title": "classes should have a small number of instance variables"
                },
                {
                  "title": "each of the methods of a class should manipulate one or more of those variables"
                },
                {
                  "title": "the more variables a method manipulates the more cohesive that method is to its class"
                },
                {
                  "title": "we would like cohesion to be high"
                },
                {
                  "title": "when class lose cohesion, split them",
                  "topics": [
                    {
                      "title": "the program might get longer"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "title": "Name",
          "topics": [
            {
              "title": "The first way of helping determine class"
            },
            {
              "title": "should describe what responsibilities it fulfills"
            },
            {
              "title": "The more ambiguous the class name, the more likely it has too many responsibilities",
              "topics": [
                {
                  "title": "weasel words like Processor, Manager, or Super"
                }
              ]
            },
            {
              "title": "should be able to write a brief description of the class in about 25 words, without the words \"if\", \"and\", \"or\", or \"but.\""
            }
          ]
        },
        {
          "title": "Adaptive to change",
          "topics": [
            {
              "title": "organize our classes so as to reduce the risk of change",
              "topics": [
                {
                  "title": "command pattern"
                }
              ]
            },
            {
              "title": "Isolate code from change",
              "topics": [
                {
                  "title": "a client class depending upon concrete details is at risk when those details change"
                },
                {
                  "title": "dependencies upon concrete details create challenges for test"
                },
                {
                  "title": "Introduce interfaces and abstract classes to help isolate the impact of details"
                }
              ]
            }
          ]
        },
        {
          "title": "Attitude to make class",
          "topics": [
            {
              "title": "Don't think we are done once the program works. Make your program clean and organized next."
            }
          ]
        }
      ]
    },
    "structure": "org.xmind.ui.map.clockwise"
  }
]