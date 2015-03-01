Title: Field encapsulation pattern in Python, part 1: getters and setters
Author: Josh Wickham
Date: 02/28/2015 09:00
Category: Software
Tags: python, getter/setter, pattern
Status: draft


Time to stir things up. Let's assume that we're adding another attribute to the object and it also is supposed to be a
uuid (my real-world object has four, so this isn't unreasonable). Using the getter/setter decorators, this is what it
could look like, ignoring the @property methods (we're not going to touch those very much in this demo):

    >>> class MyClass:
    ...     def __init__(self):
    ...         self.my_uuid = uuid.uuid4()
    ...         self.your_uuid = uuid.uuid4()
    ...
    ...     @my_uuid.setter
    ...     def my_uuid(self, value):
    ...         if not isinstance(value, uuid.UUID):
    ...             # bad value; do what you like here
    ...             raise ValueError('my_uuid must be a UUID')
    ...         self._my_uuid = value
    ...
    ...     @your_uuid.setter
    ...     def your_uuid(self, value):
    ...         if not isinstance(value, uuid.UUID):
    ...             # bad value; do what you like here
    ...             raise ValueError('your_uuid must be a UUID')
    ...         self._your_uuid = value
    ... 

Not great; there's a lot of code similarities here which could be generalized. Let's do that

    >>> class MyClass:
    ...     def __init__(self):
    ...         self.my_uuid = uuid.uuid4()
    ...         self.your_uuid = uuid.uuid4()
    ...
    ...     @my_uuid.setter
    ...     def my_uuid(self, value):
    ...         self._assert_uuid(value)
    ...         self._my_uuid = value
    ...
    ...     @your_uuid.setter
    ...     def your_uuid(self, value):
    ...         self._assert_uuid(value)
    ...         self._your_uuid = value
    ...
    ...    def _assert_uuid(self, potential_uuid):
    ...        if not isinstance(potential_uuid, uuid.UUID):
    ...             raise ValueError('must be a UUID')
    ... 

Better... but we still have code duplication. This is where we can start using Python's magic methods! These methods
are called upon various different parts of the typical object operations; the one I want to use is `__setattr__` which
gets called every time an attribute is written to. It takes the name of the attribute and the potential value as its only
arguments. Let's see how we can make this work. We'll also add in `__getattr__` which is called whenever an attribute
isn't found on the object

    >>> class MyClass:
    ...     def __init__(self):
    ...         self.my_uuid = uuid.uuid4()
    ...         self.your_uuid = uuid.uuid4()
    ...
    ...     def __setattr__(self, attr_name, value):
    ...         self._assert_uuid(value)
    ...         self.__dict__['_%s' % attr_name] = value
    ...
    ...     def __getattr__(self, attr_name):
    ...         return self.__dict__['_%s' % attr_name]
    ...
    ...    def _assert_uuid(self, potential_uuid):
    ...        if not isinstance(potential_uuid, uuid.UUID):
    ...             raise ValueError('must be a UUID')
    ... 

Looking better! As I mentioned, I had four uuid attributes on my object; let's add them:

    >>> class MyClass:
    ...     def __init__(self):
    ...         self.my_uuid = uuid.uuid4()
    ...         self.your_uuid = uuid.uuid4()
    ...         self.uuid_a = uuid.uuid4()
    ...         self.uuid_b = uuid.uuid4()
    ...
    ...     def __setattr__(self, attr_name, value):
    ...         self._assert_uuid(value)
    ...         self.__dict__['_%s' % attr_name] = value
    ...
    ...     def __getattr__(self, attr_name):
    ...         return self.__dict__['_%s' % attr_name]
    ...
    ...    def _assert_uuid(self, potential_uuid):
    ...        if not isinstance(potential_uuid, uuid.UUID):
    ...             raise ValueError('must be a UUID')
    ... 

Wow, only two new lines!

So, I hate to break it to you; it's not all fun and games. There are a couple pretty major flaws with this, as cool as
it seems. Let's take the issues one at a time.

First issue: what happens if I want a datetime attribute? I'll add it in the `__init__` function:

    ...    def __init__(self):
    ...        self.created_datetime = datetime.datetime.utcnow()

And then I'll build a new object to test changing the attribute:

    >>> obj = MyClass()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 7, in __init__
      File "<stdin>", line 9, in __setattr__
      File "<stdin>", line 13, in _assert_uuid
    ValueError: must be a UUID

What happened? Remember when I said that ALL attributes go through `__setattr__`? That includes during internal assignments,
such as during `__init__` as well. Shucks. So how do we get around this? Well, you could have a map on the class, describing
they types of each field. Then, you can reference that inside `__setattr__`:

    >>> class MyClass:
    ...     attribute_types = {
    ...         'my_uuid': uuid.UUID,
    ...         'your_uuid': uuid.UUID,
    ...         'uuid_a': uuid.UUID,
    ...         'uuid_b': uuid.UUID,
    ...         'created_datetime': datetime.datetime
    ...     }
    ...
    ...     def __init__(self):
    ...         self.my_uuid = uuid.uuid4()
    ...         self.your_uuid = uuid.uuid4()
    ...         self.uuid_a = uuid.uuid4()
    ...         self.uuid_b = uuid.uuid4()
    ...         self.created_datetime = datetime.datetime.utcnow()
    ...
    ...     def __setattr__(self, attr_name, value):
    ...         intended_type = self.attribute_types.get(attr_name)
    ...         if intended_type and not isinstance(value, intended_type):
    ...             raise ValueError('%s expected to be a %s' % (attr_name, intended_type.__name__))
    ...         self.__dict__['_%s' % attr_name] = value
    ...
    ...     def __getattr__(self, attr_name):
    ...         return self.__dict__['_%s' % attr_name]
    ... 
    >>> obj = MyClass()
    >>>

Yay, back down to three functions for five attributes, and it works! But, what happens if the attribute is not in the
`attribute_types` dict? The way we have it written, it can just be applied directly to the object:

    >>> obj.petunias = 'are lovely'
    >>> obj.petunias
    'are lovely'


