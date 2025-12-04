---
title: How to Design Program
tags: []
aliases: []
date modified: 2025-11-07 08:43:03 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

## 1. Design is the process of going from a poorly formed problem to a well structured solution

## Primitive rules
- left to right
- inside to outside

## How to Design Function

At first the HtDF recipe may seem like overkill, or it may seem overwhelming. You may suspect that these functions could be written more quickly without the recipe.

The HtDF recipe consists of the following steps:

**(but, it is not waterfall steps, order of steps can be varied)

1. Signature, purpose and stub.
	1. signature
	- Type -> Type
	2. purpose
	- purpose is a line description of what the function produces in terms of what it consumes
	- it must be more deliberate than signature.
	- `Do not just repeat signature. Add more info.`
	3. stub
	- has correct function name
	- has correct number of parameters
	- produces dummy result of correct type
2. Define examples, wrap each in check-expect.
	- Examples help us understand what function must do.
	- Multiple examples to illustrate behavior
	- Wrapping in check-expect means they will also serve as unit tests for the completed function.
3. Template and inventory.
	- template is a function with right function name and right function parameter.
	- body template is simplified like this method
		- (…ReturnValue)
4. Code the function body.
	- In this phase, developers use everything written before to help them know how to finish the function body.
5. Test and debug until correct

### How many tests are needed for a function

> It depends on code coverage. Write as many test as test covers the code and edge cases.

## How To Design Data (HTDD)

### data definition steps

1. A possible **structure definition** (not until compound data)
2. A **type comment** that defines a new type name and describes how to form data of that type.
3. An **interpretation** that describes the correspondence between information and data.
4. One or more **examples** of the data.
5. A **template** for a 1 argument function operating on data of this type.

### itemization simpler rules
- if a given class is the last subclass of its type, we can reduce the test just to guard(ie. number? c)
- if all remaining classes are of the same type, we can eliminate all guards

### Relationship between "How to Define Function" and "How to Define Data"
- (almost) orthogonal = independent
- not always orthogonal because data defines the number of tests used in function design

## The Number of Tests by Type

### Interval
- When writing tests for functions operating on intervals, be sure to test closed boundaries as well as midpoints

## Enumeration
- Functions operating on enumerations should have (at least) as many tests as there are cases in the enumeration.

## Itemization
- As always, itemizations should have enough data examples to clearly illustrate how the type represents information.
- Functions operating on itemizations should have at least as many tests as there are cases in the itemizations. If there are intervals in the itemization, then there should be tests at all points of variance in the interval. In the case of adjoining intervals it is critical to test the boundaries.
