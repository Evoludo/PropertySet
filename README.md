# PropertySet

A Python module to enumerate sets composed of strings, usable as class properties.

This stops stupid stuff like this:

```python
class States(object):
    enabled = 'enabled'
    disabled = 'disabled'
````

Instead, you can use PropertySet like so:

```python
from PropertySet import PropertySet

States = PropertySet('States', ['enabled', 'disabled'])
```

It then behaves like the code above:
```python
>>> States.enabled
'enabled'
```

But is also representable as a string and enumerable as a list:
```python
>>> States
States { disabled, enabled }
>>> list(States)
['enabled', 'disabled']
```

PropertySets are iterable and comparable:

```python
>>> 'enabled' in States
True
>>> 'slartibartfast' in States
False
>>> States2 = PropertySet('States2', ['enabled', 'disabled'])
>>> States == States2
False
>>> States2 = PropertySet('States', ['disabled', 'enabled'])
>>> States == States2
True
```

PropertySets are also immutable:

```python
>>> States.enabled = 'slartibartfast'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "PropertySet.py", line 27, in __setattr__
    raise AttributeError(msg.format(prop, type(self).__name__, self._name))
AttributeError: Cannot set attribute 'enabled' because PropertySet object 'States' is immutable
```
