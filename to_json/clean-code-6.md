[
  {
    "title": "Map 1",
    "topic": {
      "title": "6. Objects and Data Structures",
      "topics": [
        {
          "title": "Object",
          "topics": [
            {
              "title": "exposes behaviors"
            },
            {
              "title": "hides data"
            },
            {
              "title": "easy to add new classes without changing exisiting functions"
            },
            {
              "title": "The Law of Demeter",
              "topics": [
                {
                  "title": "A module should not know about the innards of the objects it manipulates"
                },
                {
                  "title": "methods that method f of a class C should only call",
                  "topics": [
                    {
                      "title": "C"
                    },
                    {
                      "title": "An object created by f"
                    },
                    {
                      "title": "An object passed as an argument to f"
                    },
                    {
                      "title": "An object held in an instance variable of C"
                    }
                  ]
                },
                {
                  "title": "The method should not invoke methods on objects that are returned by any of the allowed functions"
                },
                {
                  "title": "Do not make the call like Train Wrecks: a bunch of coupled train cars",
                  "topics": [
                    {
                      "title": "final String outputDir = ctxt.getOptions().getScratchDir();"
                    }
                  ]
                },
                {
                  "title": "Do not make Hybrid style(=half object, half data structure)",
                  "topics": [
                    {
                      "title": "Hybrids make it hard to add new functions but also make it hard to add new data structures"
                    }
                  ]
                },
                {
                  "title": "Look what the intent of train wreck is and make a behavior to achieve that."
                }
              ]
            },
            {
              "title": "Data Abstraction",
              "topics": [
                {
                  "title": "Hiding implementation is about abstraction"
                },
                {
                  "title": "An interface class exposes abstract interfaces that allow its users to manipulate the essence of the data, without having to know its implementation"
                },
                {
                  "title": "Developers do not want to expose the details of class data"
                },
                {
                  "title": "Abstraction is not merely accomplished by using interfaces and/or getters and setters. Serious thought need to be put into the best way to represent the data that an object contains"
                }
              ]
            }
          ]
        },
        {
          "title": "Object is not always an answer. Data structure is sometimes the answer. "
        },
        {
          "title": "Data Structure",
          "topics": [
            {
              "title": "exposes data"
            },
            {
              "title": "no behaviors"
            },
            {
              "title": "easy to add new functions without changing the existing data structures"
            },
            {
              "title": "Data Transfer Objects(DTO)",
              "topics": [
                {
                  "title": "A class with public fields and no methods"
                },
                {
                  "title": "useful when communicating with databases or parsing messages from sockets and so on"
                },
                {
                  "title": "The quasi-encapsulation(only getter) provides no other benefit. Do not use that pattern"
                },
                {
                  "title": "Active Record",
                  "topics": [
                    {
                      "title": "Special case of DTO"
                    },
                    {
                      "title": "public fields(or private fields with setter/getter) and methods(save, find)"
                    },
                    {
                      "title": "direct translations from database tables, or other data sources"
                    },
                    {
                      "title": "Treat Active Record as a data structure"
                    },
                    {
                      "title": "Create separate objects that contain the business rules and that hide their internal data"
                    }
                  ]
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