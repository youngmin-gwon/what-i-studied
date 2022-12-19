---

mindmap-plugin: basic

---

# 5. Test Smells: <br/>Maintainability

## smells that <br/>add to your cognitive load
- Conditional logic
   - it is difficult to parse and understand, even though it is testing a fairly trivial behavior
   - Avoid conditional execution such as if, else, for, while, and switch in your test methods
- Parameterized mess
   - a parameterized test is a good pattern, but when used too much and in wrong context, it becomes code smell
   - it is difficult
      - to understand
      - to pinpoint the actual failure when one of the tests fails
   - Distinguish the individual data sets
      - Wrap each set into a method call
      - indentation
   - Add failure message thrown from a failing assertion
- Lack of cohesion in methods
   - some fields(or fixture) of a class are not used by every method
   - these fields usually have bad names
   - Coerce the tests to use the same fixture objects

## smells that <br/>make for a maintenance nightmare
- Duplication
   - =needless repetition
   - Category
      - literal duplication
      - structural duplication
   - it is difficult to understand by logics scattered around
   - Get rid of it
      - but primary interest is readability
- Sleeping snail
   - slow tests due to drags from File I/O, sleep
   - Make test thread notified when each work thread completes: await, etc
- Pixel perfection
   - a special case of primitive assertion and magic number
   - brittle and difficult to understand because of hard-coded, low-level code
   - Replace code with a custom assertion that reads like plain english
   - Express intent at the appropriate level of abstraction

## smells that <br/>cause failures
- Flaky test
   - tests that fail intermittently
   - threads,
         race conditions,
         current date or time,
         computer's performance,
         I/O speed or the CPU load,
         network
   - solution
      - 1. Avoid it, replacing smells with nondeterministic code
      - 2. Control it with test doubles
      - 3. Isolate it in small space
- Crippling file path
   - it causes failure depending on file system
   - it forces developers to place their workspace in the same physical location
   - Avoid absolute path, and use relative paths whenever possible
   - Try to put all project resources under the project's root directory
- Persistent temp files
   - some temp files are not deleted before next test
   - Avoid using files altogether
         where they are not essential to the objects you are testing
   - Keep the use of physical files to a minimum
   - Delete the file before next test
   - Use unique names for temporary files if possible
   - Be explicit about whether or not a file should exist