.. _header-n0:

Users
=====

.. contents::

WordPress stores the Users in the ``users`` table.

.. _header-n4:

What is a user? 
----------------

Each WordPress user has, at the bare minimum, a username, password and
email address.

Once a user account is created, that user may log in using the WordPress
Admin (or programmatically) to access WordPress functions and data.

`Top ↑ <https://developer.wordpress.org/plugins/users/#top>`__

.. _header-n8:

Roles and Capabilities 
-----------------------

Users are assigned
`roles <https://developer.wordpress.org/plugins/users/roles-and-capabilities/#roles>`__,
and each role has a set of
`capabilities <https://developer.wordpress.org/plugins/users/roles-and-capabilities/#capabilities>`__.

You can create new roles with their own set of capabilities.

Custom capabilities can also be created and assigned to existing roles
or new roles.

In WordPress, developers can take advantage of user roles to limit the
set of actions an account can perform.

`Top ↑ <https://developer.wordpress.org/plugins/users/#top>`__

.. _header-n14:

The Principle of Least Privileges
---------------------------------

WordPress adheres to the principal of least privileges, the practice of
giving a user *only* the privileges that are essential for performing
the desired work.
