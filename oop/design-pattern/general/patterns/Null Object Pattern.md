# Null Object

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
