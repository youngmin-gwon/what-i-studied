# Collecting Parameter

## What?

A mutable value that we pass from method to method, accumulating data as it goes.

## Why?

Allows us to refactor a bulky method in which the results of multiple operations are collected in a single variable. This can be handy if we are sure that our method is violating the Single Responsibility Principle.

```ruby
class ScienceExperiment
  def collect_results
    results = []

    if test_validity_of_outliers?
      detected_outliers.each do |outlier|
        results << outlier if valid_outlier?(outlier)
      end
    end

    results << result_from_follow_up_check

    control_group.each do |control_group_result|
      results << reformat_control_group_result(control_group_result)
    end

    results
  end
end
```

## How?

The above code is pretty messy. Let's apply the Collecting Parameter pattern.

```ruby
class ScienceExperimentWithCollectingParameter
  def collect_results
    results = []
    collect_valid_outliers(results)
    collect_results_from_follow_up_check(results)
    collect_formatted_control_group_results(results)
    results
  end

  private

  def collect_valid_outliers(results)
    # ... extracted code
  end

  def collect_results_from_follow_up_check(results)
    # ... extracted code
  end

  def collect_formatted_control_group_results(results)
    # ... extracted code
  end
end
```
