# Privacy Related Options, Hooks and Capabilities

[toc]


## Options 

`wp_page_for_privacy_policy` – contains the page ID of a site’s privacy page

[Top ↑](https://developer.wordpress.org/plugins/privacy/privacy-related-options-hooks-and-capabilities/#top)

## Actions 

`user_request_action_confirmed` – fired when a user confirms a privacy request

`wp_privacy_delete_old_export_files` – a scheduled action used to prune old exports from the personal data exports folder

`wp_privacy_personal_data_erased` – fired after the last page of the last eraser is complete

`wp_privacy_personal_data_export_file` – used to create a personal data export file as part of the export flow

`wp_privacy_personal_data_export_file_created` – fires after a personal data export file has been created

[Top ↑](https://developer.wordpress.org/plugins/privacy/privacy-related-options-hooks-and-capabilities/#top)

## Filters 

`user_request_action_confirmed_message` – allows modifying the action confirmation message displayed to the user

`wp_privacy_export_expiration` – controls how old export files are allowed to get, default is 3 days

`wp_privacy_personal_data_email_content` – allows modifying the email message send to users with their personal data export file link

`wp_privacy_personal_data_erasers` – supports registration of core and plugin personal data erasers

`wp_privacy_personal_data_exporters` – supports registration of core and plugin personal data exporters

[Top ↑](https://developer.wordpress.org/plugins/privacy/privacy-related-options-hooks-and-capabilities/#top)

## Capabilities

Access to the privacy tools is controlled by a few new capabilities. These capabilities are:

`erase_others_personal_data` – determines if the Erase Personal Data sub-menu is available under Tools

`export_others_personal_data` – determines if the Export Personal Data sub-menu is available under Tools

`manage_privacy_options` – determines if the Privacy sub-menu is available under Settings

Administrators (on non-multisite installations) have these capabilities by default.