# Nonces

[toc]

Nonces are generated numbers used to verify origin and intent of requests for security purposes. Each nonce can only be used once.

If your plugin allows users to submit data; be it on the Admin or the Public side; you have to make sure that the user is who they say they are and that they [have the necessary capability](https://developer.wordpress.org/plugins/security/checking-user-capabilities/) to perform the action. Doing both in tandem means that data is only changing when the user *expects* it to be changing.

## Using Nonces

Following our [checking user capabilities example](https://developer.wordpress.org/plugins/security/checking-user-capabilities/#restricted-to-a-specific-capability), the next step in user data submission security is using nonces.

The capability check ensures that only users who have permission to delete a post are able to delete a post. But what if someone were to trick you into clicking that link? You have the necessary capability, so you could unwittingly delete a post.

Nonces can be used to check that the current user actually intends to perform the action.

When you generate the delete link, you’ll want to use [wp_create_nonce()](https://developer.wordpress.org/reference/functions/wp_create_nonce/) function to add a nonce to the link, the argument passed to the function ensures that the nonce being created is unique to that particular action.

Then, when you’re processing a request to delete a link, you can check that the nonce is what you expect it to be.

For more information, Mark Jaquith’s [post on WordPress nonces](http://markjaquith.wordpress.com/2006/06/02/wordpress-203-nonces/) is a great resource.

[Top ↑](https://developer.wordpress.org/plugins/security/nonces/#top)

## Complete Example 
Complete example using capability checks, data validation, secure input, secure output and nonces:

```php
<?php
/**
 * generate a Delete link based on the homepage url
 */
function wporg_generate_delete_link($content)
{
    // run only for single post page
    if (is_single() && in_the_loop() && is_main_query()) {
        // add query arguments: action, post, nonce
        $url = add_query_arg(
            [
                'action' => 'wporg_frontend_delete',
                'post'   => get_the_ID(),
                'nonce'  => wp_create_nonce('wporg_frontend_delete'),
            ],
            home_url()
        );
        return $content . ' <a href="' . esc_url($url) . '">' . esc_html__('Delete Post', 'wporg') . '</a>';
    }
    return null;
}
 
/**
 * request handler
 */
function wporg_delete_post()
{
    if (
        isset($_GET['action']) &&
        isset($_GET['nonce']) &&
        $_GET['action'] === 'wporg_frontend_delete' &&
        wp_verify_nonce($_GET['nonce'], 'wporg_frontend_delete')
    ) {
 
        // verify we have a post id
        $post_id = (isset($_GET['post'])) ? ($_GET['post']) : (null);
 
        // verify there is a post with such a number
        $post = get_post((int)$post_id);
        if (empty($post)) {
            return;
        }
 
        // delete the post
        wp_trash_post($post_id);
 
        // redirect to admin page
        $redirect = admin_url('edit.php');
        wp_safe_redirect($redirect);
 
        // we are done
        die;
    }
}
 
if (current_user_can('edit_others_posts')) {
    /**
     * add the delete link to the end of the post content
     */
    add_filter('the_content', 'wporg_generate_delete_link');
 
    /**
     * register our request handler with the init hook
     */
    add_action('init', 'wporg_delete_post');
}
```