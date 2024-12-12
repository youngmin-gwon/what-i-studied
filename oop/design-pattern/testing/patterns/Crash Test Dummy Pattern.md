# Crash Test Dummy

## What?

A Crash Test Dummy is an object that we have created to fail in a specific — and spectacular — way.

## Why?

We're our own error handling code around a third party API, file system, or similar with well defined but difficult to reproduce failure modes. How do you force someone elses' API to return a given error code, for example, or test that your application gracefully handles a full hard disk without filling the hard disk with trash data?

## How?

We can make a crash test dummy by mocking or stubbing the object that does the actual system interaction and forcing it to raise a certain exception. This allows us to test the error handling in our code without performing extreme acts.

```ruby
require 'net/http'

# Our API client. It performs HTTP interactions, it (usually) works, but it
# doesn't do any error handling of its own.
class MyApiClient
  def read_from_endpoint
    :some_good_stuff_returned_from_the_api
  end
end

# The class under test. This class consumes data from the API using the
# API client, and we want to ensure that our rescue block behaves as
# expected.
class ApiConsumer
  def pull_data
    response = MyApiClient.new.read_from_endpoint
  rescue Net::ReadTimeout
    response = :read_timeout_failure
  ensure
    response
  end
end

RSpec.describe ApiConsumer do
  it 'handles read timeouts from the api' do
    # We're using a stubbed method to implement our crash test dummy.
    expect_any_instance_of(MyApiClient).to receive(:read_from_endpoint)
                                             .and_raise(Net::ReadTimeout)

    consumer = ApiConsumer.new
    expect(consumer.pull_data).to eq(:read_timeout_failure)
  end
end
```
