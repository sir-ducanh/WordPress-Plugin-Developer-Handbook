.. _header-n0:

How to Internationalize Your Plugin
===================================

.. contents::

In order to make a string translatable in your application you have to
wrap the original strings in a call to one of a set of special
functions.

.. _header-n4:

Introduction to Gettext 
------------------------

WordPress uses the `gettext <http://www.gnu.org/software/gettext/>`__
libraries and tools for i18n. If you look online, you’ll see the ``_()``
function which refers to the native PHP gettext-compliant translation
function. With WordPress you should use the ``__()`` WordPress defined
PHP function. If you want to get a broader and deeper view of gettext,
we recommend you read the `gettext online
manual <http://www.gnu.org/software/gettext/manual/html_node/>`__.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n7:

Text Domains 
-------------

--------------

   **Note:** After WordPress
   `4.6 <https://codex.wordpress.org/Version_4.6>`__ came out, the
   ``Text Domain`` header is no longer required if it’s the same as the
   plugin slug. It’s now the default value.

--------------

| It’s important to use a text domain to denote all text belonging to
  that plugin. The text domain is a unique identifier, which makes sure
  WordPress can distinguish between all loaded translations. This
  increases portability and plays better with already existing WordPress
  tools. The text domain must match the ``slug`` of the plugin. If your
  plugin is a single file called ``my-plugin.php`` or it is contained in
  a folder called ``my-plugin`` the domain name should be ``my-plugin``.
  If your plugin is hosted on wordpress.org it must be the slug of your
  plugin URL (``wordpress.org/plugins/``).
| The text domain name must use dashes and not underscores.

**String example:**

.. code:: php

   __( 'String (text to be internationalized)', 'text-domain' );

Change “text-domain” to the slug of your plugin.

--------------

         **Warning:** Do not use variable names or constants for the
         text domain portion of a gettext function. Do not do this as a
         shortcut: *\_( ‘Translate me.’ , $text*\ domain );

--------------

The text domain also needs to be added to the plugin header. WordPress
uses it to internationalize your plugin meta-data even when the plugin
is disabled. The text domain should be same as the one used when
`loading the text
domain <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#loading-text-domain>`__.

**Header example:**

.. code:: php

   /*
    * Plugin Name: My Plugin
    * Author: Plugin Author
    * Text Domain: my-plugin
    */

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n26:

Domain Path 
------------

--------------

   Note: The ``Domain Path`` header can be omitted if the plugin is in
   the official WordPress Plugin Directory.

--------------

The domain path is used so that WordPress knows where to find the
translation when the plugin is disabled. Only useful if the translations
are located in a separate language folder because it defaults to the
base folder the plugin is located in.

For example, if .mo files are located in the languages folder within
your plugin then Domain Path will be “/languages” and must be written
with the first slash:

**Header example:**

.. code:: php

   /*
    * Plugin Name: My Plugin
    * Author: Plugin Author
    * Text Domain: my-plugin
    * Domain Path: /languages
    */

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n36:

Basic strings 
--------------

The most commonly used one is ``__()``. It just returns the translation
of its argument:

.. code:: php

   __( 'Blog Options', 'my-plugin' );

Another simple one is ``_e()``, which outputs the translation of its
argument. Instead of writing:

.. code:: php

   echo __( 'WordPress is the best!', 'my-plugin' );

you can use the shorter:

.. code:: php

   _e( 'WordPress is the best!', 'my-plugin' );

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n44:

Variables 
----------

If you are using variables in strings like in the example below you
would use placeholders.

.. code:: php

   echo 'Your city is $city.'

The solution is to use the ``printf`` family of functions. Especially
helpful are ``printf`` and ``sprintf``. Here is what the right solution
looks like:

.. code:: php

   printf(
       /* translators: %s: Name of a city */
       __( 'Your city is %s.', 'my-plugin' ),
       $city
   );

Notice that here the string for translation is just the template
``"Your city is %s."``, which is the same both in the source and at
run-time.

If you have more than one placeholder in a string, it is recommended
that you use `argument
swapping <http://www.php.net/manual/en/function.sprintf.php#example-4829>`__.
In this case, single quotes ``(')`` are mandatory : double quotes
``(")`` will tell php to interpret the ``$s`` as the ``s`` variable,
which is not what we want.

.. code:: php

   printf(
       /* translators: 1: Name of a city 2: ZIP code */
       __( 'Your city is %1$s, and your zip code is %2$s.', 'my-plugin' ),
       $city,
       $zipcode
   );

Here the zip code is being displayed after the city name. In some
languages displaying the zip code and city in opposite order would be
more appropriate. Using %s prefix in the above example, allows for such
a case. A translation can thereby be written:

.. code:: php

   printf(
       /* translators: 1: Name of a city 2: ZIP code */
       __( 'Your zip code is %2$s, and your city is %1$s.', 'my-plugin' ),
       $city,
       $zipcode
   );

**Important!** This code is incorrect.

.. code:: php

   // This is incorrect do not use.
   _e( "Your city is $city.", 'my-plugin' );

The strings for translation are extracted from the sources, so the
translators will get this phrase to translate:
``"Your city is $city."``.

However in the application ``_e`` will be called with an argument like
``"Your city is London."`` and ``gettext`` won’t find a suitable
translation of this one and will return its argument:
``"Your city is London."``. Unfortunately, it isn’t translated
correctly.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n59:

Plurals 
--------

.. _header-n60:

Basic Pluralization 
~~~~~~~~~~~~~~~~~~~~

If you have string that changes when the number of items changes. In
English you have ``"One comment"`` and ``"Two comments"``. In other
languages you can have multiple plural forms. To handle this in
WordPress you can use the ``_n()`` function.

.. code:: php

   printf(
       _n(
           '%s comment',
           '%s comments',
           get_comments_number(),
           'my-plugin'
       ),
       number_format_i18n( get_comments_number() )
   );

``_n()`` accepts 4 arguments:

-  singular – the singular form of the string (note that it can be used
   for numbers other than one in some languages, so ``'%s item'`` should
   be used instead of ``'One item'``)

-  plural – the plural form of the string

-  count – the number of objects, which will determine whether the
   singular or the plural form should be returned (there are languages,
   which have far more than 2 forms)

-  text domain – the plugins text domain

The return value of the functions is the correct translated form,
corresponding to the given count.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n75:

Pluralization done later 
~~~~~~~~~~~~~~~~~~~~~~~~~

You first set the plural strings with ``_n_noop()`` or ``_nx_noop()``.

.. code:: php

   $comments_plural = _n_noop(
       '%s comment.',
       '%s comments.'
   );

Then at a later point in the code you can use
``translate_nooped_plural()`` to load the strings.

.. code:: php

   printf(
       translate_nooped_plural(
           $comments_plural,
           get_comments_number(),
           'my-plugin'
       ),
       number_format_i18n( get_comments_number() )
   );

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n81:

Disambiguation by context 
--------------------------

Sometimes one term is used in several contexts and although it is one
and the same word in English it has to be translated differently in
other languages. For example the word ``Post`` can be used both as a
verb ``"Click here to post your comment"`` and as a noun
``"Edit this post"``. In such cases the ``_x()`` or ``_ex()`` function
should be used. It is similar to ``__()`` and ``_e()``, but it has an
additional argument — the context:

.. code:: php

   _x( 'Post', 'noun', 'my-plugin' );
   _x( 'Post', 'verb', 'my-plugin' );

Using this method in both cases we will get the string Comment for the
original version, but the translators will see two Comment strings for
translation, each in the different contexts.

Note that similarly to ``__()``, ``_x()`` has an ``echo`` version:
``_ex()``. The previous example could be written as:

.. code:: php

   _ex( 'Post', 'noun', 'my-plugin' );
   _ex( 'Post', 'verb', 'my-plugin' );

Use whichever you feel enhances legibility and ease-of-coding.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n89:

Descriptions
------------

So that translators know how to translate a string like
``__( 'g:i:s a' )`` you can add a clarifying comment in the source code.
It has to start with the words ``translators:`` and to be the last PHP
comment before the gettext call. Here is an example:

.. code:: php

   /* translators: draft saved date format, see http://php.net/date */
   $saved_date_format = __( 'g:i:s a' );

It’s also used to explain placeholders in a string like
``_n_noop( 'Version %1$s addressed %2$s bug.','Version %1$s addressed %2$s bugs.' )``.

.. code:: php

   /* translators: 1: WordPress version number, 2: plural number of bugs. */
   _n_noop( '<strong>Version %1$s</strong> addressed %2$s bug.',
            '<strong>Version %1$s</strong> addressed %2$s bugs.' );

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n95:

Newline characters 
-------------------

Gettext doesn’t like ``\r`` (ASCII code: 13) in translatable strings, so
please avoid it and use ``\n`` instead.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n98:

Empty strings 
--------------

The empty string is reserved for internal Gettext usage and you must not
try to internationalize the empty string. It also doesn’t make any
sense, because the translators won’t see any context.

If you have a valid use-case to internationalize an empty string, add
context to both help translators and be in peace with the Gettext
system.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n102:

Handling JavaScript files 
--------------------------

Use ``wp_localize_script()`` to add translated strings or other
server-side data to a previously enqueued script.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n105:

Escaping strings 
-----------------

It is good to escape all of your strings, this way the translators
cannot run malicious code. There are a few escape functions that are
integrated with internationalisation functions.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n108:

Localization functions 
-----------------------

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n110:

Basic functions 
~~~~~~~~~~~~~~~~

-  `\__() <https://developer.wordpress.org/reference/functions/__/>`__

-  `\_e() <https://developer.wordpress.org/reference/functions/_e/>`__

-  `\_x() <https://developer.wordpress.org/reference/functions/_x/>`__

-  `\_ex() <https://developer.wordpress.org/reference/functions/_ex/>`__

-  `\_n() <https://developer.wordpress.org/reference/functions/_n/>`__

-  `\_nx() <https://developer.wordpress.org/reference/functions/_nx/>`__

-  `n\ noop() <https://developer.wordpress.org/reference/functions/_n_noop/>`__

-  `nx\ noop() <https://developer.wordpress.org/reference/functions/_nx_noop/>`__

-  `translate\ nooped\ plural() <https://developer.wordpress.org/reference/functions/translate_nooped_plural()/>`__

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n131:

Translate & Escape functions 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Strings that require translation and is used in attributes of html tags
must be escaped.

-  `esc_html__() <https://developer.wordpress.org/reference/functions/esc_html__/>`__

-  `esc\ html\ e() <https://developer.wordpress.org/reference/functions/esc_html_e/>`__

-  `esc\ html\ x() <https://developer.wordpress.org/reference/functions/esc_html_x/>`__

-  `esc_attr__() <https://developer.wordpress.org/reference/functions/esc_attr__/>`__

-  `esc\ attr\ e() <https://developer.wordpress.org/reference/functions/esc_attr_e/>`__

-  `esc\ attr\ x() <https://developer.wordpress.org/reference/functions/esc_attr_x/>`__

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n147:

Date and number functions 
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `number\ format\ i18n() <https://developer.wordpress.org/reference/functions/number_format_i18n>`__

-  `date_i18n() <https://developer.wordpress.org/reference/functions/date_i18n>`__

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n154:

Best Practices for writing strings 
-----------------------------------

Here are the best practices for writing strings

-  Use decent English style – minimize slang and abbreviations.

-  Use entire sentences – in most languages word order is different than
   that in English.

-  Split at paragraphs – merge related sentences, but do not include a
   whole page of text in one string.

-  Do not leave leading or trailing whitespace in a translatable phrase.

-  Assume strings can double in length when translated

-  Avoid unusual markup and unusual control characters – do not include
   tags that surround your text

-  Do not put unnecessary HTML markup into the translated string

-  Do not leave URLs for translation, unless they could have a version
   in another language.

-  Add the variables as placeholders to the string as in some languages
   the placeholders change position.

.. code:: php

   printf(
       __( 'Search results for: %s', 'my-plugin' ),
       get_search_query()
   );

-  Use format strings instead of string concatenation – translate
   phrases and not words –

   .. code:: php

      printf(
        	__( 'Your city is %1$s, and your zip code is %2$s.', 'my-plugin' ),
        	$city,
        	$zipcode
      );

   is always better than:

   .. code:: php

      __( 'Your city is ', 'my-plugin' ) . $city . __( ', and your zip code is ', 'my-plugin' ) . $zipcode;

-  Try to use the same words and same symbols so not multiple strings
   needs to be translated e.g.\ ``__( 'Posts:', 'my-plugin' );`` and
   ``__( 'Posts', 'my-plugin' );``

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n185:

Add Text Domain to strings 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must add your Text domain as an argument to every ``__()``, ``_e()``
and ``__n()`` gettext call, or your translations won’t work.

Examples:

-  .. code:: php

      __( 'Post' )

   should become

   .. code:: php

      __( 'Post', 'my-theme' )

-  .. code:: php

      _e( 'Post' )

   should become

   .. code:: php

      _e( 'Post', 'my-theme' )

-  .. code:: php

      _n( '%s post', '%s posts', $count )

   should become

   .. code:: php

      _n( '%s post', '%s posts', $count, 'my-theme' )

If there are strings in your plugin that are also used in WordPress core
(e.g. ‘Settings’), you should still add your own text domain to them,
otherwise they’ll become untranslated if the core string changes (which
happens).

Adding the text domain by hand can be a burden if not done continuously
when writing code and that’s why you can do it automatically:

-  Download the ``add-textdomain.php`` script to the folder where the
   file is you want to add the text domain

-  In command line move to the directory where the file is

-  Run this command to create a new file with the text domain added

.. code:: php

   php add-textdomain.php my-plugin my-plugin.php > new-my-plugin.php

If you wish to have the ``add-textdomain.php`` in a different folder you
just need to define the location in the command.

.. code:: php

   php \path\to\add-textdomain.php my-plugin my-plugin.php > new-my-plugin.php

Use this command if you don’t want a new file outputted.

.. code:: php

   php add-textdomain.php -i my-plugin my-plugin.php

If you want to change multiple files in a directory you can also pass a
directory to the script.

.. code:: php

   php add-textdomain.php -i my-plugin my-plugin-directory

After it’s done, the text domain will be added to the end of all gettext
calls in the file. If there is an existing text domain it will not be
replaced.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n222:

Loading Text Domain 
--------------------

   | **Note:** After WordPress
     `4.6 <https://codex.wordpress.org/Version_4.6>`__ came out,
     translations now take
     `translate.wordpress.org <https://translate.wordpress.org/>`__ as
     priority and so plugins that are translated via
     translate.wordpress.org do not necessary require
     ``load_plugin_textdomain()`` anymore.
   | If you don’t want to add a ``load_plugin_textdomain()`` call to
     your plugin you have to set the ``Requires at least:`` field in
     your readme.txt to 4.6.

You need to load the MO file with your plugin’s translations. You can
load them by calling the function ``load_plugin_textdomain()``. This
call loads ``{text-domain}-{locale}.mo`` from your plugin’s base
directory. The locale is the language code and/or country code of the
site language setting under General Settings. For more information about
language and country codes, see `WordPress in Your
Language <https://codex.wordpress.org/WordPress_in_Your_Language>`__.

| From the code example above the text domain is ``my-plugin`` therefore
  the German MO and PO files should be named ``my-plugin-de_DE.mo`` and
  ``my-plugin-de_DE.po``.
| Example:

.. code:: php

   function my_plugin_load_plugin_textdomain() {
       load_plugin_textdomain( 'my-plugin', FALSE, basename( dirname( __FILE__ ) ) . '/languages/' );
   }
   add_action( 'plugins_loaded', 'my_plugin_load_plugin_textdomain' );

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#top>`__

.. _header-n229:

Language Packs `#Language Packs <https://developer.wordpress.org/plugins/internationalization/how-to-internationalize-your-plugin/#language-packs>`__
-----------------------------------------------------------------------------------------------------------------------------------------------------

If you’re interested in language packs and how the import to
translate.wordpress.org is working, please read the `Meta Handbook page
about
Translations <https://make.wordpress.org/meta/handbook/documentation/translations/>`__.
