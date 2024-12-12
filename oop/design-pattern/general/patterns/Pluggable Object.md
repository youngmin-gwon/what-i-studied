# Pluggable Object

## What?

Store a reference to an object which implements a known interface and make references to it throughout the rest of the object.

## Why?

We would like to reduce the amount of conditional logic in the following code, which controls movement for a person who is either driving or walking. It's messy as it is, and if we add a third mode of transport, we're really going to be suffering.

```ruby
class Driver
  def start
    @driving = driving?

    if @driving
      press_accelerator
    else
      pedal
    end
  end

  def steer
    if @driving
      turn_wheel
    else
      turn_handlebars
    end
  end

  def stop
    if @driving
      release_accelerator
    else
      stop_pedaling
    end
  end
end
```

## How?

```ruby
class Driver
  def start
    @mode = if driving?
              DrivingMode.new
            else
              CyclingMode.new
            end

    @mode.start
  end

  def steer
    @mode.steer
  end

  def stop
    @mode.stop
  end
end
```
