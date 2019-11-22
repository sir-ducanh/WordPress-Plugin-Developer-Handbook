.. _header-n0:

Localization
============

.. contents::

.. _header-n4:

What is localization? 
----------------------

Localization describes the subsequent process of translating an
internationalized plugin. Localization is abbreviated as ``l10n``
(because there are 10 letters between the l and the n.)

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n7:

Localization files 
-------------------

.. _header-n8:

POT (Portable Object Template) files 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file contains the original strings (in English) in your plugin.
Here is an example ``POT`` file entry:

.. code:: php

   #: plugin-name.php:123
   msgid "Page Title"
   msgstr ""

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n12:

PO (Portable Object) files 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every translator will take the ``POT`` file and translate the ``msgstr``
sections in their own language. The result is a ``PO`` file with the
same format as a ``POT``, but with translations and some specific
headers. There is one PO file per language.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n15:

MO (Machine Object) files 
~~~~~~~~~~~~~~~~~~~~~~~~~~

From every translated ``PO`` file a ``MO`` file is built. These are
machine-readable, binary files that the gettext functions actually use
(they don’t care about .POT or .PO files), and are a “compiled” version
of the PO file. The conversion is done using the ``msgfmt`` tool. In
general, an application may use more than one large logical translatable
module and a different ``MO`` file accordingly. A text domain is a
handle of each module, which has a different ``MO`` file.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n18:

Generating POT file 
--------------------

The POT file is the one you need to hand to translators, so that they
can do their work. The POT and PO files can easily be interchangeably
renamed to change file types without issues. It is a good idea to offer
the POT file along with your plugin, so that translators won’t have to
ask you specifically about it. There are a couple of ways to generate a
POT file for your plugin:

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n21:

WP-CLI 
~~~~~~~

Install `WP-CLI <https://make.wordpress.org/cli/handbook/installing/>`__
and use the ``wp i18n make-pot`` command according to the
`documentation <https://developer.wordpress.org/cli/commands/i18n/make-pot/>`__.

Open command line and run the command like this:

.. code:: shell

   wp i18n make-pot path/to/your-plugin-directory

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n26:

Poedit 
~~~~~~~

You can also use `Poedit <http://www.poedit.net/>`__ locally when
translating. This is an open source tool for all major OS. The free
Poedit default version supports manual scanning of all source code with
Gettext functions. A pro version of it also features one-click scanning
for WordPress plugins. After generating the po file you can rename the
file to POT. If a mo was generated then you can delete that file as it
is not needed. If you don’t have the pro version you can easily get the
`Blank POT <https://github.com/fxbenard/Blank-WordPress-Pot>`__ and use
that as the base of your POT file. Once you have placed the blank POT in
the languages folder you can click “Update” in Poedit to update the POT
file with your strings.

.. figure:: https://developer.wordpress.org/files/2014/10/internationalization-localization-03.jpg
   :alt: 

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n30:

Grunt Tasks 
~~~~~~~~~~~~

| There are even some grunt tasks that you can use to create the POTs.
  `grunt-wp-i18n <https://github.com/blazersix/grunt-wp-i18n>`__ &
  `grunt-pot <https://www.npmjs.org/package/grunt-pot>`__
| To set it up you need to install `node.js <http://nodejs.org/>`__. It
  is a simple installation. Then you need to `install
  grunt <http://gruntjs.com/getting-started>`__ in the directory that
  you would like to use grunt in. This is done via `command
  line <http://leveluptuts.com/tutorials/command-line-basics>`__. An
  `example Grunt.js and
  package.json <https://gist.github.com/grappler/10187003>`__ that you
  can place in the root of your plugin. You can the grunt tasks with a
  simple command in the command line.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n33:

Translate PO file 
------------------

There are multiple ways to translate a PO file.

You can use a text editor to enter the translation. In a text editor it
will look like this.

.. code:: php

   #: plugin-name.php:123
   msgid "Page Title"
   msgstr ""

You enter the translation between the quotation marks. For the German
translation it would look like this.

.. code:: php

   #: plugin-name.php:123
   msgid "Page Title"
   msgstr "Seitentitel"

You can also use `Poedit <http://www.poedit.net/>`__ when translating.
This is an open source tool for all major OS. The free Poedit default
version supports manual scanning of all source code with Gettext
functions. A pro version of it also features one-click scanning for
WordPress plugins and themes.

A third option is to use a online translation service. The general idea
is that you upload the POT file and then you can give permission to
users or translators to translate your plugin. This allows you to track
the changes, always have the latest translation and reduce the
translation being done twice.

Here are a few tools that can be used to translate PO files online:

-  `Transifex <https://www.transifex.com/>`__

-  `WebTranslateIt <https://webtranslateit.com/en>`__

-  `Poeditor <https://poeditor.com/>`__

-  `Google Translator Toolkit <http://translate.google.com/toolkit/>`__

-  `GlotPress <http://blog.glotpress.org/>`__

The translated file is to be saved as ``my-plugin-{locale}.mo``. The
locale is the language code and/or country code you defined in the
constant ``WPLANG`` in the file ``wp-config.php``. For example, the
locale for German is ``de_DE``. From the code example above the text
domain is ‘my-plugin’ therefore the German MO and PO files should be
named ``my-plugin-de_DE.mo`` and ``my-plugin-de_DE.po``. For more
information about language and country codes, see `Installing WordPress
in Your
Language <https://codex.wordpress.org/Installing_WordPress_in_Your_Language>`__.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n55:

Generate MO file 
-----------------

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n57:

Command line 
~~~~~~~~~~~~~

A program ``msgfmt`` is used to create the MO file. ``msgfmt`` is part
of Gettext package. Otherwise command line can be used. A typical
``msgfmt`` command looks like this:

**Unix Operating Systems**

.. code:: shell

   msgfmt -o filename.mo filename.po

**Windows Operating Systems**

.. code:: powershell

   msgfmt -o filename.mo filename.po

If you have a lot of ``PO`` files to convert at once, you can run it as
a batch. For example, using a ``bash`` command:

**Unix Operating Systems**

.. code:: shell

   # Find PO files, process each with msgfmt and rename the result to MO
   for file in `find . -name "*.po"` ; do msgfmt -o ${file/.po/.mo} $file ; done

| **Windows Operating Systems**
| For Windows you need to install `Cygwin <http://www.cygwin.com/>`__
  first.

Create a potomo.sh

.. code:: shell

   #! /bin/sh
   # Find PO files, process each with msgfmt and rename the result to MO
   for file in `/usr/bin/find . -name '*.po'` ; do /usr/bin/msgfmt -o ${file/.po/.mo} $file ; done

You can run this command in the command line.

.. code:: shell

   cd C:/path/to/language/folder/my-plugin/languages & C:/cygwin/bin/bash -c /cygdrive/c/path/to/script/directory/potomo.sh

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n72:

Poedit 
~~~~~~~

``msgfmt`` is also integrated in `Poedit <http://www.poedit.net/>`__
allowing you to use it to generate the MO file. There is a setting in
the preferences where you can enable or disable it.

.. figure:: https://developer.wordpress.org/files/2014/10/internationalization-localization-04.jpg
   :alt: 

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n76:

Grunt task 
~~~~~~~~~~~

There is `grunt-po2mo <https://www.npmjs.org/package/grunt-po2mo>`__
that will convert all of the files.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n79:

Tips for Good Translations 
---------------------------

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n81:

Don’t translate literally, translate organically 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Being bi- or multi-lingual, you undoubtedly know that the languages you
speak have different structures, rhythms, tones, and inflections.
Translated messages don’t need to be structured the same way as the
English ones: take the ideas that are presented and come up with a
message that expresses the same thing in a natural way for the target
language. It’s the difference between creating an equal message and an
equivalent message: don’t replicate, replace. Even with more structural
items in messages, you have creative license to adapt and change if you
feel it will be more logical for, or better adapted to, your target
audience.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n84:

Try to keep the same level of formality (or informality) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each message has a different level of formality or informality. Exactly
what level of formality or informality to use for each message in your
target language is something you’ll have to figure out on your own (or
with your team), but WordPress messages (informational messages in
particular) tend to have a politely informal tone in English. Try to
accomplish the equivalent in the target language, within your cultural
context.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n87:

Don’t use slang or audience-specific terms 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some amount of terminology is to be expected in a blog, but refrain from
using colloquialisms that only the “in” crowd will get. If the
uninitiated blogger were to install WordPress in your language, would
they know what the term means? Words like pingback, trackback, and feed
are exceptions to this rule; they’re terminology that are typically
difficult to translate, and many translators choose to leave in English.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n90:

Read other software’s localizations in your language 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get stuck or need direction, try reading through the translations
of other popular software tools to get a feel for what terms are
commonly used, how formality is addressed, etc. Of course, WordPress has
its own tone and feel, so keep that in mind when you’re reading other
localizations, but feel free to dig up UI terms and the like to maintain
consistency with other software in your language.

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n93:

Using Localizations 
--------------------

Place the localization files in the language folder, either in the
plugin ``languages`` folder or as of WordPress 3.7 in the plugin
``languages`` folder normally under ``wp-content``. The full path would
be ``wp-content/languages/plugins/my-plugin-fr_FR.mo``.

As of `WordPress
4.0 <https://make.wordpress.org/core/2014/09/05/language-chooser-in-4-0/>`__
you can change the language in the “General Settings”. If you do not see
any option or the language that you want to switch to then do the
following steps:

-  Define WPLANG inside of wp-config.php to your chosen language. For
   example, if you wanted to use french, you would have:

   .. code:: php

      define ('WPLANG', 'fr_FR');

-  Go to ``wp-admin/options-general.php`` or “Settings” -> “General”

-  Select your language in “Site Language” dropdown

-  Go to ``wp-admin/update-core.php``

-  Click “Update translations”, when available

-  Core translations files are downloaded, when available

`Top
↑ <https://developer.wordpress.org/plugins/internationalization/localization/#top>`__

.. _header-n111:

Resources 
----------

-  `Creating .pot file for your theme or
   plugin <https://foxland.fi/creating-pot-file-for-your-theme-or-plugin/>`__

-  `How To Internationalize WordPress
   Plugins <http://tommcfarlin.com/internationalize-wordpress-plugins/>`__

-  `Translating Your
   Theme <http://wp.tutsplus.com/tutorials/theme-development/translating-your-theme/>`__

-  `Blank WordPress
   POT <https://github.com/fxbenard/Blank-WordPress-Pot>`__

-  `Improved i18n WordPress tools <https://github.com/grappler/i18n>`__

-  `How to update translations
   quickly <http://ulrich.pogson.ch/update-translations-quickly>`__

-  `Workflow between
   GitHub/Transifex <http://wp-translations.org/workflow-using-github/>`__

-  `Gist: Complete Localization Grunt
   task <https://gist.github.com/grappler/10187003>`__

-  `WordPress.tv <http://wordpress.tv/>`__ tags:
   `i18n <http://wordpress.tv/tag/i18n/>`__,
   `internationalization <http://wordpress.tv/tag/internationalization/>`__
   and `translation <http://wordpress.tv/tag/translation/>`__
