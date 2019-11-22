.. _header-n0:

Server Side PHP and Enqueuing
=============================

.. contents::

There are two parts to the server side PHP script that are needed to
implement AJAX communication. First we need to enqueue the jQuery script
on the web page and localize any PHP values that the jQuery script
needs. Second is the actual handling of the AJAX request.

.. _header-n4:

Enqueue Script 
---------------

This section covers the two major quirks of AJAX in WordPress that trip
up experienced coders new to WordPress. One is the need to enqueue
scripts in order to get meta links to appear correctly in the page’s
head section. The other is that **all** AJAX requests need to be sent
through ``wp-admin/admin-ajax.php``. Never send requests directly to
your plugin pages.

.. _header-n6:

Enqueue 
~~~~~~~~

Use the function ``wp_enqueue_script()`` to get WordPress to insert a
meta link to your script in the page’s section. Never hardcode such
links in the header template. As a plugin developer, you do not have
ready access to the header template, but this rule bears mentioning
anyway.

The enqueue function takes three parameters. The first is an arbitrary
tag or handle that is used to refer to your script in other functions.
The second is the complete URL to your script file. For portability, use
``plugins_url()`` to build the proper URL. If you are enqueuing the
script for something besides a plugin, use some related function to
create a proper URL – never hardcode it. The third parameter is an array
of any script tags that your script is dependent on. Since we are using
jQuery to send an AJAX request, you will at least need to list
*‘jquery’* in the array. Always use an array even if it is for a single
dependency. The enqueue call for our example looks like this:

.. code:: php

   wp_enqueue_script( 'ajax-script',
       plugins_url( '/js/myjquery.js', __FILE__ ),
       array('jquery')
   );

You cannot enqueue scripts directly from your plugin code page when it
is loaded. Scripts must be enqueued from one of a few action hooks –
which one depends on what sort of page the script needs to be linked to.
For administration pages, use ``admin_enqueue_scripts``. For front-end
pages use ``wp_enqueue_scripts``, except for the login page, in which
case use ``login_enqueue_scripts``.

The ``admin_enqueue_scripts`` hook passes the current page filename to
your callback. Use this information to only enqueue your script on pages
where it is needed. The front-end version does not pass anything. In
that case, use template tags such as ``is_home()``, ``is_single()``,
etc. to ensure that you only enqueue your script where it is needed.
This is the complete enqueue code for our example:

.. code:: php

   add_action( 'admin_enqueue_scripts', 'my_enqueue' );
   function my_enqueue( $hook ) {
       if( 'myplugin_settings.php' != $hook ) return;
       wp_enqueue_script( 'ajax-script',
           plugins_url( '/js/myjquery.js', __FILE__ ),
           array( 'jquery' )
       );
   }

Why do we use a named function here but use anonymous functions with
jQuery? Because closures are only recently supported by PHP. jQuery has
supported them for quite some time. Since some people may still be
running older versions of PHP, we always use named functions for maximum
compatibility. If you have a recent PHP version and are developing only
for your own installation, go ahead and use closures if you like.

.. _header-n14:

Register vs. Enqueue 
^^^^^^^^^^^^^^^^^^^^^

You will see examples in other tutorials that religiously use
``wp_register_script()``. This is fine, but its use is optional. What is
not optional is ``wp_enqueue_script()``. This function must be called in
order for your script file to be properly linked on the web page. So why
register scripts? It creates a useful tag or handle with which you can
easily reference the script in various parts of your code as needed. If
you just need your script loaded and are not referencing it elsewhere in
your code, there is no need to register it.

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n17:

Nonce 
~~~~~~

You need to create a nonce so that the jQuery AJAX request can be
validated as a legitimate request instead of a potentially nefarious
request from some unknown bad actor. Only your PHP script and your
jQuery script will know this value. When the request is received, you
can verify it is the same value created here. This is how to create a
nonce for our example:

.. code:: php

   $title_nonce = wp_create_nonce( 'title_example' );

The parameter ``title_example`` can be any arbitrary string. It’s
suggested the string be related to what the nonce is used for, but it
can really be anything that suits you.

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n22:

Localize 
~~~~~~~~~

If you recall from the `jQuery
Section <https://developer.wordpress.org/plugins/javascript/jquery/>`__,
data created by PHP for use by jQuery was passed in a global object
named ``my_ajax_obj``. In our example, this data was a nonce and the
complete URL to ``admin-ajax.php``. The process of assigning object
properties and creating the global jQuery object is called
**localizing**. This is the localizing code used in our example which
uses ``wp_localize_script()``.

.. code:: php

   wp_localize_script( 'ajax-script', 'my_ajax_obj', array(
       'ajax_url' => admin_url( 'admin-ajax.php' ),
       'nonce'    => $title_nonce, // It is common practice to comma after
   ) );                // the last array item for easier maintenance

Note how our script handle ``ajax-script`` is used so that the global
object is assigned to the right script. The object is global to our
script, not to all scripts. Localization can also be called from the
same hook that is used to enqueue scripts. The same goes for creating a
nonce, though that particular function can be called virtually anywhere.
All of that combined together in a single hook callback looks like this:

.. code:: php

   add_action( 'admin_enqueue_scripts', 'my_enqueue' );
   function my_enqueue( $hook ) {
       if( 'myplugin_settings.php' != $hook ) return;
       wp_enqueue_script( 'ajax-script',
           plugins_url( '/js/myjquery.js', __FILE__ ),
           array( 'jquery' )
       );
       $title_nonce = wp_create_nonce( 'title_example' );
       wp_localize_script( 'ajax-script', 'my_ajax_obj', array(
          'ajax_url' => admin_url( 'admin-ajax.php' ),
          'nonce'    => $title_nonce,
       ) );
   }

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n28:

AJAX Action 
------------

The other major part of the server side PHP code is the actual AJAX
handler that receives the POSTed data, does something with it, then
sends an appropriate response back to the browser. This takes on the
form of a WordPress `action
hook <https://developer.wordpress.org/plugins/hooks/actions/>`__. Which
hook tag you use depends on whether the user is logged in or not and
what value your jQuery script passed as the *action:* value.

--------------

   **Note:\ ``$_GET`` , ``$_POST`` and ``$_COOKIE`` vs ``$_REQUEST``**

   You’ve probably used one or more of the PHP super globals such as
   ``$_GET`` or ``$_POST`` to retrieve values from forms or cookies
   (using ``$_COOKIE``). Maybe you prefer ``$_REQUEST`` instead, or at
   least have seen it used. It’s kind of cool – regardless of the
   request method, ``POST`` or ``GET``, it will have the form values.
   Works great for pages that use both methods. On top of that, it has
   cookie values as well. One stop shopping! Therein lies its tragic
   flaw. In the case of a name conflict, the cookie value will override
   any form values. Thus it is ridiculously easy for a bad actor to
   craft a counterfeit cookie on their browser, which will overwrite any
   form value you might be expecting from the request. ``$_REQUEST`` is
   an easy route for hackers to inject arbitrary data into your form
   values. To be extra safe, stick to the specific variables and avoid
   the one size fits all.

--------------

Since our AJAX exchange is for the plugin’s settings page, the user must
be logged in. If you recall from the `jQuery
section <https://developer.wordpress.org/plugins/javascript/jquery/>`__,
the ``action:`` value is ``"my_tag_count"``. This means our action hook
tag will be ``wp_ajax_my_tag_count``. If our AJAX exchange were to be
utilized by users who were not currently logged in, the action hook tag
would be ``wp_ajax_nopriv_my_tag_count`` The basic code used to hook the
action looks like this:

.. code:: php

   add_action( 'wp_ajax_my_tag_count', 'my_ajax_handler' );
   function my_ajax_handler() {
       // Handle the ajax request
       wp_die(); // All ajax handlers die when finished
   }

The first thing your AJAX handler should do is verify the nonce sent by
jQuery with ``check_ajax_referer()``, which should be the same value
that was localized when the script was enqueued.

.. code:: php

   check_ajax_referer( 'title_example' );

The provided parameter must be identical to the parameter provided
`earlier <https://developer.wordpress.org/plugins/javascript/enqueuing/#php-nonce>`__
to ``wp_create_nonce()``. The function simply dies if the nonce does not
check out. If this were a true nonce, now that it was used, the value is
no longer any good. You would then generate a new one and send it to the
callback script so that it can be used for the next request. But since
WordPress nonces are good for twenty-four hours, you needn’t do anything
but check it.

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n41:

Data 
~~~~~

With the nonce out of the way, our handler can deal with the data sent
by the jQuery script contained in ``$_POST['title']``. We can save the
user’s selection in user meta by using
`update\ user\ meta() <https://developer.wordpress.org/reference/functions/update_user_meta/>`__.

.. code:: php

   update_user_meta( get_current_user_id(), 'title_preference', $_POST['title']);

Then we build a query in order to get the post count for the selected
title tag.

.. code:: php

   $args = array(
       'tag' => $_POST['title'],
   );
   $the_query = new WP_Query( $args );

Finally we can send the response back to the jQuery script. There’s
several ways to transmit data. Let’s look at some of the options before
we deal with the specifics of our example.

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n48:

XML 
^^^^

PHP support for XML leaves something to be desired. Fortunately,
WordPress provides the ``WP_Ajax_Response`` class to make the task
easier. The
`WP\ Ajax\ Response <https://developer.wordpress.org/reference/classes/wp_ajax_response/>`__
class will generate an XML-formatted response, set the correct content
type for the header, output the response xml, then die — ensuring a
proper XML response.

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n51:

JSON 
^^^^^

This format is lightweight and easy to use, and WordPress provides the
``wp_send_json`` function to json-encode your response, print it, and
die — effectively replacing
`WP\ Ajax\ Response <https://developer.wordpress.org/reference/classes/wp_ajax_response/>`__.
WordPress also provides the ``wp_send_json_success`` and
``wp_send_json_error`` functions, which allow the appropriate done() or
fail() callbacks to fire in JS.

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n54:

Other 
^^^^^^

You can transfer data any way you like, as long as the sender and
receiver are coordinated. Text formats like comma delimited or tab
delimited are one of many possibilities. For small amounts of data,
sending the raw stream may be adequate. That is what we will do with our
example – we will send the actual replacement HTML, nothing else.

.. code:: php

   echo $_POST['title'].' ('.$the_query->post_count.') ';

In a real world application, you must account for the possibility that
the action could fail for some reason–for instance, maybe the database
server is down. The response should allow for this contingency, and the
jQuery script receiving the response should act accordingly, perhaps
telling the user to try again later.

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n59:

Die 
~~~~

When the handler has finished all of its tasks, it needs to die. If you
are using the
`WP\ Ajax\ Response <https://developer.wordpress.org/reference/classes/wp_ajax_response/>`__
or wp\ *send*\ json\* functions, this is automatically handled for you.
If not, simply use the WordPress ``wp_die()``\ function.

.. code:: php

   wp_die();
   // That's all folks!

`Top
↑ <https://developer.wordpress.org/plugins/javascript/enqueuing/#top>`__

.. _header-n63:

AJAX Handler Summary 
~~~~~~~~~~~~~~~~~~~~~

The complete AJAX handler for our example looks like this:

.. code:: php

   //JSON
   function my_ajax_handler() {
       check_ajax_referer( 'title_example' );
       update_user_meta( get_current_user_id(), 'title_preference', $_POST['title'] );
       $args = array(
           'tag' => $_POST['title'],
       );
       $the_query = new WP_Query( $args );
           wp_send_json( $_POST['title'] . ' (' . $the_query->post_count . ') ' );
   }

.. code:: php

   //Other
   function my_ajax_handler() {
       check_ajax_referer( 'title_example' );
       update_user_meta( get_current_user_id(), 'title_preference', $_POST['title'] );
       $args = array(
           'tag' => $_POST['title'],
       );
       $the_query = new WP_Query( $args );
       echo $_POST['title'].' ('.$the_query->post_count.') ';
       wp_die(); // All ajax handlers should die when finished
   }
