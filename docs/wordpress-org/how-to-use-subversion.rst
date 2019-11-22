.. _header-n0:

Using Subversion
================

.. contents::

SVN, or Subversion, is a version control system similar to Git. It can
be used via command line, or one of numerous GUI applications, such as
`Tortoise SVN <https://tortoisesvn.net/>`__,
`SmartSVN <https://www.smartsvn.com/>`__, and more. If you’re new to
SVN, we recommend reviewing a `comparison of SVN
clients <https://en.wikipedia.org/wiki/Comparison_of_Subversion_clients>`__
before deciding which is best for you.

This document is *not* a complete and robust explanation for using SVN,
but more a quick primer to get started with plugins on WordPress.org.
For more comprehensive documentation, see `The SVN
Book <http://svnbook.red-bean.com/>`__.

We’ll describe here some of the basics about using subversion as it
relates to WordPress.org hosting.

For additional information, please see these documents:

-  `How the readme.txt
   works <https://developer.wordpress.org/plugins/wordpress-org/how-your-readme-txt-works/>`__

-  `How plugin assets (header images and icons)
   work <https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/>`__

..

   **Warning:** SVN and the Plugin Directory are a *release* repository.
   Unlike Git, you shouldn’t commit every small change, as doing so can
   degrade performance. Please only push **finished** changes to your
   SVN repository.

.. _header-n14:

Overview 
---------

All your files will be centrally stored in the **svn repository** on our
servers. From that repository, anyone can **check out** a copy of your
plugin files onto their local machine, but, as a plugin author, only you
have the authority to **check in**. That means you can make changes to
the files, add new files, and delete files on your local machine and
upload those changes back to the central server. It’s this process of
checking in that updates both the files in the repository and also the
information displayed in the WordPress.org Plugin Directory.

Subversion keeps track of all these changes so that you can go back and
look at old versions or **revisions** later if you ever need to. In
addition to remembering each individual revision, you can tell
subversion to **tag** certain revisions of the repository for easy
reference. Tags are great for `labelling different releases of your
plugin <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#task-3>`__.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n18:

Your Account 
-------------

Your account for SVN will be the same username (not the email) of the
account you used when you submitted the plugin. This is the user ID you
use for the WordPress forums as well.

Remember, *capitalization matters*, so if your username is JaneDoe, then
you must use the capital J and D or else SVN will fail.

If you need to reset your password, go to
`login.wordpress.org <https://login.wordpress.org/>`__

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n23:

SVN Folders 
------------

There are four directories created by default in all SVN repositories.

.. code:: 

   `/assets/`
   `/branches/`
   `/tags/`
   `/trunk/`

-  Use ``assets`` for `screenshots, plugin headers, and plugin
   icons <https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/>`__.

-  Development work belongs in ``trunk``.

-  Releases go in ``tags``.

-  Divergent branches of code go into ``branches``.

.. _header-n35:

Trunk 
~~~~~~

The ``/trunk`` directory is where your plugin code should live. The
trunk can be considered to be the latest and greatest code, however this
is not necessarily the latest *stable* code. Trunk is for the
development version. Hopefully, the code in trunk should always be
working code, but it may be buggy from time to time because it’s not
necessarily the “stable” version. For simple plugins, the trunk may be
the only version of the code that exists, and that’s fine as well.

Even if you do your development work elsewhere (like a git repository),
we recommend you keep the trunk folder up to date with your code for
easy SVN compares.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n39:

Tags 
~~~~~

The ``/tags`` directory is where you can put versions of the plugin at
some specific point in time. Usually, you’ll use version numbers for the
subdirectories here. So version 1.0 of the plugin would be in
``/tags/1.0``, version 1.1 would be in ``/tags/1.1``, and so forth.
Again, not every plugin uses tags for versioning, however for those that
do we strongly encourage the use of `semantic software
versioning <https://en.wikipedia.org/wiki/Software_versioning>`__.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n42:

Branches 
~~~~~~~~~

The ``/branches`` directory is a place that you can use to store
branches of the plugin. Perhaps versions that are in development, or
test code, etc. The WordPress.org system does not use the branches
directory for anything at all, it’s considered to be strictly for
developers to use as they need it.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n45:

Assets 
~~~~~~~

   Note: See also: `How Your Plugin Assets
   Work <https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/>`__

Assets is where your screenshots, header images, and plugin icons
reside. It’s recommended but not required to put screenshot files in
``/assets``

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n50:

Best Practices 
---------------

In order to make your code the most accessible for other developers, the
following practices are considered to be optimum.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n53:

Don’t use SVN for development 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is often confusing. Unlike GitHub, SVN is meant to be a *release*
system, not a development system. You don’t need to commit and push
every small change, and in fact doing so is detrimental to the system.
Every time you push code to SVN, it rebuilds *all* your zip files for
all versions in SVN. This is why sometimes your plugin updates don’t
show for up to 6 hours. Instead, you should push one time, when you’re
ready to go.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n56:

Use the trunk folder for code 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many people use ``trunk`` as a placeholder. While it’s possible to
simply update the ``readme.txt`` file in trunk and put everything in tag
folders, doing so makes it more difficult to compare any changes in your
code. Instead, trunk should contain the latest version of your code,
even if that version is a beta.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n59:

Create tags from trunk 
~~~~~~~~~~~~~~~~~~~~~~~

Instead of pushing your code directly to a tag folder, you should update
the code in trunk, complete with the stable version in the readme, and
*then* copy the code from trunk to the new tag.

Not only will this make it easier see any changes, you will be making
smaller commits as SVN will only update the changed code. This will save
you time and reduce potential errors (such as updating to the wrong
stable tag and pushing bad code to users).

Don’t worry about the tag folder not existing for a short while.
WordPress is smart enough to fall back to the trunk folder.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n64:

Delete old versions 
~~~~~~~~~~~~~~~~~~~~

Since SVN is a release repository, it’s encouraged that you remove older
versions of your code. This will make it faster when you need to
checkout a fresh copy of SVN, but also will make new builds of your code
faster. Keeping the last version of each major release is an easy way to
keep the size down.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n67:

Examples 
---------

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n69:

Starting a New Plugin 
~~~~~~~~~~~~~~~~~~~~~~

To start your plugin, you need to add the files you already have to your
new SVN repository.

First create a local directory on your machine to house a copy of the
SVN repository:

.. code:: shell

   $ mkdir my-local-dir

Next, check out the pre-built repository

.. code:: shell

   $ svn co https://plugins.svn.wordpress.org/your-plugin-name my-local-dir
   > A my-local-dir/trunk
   > A my-local-dir/branches
   > A my-local-dir/tags
   > Checked out revision 11325.

In our example, subversion has added ( “A” for “add” ) all of the
directories from the central SVN repository to your local copy.

To add your code, navigate into the ``my-local-dir`` folder:
``$ cd my-local-dir``

Now you can add your files to the ``trunk/`` directory of your local
copy of the repository using copy/paste commands via command line, or
dragging and dropping. Whatever you’re comfortable with.

   **Warning:** Do not put your *main* plugin file in a subfolder of
   trunk, like ``/trunk/my-plugin/my-plugin.php`` as that will break
   downloads. You may use subfolders for included files.

Once your files are in the trunk folder, you must let subversion know
you want to add those new files back into the central repository.

.. code:: shell

   $ cd my-local-dir
   my-local-dir/ $ svn add trunk/*
   > A trunk/my-plugin.php
   > A trunk/readme.txt

After you add all your files, you’ll check in the changes back to the
central repository.

.. code:: shell

   my-local-dir/ $ svn ci -m 'Adding first version of my plugin'
   > Adding trunk/my-plugin.php
   > Adding trunk/readme.txt
   > Transmitting file data .
   > Committed revision 11326.

It’s required to include a commit message for all checkins.

If the commit fails because of ‘Access forbidden’ and you **know** you
have commit access, add your username and password to the check-in
command.

.. code:: shell

   my-local-dir/ $ svn ci -m 'Adding first version of my plugin' --username your_username --password your_password

Remember your username is *case sensitive*.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n89:

Editing Existing Files 
~~~~~~~~~~~~~~~~~~~~~~~

Once your plugin is in the directory, you will likely need to edit the
code at some point.

First go into your your local copy of the repository and make sure it’s
up to date.

.. code:: shell

   $ cd my-local-dir/
   my-local-dir/ $ svn up
   > At revision 11326.

In the above example, we’re all up to date. If there had been changes in
the central repository, they would have been downloaded and merged into
your local copy.

Now you can edit the file that needs changing using whatever editor you
prefer.

If you’re not using an SVN GUI tool (like SubVersion or Coda) you can
still check and see what’s different between your local copy and the
central repository after you make changes. First we check the status of
the local copy:

.. code:: shell

   my-local-dir/ $ svn stat
   > M trunk/my-plugin.php

This tells us that our local ``trunk/my-plugin.php`` is different from
the copy we downloaded from the central repository ( “M” for “modified”
).

Let’s see what exactly has changed in that file, so we can check it over
and make sure things look right.

.. code:: shell

   my-local-dir/ $ svn diff
   > * What comes out is essentially the result of a
     * standard `diff -u` between your local copy and the
     * original copy you downloaded.

If it all looks good then it’s time to check in those changes to the
central repository.

.. code:: shell

   my-local-dir/ $ svn ci -m "fancy new feature: now you can foo *and* bar at the same time"
   > Sending trunk/my-plugin.php
   > Transmitting file data .
   > Committed revision 11327.

And now you’ve successfully updated trunk.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n104:

“Tagging” New Versions 
~~~~~~~~~~~~~~~~~~~~~~~

Each time you make a formal release of your plugin, you should tag a
copy of that release’s code. This lets your users easily grab the latest
(or an older) version, it lets you keep track of changes more easily,
and lets the WordPress.org Plugin Directory know what version of your
plugin it should tell people to download.

First copy your code to a subdirectory in the ``tags/`` directory. For
the sake of the WordPress.org plugin browser, the new subdirectory
should always look like a version number. ``2.0.1.3`` is good.
``Cool hotness tag`` is **bad**.

We want to use ``svn cp`` instead of the regular ``cp`` in order to take
advantage of SVN’s features.

.. code:: shell

   my-local-dir/ $ svn cp trunk tags/2.0
   > A tags/2.0

As always, check in the changes.

.. code:: shell

   my-local-dir/ $ svn ci -m "tagging version 2.0"
   > Adding         tags/2.0
   > Adding         tags/2.0/my-plugin.php
   > Adding         tags/2.0/readme.txt
   > Committed revision 11328.

Alternately, you can use http URLs to copy, and save yourself bandwidth:

.. code:: shell

   my-local-dir/ $ svn cp https://plugins.svn.wordpress.org/your-plugin-name/trunk https://plugins.svn.wordpress.org/your-plugin-name/tags/2.0

Doing that will perform the copy remotely instead of copying everything
locally and uploading. This can be beneficial if your plugin is larger.

After tagging a new version, **remember to update** the ``Stable Tag``
field in
```trunk/readme.txt`` <https://wordpress.org/plugins/developers/#readme>`__!

Congratulations! You’ve updated your code!

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n117:

Notes 
------

Don’t put anything in SVN that you’re not willing and prepared to have
deployed to everyone who uses your plugin. This *includes* vendor files,
``.gitignore`` and everything else.

`Top
↑ <https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#top>`__

.. _header-n120:

See Also 
~~~~~~~~~

-  `How the readme.txt
   works <https://developer.wordpress.org/plugins/wordpress-org/how-your-readme-txt-works/>`__

-  `How plugin assets (header images and icons)
   work <https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/>`__

-  `The SVN Book <http://svnbook.red-bean.com/>`__
