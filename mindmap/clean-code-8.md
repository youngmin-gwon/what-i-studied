
---

mindmap-plugin: basic

---

    
# 8. Boundary
## Third-Party Code
- Do not make it propagate all over the application
  - always better to depend on something you control than on something you don't control, lest it ending up controlling you
  - Make boundaries and keep it inside a class or close family of classes
- How to be consistent across boundaries
  - Learning Test
    - Benefits
      - can make us understand the third party code
      - can do controlled experiments that check our understanding of the API
      - cost nothing
      - verify the outer code works if new version releases
  - Adapter Pattern
    - Benefits
      - helps write code for unknown world
      - convenient for testing
      - helps client code more readable and focused on what it is trying to accomplish