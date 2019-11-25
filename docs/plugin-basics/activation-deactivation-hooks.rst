.. _header-n0:

Activation / Deactivation Hooks
===============================

.. contents::

Activation and deactivation hooks provide ways to perform actions when
plugins are activated or deactivated.

On activation, plugins can run a routine to add rewrite rules, add
custom database tables, or set default option values.

On deactivation, plugins can run a routine to remove temporary data such
as cache and temp files and directories.

   Alert:The deactivation hook is sometimes confused with the `uninstall
   hook <https://developer.wordpress.org/plugins/the-basics/uninstall-methods/>`__.
   The uninstall hook is best suited to **delete all data permanently**
   such as deleting plugin options and custom tables, etc.

.. _header-n8:

Activation
----------

To set up an activation hook, use the
`register\ activation\ hook() <https://developer.wordpress.org/reference/functions/register_activation_hook/>`__
function:

.. code-block:: php

   register_activation_hook( __FILE__, 'pluginprefix_function_to_run' );

.. _header-n12:

Deactivation
------------

To set up a deactivation hook, use the
`register\ deactivation\ hook() <https://developer.wordpress.org/reference/functions/register_deactivation_hook/>`__
function:

.. code-block:: php

   register_deactivation_hook( __FILE__, 'pluginprefix_function_to_run' );

The first parameter in each of these functions refers to your main
plugin file, which is the file in which you have placed the `plugin
header comment <header-requirements.md>`__. Usually these two functions
will be triggered from within the main plugin file; however, if the
functions are placed in any other file, you must update the first
parameter to correctly point to the main plugin file.

.. _header-n17:

Example
-------

One of the most common uses for an activation hook is to refresh
WordPress permalinks when a plugin registers a custom post type. This
gets rid of the nasty 404 errors.

Let’s look at an example of how to do this:

.. code-block:: php

   function pluginprefix_setup_post_type() {  
   	// register the "book" custom post type
     register_post_type( 'book', ['public' => 'true'] );
   }
   add_action( 'init', 'pluginprefix_setup_post_type' );

   function pluginprefix_install() {
     // trigger our function that registers the custom post type
     pluginprefix_setup_post_type();
     
     // clear the permalinks after the post type has been registered
     flush_rewrite_rules();
   }
   register_activation_hook( __FILE__, 'pluginprefix_install' );

If you are unfamiliar with registering custom post types, don’t worry –
this will be covered later. This example is used simply because it’s
very common.

Using the example from above, the following is how to reverse this
process and deactivate a plugin:

.. code-block:: php

   function pluginprefix_deactivation() {
   	// unregister the post type, so the rules are no longer in memory
   	unregister_post_type( 'book' );
   	
   	// clear the permalinks to remove our post type's rules from the database
   	flush_rewrite_rules();
   }
   register_deactivation_hook( __FILE__, 'pluginprefix_deactivation' );

For further information regarding activation and deactivation hooks,
here are some excellent resources:

-  `register\ activation\ hook() <https://developer.wordpress.org/reference/functions/register_activation_hook/>`__
   in the WordPress function reference.

-  `register\ deactivation\ hook() <https://developer.wordpress.org/reference/functions/register_deactivation_hook/>`__
   in the WordPress function reference.
