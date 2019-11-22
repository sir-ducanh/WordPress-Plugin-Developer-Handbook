.. _header-n0:

Hooks
=====

**Hooks are a way for one piece of code to interact/modify another piece
of code.** They make up the foundation for how plugins and themes
interact with WordPress Core, but they’re also used extensively by Core
itself.

**There are two types of hooks:**
`Actions <https://developer.wordpress.org/plugins/hooks/actions/>`__ and
`Filters <https://developer.wordpress.org/plugins/hooks/filters/>`__. To
use either, you need to write a custom function known as a ``Callback``,
and then register it with WordPress hook for a specific Action or
Filter.

`Actions <https://developer.wordpress.org/plugins/hooks/actions/>`__
allow you to add data or change how WordPress operates. Callback
functions for Actions will run at a specific point in in the execution
of WordPress, and can perform some kind of a task, like echoing output
to the user or inserting something into the database.

`Filters <https://developer.wordpress.org/plugins/hooks/filters/>`__
give you the ability to change data during the execution of WordPress.
Callback functions for Filters will accept a variable, modify it, and
return it. They are meant to work in an isolated manner, and should
never have `side
effects <https://en.wikipedia.org/wiki/Side_effect_(computer_science)>`__
such as affecting global variables and output.

WordPress provides many hooks that you can use, but you can also `create
your
own <https://developer.wordpress.org/plugins/hooks/custom-hooks/>`__ so
that other developers can extend and modify your plugin or theme.

.. _header-n7:

External Resources
------------------

-  `Filter
   Reference <https://codex.wordpress.org/Plugin_API/Filter_Reference>`__

-  `Action
   Reference <https://codex.wordpress.org/Plugin_API/Action_Reference>`__

-  `Adam Brown’s database of hooks <http://adambrown.info/p/wp_hooks>`__

-  `Actions and Filters are Not the Same
   Thing <http://ottopress.com/2011/actions-and-filters-are-not-the-same-thing/>`__
