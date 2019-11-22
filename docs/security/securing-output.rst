.. _header-n0:

Securing Output
===============

.. contents::

Securing output is the process of escaping output data.

Escaping means stripping out unwanted data, like malformed HTML or
script tags.

**Whenever you’re rendering data, make sure to properly escape it.
Escaping output prevents XSS (Cross-site scripting) attacks.**

--------------

**Note:**

      `Cross-site scripting
      (XSS) <https://en.wikipedia.org/wiki/Cross-site_scripting>`__ is a
      type of computer security vulnerability typically found in web
      applications. XSS enables attackers to inject client-side scripts
      into web pages viewed by other users. A cross-site scripting
      vulnerability may be used by attackers to bypass access controls
      such as the same-origin policy.

--------------

.. _header-n12:

Escaping 
---------

Escaping helps securing your data prior to rendering it for the end
user. WordPress has a few helper functions you can use for most common
scenarios.

-  `esc_html() <https://developer.wordpress.org/reference/functions/esc_html/>`__
   – Use this function anytime an HTML element encloses a section of
   data being displayed.

-  `esc_url() <https://developer.wordpress.org/reference/functions/esc_url/>`__
   – Use this function on all URLs, including those in the ``src`` and
   ``href`` attributes of an HTML element.

-  ``esc_js()``– Use this function for inline Javascript.

-  `esc_attr() <https://developer.wordpress.org/reference/functions/esc_attr/>`__
   – Use this function on everything else that’s printed into an HTML
   element’s attribute.

--------------

   **Alert:** Most WordPress functions properly prepare data for output,
   so you don’t need to escape the data again. For example, you can
   safely call
   `the_title() <https://developer.wordpress.org/reference/functions/the_title/>`__
   without escaping.

--------------

`Top
↑ <https://developer.wordpress.org/plugins/security/securing-output/#top>`__

.. _header-n28:

Escaping with Localization 
---------------------------

Rather than using ``echo`` to output data, it’s common to use the
WordPress localization functions, such as
`\_e() <https://developer.wordpress.org/reference/functions/_e/>`__ or
`\__() <https://developer.wordpress.org/reference/functions/__/>`__.

These functions simply wrap a localization function inside an escaping
function:

.. code:: php

   esc_html_e( 'Hello World', 'text_domain' );
   // same as
   echo esc_html( __( 'Hello World', 'text_domain' ) );

These helper functions combine localization and escaping:

-  `esc_html__() <https://developer.wordpress.org/reference/functions/esc_html__/>`__

-  `esc\ html\ e() <https://developer.wordpress.org/reference/functions/esc_html_e/>`__

-  `esc\ html\ x() <https://developer.wordpress.org/reference/functions/esc_html_x/>`__

-  `esc_attr__() <https://developer.wordpress.org/reference/functions/esc_attr__/>`__

-  `esc\ attr\ e() <https://developer.wordpress.org/reference/functions/esc_attr_e/>`__

-  `esc\ attr\ x() <https://developer.wordpress.org/reference/functions/esc_attr_x/>`__

`Top
↑ <https://developer.wordpress.org/plugins/security/securing-output/#top>`__

.. _header-n47:

Custom Escaping 
----------------

In the case that you need to escape your output in a specific way, the
function
`wp_kses() <https://developer.wordpress.org/reference/functions/wp_kses/>`__
(pronounced “kisses”) will come in handy.

This function makes sure that only the specified HTML elements,
attributes, and attribute values will occur in your output, and
normalizes HTML entities.

.. code:: php

   $allowed_html = [
   'a'      => [
   'href'  => [],
   'title' => [],
   ],
   'br'     => [],
   'em'     => [],
   'strong' => [],
   ];
   echo wp_kses( $custom_content, $allowed_html );

wp\ *kses*\ post() is a wrapper function for wp\ *kses where
$allowed*\ html is a set of rules used by post content.

.. code:: php

   echo wp_kses_post( $post_content );
