.. _header-n0:

Shortcodes with Parameters
==========================

.. contents::

Now that we know how to create a `basic
shortcode <https://developer.wordpress.org/plugins/shortcodes/basic-shortcodes/>`__
and how to use it as `self-closing and
enclosing <https://developer.wordpress.org/plugins/shortcodes/enclosing-shortcodes/>`__,
we will look at using parameters in shortcode ``[$tag]`` and handler
function.

Shortcode ``[$tag]`` can accept parameters, known as attributes:

.. code:: php

   [wporg title="WordPress.org"]
   Having fun with WordPress.org shortcodes.
   [/wporg]

Shortcode handler function can accept 3 parameters:

-  ``$atts`` – array – [$tag] attributes

-  ``$content`` – string – post content

-  ``$tag`` – string – the name of the [$tag] (i.e. the name of the
   shortcode)

.. code:: php

   function wporg_shortcode($atts = [], $content = null, $tag = '') {}

.. _header-n15:

Parsing Attributes 
-------------------

For the user, shortcodes are just strings with square brackets inside
the post content. The user have no idea which attributes are available
and what happens behind the scenes.

For plugin developers, there is no way to enforce a policy on the use of
attributes. The user may include one attribute, two or none at all.

To gain control of how the shortcodes are used:

-  Declare default parameters for the handler function

-  Performing normalization of the key case for the attributes array
   with
   `array\ change\ key_case() <http://php.net/manual/en/function.array-change-key-case.php>`__

-  Parse attributes using
   `shortcode_atts() <https://developer.wordpress.org/reference/functions/shortcode_atts/>`__
   providing default values array and user ``$atts``

-  `Secure the
   output <https://developer.wordpress.org/plugins/security/securing-output/>`__
   before returning it

`Top
↑ <https://developer.wordpress.org/plugins/shortcodes/shortcodes-with-parameters/#top>`__

.. _header-n29:

Complete Example 
-----------------

Complete example using a basic shortcode structure, taking care of
self-closing and enclosing scenarios, shortcodes within shortcodes and
securing output.

A [wporg] shortcode that will accept a title and will display a box that
we can style with CSS.

.. code:: php

   <?php
   function wporg_shortcode($atts = [], $content = null, $tag = '')
   {
       // normalize attribute keys, lowercase
       $atts = array_change_key_case((array)$atts, CASE_LOWER);
    
       // override default attributes with user attributes
       $wporg_atts = shortcode_atts([
                                        'title' => 'WordPress.org',
                                    ], $atts, $tag);
    
       // start output
       $o = '';
    
       // start box
       $o .= '<div class="wporg-box">';
    
       // title
       $o .= '<h2>' . esc_html__($wporg_atts['title'], 'wporg') . '</h2>';
    
       // enclosing tags
       if (!is_null($content)) {
           // secure output by executing the_content filter hook on $content
           $o .= apply_filters('the_content', $content);
    
           // run shortcode parser recursively
           $o .= do_shortcode($content);
       }
    
       // end box
       $o .= '</div>';
    
       // return output
       return $o;
   }
    
   function wporg_shortcodes_init()
   {
       add_shortcode('wporg', 'wporg_shortcode');
   }
    
   add_action('init', 'wporg_shortcodes_init');
