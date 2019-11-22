.. _header-n0:

Including a Software License
============================

Most WordPress plugins are released under the
`GPL <http://www.gnu.org/licenses/gpl.html>`__, which is the same
license that WordPress itself uses. However, there are other options
available. It is always best to clearly indicate the license your plugin
uses.

In the `Header Requirements <header-requirements.md>`__ section, we
briefly mentioned how you can indicate your plugin’s license within the
plugin header comment. Another common, and encouraged, practice is to
place a license block comment near the top of your main plugin file (the
same one that has the plugin header comment).

This license block comment usually looks something like this:

.. code:: php

   /*
   {Plugin Name} is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 2 of the License, or
   any later version.

   {Plugin Name} is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with {Plugin Name}. If not, see {URI to Plugin License}.
   */

When combined with the plugin header comment:

.. code:: php

   /*
   Plugin Name: WordPress.org Plugin
   Plugin URI: https://developer.wordpress.org/plugins/the-basics/
   Description: Basic WordPress Plugin Header Comment
   Version:   20160911
   Author:   WordPress.org
   Author URI: https://developer.wordpress.org/
   Text Domain: wporg
   Domain Path: /languages
   License:   GPL2

   {Plugin Name} is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 2 of the License, or
   any later version.

   {Plugin Name} is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with {Plugin Name}. If not, see {License URI}.
   */
