---

mindmap-plugin: basic

---

# 2. Meaningful Names

## Clarity
- Use intention-revealing names
- Avoid disinformation
   - Don't use lower-case L with 1 or uppercase O with 0 as variable names, especially in combination
   - Refrain from using hypotenuse like hp
   - Beware of using names like List when it is not actually a List => accounts, accountGroup, bunchOfAccounts
   - Beware of names which vary in small ways like ~HandlingOfStrings and ~StorageOfStrings
- Make meaningful distinction
   - not a1, a2, a3
   - not nameString, but name
- Avoid mental mapping
- Pick one word per concept
- Don't pun
- Add meaningful context
   - state(?)
   - addressState(!)

## Use searchable-enough long names
- single-letter names can only be used as local variables inside short methods

## Class Name
- noun, noun phrase names

## Method Name
- verb, verb phrase names

## Use pronounceable names
- If you can't pronounce it, you cannot discuss it without sounding like an idiot
- Avoid encodings for pronounceability

## Use domain names
- Solution Domain
   - Visitor, Queue, etc
- Problem Domain
   - CameraProduction, etc

## Don't add gratuitous context
- bad idea to prefix every class with GSD