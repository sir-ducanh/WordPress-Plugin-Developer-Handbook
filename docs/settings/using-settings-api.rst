.. _header-n0:

Using Settings API
==================

.. contents::

.. _header-n4:

Adding Settings
---------------

You must define a new setting using
`register_setting() <https://developer.wordpress.org/reference/functions/register_setting/>`__,
it will create an entry in the ``{$wpdb->prefix}_options`` table.

You can add new sections on existing pages using
`add\ settings\ section() <https://developer.wordpress.org/reference/functions/add_settings_section/>`__.

You can add new fields to existing sections using
`add\ settings\ field() <https://developer.wordpress.org/reference/functions/add_settings_field/>`__.

--------------

   **Alert:**
   `register_setting() <https://developer.wordpress.org/reference/functions/register_setting/>`__
   as well as the mentioned ``add_settings_*()`` functions should all be
   added to the ``admin_init`` action hook.

--------------

.. _header-n12:

Add a Setting 
~~~~~~~~~~~~~~

.. code:: php

   register_setting( 
       string $option_group, 
       string $option_name, 
       callable $sanitize_callback = ''
   );

Please refer to the Function Reference about
`register_setting() <https://developer.wordpress.org/reference/functions/register_setting/>`__
for full explanation about the used parameters.

`Top
↑ <https://developer.wordpress.org/plugins/settings/using-settings-api/#top>`__

.. _header-n16:

Add a Section 
~~~~~~~~~~~~~~

.. code:: php

   add_settings_section( 
       string $id, 
       string $title, 
       callable $callback, 
       string $page
   );

Sections are the groups of settings you see on WordPress settings pages
with a shared heading. In your plugin you can add new sections to
existing settings pages rather than creating a whole new page. This
makes your plugin simpler to maintain and creates fewer new pages for
users to learn.

Please refer to the Function Reference about
`add\ settings\ section() <https://developer.wordpress.org/reference/functions/add_settings_section/>`__
for full explanation about the used parameters.

`Top
↑ <https://developer.wordpress.org/plugins/settings/using-settings-api/#top>`__

.. _header-n21:

Add a Field
~~~~~~~~~~~

.. code:: php

   add_settings_field(
       string $id, 
       string $title, 
       callable $callback, 
       string $page, 
       string $section = 'default', 
       array $args = []
   );

Please refer to the Function Reference about
`add\ settings\ field() <https://developer.wordpress.org/reference/functions/add_settings_field/>`__
for full explanation about the used parameters.

`Top
↑ <https://developer.wordpress.org/plugins/settings/using-settings-api/#top>`__

.. _header-n25:

Example 
~~~~~~~~

.. code:: php

   <?php
   function wporg_settings_init()
   {
       // register a new setting for "reading" page
       register_setting('reading', 'wporg_setting_name');
    
       // register a new section in the "reading" page
       add_settings_section(
           'wporg_settings_section',
           'WPOrg Settings Section',
           'wporg_settings_section_cb',
           'reading'
       );
    
       // register a new field in the "wporg_settings_section" section, inside the "reading" page
       add_settings_field(
           'wporg_settings_field',
           'WPOrg Setting',
           'wporg_settings_field_cb',
           'reading',
           'wporg_settings_section'
       );
   }
    
   /**
    * register wporg_settings_init to the admin_init action hook
    */
   add_action('admin_init', 'wporg_settings_init');
    
   /**
    * callback functions
    */
    
   // section content cb
   function wporg_settings_section_cb()
   {
       echo '<p>WPOrg Section Introduction.</p>';
   }
    
   // field content cb
   function wporg_settings_field_cb()
   {
       // get the value of the setting we've registered with register_setting()
       $setting = get_option('wporg_setting_name');
       // output the field
       ?>
       <input type="text" name="wporg_setting_name" value="<?php echo isset( $setting ) ? esc_attr( $setting ) : ''; ?>">
       <?php
   }

`Top
↑ <https://developer.wordpress.org/plugins/settings/using-settings-api/#top>`__

.. _header-n28:

Getting Settings 
-----------------

.. code:: php

   get_option(
       string $option,
       mixed $default = false
   );

| Getting settings is accomplished with the
  `get_option() <https://developer.wordpress.org/reference/functions/get_option/>`__
  function.
| The function accepts two parameters: the name of the option and an
  optional default value for that option.

`Top
↑ <https://developer.wordpress.org/plugins/settings/using-settings-api/#top>`__

.. _header-n32:

Example 
~~~~~~~~

.. code:: php

   // get the value of the setting we've registered with register_setting()
   $setting = get_option('wporg_setting_name');
