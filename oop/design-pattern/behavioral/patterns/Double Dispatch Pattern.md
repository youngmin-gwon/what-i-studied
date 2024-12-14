---
title: Double Dispatch
created at: 2024-12-12
tags:
  - oop
  - design-pattern
  - behavioral-pattern
aliases:
---

## What?

To properly understand Double Dispatch, it'll be useful to understand what is meant by Single Dispatch.

You are probably used to looking at code such as the following.

```ruby
user.validate_password(password)
```

In the above code, the specific method that ends up being executed depends on the runtime type of a single object: user.

This is known as single dispatch.

In a multiple dispatch system, the implementation of validate_password that ends up being invoked would depend on the runtime types of both user and password.

When working with languages that don't directly support double dispatch (like Ruby), we can implement the Double Dispatch Pattern to gain the benefits.

## Why?

The Double Dispatch Pattern is useful for scenarios where you have a set of classes, any one of which may have to interact with another. Imagine we're building a document display system where a number of objects may be rendered inside a number of media.

```ruby
class LineGraph
  def render(medium)
    case medium
    when WordDoc
      # ...
    when Website
      # ...
    when Pdf
      # ...
    end
  end
end

class BarChart
  def render(medium)
    case medium
    when WordDoc
      # ...
    when Website
      # ...
    when Pdf
      # ...
    end
  end
end
```

The problem with the above is twofold:

Each object must know the rendering internals of multiple media.
If we add a new medium, all of our objects must be updated to account for it.
Applying the Double Dispatch Pattern allows us to bring the rendering logic out of our objects and in to a more sensible place, as well as reducing the number of classes that must be edited if we add a new medium in which our objects can be displayed.

## How?

```ruby
# Our objects
class LineGraph
  def render(medium)
    medium.render_line_graph(self)
  end
end

class BarChart
  def render(medium)
    medium.render_bar_chart(self)
  end
end

# Our display media
class WordDoc
  def render_line_graph(line_graph)
    # ...
  end

  def render_bar_chart(line_graph)
    # ...
  end
end

class Website
  def render_line_graph(line_graph)
    # ...
  end

  def render_bar_chart(line_graph)
    # ...
  end
end
```
