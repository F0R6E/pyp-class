# Question 4

Write a simple animal hierarchy using Python inheritance. Classes `Cat`, `Dog` and `Cow`
must be supported, all inheriting from the `Animal` class. Each class receives
an unique initialization argument `name`.

All animals must be polymorphic, and support the `talk()` method. Each animal
will "talk" as they know:
- Cat: `"Meow!"`
- Dog: `"Woof! Woof!"`
- Cow: `"Moo! Moo!"`

Make sure to use the `return` statement in the `talk()` method, and not `print()`, otherwise
tests won't pass.

The `Animal` class must not support the `talk()` method, as talking is something
particular of each class. You must raise `NotImplementedError` exception if
someone tries to call `talk()` on an `Animal` instance.
