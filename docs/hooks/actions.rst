.. _header-n0:

Actions
=======

.. contents::

**Actions** are one of the two types of
`Hooks <https://developer.wordpress.org/plugins/hooks/>`__.

They provide a way for running a function at a specific point in the
execution of WordPress Core, plugins, and themes. They are the
counterpart to
`Filters <https://developer.wordpress.org/plugin/hooks/filters/>`__.

.. _header-n5:

Add Action 
-----------

The process of adding an action includes two steps.

First, you need to create a Callback function which will be called when
the action is run. Second, you need to add your Callback function to a
hook which will perform the calling of the function.

You will use the
`add_action() <https://developer.wordpress.org/reference/functions/add_action/>`__
function, passing at least two parameters, ``string $tag``,
``callable $function_to_add``.

The example below will run when the ``init`` hook is executed:

.. code:: php

   <?php
   function wporg_custom()
   {
       // do something
   }
   add_action('init', 'wporg_custom');

You can refer to the
`Hooks <https://developer.wordpress.org/plugins/hooks/>`__ chapter for a
list of available hooks.

As you gain more experience, looking through WordPress Core source code
will allow you to find the most appropriate hook.

.. _header-n13:

Additional Parameters 
~~~~~~~~~~~~~~~~~~~~~~

`add_action() <https://developer.wordpress.org/reference/functions/add_action/>`__
can accept two additional parameters, ``int $priority`` for the priority
given to the callback function, and ``int $accepted_args`` for the
number of arguments that will be passed to the callback function.

.. _header-n15:

Priority 
^^^^^^^^^

The priority determines when the callback function will be executed in
relation to the other callback functions associated with a given hook.

A function with a priority of 11 will run *after* a function with a
priority of 10; and a function with a priority of 9 will run *before* a
function with a priority of 10. Any positive integer is an acceptable
value, and the default value is 10.

If two callback functions are registered for the same hook with the same
priority, then will be run in the order that they were registered to the
hook.

| For example, the following callback functions are all registered to
  the
| ``init`` hook, but with different priorities:

.. code:: php

   <?php
   add_action('init', 'run_me_early', 9);
   add_action('init', 'run_me_normal');    // default value of 10 is used since a priority wasn't specified
   add_action('init', 'run_me_late', 11);

The first function to run will be ``run_me_early()``, followed by
``run_me_normal(),`` and finally the last one to run will be
``run_me_late()``.

`Top ↑ <https://developer.wordpress.org/plugins/hooks/actions/#top>`__

.. _header-n23:

Number of Arguments 
^^^^^^^^^^^^^^^^^^^^

Sometimes it’s desirable for a callback function to receive some extra
data related to the function that it’s hooking into.

For example, when WordPress saves a post and runs the ``save_post``
hook, it passes two parameters to the callback function: the ID of the
post being saved, and the post object itself:

.. code:: php

   do_action('save_post', $post->ID, $post);

So, when a callback function is registered for the ``save_post`` hook,
it can specify that it wants to receive those two arguments:

.. code:: php

   add_action('save_post', 'wporg_custom', 10, 2);

…and then it can register the arguments in the function definition:

.. code:: php

   function wporg_custom($post_id, $post)
   {
       // do something
   }

`Top ↑ <https://developer.wordpress.org/plugins/hooks/actions/#top>`__

.. _header-n32:

Example 
--------

If you wanted to modify the query that fetches search results during
`The Loop <https://codex.wordpress.org/the_loop>`__ on the frontend, you
could hook into the ``pre_get_posts`` hook.

.. code:: php

   <?php
   function wporg_search($query)
   {
       if (!is_admin() && $query->is_main_query() && $query->is_search) {
           $query->set('post_type', ['post', 'movie']);
       }
   }
   add_action('pre_get_posts', 'wporg_search');
