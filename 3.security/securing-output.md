# Securing Output

[toc]
Securing output is the process of escaping output data.

Escaping means stripping out unwanted data, like malformed HTML or script tags.

**Whenever you’re rendering data, make sure to properly escape it. Escaping output prevents XSS (Cross-site scripting) attacks.**

---
**Note:**
> > [Cross-site scripting (XSS)](https://en.wikipedia.org/wiki/Cross-site_scripting) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy.
---

## Escaping 

Escaping helps securing your data prior to rendering it for the end user. WordPress has a few helper functions you can use for most common scenarios.

- [esc_html()](https://developer.wordpress.org/reference/functions/esc_html/) – Use this function anytime an HTML element encloses a section of data being displayed.
- [esc_url()](https://developer.wordpress.org/reference/functions/esc_url/) – Use this function on all URLs, including those in the `src` and `href` attributes of an HTML element.
- `esc_js()`– Use this function for inline Javascript.
- [esc_attr()](https://developer.wordpress.org/reference/functions/esc_attr/) – Use this function on everything else that’s printed into an HTML element’s attribute.

---
> **Alert:** Most WordPress functions properly prepare data for output, so you don’t need to escape the data again. For example, you can safely call [the_title()](https://developer.wordpress.org/reference/functions/the_title/) without escaping.
---

[Top ↑](https://developer.wordpress.org/plugins/security/securing-output/#top)

## Escaping with Localization 

Rather than using `echo` to output data, it’s common to use the WordPress localization functions, such as [_e()](https://developer.wordpress.org/reference/functions/_e/) or [__()](https://developer.wordpress.org/reference/functions/__/).

These functions simply wrap a localization function inside an escaping function:

```php
esc_html_e( 'Hello World', 'text_domain' );
// same as
echo esc_html( __( 'Hello World', 'text_domain' ) );
```

These helper functions combine localization and escaping:

- [esc_html__()](https://developer.wordpress.org/reference/functions/esc_html__/)
- [esc_html_e()](https://developer.wordpress.org/reference/functions/esc_html_e/)
- [esc_html_x()](https://developer.wordpress.org/reference/functions/esc_html_x/)
- [esc_attr__()](https://developer.wordpress.org/reference/functions/esc_attr__/)
- [esc_attr_e()](https://developer.wordpress.org/reference/functions/esc_attr_e/)
- [esc_attr_x()](https://developer.wordpress.org/reference/functions/esc_attr_x/)

[Top ↑](https://developer.wordpress.org/plugins/security/securing-output/#top)

## Custom Escaping 

In the case that you need to escape your output in a specific way, the function [wp_kses()](https://developer.wordpress.org/reference/functions/wp_kses/) (pronounced “kisses”) will come in handy.

This function makes sure that only the specified HTML elements, attributes, and attribute values will occur in your output, and normalizes HTML entities.

```php
$allowed_html = [
'a'      => [
'href'  => [],
'title' => [],
],
'br'     => [],
'em'     => [],
'strong' => [],
];
echo wp_kses( $custom_content, $allowed_html );
```

wp_kses_post() is a wrapper function for wp_kses where $allowed_html is a set of rules used by post content.

```php
echo wp_kses_post( $post_content );
```
