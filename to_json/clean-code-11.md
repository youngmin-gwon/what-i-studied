[
  {
    "title": "Map 1",
    "topic": {
      "title": "11. System",
      "topics": [
        {
          "title": "Seperate constructing a system from using it",
          "topics": [
            {
              "title": "construction is a very different process from use"
            },
            {
              "title": "Do not use hard-coded dependency",
              "topics": [
                {
                  "title": "when testing, it is hard to inject test double or mock object"
                }
              ]
            },
            {
              "title": "should separate the startup process, when the application objects are constructed and the dependencies are \"wired\" together, from the runtime logic that takes over after startup",
              "topics": [
                {
                  "title": "Move all aspects of construction to main"
                },
                {
                  "title": "abstract factory pattern"
                }
              ]
            },
            {
              "title": "a means to decouple application from the details of how to build objects"
            }
          ]
        },
        {
          "title": "Scale up",
          "topics": [
            {
              "title": "should adopt iterative and incremental way to expand",
              "topics": [
                {
                  "title": "Implement only today's stories, then refactor and expand the system to implement next stories tomorrow"
                },
                {
                  "title": "TDD, refactoring, clean code"
                }
              ]
            },
            {
              "title": "hard to grow system incrementally only if we maintain the proper separation of concerns"
            },
            {
              "title": "Cross-cutting concerns",
              "topics": [
                {
                  "title": "Some concerns like persistence tend to cut across the object boundaries of domain",
                  "topics": [
                    {
                      "title": "AOP",
                      "topics": [
                        {
                          "title": "programming method to focus on core concerns and minimize duplication for cross-cutting concerns"
                        },
                        {
                          "title": "3 aspect-like mechanisms in Java",
                          "topics": [
                            {
                              "title": "1. Java Proxy",
                              "topics": [
                                {
                                  "title": "suitable for simple situations, such as wrapping method calls"
                                },
                                {
                                  "title": "1. define a interface\n2. implement the interface(POJO)\n3. wrap implementation with proxy"
                                },
                                {
                                  "title": "too much code and not proper for system-wide execution"
                                }
                              ]
                            },
                            {
                              "title": "2. Pure Java AOP Frameworks",
                              "topics": [
                                {
                                  "title": "decorator pattern"
                                },
                                {
                                  "title": "easy to test"
                                }
                              ]
                            },
                            {
                              "title": "3. AspectJ"
                            }
                          ]
                        },
                        {
                          "title": "POJO",
                          "topics": [
                            {
                              "title": "are purely focused on domain"
                            },
                            {
                              "title": "no dependencies on enterprise frameworks"
                            }
                          ]
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
          "title": "Dependency Injection",
          "topics": [
            {
              "title": "the application of Inversion of Dependency to dependency management"
            },
            {
              "title": "a special-purpose container to take responsibility for instantiating dependencies"
            },
            {
              "title": "most DI containers will provide mechanisms for invoking factories or proxies and won't construct an object until needed = lazy initialization"
            }
          ]
        },
        {
          "title": "Domain-Specific Languages",
          "topics": [
            {
              "title": "good DSL minimized the communication gap between a domain concept and the code that implements it"
            },
            {
              "title": "code idioms and design patterns"
            }
          ]
        },
        {
          "title": "Postpone architectural decisions until the last possible moment"
        },
        {
          "title": "Test-driven system",
          "topics": [
            {
              "title": "POJO first"
            },
            {
              "title": "can be evolved from simple to sophisticated"
            }
          ]
        },
        {
          "title": "Use standards wisely, when they add demonstrable value",
          "topics": [
            {
              "title": "somewhat good, somewhat bad",
              "topics": [
                {
                  "title": "easier to reuse ideas and components, recruit people with relevant experience, encapsulate good ideas, and wire components together"
                },
                {
                  "title": "creating standards takes too long to wait, and some standards lose touch with the real needs"
                }
              ]
            }
          ]
        },
        {
          "title": "Aspect Oriented Programming"
        }
      ]
    },
    "structure": "org.xmind.ui.map.clockwise"
  }
]