# Determining Plugin and Content Directories
[toc]


When coding WordPress plugins you often need to reference various files and folders throughout the WordPress installation and within your plugin or theme.

WordPress provides several functions for easily determining where a given file or directory lives. Always use these functions in your plugins instead of hard-coding references to the wp-content directory or using the WordPress internal constants.

Tip:WordPress allows users to place their wp-content directory anywhere they want and rename it whatever they want. Never assume that plugins will be in wp-content/plugins, uploads will be in wp-content/uploads, or that themes will be in wp-content/themes.

PHP’s `__FILE__` magic-constant resolves symlinks automatically, so if the `wp-content` or `wp-content/plugins` or even the individual plugin directory is symlinked, hardcoded paths will not work correctly.

## Common Usage

If your plugin includes JavaScript files, CSS files or other external files, then it’s likely you’ll need the URL to these files so you can load them into the page. To do this you should use the [plugins_url()](https://developer.wordpress.org/reference/functions/plugins_url/) function like so:

```php
plugins_url( 'myscript.js', _FILE_ );
```

This will return the full URL to myscript.js, such as `example.com/wp-content/plugins/myplugin/myscript.js`.

To load your plugins’ JavaScript or CSS into the page you should use [`wp_enqueue_script()`](https://developer.wordpress.org/reference/functions/wp_enqueue_script/) or [`wp_enqueue_style()`](https://developer.wordpress.org/reference/functions/wp_enqueue_style/) respectively, passing the result of `plugins_url()` as the file URL.

[Top ↑](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/#top)

## Available Functions

WordPress includes many other functions for determining paths and URLs to files or directories within plugins, themes, and WordPress itself. See the individual Codex pages for each function for complete information on their use.

### Plugins 

```php
plugins_url()
plugin_dir_url()
plugin_dir_path()
plugin_basename()
```

[Top ↑](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/#top)

### Themes 

```php
get_template_directory_uri()
get_stylesheet_directory_uri()
get_stylesheet_uri()
get_theme_root_uri()
get_theme_root()
get_theme_roots()
get_stylesheet_directory()
get_template_directory()
```

[Top ↑](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/#top)

### Site Home 

```php
home_url()
get_home_path()
```

[Top ↑](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/#top)

### WordPress 

```php
admin_url()
site_url()
content_url()
includes_url()
wp_upload_dir()
```

[Top ↑](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/#top)

### Multisite 

```php
get_admin_url()
get_home_url()
get_site_url()
network_admin_url()
network_site_url()
network_home_url()
```

[Top ↑](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/#top)

## Constants 
WordPress makes use of the following constants when determining the path to the content and plugin directories. These should not be used directly by plugins or themes, but are listed here for completeness.

```php
WP_CONTENT_DIR  // no trailing slash, full paths only
WP_CONTENT_URL  // full url 
WP_PLUGIN_DIR  // full path, no trailing slash
WP_PLUGIN_URL  // full url, no trailing slash
// Available per default in MS, not set in single site install
// Can be used in single site installs (as usual: at your own risk)
UPLOADS // (If set, uploads folder, relative to ABSPATH) (for e.g.: /wp-content/uploads)
```

[Top ↑](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/#top)

## Related 

***\*WordPress Directories\****:

| ***\*WordPress Directories\****:                             |                                         |                                                              |
| :----------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------ |
| [home_url()](https://developer.wordpress.org/reference/functions/home_url/) | Home URL                                | [http://www.example.com](http://www.example.com/)            |
| [site_url()](https://developer.wordpress.org/reference/functions/site_url/) | Site directory URL                      | [http://www.example.com](http://www.example.com/) or http://www.example.com/wordpress |
| [admin_url()](https://developer.wordpress.org/reference/functions/admin_url/) | Admin directory URL                     | http://www.example.com/wp-admin                              |
| [includes_url()](https://developer.wordpress.org/reference/functions/includes_url/) | Includes directory URL                  | http://www.example.com/wp-includes                           |
| [content_url()](https://developer.wordpress.org/reference/functions/content_url/) | Content directory URL                   | http://www.example.com/wp-content                            |
| [plugins_url()](https://developer.wordpress.org/reference/functions/plugins_url/) | Plugins directory URL                   | http://www.example.com/wp-content/plugins                    |
| [wp_upload_dir()](https://developer.wordpress.org/reference/functions/wp_upload_dir/) | Upload directory URL (returns an array) | http://www.example.com/wp-content/uploads                    |