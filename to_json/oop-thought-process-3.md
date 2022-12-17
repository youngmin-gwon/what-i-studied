[
  {
    "title": "Map 1",
    "topic": {
      "title": "3. More Object-Oriented Concepts",
      "topics": [
        {
          "title": "Constructor",
          "topics": [
            {
              "title": "methods that share the same name as the class"
            },
            {
              "title": "one of the first things called when a new object is created"
            },
            {
              "title": "functions",
              "topics": [
                {
                  "title": "memory allocation"
                },
                {
                  "title": "attribute initialization"
                }
              ]
            },
            {
              "title": "default constructor",
              "topics": [
                {
                  "title": "at least one constructor always exists, regardless of whether you write a constructor yourself"
                },
                {
                  "title": "Provide default constructor. Do not count on the compiler to initialize attribute"
                }
              ]
            },
            {
              "title": "multiple constructor",
              "topics": [
                {
                  "title": "in some languages, multiple constructor can be provided using method overloading"
                }
              ]
            },
            {
              "title": "How the superclass is costructed",
              "topics": [
                {
                  "title": "1. Inside the constructor, the constructor of the class’s superclass is called"
                },
                {
                  "title": "2. Each class attribute of the object is initialized"
                },
                {
                  "title": "3. The rest of the code in the constructor executes"
                }
              ]
            }
          ]
        },
        {
          "title": "Operator Overloading",
          "topics": [
            {
              "title": "it can be downright confusing for people who read and maintain code"
            }
          ]
        },
        {
          "title": "Error Handling",
          "topics": [
            {
              "title": "important advantage for OO programming languages"
            },
            {
              "title": "this solves the problem of trying to figure out where the problem started and unwinding the code to the proper point"
            }
          ]
        },
        {
          "title": "Scope",
          "topics": [
            {
              "title": "attributes (and methods) exist within a particular scope"
            },
            {
              "title": "types",
              "topics": [
                {
                  "title": "1. Local attribute"
                },
                {
                  "title": "2. Object attribute",
                  "topics": [
                    {
                      "title": "member variable"
                    },
                    {
                      "title": "not shared between different objects"
                    }
                  ]
                },
                {
                  "title": "3. Class attribute",
                  "topics": [
                    {
                      "title": "static variable",
                      "topics": [
                        {
                          "title": "as close to global data as we get in OO design"
                        }
                      ]
                    },
                    {
                      "title": "shared between different objects"
                    },
                    {
                      "title": "potential synchronization problem"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "title": "Multiple Inheritance",
          "topics": [
            {
              "title": "one of the more powerful and challenging aspects of class design"
            },
            {
              "title": "multiple inheritance can significantly increase complexity of a system, both for the programer and the compiler writers"
            },
            {
              "title": "The modern concept of inheritance is a single-parent inheritance"
            }
          ]
        },
        {
          "title": "Object Operation",
          "topics": [
            {
              "title": "copyWith(), equals() operation",
              "topics": [
                {
                  "title": "deep copy",
                  "topics": [
                    {
                      "title": "make new copy for all referenced objects"
                    },
                    {
                      "title": "the copy itself can create significant overhead"
                    }
                  ]
                },
                {
                  "title": "shallow copy",
                  "topics": [
                    {
                      "title": "simple copy the reference and not follow the levels"
                    }
                  ]
                }
              ]
            },
            {
              "title": "not quite simple because object contains reference"
            }
          ]
        }
      ]
    },
    "structure": "org.xmind.ui.map.clockwise"
  }
]