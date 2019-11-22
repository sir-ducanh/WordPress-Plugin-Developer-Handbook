.. _header-n0:

Basic Shortcodes
================

.. contents::

.. _header-n4:

Add a Shortcode 
----------------

It is possible to add your own shortcodes by using the Shortcode API.
The process involves registering a callback ``$func`` to a shortcode
``$tag`` using
`add_shortcode() <https://developer.wordpress.org/reference/functions/add_shortcode/>`__.

.. code:: php

   <?php
   add_shortcode(
       string $tag,
       callable $func
   );
   ?>

``[wporg]`` is your new shortcode. The use of the shortcode will trigger
the ``wporg_shortcode`` callback function.

Unlike a Theme, a Plugin is run at a very early stage of the loading
process thus requiring us to postpone the adding of our shortcode until
WordPress has been initialized.

We recommend the ``init`` action hook.

.. code:: php

   <?php
   function wporg_shortcodes_init()
   {
       function wporg_shortcode($atts = [], $content = null)
       {
           // do something to $content
    
           // always return
           return $content;
       }
       add_shortcode('wporg', 'wporg_shortcode');
   }
   add_action('init', 'wporg_shortcodes_init');
   ?>

`Top
↑ <https://developer.wordpress.org/plugins/shortcodes/basic-shortcodes/#top>`__

.. _header-n12:

Remove a Shortcode 
-------------------

It is possible to remove shortcodes by using the Shortcode API. The
process involves removing a registered ``$tag`` using
`remove_shortcode() <https://developer.wordpress.org/reference/functions/remove_shortcode/>`__.

.. code:: php

   <?php
   remove_shortcode(
       string $tag
   );
   ?>

Make sure that the shortcode have been registered before attempting to
remove. Specify a higher priority number for
`add_action() <https://developer.wordpress.org/reference/functions/add_action/>`__
or hook into an action hook that is run later.

`Top
↑ <https://developer.wordpress.org/plugins/shortcodes/basic-shortcodes/#top>`__

.. _header-n17:

Check if a Shortcode Exists 
----------------------------

To check whether a shortcode has been registered use
`shortcode_exists() <https://developer.wordpress.org/reference/functions/shortcode_exists/>`__.
