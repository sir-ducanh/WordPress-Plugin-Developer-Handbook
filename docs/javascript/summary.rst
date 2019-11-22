.. _header-n0:

Summary
=======

.. contents::

Here are all the example code snippets from the preceding discussion,
assembled into two complete code pages: one for jQuery and the other for
PHP.

.. _header-n4:

PHP 
----

This code resides on one of your plugin pages.

.. code:: php

   <?php add_action('admin_enqueue_scripts', 'my_enqueue');
   function my_enqueue($hook) {
       if( 'myplugin_settings.php' != $hook) return;
       wp_enqueue_script( 'ajax-script',
           plugins_url( '/js/myjquery.js', __FILE__ ),
           array('jquery')
       );
       $title_nonce = wp_create_nonce('title_example');
       wp_localize_script('ajax-script', 'my_ajax_obj', array(
           'ajax_url' => admin_url( 'admin-ajax.php' ),
           'nonce'    => $title_nonce,
       ));
   }
    
   add_action('wp_ajax_my_tag_count', 'my_ajax_handler');
   function my_ajax_handler() {
       check_ajax_referer('title_example');
       update_user_meta( get_current_user_id(), 'title_preference', $_POST['title']);
       $args = array(
          'tag' => $_POST['title'],
       );
       $the_query = new WP_Query( $args );
       echo $_POST['title'].' ('.$the_query->post_count.') ';
       wp_die(); // all ajax handlers should die when finished
   }

`Top
↑ <https://developer.wordpress.org/plugins/javascript/summary/#top>`__

.. _header-n8:

jQuery 
-------

This code is in the file ``js/myjquery.js`` below your plugin folder.

.. code:: javascript

   jQuery(document).ready(function($) {       //wrapper
       $(".pref").change(function() {         //event
           var this2 = this;                  //use in callback
           $.post(my_ajax_obj.ajax_url, {     //POST request
              _ajax_nonce: my_ajax_obj.nonce, //nonce
               action: "my_tag_count",        //action
               title: this.value              //data
           }, function(data) {                //callback
               this2.nextSibling.remove();    //remove the current title
               $(this2).after(data);          //insert server response
           });
       });
   });

And after storing the preference, the resulting post count is added to
the selected title.

.. _header-n12:

More Information
----------------

-  `How To Use AJAX In
   WordPress <http://wp.smashingmagazine.com/2011/10/18/how-to-use-ajax-in-wordpress/>`__

-  `AJAX for
   WordPress <http://www.glennmessersmith.com/pages/wpajax.html>`__
