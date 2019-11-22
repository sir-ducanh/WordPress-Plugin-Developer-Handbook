.. _header-n0:

Sub-Menus
=========

.. contents::

.. _header-n4:

Add a Sub-Menu 
---------------

To add a new Sub-menu to WordPress Administration, use the
``add_submenu_page()`` function.

.. code:: php

   add_submenu_page(
       string $parent_slug,
       string $page_title,
       string $menu_title,
       string $capability,
       string $menu_slug,
       callable $function = ''
   );

.. _header-n7:

Example
~~~~~~~

Lets say we want to add a Sub-menu “WPOrg Options” to the “Tools”
Top-level menu.

**The first step** will be creating a function which will output the
HTML. In this function we will perform the necessary security checks and
render the options we’ve registered using the `Settings
API <https://developer.wordpress.org/plugins/settings/>`__.

--------------

   **Note:** We recommend wrapping your HTML using a with a class of
   ``wrap``.

--------------

.. code:: php

   function wporg_options_page_html()
   {
       // check user capabilities
       if (!current_user_can('manage_options')) {
           return;
       }
       ?>
       <div class="wrap">
           <h1><?= esc_html(get_admin_page_title()); ?></h1>
           <form action="options.php" method="post">
               <?php
               // output security fields for the registered setting "wporg_options"
               settings_fields('wporg_options');
               // output setting sections and their fields
               // (sections are registered for "wporg", each field is registered to a specific section)
               do_settings_sections('wporg');
               // output save settings button
               submit_button('Save Settings');
               ?>
           </form>
       </div>
       <?php
   }

**The second step** will be registering our WPOrg Options Sub-menu. The
registration needs to occur during the ``admin_menu`` action hook.

.. code:: php

   function wporg_options_page()
   {
       add_submenu_page(
           'tools.php',
           'WPOrg Options',
           'WPOrg Options',
           'manage_options',
           'wporg',
           'wporg_options_page_html'
       );
   }
   add_action('admin_menu', 'wporg_options_page');

For a list of parameters and what each do please see the
`add\ submenu\ page() <https://developer.wordpress.org/reference/functions/add_submenu_page/>`__
in the reference.

`Top
↑ <https://developer.wordpress.org/plugins/administration-menus/sub-menus/#top>`__

.. _header-n19:

Predefined Sub-Menus 
---------------------

Wouldn’t it be nice if we had helper functions that define the
``$parent_slug`` for WordPress built-in Top-level menus and save us from
manually searching it through the source code?

Below is a list of parent slugs and their helper functions:

-  `add\ dashboard\ page() <https://developer.wordpress.org/reference/functions/add_dashboard_page/>`__
   – ``index.php``

-  `add\ posts\ page() <https://developer.wordpress.org/reference/functions/add_posts_page/>`__
   – ``edit.php``

-  `add\ media\ page() <https://developer.wordpress.org/reference/functions/add_media_page/>`__
   – ``upload.php``

-  `add\ pages\ page() <https://developer.wordpress.org/reference/functions/add_pages_page/>`__
   – ``edit.php?post_type=page``

-  `add\ comments\ page() <https://developer.wordpress.org/reference/functions/add_comments_page/>`__
   – ``edit-comments.php``

-  `add\ theme\ page() <https://developer.wordpress.org/reference/functions/add_theme_page/>`__
   – ``themes.php``

-  `add\ plugins\ page() <https://developer.wordpress.org/reference/functions/add_plugins_page/>`__
   – ``plugins.php``

-  `add\ users\ page() <https://developer.wordpress.org/reference/functions/add_users_page/>`__
   – ``users.php``

-  `add\ management\ page() <https://developer.wordpress.org/reference/functions/add_management_page/>`__
   – ``tools.php``

-  `add\ options\ page() <https://developer.wordpress.org/reference/functions/add_options_page/>`__
   – ``options-general.php``

-  `add\ options\ page() <https://developer.wordpress.org/reference/functions/add_options_page/>`__
   – ``settings.php``

-  `add\ links\ page() <https://developer.wordpress.org/reference/functions/add_links_page/>`__
   – ``link-manager.php`` – requires a plugin since WP 3.5+

-  Custom Post Type – ``edit.php?post_type=wporg_post_type``

-  Network Admin – ``settings.php``

`Top
↑ <https://developer.wordpress.org/plugins/administration-menus/sub-menus/#top>`__

.. _header-n52:

Remove a Sub-Menu 
------------------

The process of removing Sub-menus is exactly the same as `removing
Top-level
menus <https://developer.wordpress.org/plugins/administration-menus/top-level-menus/#remove-a-top-level-menu>`__.

`Top
↑ <https://developer.wordpress.org/plugins/administration-menus/sub-menus/#top>`__

.. _header-n55:

Submitting forms 
-----------------

The process of handling form submissions within Sub-menus is exactly the
same as `Submitting forms within Top-Level
Menus <https://developer.wordpress.org/plugins/administration-menus/top-level-menus/#submitting-forms>`__.

``add_submenu_page()`` along with all functions for pre-defined
sub-menus (``add_dashboard_page``, ``add_posts_page``, etc.) will return
a ``$hookname``, which you can use as the first parameter of
``add_action`` in order to handle the submission of forms within custom
pages:

.. code:: php

   function wporg_options_page() {
       $hookname = add_submenu_page(
           'tools.php',
           'WPOrg Options',
           'WPOrg Options',
           'manage_options',
           'wporg',
           'wporg_options_page_html'
       );
    
       add_action( 'load-' . $hookname, 'wporg_options_page_html_submit' );
   }
    
   add_action('admin_menu', 'wporg_options_page');

As always, do not forget to check whether the form is being submitted,
do CSRF verification,
`validation <https://developer.wordpress.org/plugins/security/data-validation/>`__,
and sanitization.
