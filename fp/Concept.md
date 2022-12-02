## Motive

> keep the computation and business logic pure and free from side effects.

All of the API calls, database transactions and stuff with side effects move towards the external layer of the application

## Mathmetical Functions

In Mathematics, functions are mappers i.e., they map inputs to outputs

### Total Function

> A function defined for all its inputs

![[total_fn.png]]

### Partial Function

> A function that is not defined for some of its inputs

![[partial_fn.png]]

## Pure function

> A function that is deterministic(always giving same output) and has no side effects.

1. deterministic

- giving always same output

```dart
void main() {
	final _result = doubleValue(5);
	assert(_result == 10);
}

int doubleValue(int value) => value*2;
```

2. has no side effect
- not dealing with external states

has side effect
```dart
void main() {
	greetImpure();
	name = "Bob";
	greetImpure();
}

String name = "John";

void greetImpure() => "Hello, $name";
```

has no side effect
```dart
void main() {
	greet("John");
	greet("Bob");
}

void greetImpure(String name) => "Hello, $name";
```

more example
```dart
DateTime getDateTime() => DateTime.now(); // impure

int add(int a, int b) => a+b; // pure

int getRandomNumber() => Random().nextInt(100); // impure

int? double2(int value) {
	if (value == 1) return 2;
	if (value == 2) return 4;
	if (value == 3) return 6;
} // total, pure

int counter = 0;

int increment(int delta) => (count++) + delta; // total, impure

// total(if divider == 0, the function will return double.infinity)
num totalDivide(int dividend, int divider) => dividend / divider;

// partial(if divider == 0, the function will throw exception)
num partialDivide(int dividend, int divider) => dividend ~/ divider;
```

#### benefits

1. pure function is easy to unit test
2. the chances of unexpected bugs reduce
3. pure function provides caching mechanisms that help in reducing heavy computation
4. pure function is easy to prallelize

#### referential transparency

> a function call can be reduced by its return value and not affect the rest of the program



another way to determine if a function is pure

## Difference between parameter and argument

### Parameter
> part of function declaration

### Argument
> values passed to function

## Arity
> the number of arguments a function takes

```dart
int increment(int number) => number+1; // arity: 1(unary)

int add(int numberOne, int numberTwo) => numberOne + numberTwo;// arity: 2(binary)

DateTime now() => DateTime.now()// arity: 0(nullary);

bool isOdd(int number) => number %2 == 1;// arity: 1(unary), predicate function(a function that returns a boolean value)
```

## Closure
> when a function is defined into another function, that inner function remembers the scope of the outer function even if the outer function is executed and no longer available

```dart
typedef IntCallback = int Function(int number);

void main() {
	final _firstFnResult = _firstFunction();
	_firstFnResult();

	final _increment = add(1);
	print(_increment(2));
}

Function _firstFunction() {
	final _someValue = 'First function scope';

	void _secondFunction() {
		print(_someValue);
	}

	return _secondFunction;
}

IntCallback add(int a) {
	return (int b) {
		return a+b;
	}
}
```

## Partial Application

> a function applied to some of its inputs

closure helps us to achieve partial application

idea: lock in some of the parameters, so we don't have to pass them repeatedly

The `add` function above needs two arguments in series to return the result, but we have passed a single argument and assigned it to the `_increment` variable. We have not given all the arguments; we have partially applied the function.

## Point-free style

> a function without needing to pass in the arguments explicitly

```dart
void main() {
	const _numbers = [1,2,3,4,5];
	// not point free
	final result1 = _numbers.map((e)=>increment(e)).toList();
	// point free
	final results = _numbers.map(increment).toList();
}

int increment(int number) => number+1;
```

## Currying

> Breaking down a multi-argument function into a series of single-argument functions

```dart
void main(List‹String> args) {
	// Non curried
	print(greet('Hello', 'Noah')); // Hello Noah
	// Curried
	print(curriedGreet('Hello')('Noah')); // Hello Noah
}

String greet(String salutation, String name) = '$salutation $name*';

typedef StringCallback = String Function(String name);

// to nested? consider packages like dartz, fpdart
StringCallback curriedGreet(String salutation) {
	return (String name) {
		return '$salutation $name';
	}
}
```

## Currying vs Partial Application

> The partial application can take more than one argument at a time,
> whereas the curried function always has to return a unary function

Curried functions are used to create partial applications, but all partial applications are not curried functions.

