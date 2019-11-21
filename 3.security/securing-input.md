# Securing Input

[toc]

Securing input is the process of sanitizing (cleaning, filtering) input data.

You use sanitizing when you don’t know what to expect or you don’t want to be strict with [data validation](data-validation.md).

**Any time you’re accepting potentially unsafe data, it is important to validate or sanitize it.**

## Sanitizing the Data 

The easiest way to sanitize data is with built-in WordPress functions.

The `sanitize_*()` series of helper functions are super nice, as they ensure you’re ending up with safe data, and they require minimal effort on your part:

- [sanitize_email()](https://developer.wordpress.org/reference/functions/sanitize_email/)
- [sanitize_file_name()](https://developer.wordpress.org/reference/functions/sanitize_file_name/)
- [sanitize_hex_color()](https://developer.wordpress.org/reference/functions/sanitize_hex_color/)
- [sanitize_hex_color_no_hash()](https://developer.wordpress.org/reference/functions/sanitize_hex_color_no_hash/)
- [sanitize_html_class()](https://developer.wordpress.org/reference/functions/sanitize_html_class/)
- [sanitize_key()](https://developer.wordpress.org/reference/functions/sanitize_key/)
- [sanitize_meta()](https://developer.wordpress.org/reference/functions/sanitize_meta/)
- [sanitize_mime_type()](https://developer.wordpress.org/reference/functions/sanitize_mime_type/)
- [sanitize_option()](https://developer.wordpress.org/reference/functions/sanitize_option/)
- [sanitize_sql_orderby()](https://developer.wordpress.org/reference/functions/sanitize_sql_orderby/)
- [sanitize_text_field()](https://developer.wordpress.org/reference/functions/sanitize_text_field/)
- [sanitize_title()](https://developer.wordpress.org/reference/functions/sanitize_title/)
- [sanitize_title_for_query()](https://developer.wordpress.org/reference/functions/sanitize_title_for_query/)
- [sanitize_title_with_dashes()](https://developer.wordpress.org/reference/functions/sanitize_title_with_dashes/)
- [sanitize_user()](https://developer.wordpress.org/reference/functions/sanitize_user/)
- [esc_url_raw()](https://developer.wordpress.org/reference/functions/esc_url_raw/)
- [wp_filter_post_kses()](https://developer.wordpress.org/reference/functions/wp_filter_post_kses/)
- [wp_filter_nohtml_kses()](https://developer.wordpress.org/reference/functions/wp_filter_nohtml_kses/)

[Top ↑](https://developer.wordpress.org/plugins/security/securing-input/#top)

## Example 

Let’s say we have an input field named title.

```php
<input id="title" type="text" name="title">
```

You can sanitize the input data with the [sanitize_text_field()](https://developer.wordpress.org/reference/functions/sanitize_text_field/) function:

```php
$title = sanitize_text_field($_POST['title']);
update_post_meta($post->ID, 'title', $title);
```

Behind the scenes, [sanitize_text_field()](https://developer.wordpress.org/reference/functions/sanitize_text_field/) does the following:

- Checks for invalid UTF-8
- Converts single less-than characters (<) to entity
- Strips all tags
- Removes line breaks, tabs and extra white space
- Strips octets

 