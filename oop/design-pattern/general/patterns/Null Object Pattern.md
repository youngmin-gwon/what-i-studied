# Null Object

#design-pattern

## Description

`null` 값을 사용하는 대신 특정 작업을 수행하지 않는 객체를 제공하는 디자인 패턴

이 패턴은 `null` 체크를 줄이고, 코드의 복잡성을 감소시키며, 기본 동작을 정의할 수 있게 함.

---

## Structure

1. **Abstract Interface**: 공통 작업(메서드)을 정의하는 인터페이스나 추상 클래스.
2. **Concrete Implementation**: 실제 동작을 수행하는 클래스.
3. **Null Object**: 아무 동작도 하지 않거나 기본 동작을 제공하는 클래스.

## Example

### Before

기존 방식으로 null check

```dart
abstract class Animal {
  void makeSound();
}

class Dog implements Animal {
  @override
  void makeSound() => print("Woof!");
}

void playWithAnimal(Animal? animal) {
  if (animal != null) {
    animal.makeSound();
  } else {
    print("No animal to play with.");
  }
}

void main() {
  Animal? dog = Dog();
  Animal? nullAnimal = null;

  playWithAnimal(dog);
  playWithAnimal(nullAnimal);
}
```

### After

null check 하지 않음

```dart
abstract class Animal {
  void makeSound();
}

class Dog implements Animal {
  @override
  void makeSound() => print("Woof!");
}

// Null Object
class NullAnimal implements Animal {
  @override
  void makeSound() {
    // No operation or default behavior
    print("Silence...");
  }
}

void playWithAnimal(Animal animal) {
  animal.makeSound();
}

void main() {
  Animal dog = Dog();
  Animal nullAnimal = NullAnimal();

  playWithAnimal(dog);         // Output: Woof!
  playWithAnimal(nullAnimal);  // Output: Silence...
}```

## Adaptability

1. null 체크를 피하고 싶을 때:
- 메서드나 클래스가 항상 유효한 객체를 기대할 때.
2. 기본 동작을 정의해야 할 때:
- 비어 있거나 기본값으로 동작해야 하는 경우.
3. 코드의 복잡도를 줄이고 싶을 때:
- 여러 if-else 또는 null 체크가 반복적으로 사용되는 경우.
4. 다형성을 유지하려는 경우:
- null 대신 특정 인터페이스의 구현체를 사용하여 객체의 행위를 일관되게 유지.

## What?

Replace conditional checks for nil with an object that returns default data or nil.

## Why?

To tidy up conditional logic in our code.

Imagine you're building a message board. Messages are posted by registered users, but if a user should delete their account, the message is preserved and displayed without any identifying information.

Our view code may be scattered with helper methods like the following:

```ruby
def author_username(post)
  if post.author.present?
    post.author.username
  else
    'Deleted user'
  end
end
```

The more attributes of the user that we're displaying in the page, the more conditional statements we have checking for the existence of said user.

## How?

How might we describe a user that no longer exists? We would like them to return some sensible data about what such a user might be, and if we ask them anything else that we might ask of an existing user, we at least want the system to not crash.

```ruby
class NullUser
  def username
    'Deleted user'
  end

  def method_missing(*)
    nil
  end
end
```

And what if our instances of Post had an author, even when they didn't?

```ruby
class Post
  def author
    self[:author] || NullUser.new
  end
end
Now the logic towards our view level becomes considerably more simple.

def author_username(post)
  post.author.username
end
```

In fact, our helper method is now so simple that there is a strong argument for removing it entirely and calling our username method directly from the view.

```html
<div class="post">
  <span class="author"><%= @post.author.username %></span>
</div>
```
