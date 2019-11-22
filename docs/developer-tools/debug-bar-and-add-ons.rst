.. _header-n0:

Debug Bar and Add-Ons
=====================

.. contents::

.. _header-n4:

Debug Bar 
----------

The debug bar, when active, adds a debug menu to the admin bar that
shows query, cache, and other helpful debugging information.

When WP_DEBUG is enabled it also tracks PHP Warnings and Notices to make
them easier to find.

When SAVEQUERIES is enabled the mysql queries are tracked and displayed.

`Visit Debug Bar <https://wordpress.org/plugins/debug-bar/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n10:

Debug Bar Console 
------------------

This plugin provides a large textarea in which you can run arbitrary
PHP. This is excellent for testing the contents of variables etc.

`Visit Debug Bar
Console <https://wordpress.org/plugins/debug-bar-console/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n14:

Debug Bar Shortcodes 
---------------------

Debug Bar Shortcodes adds a new panel to the Debug Bar that displays the
registered shortcodes for the current request.

Additionally it will show you:

-  Which function/method is called by the shortcode.

-  Whether the shortcode is used on the current post/page/post type and
   how (only when on singular).

-  Any additional information available about the shortcode, such as a
   description, which parameters it takes, whether or not it is
   self-closing.

-  Find out all pages/posts/etc on which a shortcode is used.

`Visit Debug Bar
Shortcodes <https://wordpress.org/plugins/debug-bar-shortcodes/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n28:

Debug Bar Constants 
--------------------

Debug Bar Constants adds three new panels to the Debug Bar that display
the defined constants available to you as a developer for the current
request:

-  WP Constants

-  WP Class Constants

-  PHP Constants

`Visit Debug Bar
Constants <https://wordpress.org/plugins/debug-bar-constants/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n39:

Debug Bar Post Types 
---------------------

Debug Bar Post Types adds a new panel to the Debug Bar that displays
detailed information about the registered post types for your site.

`Visit Debug Bar Post
Types <https://wordpress.org/plugins/debug-bar-post-types/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n43:

Debug Bar Cron 
---------------

Debug Bar Cron adds information about WP scheduled events to a new panel
in the Debug Bar. This plugin is an extension for Debug Bar and thus is
dependent upon Debug Bar being installed for it to work properly.

Once installed, you will have access to the following information:

-  Number of scheduled events

-  If cron is currently running

-  Time of next event

-  Current time

-  List of custom scheduled events

-  List of core scheduled events

-  List of schedules

`Visit Debug Bar Cron <https://wordpress.org/plugins/debug-bar-cron/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n63:

Debug Bar Actions and Filters Addon
-----------------------------------

This plugin adds two more tabs in the Debug Bar to display hooks(Actions
and Filters) attached to the current request. Actions tab displays the
actions hooked to current request. Filters tab displays the filter tags
along with the functions attached to it with respective priority.

`Visit Debug Bar Actions and Filters
Addon <https://wordpress.org/plugins/debug-bar-actions-and-filters-addon/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n67:

Debug Bar Transients 
---------------------

Debug Bar Transients adds information about WordPress Transients to a
new panel in the Debug Bar. This plugin is an extension for Debug Bar
and thus is dependent upon Debug Bar being installed for it to work
properly.

Once installed, you will have access to the following information:

-  Number of existing transients

-  List of custom transients

-  List of core transients

-  List of custom site transients

-  List of core site transients

-  An option to delete a transient

`Visit Debug Bar
Transients <https://wordpress.org/plugins/debug-bar-transients/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n85:

Debug Bar List Script & Style Dependencies 
-------------------------------------------

Lists scripts and styles that are loaded, in which order they’re loaded,
and what dependencies exist.

`Visit Debug Bar List Script & Style
Dependencies <https://wordpress.org/plugins/debug-bar-list-dependencies/>`__

`Top
↑ <https://developer.wordpress.org/plugins/developer-tools/debug-bar-and-add-ons/#top>`__

.. _header-n89:

Debug Bar Remote Requests 
--------------------------

This will log and profile remote requests made through the HTTP API.

This plugin will add a “Remote Requests” panel to Debug Bar that will
display the:

-  Request method (GET, POST, etc)

-  URL

-  Time per request

-  Total time for all requests

-  Total number of requests

Optionally, you can add ?dbrr_full=1 to your URL to get additional
information, including all request parameters and a full dump of the
response with headers.

`Visit Debug Bar Remote
Requests <https://wordpress.org/plugins/debug-bar-remote-requests/>`__
