.. _header-n0:

Simple Testing of WP-Cron
=========================

.. contents::

In this tutorial we will be creating a plugin that runs a task every 5
seconds and displays a message. In order to test this we will load the
wp-cron.php file directly in our browser and output data to the display,
otherwise we would have to perform some other action, maybe in the
database, as the output is typically not shown on the site. So let’s run
through the initial steps to get this setup quickly.

.. _header-n4:

Create the plugin file 
-----------------------

In the wp-content/plugins folder create the folder ‘my-wp-cron-test’ and
the file ‘my-wp-cron-test.php’. Obviously you can name it whatever you
would like. This name is simply descriptive of our intended use.

Open the PHP file for editing and insert the following lines

.. code:: php

   <?php
   /*
   Plugin Name: My WP-Cron Test
   */

This text will setup the plugin for display and activation in your
wp-admin Plugins menu. Be sure to enable the plugin.

`Top
↑ <https://developer.wordpress.org/plugins/cron/simple-testing/#top>`__

.. _header-n10:

Testing the code 
-----------------

Open your browser and point it to YOUR\ *SITE*\ URL/wp-cron.php

`Top
↑ <https://developer.wordpress.org/plugins/cron/simple-testing/#top>`__

.. _header-n13:

View all currently scheduled tasks 
-----------------------------------

WordPress has an undocumented function, *get*\ cron\ *array, that
returns an array of all currently scheduled tasks. We are going to use a
crude but effective method to dump out all the tasks using var*\ dump.
For ease of use place the following code in the plugin:

.. code:: php

   echo '<pre>'; print_r( _get_cron_array() ); echo '</pre>';

Into an easy to call function like:

.. code:: php

   function bl_print_tasks() {
       echo '<pre>'; print_r( _get_cron_array() ); echo '</pre>';
   }
