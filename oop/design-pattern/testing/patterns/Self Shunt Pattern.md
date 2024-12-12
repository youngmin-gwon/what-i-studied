# Self Shunt

The Self Shunt Pattern allows us to turn our test class itself into the mock object we pass to our object under test.

## Why?

If we are testing object A and want to ensure that it performs the appropriate actions on object B, we might construct a mock B to pass to A.

We can reduce the complexity of our test and the number of objects required by ensuring that our test itself implements the interface we would expect of B, and then pass self to A.

## How?

```ruby
# The class that we're trying to test. We want to ensure that when passed an
# object which adheres to the loggable interface, the `write_to_log` method
# adds a log line to the logger object.
class SomeClass
  def write_to_log(logger, log_line)
    logger.add(log_line)
  end
end

# This defines the behaviour of the logger object, extracted to a module for
# convenience. In a real example, we might not be so lucky to have everything
# wrapped into a little bundle for us, but hey.
module Loggable
  attr_reader :lines

  def add(log_line)
    @lines ||= []
    @lines << log_line
  end
end

class Logger
  include Loggable
end


RSpec.describe SomeClass do
  include Loggable

  it 'uses the self shunt pattern to make an object under test interact directly with the test class' do
    object_under_test = SomeClass.new
    object_under_test.write_to_log(self, 'this_is_a_test')
    expect(lines.include?('this_is_a_test')).to be true 
  end
end
```
