# Custom Hooks

[toc]


**An important, but often overlooked practice is using custom hooks in your plugin so that other developers can extend and modify it.**

Custom hooks are created and called in the same way that WordPress Core hooks are.

## Create a Hook

To create a custom hook, use [do_action()](https://developer.wordpress.org/reference/functions/do_action/) for [Actions](https://developer.wordpress.org/plugins/hooks/actions/) and [apply_filters()](https://developer.wordpress.org/reference/functions/apply_filters/) for [Filters](https://developer.wordpress.org/plugins/hooks/filters/).

---
> > **Note:** We recommend using [apply_filters()](https://developer.wordpress.org/reference/functions/apply_filters/) on any text that is output to the browser. Particularly on the frontend.
> > 
> > This makes it easier for plugins to be modified according to the user’s needs.
---

[Top ↑](https://developer.wordpress.org/plugins/hooks/custom-hooks/#top)

## Add a Callback to the Hook 

To add a callback function to a custom hook, use [add_action()](https://developer.wordpress.org/reference/functions/add_action/) for [Actions](https://developer.wordpress.org/plugins/hooks/actions/) and [add_filter()](https://developer.wordpress.org/reference/functions/add_filter/) for [Filters](https://developer.wordpress.org/plugins/hooks/filters/).

[Top ↑](https://developer.wordpress.org/plugins/hooks/custom-hooks/#top)

## Naming Conflicts 

Since any plugin can create a custom hook, it’s important to prefix your hook names to avoid collisions with other plugins.

For example, a filter named `email_body` would be less useful because it’s likely that another developer will choose that same name. If the user installs both plugins, it could lead to bugs that are difficult to track down.

Naming the function `wporg_email_body` (where `wporg_` is a unique prefix for your plugin) would avoid any collisions.

[Top ↑](https://developer.wordpress.org/plugins/hooks/custom-hooks/#top)

## Examples 

### Extensible Action: Settings Form 

If your plugin adds a settings form to the Administrative Panels, you can use Actions to allow other plugins to add their own settings to it.

```php
<?php
function wporg_settings_page_html()
{
    ?>
    Foo: <input id="foo" name="foo" type="text">
    Bar: <input id="bar" name="bar" type="text">
    <?php
    do_action('wporg_after_settings_page_html');
}
```

Now another plugin can register a callback function for the `wporg_after_settings_page_html` hook and inject new settings:

```php
<?php
function myprefix_add_settings()
{
    ?>
    New 1: <input id="new_setting" name="new_settings" type="text">
    <?php
}
add_action('wporg_after_settings_page_html', 'myprefix_add_settings');
```

[Top ↑](https://developer.wordpress.org/plugins/hooks/custom-hooks/#top)

### Extensible Filter: Custom Post Type 

In this example, when the new post type is registered, the parameters that define it are passed through a filter, so another plugin can change them before the post type is created.

```php
<?php
function wporg_create_post_type()
{
    $post_type_params = [/* ... */];
 
    register_post_type(
        'post_type_slug',
        apply_filters('wporg_post_type_params', $post_type_params)
    );
}
```

Now another plugin can register a callback function for the `wporg_post_type_params` hook and change post type parameters:

```php
<?php
function myprefix_change_post_type_params($post_type_params)
{
    $post_type_params['hierarchical'] = true;
    return $post_type_params;
}
add_filter('wporg_post_type_params', 'myprefix_change_post_type_params');

```

[Top ↑](https://developer.wordpress.org/plugins/hooks/custom-hooks/#top)

## External Resources 

- [Extendable Extensions](http://wordpress.tv/2012/08/27/michael-fields-extendable-extensions/) by Michael Fields
- [WordPress Plugins as Frameworks](http://picklewagon.com/2011/09/26/wordpress-plugins-as-frameworks/) by Josh Harrison
- [The Pluggable Plugin](http://wordpress.tv/2010/12/03/brandon-dove-the-pluggable-plugin/) by Brandon Dove
- [WordPress Plugin Pet Peeves #3: Not Being Extensible](http://willnorris.com/2009/06/wordpress-plugin-pet-peeve-3-not-being-extensible) by Will Norris