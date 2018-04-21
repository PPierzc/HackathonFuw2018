# HackathonFuw2018

---
### Correlation
To calculate correlation between the height of the function and it's curvature you need to:

```python
 import correlate
 correlate.correlate(data)
```

_data_ is an 2D array of the structure:

    [
        [func1 a, func1 b, func1 h],
        [func2 a, func2 b, func2 h],
        [func3 a, func3 b, func3 h],
        ...
    ]
returns the correlation coefficient