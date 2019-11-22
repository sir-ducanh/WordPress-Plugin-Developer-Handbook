.. _header-n0:

Scheduling WP Cron Events
=========================

.. contents::

.. _header-n4:

Scheduling a recurring task 
----------------------------

In order to get your task to execute you must create your own custom
hook and give that hook the name of a function to execute. This is a
very important step. Forget it and your task will never run.

The following will create the hook. The first parameter is the name of
the hook, and the second is the name of your function to call.

.. code:: php

   add_action( 'bl_cron_hook', 'bl_cron_exec' );

Now on to the actual scheduling of the task. Another important note is
that WP-Cron is kind of naive when scheduling tasks. Tasks are driven by
the hook provided for the task, however if you call
`wp\ schedule\ event() <https://developer.wordpress.org/reference/functions/wp_schedule_event/>`__
multiple times, even with the same hook name, the event will be
scheduled multiple times. If your code adds the task on each page load
this could result in the task being scheduled several thousand times.
Probably not a great idea. WordPress provides a convenient function
called
`wp\ next\ scheduled() <https://developer.wordpress.org/reference/functions/wp_next_scheduled/>`__
to check if a particular hook is already scheduled.

`wp\ next\ scheduled() <https://developer.wordpress.org/reference/functions/wp_next_scheduled/>`__
takes one parameter, the name of the hook. It will return either a
string containing the timestamp of the next execution or false,
signifying the task is not scheduled. It is used like so:

.. code:: php

   wp_next_scheduled( 'bl_cron_hook' )

Scheduling a recurring task is accomplished with
`wp\ schedule\ event() <https://developer.wordpress.org/reference/functions/wp_schedule_event/>`__.
This function takes three required parameters, and one additional
parameter that is an array that can be passed to the function executing
the wp-cron task. We will focus on the first three parameters. The
parameters are as follows:

1. $timestamp – The UNIX timestamp of the first time this task should
   execute

2. $recurrence – The name of the interval in which the task will recur
   in seconds

3. $hook – The name of our custom hook to call

We will use the 5 second interval and the hook we created earlier like
so:

.. code:: php

   wp_schedule_event( time(), 'five_seconds', 'bl_cron_hook' );

Remember, we need to first ensure the task is not already scheduled, the
full code for that is the following:

.. code:: php

   if ( ! wp_next_scheduled( 'bl_cron_hook' ) ) {
       wp_schedule_event( time(), 'five_seconds', 'bl_cron_hook' );
   }

`Top
↑ <https://developer.wordpress.org/plugins/cron/scheduling-wp-cron-events/#top>`__

.. _header-n24:

Unscheduling tasks
------------------

When you no longer need a task scheduled you can unschedule tasks with
`wp\ unschedule\ event() <https://developer.wordpress.org/reference/functions/wp_unschedule_event/>`__.
This function takes the following two parameters:

1. $timestamp – Timestamp of the next occurrence of the task

2. $hook – Name of the custom hook to be called

This function will not only unschedule the task indicated by the
timestamp, it will also unschedule all future occurrences of the task.
Since you probably will not know the timestamp for the next task there
is function, wp\ *next*\ schedule() that will find it for you.
`wp\ next\ scheduled() <https://developer.wordpress.org/reference/functions/wp_next_scheduled/>`__
takes one parameter (that we care about):

1. $hook – The name of the hook that is called to execute the task

Put it all together and the code looks like:

.. code:: php

   $timestamp = wp_next_scheduled( 'bl_cron_hook' );
   wp_unschedule_event( $timestamp, 'bl_cron_hook' );

It is very important to unschedule tasks when you no longer need them as
WordPress will continue to attempt to execute the tasks, even though
they are no longer in use. An important place to remember to unschedule
your tasks is upon plugin deactivation. Unfortunately there are many
plugins in the WordPress.org Plugin Directory that do not clean up after
themselves. If you find one of these plugins please let the author know
to update their code. WordPress provides a function called
`register\ deactivation\ hook() <https://developer.wordpress.org/reference/functions/register_deactivation_hook/>`__
that allows developers to run a function when their plugin is
deactivated. It is very simple to setup and looks like:

.. code:: php

   register_deactivation_hook( __FILE__, 'bl_deactivate' );
    
   function bl_deactivate() {
      $timestamp = wp_next_scheduled( 'bl_cron_hook' );
      wp_unschedule_event( $timestamp, 'bl_cron_hook' );
   }
