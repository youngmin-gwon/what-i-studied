## 1.  Design is the process of going from a poorly formed problem to a well structured solution.

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
		- (...ReturnValue)
4. Code the function body.
	- In this phase, developers use everything written before to help them know how to finish the function body.
5. Test and debug until correct

### How many tests are needed for a function

> It depends on code coverage. Write as many test as test covers the code and edge cases.