[
  {
    "title": "Map 2",
    "topic": {
      "title": "5. Class Design Guidelines",
      "topics": [
        {
          "title": "Goals",
          "topics": [
            {
              "title": "Model real-world systems in ways similar to the ways in which people actually think"
            }
          ]
        },
        {
          "title": "Encapsulate the behaviors into single-responsibility interfaces and code to the interfaces"
        },
        {
          "title": "Steps",
          "topics": [
            {
              "title": "Identify the public interfaces",
              "topics": [
                {
                  "title": "minimum public interface makes the class as concise as possible"
                },
                {
                  "title": "the implementation should not involve the users at all",
                  "topics": [
                    {
                      "title": "the best way to enable change of behaviors:\nthe use of interfaces and composition"
                    }
                  ]
                }
              ]
            },
            {
              "title": "Design robust constructors (and perhaps destructors)",
              "topics": [
                {
                  "title": "a constructor should put an object into an initial, safe state"
                },
                {
                  "title": "In languages that include destructors, it is of vital importance that the destructors include proper clean-up functions"
                }
              ]
            },
            {
              "title": "Design error handling into a class",
              "topics": [
                {
                  "title": "application should never crash"
                }
              ]
            },
            {
              "title": "Design with reuse in mind"
            },
            {
              "title": "Design with extensibility in mind",
              "topics": [
                {
                  "title": "OCP"
                },
                {
                  "title": "Make names descriptive"
                },
                {
                  "title": "Abstract out non-portable code"
                },
                {
                  "title": "Provide a way to copy and compare objects"
                },
                {
                  "title": "Keep the scope as small as possible"
                }
              ]
            },
            {
              "title": "Design with maintainability in mind",
              "topics": [
                {
                  "title": "Make class as small as possible",
                  "topics": [
                    {
                      "title": "changes in one class have no impact or minimal impact on other classes"
                    }
                  ]
                },
                {
                  "title": "Use iteration in the development process"
                },
                {
                  "title": "Test the interface",
                  "topics": [
                    {
                      "title": "Use stub and do not delete it"
                    }
                  ]
                }
              ]
            },
            {
              "title": "Use object persistence",
              "topics": [
                {
                  "title": "the state of the object must be saved for later use"
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