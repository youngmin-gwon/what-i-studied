# Pluggable Selector

## What?

Replace subclasses with dynamically generated method calls.

## Why?

If we have a large number of subclasses that each implement a single method, the overhead involved in maintaining the code can outweigh the benefit of separating them.

```ruby
class Person
  def greeting
    raise NotImplementedError
  end
end

class EnglishSpeaker < Person
  def greeting
    'Hello!'
  end
end

class FrenchSpeaker < Person
  def greeting
    'Bonjour!'
  end
end
```

## How?

By dynamically constructing our method call based on the desired type, we limit the area in which our changes must take place and the system is easier to maintain and comprehend.

```ruby
class Person
  def greet(language)
    send "#{language}_greeting"
  end

  def english_greeting
    'Hello!'
  end

  def french_greeting
    'Bonjour!'
  end
end
```
