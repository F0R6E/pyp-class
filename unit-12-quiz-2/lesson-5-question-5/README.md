# Question 5

Let's augment the `PhotoAlbum` class to support the iteration pattern. There're two
special magic methods you will need to add to the `PhotoAlbum` class in order to
make it iterable.

Make sure the `PhotoAlbum` is able to be iterated successive times, one after the other,
even using the same instance of the class. For that, you will need to keep the
state of the interation in the instance and make sure to reset it to the initial
state each time the iteration is restarted.

Finally, ensure that the interation pattern is supported for both Python 2.x and
3.x.
