.. _header-n0:

Filters
=======

.. contents::

**Filters** are one of the two types of
`Hooks <https://developer.wordpress.org/plugins/hooks/>`__.

They provide a way for functions to modify data of other functions. They
are the counterpart to
`Actions <https://developer.wordpress.org/plugins/hooks/actions/>`__.

Unlike
`Actions <https://developer.wordpress.org/plugins/hooks/actions/>`__,
filters are meant to work in an isolated manner, and should never have
`side
effects <https://en.wikipedia.org/wiki/Side_effect_(computer_science)>`__
such as affecting global variables and output.

.. _header-n6:

Add Filter 
-----------

The process of adding a filter includes two steps.

First, you need to create a Callback function which will be called when
the filter is run. Second, you need to add your Callback function to a
hook which will perform the calling of the function.

You will use the
`add_filter() <https://developer.wordpress.org/reference/functions/add_filter/>`__
function, passing at least two parameters, ``string $tag``,
``callable $function_to_add``.

The example below will run when the ``the_title`` filter is executed.

.. code:: php

   <?php
   function wporg_filter_title($title)
   {
       return 'The ' . $title . ' was filtered';
   }
   add_filter('the_title', 'wporg_filter_title');

Lets say we have a post title, “Learning WordPress”, the above example
will modify it to be “The Learning WordPress was filtered”.

You can refer to the
`Hooks <https://developer.wordpress.org/plugins/hooks/>`__ chapter for a
list of available hooks.

As you gain more experience, looking through WordPress Core source code
will allow you to find the most appropriate hook.

.. _header-n15:

Additional Parameters 
~~~~~~~~~~~~~~~~~~~~~~

`add_filter() <https://developer.wordpress.org/reference/functions/add_filter/>`__
can accept two additional parameters, ``int $priority`` for the priority
given to the callback function, and ``int $accepted_args`` for the
number of arguments that will be passed to the callback function.

For detailed explanation of these parameters please read the article on
`Actions <https://developer.wordpress.org/plugins/hooks/actions/>`__.

`Top ↑ <https://developer.wordpress.org/plugins/hooks/filters/#top>`__

.. _header-n19:

Example 
~~~~~~~~

To add a CSS class to the tag when a certain condition is met:

.. code:: php

   <?php
   function wporg_css_body_class($classes)
   {
       if (!is_admin()) {
           $classes[] = 'wporg-is-awesome';
       }
       return $classes;
   }
   add_filter('body_class', 'wporg_css_body_class');
