.. _header-n0:

Securing Input
==============

.. contents::

Securing input is the process of sanitizing (cleaning, filtering) input
data.

You use sanitizing when you don’t know what to expect or you don’t want
to be strict with `data validation <data-validation.md>`__.

**Any time you’re accepting potentially unsafe data, it is important to
validate or sanitize it.**

.. _header-n6:

Sanitizing the Data 
--------------------

The easiest way to sanitize data is with built-in WordPress functions.

The ``sanitize_*()`` series of helper functions are super nice, as they
ensure you’re ending up with safe data, and they require minimal effort
on your part:

-  `sanitize_email() <https://developer.wordpress.org/reference/functions/sanitize_email/>`__

-  `sanitize\ file\ name() <https://developer.wordpress.org/reference/functions/sanitize_file_name/>`__

-  `sanitize\ hex\ color() <https://developer.wordpress.org/reference/functions/sanitize_hex_color/>`__

-  `sanitize\ hex\ color\ no\ hash() <https://developer.wordpress.org/reference/functions/sanitize_hex_color_no_hash/>`__

-  `sanitize\ html\ class() <https://developer.wordpress.org/reference/functions/sanitize_html_class/>`__

-  `sanitize_key() <https://developer.wordpress.org/reference/functions/sanitize_key/>`__

-  `sanitize_meta() <https://developer.wordpress.org/reference/functions/sanitize_meta/>`__

-  `sanitize\ mime\ type() <https://developer.wordpress.org/reference/functions/sanitize_mime_type/>`__

-  `sanitize_option() <https://developer.wordpress.org/reference/functions/sanitize_option/>`__

-  `sanitize\ sql\ orderby() <https://developer.wordpress.org/reference/functions/sanitize_sql_orderby/>`__

-  `sanitize\ text\ field() <https://developer.wordpress.org/reference/functions/sanitize_text_field/>`__

-  `sanitize_title() <https://developer.wordpress.org/reference/functions/sanitize_title/>`__

-  `sanitize\ title\ for_query() <https://developer.wordpress.org/reference/functions/sanitize_title_for_query/>`__

-  `sanitize\ title\ with_dashes() <https://developer.wordpress.org/reference/functions/sanitize_title_with_dashes/>`__

-  `sanitize_user() <https://developer.wordpress.org/reference/functions/sanitize_user/>`__

-  `esc\ url\ raw() <https://developer.wordpress.org/reference/functions/esc_url_raw/>`__

-  `wp\ filter\ post_kses() <https://developer.wordpress.org/reference/functions/wp_filter_post_kses/>`__

-  `wp\ filter\ nohtml_kses() <https://developer.wordpress.org/reference/functions/wp_filter_nohtml_kses/>`__

`Top
↑ <https://developer.wordpress.org/plugins/security/securing-input/#top>`__

.. _header-n47:

Example 
--------

Let’s say we have an input field named title.

.. code:: php

   <input id="title" type="text" name="title">

You can sanitize the input data with the
`sanitize\ text\ field() <https://developer.wordpress.org/reference/functions/sanitize_text_field/>`__
function:

.. code:: php

   $title = sanitize_text_field($_POST['title']);
   update_post_meta($post->ID, 'title', $title);

Behind the scenes,
`sanitize\ text\ field() <https://developer.wordpress.org/reference/functions/sanitize_text_field/>`__
does the following:

-  Checks for invalid UTF-8

-  Converts single less-than characters (<) to entity

-  Strips all tags

-  Removes line breaks, tabs and extra white space

-  Strips octets
