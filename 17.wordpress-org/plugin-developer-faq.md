# Plugin Developer FAQ

[toc]


There are lot of ins and outs to hosting WordPress plugins. Please take a minute to see if your question is answered here before reaching out for assistance.

> Note: Last Updated: 1 July 2019
>

## How do I contact the Plugin Review team? 

You can contact us by email at `plugins@wordpress.org` – we reply to all emails within 7 business days.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## Submissions and Reviews 

### Where do I submit my plugin? 

Go to the [Add](https://wordpress.org/plugins/developers/add/) page and upload your zip. Your file should be under **10 megs** and be a complete plugin. We do not accept placeholders or plugins that aren’t ready to be used.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What happens after submission? 

You will get an automated email telling you about the submission immediately. At that point, someone will manually download and review your code. If we find no issues with the security, documentation, or presentation, your plugin will be approved. If we determine there are issues, you will receive a second email with details explaining what needs to be fixed.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What will my plugin URL be? 

When you submit a plugin, you get an automated email telling you what the slug will be. This is populated based on the value of Plugin Name in your main plugin file (the one with the plugin headers). If you set yours as `Plugin Name: Boaty McBoatface` then your URL will be `wordpress.org/plugins/boaty-mcboatface` and your slug will be `boaty-mcboatface` for example. If there is an existing plugin with your name, then you’ll get a warning on submission.

This is *also* the folder name (in SVN and installed on WordPress) for your plugin and your text-domain, so pay attention carefully.

Once your plugin is approved, this name **cannot** be renamed. Please chose wisely.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why did I get a different slug than I was told? 

Sometimes we notice typos and fix them for you. Other times, the name you chose has an obvious issue and cannot be used. For example, if you submit “WooCommerce Tango Salsa Add-on” that would make your slug `woocommerce-tango-salsa-add-on` by default. If you don’t work for WooCommerce, we would just change that to `woo-tango-salsa-add-on` for you. If, however, your zip was named `woo-tango-salsa`,  or you use a textdomain or class name with an intentional spelling, then we’d likely use that.

Basically we’ll fix the stuff we know is wrong for you, and if we’re ever not sure, we’ll email you and ask. For the obvious errors, or ones we’re required to make, we will fix that or you.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I submit an official plugin? 

Log in as the official company user account and submit with that account *only*. We cannot accept plugins submitted by individual developer accounts, unless they’re clearly company ones as well. For example, submitting your official Facerange plugin with a user that has a gmail address is likely to be flagged for trademark infringement.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What if I submitted the plugin with the wrong user ID?

Just reply to the email right away and let us know. We can transfer ownership for you. If you forget to do this, you can fix it yourself by [adding the correct account as a committer](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#how-do-i-give-someone-else-access-to-my-plugin) and then having that account remove your own.

**DO NOT** resubmit your plugin. Just tell us right away and we’ll fix it.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How long does it take to get a plugin approved? 

There’s no official average, as no two plugins are the same. If your plugin is small and all the code is correct, it should be approved within **fourteen** days. If your plugin has any code issues, it will take as long as it takes for you to correct the issues. Either way, you *will* get an email from `plugins@wordpress.org` with the status, so please add that to your email whitelist and patiently wait for our response.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### If my plugin has a problem, how long do I have to fix it? 

There’s no timeline and as long as we know you’re working on it and we feel you’re making progress, we’ll leave the review open.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why was my plugin rejected after six months? 

If you **never** reply to our review within 6 months, we may reject it, in order to keep the pending queue under 700. If you’ve replied, even once, even to tell us you’re working on the code, we won’t reject until another 6 months has passed without reply, or your email bounces.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### I finally fixed my plugin. Should I resubmit? 

No. Reply to the email. Even if it’s been a year and a half. The longest time to date has been 3 years. We don’t mind if it takes a while.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How many plugins can I submit for review at a time? 

Just one.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why can’t I submit more than one plugin at a time? 

Allowing people to have multiple submissions at once was proven to be detrimental to the review process. Errors were regularly found in all the plugins, resulting in the same emails being sent multiple times. In addition, people often got confused as to which review they were working on, muddying the waters about what needed to be solved. By changing this to one-at-a-time, confusion in those matters dropped significantly.

In addition, many new users don’t know how to use SVN, and wound up submitting multiple plugins and never using any. That can be a drain on our resources, so we do limit people.

Since all plugins get an initial review within two weeks, this should not be a hardship.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I submit multiple plugins with multiple accounts?

No. And if you do so, we will suspend all your secondary accounts. Don’t try to get around the one-at-a-time rule please.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### I need my plugin approved by a specific date, what should I do? 

Submit it as early as possible. Unless the plugin is meant to address a security or legal issue, we don’t permit queue jumping. If it *is* related to one of those, please email `plugins@wordpress.org` and explain the situation.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Are there specific things that I should avoid doing?

We look for some pretty obvious things, all of which are listed [in our guidelines](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/). Most can be summed up as “Don’t be a spammer,” but to touch on the ones people do the most:

- Not including a `readme.txt` file when acting as a service
- Not testing the plugin with `WP_DEBUG`
- Including custom versions of packaged JavaScript libraries
- Calling external files unnecessarily
- “Powered By” links
- Phoning home

Again, this is a brief overview. Please read the guidelines, as the full list is quite detailed.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Are there plugins you don’t accept?

We don’t accept plugins that do ‘nothing,’ are illegal, or encourage bad behavior. This includes black hat SEO spamming, content spinners, hate-plugins, and so on.

Similarly we do not accept framework plugins or library plugins. If your plugin has to require other plugins or themes to edit themselves in order to use your plugin, it’s a library. If your plugin is a template from which more code can be built by customizing the files directly, it’s a framework or boilerplate. Frameworks and libraries should be packaged with each plugin (hopefully in a way that doesn’t conflict with other plugins using the framework or libraries). At least until core supports plugin dependencies.

We also don’t accept 100% copies of other people’s work or plugins that duplicate functionality found in WordPress Core. Basically, your plugin should do something new, or in a new way, or solve a specific issue.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### I want to redo, upgrade, or rebrand my existing plugin. I just submit again, right? 

No. Instead, you should rewrite the existing plugin. Make it a major version release. We can’t rename plugins or transfer users, so a new one wouldn’t carry over any existing users, reviews, support topics, ratings, downloads, favorites, etc. Basically you’d leave *all* your current users out in the cold, and that’s mean.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### I made a mistake with my submission. How can I fix it? 

Every submission gets an automated reply with directions. Reply to that or email `plugins@wordpress.org` and explain the situation.

We can correct plugin slugs before approval, so we are often able to fix that for you. If not, we’ll let you know what to do. We try to catch typos in names before we approve anything, but we make mistakes too.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Are there things I can’t do in a plugin name? 

We have the following restrictions:

- Plugins may not use vulgarities in the name or slug
- Plugins may not use ‘WordPress’ or ‘Plugin’ in their slugs except under extreme situations
- Plugins may not use version numbers in plugin slugs
- Due to system limitations, only English letters and Arabic numbers are permitted in the slug
- Plugins may not **start** with a trademarked term or name of a specific project/library/tool *unless* submitted by an official representative

We encourage everyone to be creative and come up with unique slugs. We automatically correct any plugin that has an unacceptable slug. If there’s a question as to the best choice, we will contact you to be sure.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## Using The SVN Repository

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Where do I put my files? 

Put your code files directly in the `trunk/` directory of your repository. Whenever you release a new version, [tag that release](https://developer.wordpress.org/plugins/wordpress-org/how-to-use-subversion/#task-3) by copying the current trunk revision to a new subdirectory of the `tags/` directory.

Make sure you update [`trunk/readme.txt`](https://wordpress.org/plugins/developers/#readme) to reflect the new stable tag.

Images for the readme (such as [screenshots, plugin headers, and plugin icons](https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/)), belong in the `assets/` directory (which you may need to create) in the root of your SVN checkout. This will be on the same level as `tags/` and `trunk/`, for example.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I put my files in a subdirectory of `trunk/`? 

No. Doing that will cause the zip generator to break.

If you have complicated plugin with lots of files, you can of course organize them into subdirectories, but the [readme.txt file](https://wordpress.org/plugins/developers/#readme) and the root plugin file should go straight into `trunk/`.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How should I name my tags (a.k.a. releases)? 

Your Subversion tags should look like version numbers. Specifically, they should only contain **numbers and periods**. `2.8.4` is a good lookin’ tag, `my neato releaso` is a bad lookin’ tag. We recommend you use [Semantic Versioning](http://semver.org/) to keep track of releases, but we do not enforce this.

Note that we’re talking about *Subversion* tags here, not readme.txt search type tags.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How many old releases should I keep in SVN? 

As few as possible. Very rarely does anyone need your old code in the release repository. Remember, SVN is **not** meant for your code versioning. You can use Github for stuff like that. SVN should have your current release versions, but you don’t need all the minor releases to all the previous versions. Just the last one or two for them is good.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I include SVN externals in my plugin? 

No. You can add [svn externals](http://svnbook.red-bean.com/en/1.0/ch07s03.html) to your repository, but they won’t get added to the downloadable zip file.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I put zips and other compressed files in my plugin?

No.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## Your WordPress.Org Page 

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### When does my plugin go ‘live’?

As soon as you push code to the SVN folders, your plugin will be live. **DO NOT** push code if you’re not ready, as there’s no ‘off’ switch except to [close the plugin](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#closed-plugins). As closing a plugin is permanent, we recommend you not push code until you’re read to go live.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Where does the WordPress.org Plugin Directory get its data?

From the information you specify in the plugin file and in the [readme.txt file](https://wordpress.org/plugins/developers/#readme), and from the Subversion repository itself. Read [about how the readme.txt works](https://developer.wordpress.org/plugins/wordpress-org/how-your-readme-txt-works/) for more information.

You should also make full use of the [Plugin Headers](https://developer.wordpress.org/plugins/the-basics/header-requirements/) in your main plugin file. Those will define how your username shows up on the WordPress.org hosting page, as well as in the WordPress Admin. We recommend using all those headers to fully document your plugin.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I specify what version of my plugin the WordPress.org Plugin Directory should use? 

Yes, by specifying the `Stable Tag` field in your trunk directory’s [readme.txt file](https://wordpress.org/plugins/developers/#readme).

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What version of WordPress should the “Tested Up To” value be? 

Logically, whatever version you tested up to. However, never go above the current release candidate. If there is none, don’t go above the active version. So if WordPress’ stable release is 6.0.9, you can use 6.0 to 6.0.9 and everything will be fine. If there is a release of 6.1-RC then you may use 6.1, however you can go no higher. Do not attempt to be clever and use 6.5 or 7. This will result in errors on your page.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What should be in my changelog? 

A changelog is a log or record of all or all notable changes made to your plugin, including records of changes such as bug fixes, new features, etc. If you need help formatting your changelogs, we recommend [Keep A Changelog](http://keepachangelog.com/) as  that’s the format used by many products out there.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How many versions should I keep in my changelog? 

Always keep the current major release in your change log. For example, if your current version is 3.9.1, you’ll want that and 3.9 in the change log. Older versions should be removed and migrated to a `changelog.txt` file. That will allow them to be accessible to users, while keeping your readme shorter and more pertinent. At most, keep the most recent version of your plugin and one major version back in your readme’s changelog. Your `changelog.txt` will **not** be visible within the WordPress.org Plugin Directory, but that’s okay. Most users just want to know what’s new.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I include videos on plugin description pages? 

For YouTube and Vimeo videos, simply paste the video link on a line by itself in your description. Note that the video must be set to allow embedding for the embed process to work. For videos hosted by the WordPress.com VideoPress service, use the `[wpvideo]` shortcode. Shortcodes can also be used for YouTube and Vimeo, if needed, just like in WordPress.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why does my plugin say it’s not been tested with the most recent WordPress versions?

That happens when you neglected to use a proper ‘Tested Up To’ value in your header. That value should be the latest version of WordPress that you’ve tested your plugin against. If the latest WordPress version is 4.9.1, then you should have the value `4.9.1` to indicate compatibility. Keep in mind, if you put in non-released versions of WordPress (like 6.0) you’ll see the same message.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How long does it take for the Plugin Directory to reflect my changes? 

The WordPress.org Plugin Directory updates every few minutes. However, it may take longer for your changes to appear depending on the size of the update queue. Please give it at least **6 hours** before contacting us.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I make one of those cool banners for my plugin page? 

You can make your own [plugin headers](https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/#plugin-headers) by uploading the correctly named files into the `assets` folder. Read [about plugin headers](https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/#plugin-headers) for more information.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I make a plugin icon?

You can make your own [plugin icons](https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/#plugin-icons) by uploading the correctly named files into the `assets` folder. Read [about plugin icons](https://developer.wordpress.org/plugins/wordpress-org/plugin-assets/#plugin-icons) for more information.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I use official logos in my plugin? 

Usually no.

Your plugin icon should *never* be the unaltered, official logo of, say, Facerange. That would be infringing on their property. You can use an **edited** one in your header, or the official one in the plugin code itself, but don’t use their logos for your branding here. Even if you have permission to do so on your site, *we* don’t have that permission here.

Much like your plugin name, we recommend your icons and headers be something unique to you. They tend to be more memorable that way.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How many tags can I use in my readme? 

Per the guidelines, [plugins are limited to 12 tags in their readme](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/#12-public-facing-pages-on-wordpress-org-readmes-must-not-spam). This is to control spam. That said, only the first **FIVE** tags will display on WordPress.org, much for the same reason. The first 12 tags are used for searches, and the rest are ignored, so tag-stuffing won’t help you at all.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## Plugin Names 

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I change my plugin’s name after it’s approved?

Yes and no. You can change the display name, but the *slug* — that part of the plugin URL that is yours — cannot be changed once a plugin is approved. That’s why we warn you, multiple times, upon submission.

To change the display name, edit your main plugin file and change the value of “Plugin Name:” to the new name. You may also want to edit your header in your readme.txt

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why can’t I use someone’s trademark/brand as my plugin name?

Simply put, because you’re not them.

If you have written an add-on plugin for BooCommerce, you may not name it “BooCommerce Improved Product Search” as that would generate the slug `boocommerce-improved-product-search` and that would conflict with the trademark of ‘BooCommerce.’ That said, it would be acceptable to submit the name “Boo Improved Product Search” which would use the slug `boo-improved-product-search` (“boo” not being trademarked you see).

As another example, if you have a plugin that integrates a service with a a popular cloud hosting company named Amazorn, you may call it “My Service Integration for Amazorn”, but you may **not** use “Amazorn – My Service Integration”. 

Consider the real life example of Keurig. If you made an eco-friendly brew cup, you could market it “EcoBrew Pod for Keurig” but you could NOT attempt to market it as “Keurig EcoBrew Pod.” The latter implies a direct relationship to Keurig and is actually against the law in some countries. In order to protect you, we need you to tread lightly with recognized brand names and trademarks. Always err on the side of caution; if they come and tell us to close your plugin because you used their term as the *first* word in the display name, we have to do it.

*Note: While `woo` is a registered trademark of WooCommerce, we have been permitted to allow plugins to use that as the first term in their slug for sanity reasons. If you’re at all concerned, we recommend using `wc-`instead.*

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I change my plugin’s URL/slug? 

It’s impossible to change a plugin’s URL once it’s approved and, because of that, we deny most requests for ‘new’ plugins to replace old ones, just to get a better slug.

This is because we cannot migrate users between plugins nor can we redirect traffic. This means that submitted a new plugin to change a slug is incredibly detrimental to the plugin’s SEO and reputation, as users will be abandoned. The majority of plugins don’t actually need a new URL, and instead just want to edit their display name.

Unless there’s an egregious typo, language, or legal issue related to your slug, we are **unlikely** to approve a new slug. If we do, we will flag your account to note that future rename requests are to be denied.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I change my plugin’s display name?

You’ll need to change it in the readme *and* the plugin main file.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I make my display name anything? 

Don’t use vulgarities or slurs or other intentionally abusive language. You cannot claim, or appear to claim, to be an official source if you’re not. For example, if you’ve made a plugin that connects to the Frozbaz Service, you should call your plugin “Connector to Frozbaz Service” – in this way, you have made it clear you are making a plugin for a service, rather than being the service.

If you’re combining multiple services (a payment gateway to a popular ecommerce plugin, for example), we strongly recommend you come up with an original, unique, display name.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I use WordPress or Plugin in my display name? 

Yes, but we’d rather you didn’t. It’s incredibly redundant and doesn’t actually help your SEO in any way, shape, or form. We already put WordPress *and* Plugin in your page title.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Should I use the trademark or registered symbol in my plugin name?

Assuming you actually did apply for trademarks, you certainly *can* but it’s not commonly done. Not even Google or Facebook do that. Simply by using your trademark term and having a log of it (like your SVN log), you have usually done the needed legal action required to protect your brand. Consult a lawyer for details.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## Search

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How long will it take for my plugin to show up in search? 

Usually 6 to 14 days after a plugin is committed to SVN. This is because we have to add your data, parse it, and share it to all of our *heavily* cached servers. It’s not instantaneous. Also as a new plugin, we have no data on usage, so you may need to wait a bit.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I rank higher? 

Write a good readme for the language, answer support posts promptly, get good reviews.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What’s weighted more, my URL or my display name?

Neither. Make your display name memorable and descriptive, while keeping it under 5 words, for maximum benefit.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## The Support Forums 

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I get notified for forums posts? 

Go to `https://wordpress.org/support/plugin/YOURPLUGIN` and scroll down to the bottom of the list of posts. There you will see an option for the RSS link, as well as a sign up for emails.

[![Signup links for email/rss ](https://developer.wordpress.org/files/2015/04/Screen-Shot-2016-06-20-at-9.58.21-AM.png)](https://developer.wordpress.org/files/2015/04/Screen-Shot-2016-06-20-at-9.58.21-AM.png)

Click the subscribe link for emails, or use the RSS link in your favorite reader.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I get notified for all my plugins? 

If you’re tracking the WordPress forums, `https://wordpress.org/support/view/plugin-committer/YOURID` will list all of the support requests and reviews for any plugin you have commit access.

Not a comitter, just someone listed as an author? Use `https://wordpress.org/support/view/plugin-contributor/YOURID`

Those are RSS only. If you need email, go to `https://profiles.wordpress.org/YOURID/profile/notifications/` and put in the terms you want to be emailed for.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I give a support account access to my plugin? 

You can add Support Representatives to your plugin. Support representatives can mark forum topics as resolved or sticky (same as plugin authors and contributors), but don’t have commit access to the plugin.

The UI for managing plugin support reps can be found in Advanced View on the plugin page, next to managing committers. Once someone is added as a support rep, they will get a Plugin Support badge when replying to the plugin support topics or reviews.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Will you delete bad reviews or comments on my plugin?

Generally no. A review is a reflection of an individual’s experience with your product. If they didn’t like it, that’s not for us to change. If you feel that a review is invalid (such as for a different plugin), use the `modlook` button on the post. A member of the **forums** team will investigate. Abuse of Modlook may result in suspension of your plugins. Please, use it wisely.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What is ‘Sockpuppeting’? 

That’s what happens when someone makes multiple accounts on the forums, usually to give themselves a number of 5-star reviews, or create fake support tickets to appear more responsive. Sockpuppeting is against our guidelines and will result in the reviews and posts being removed, but also may result in your account and all plugins being removed. Don’t do it and don’t flagrantly accuse others of doing it.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## Closed Plugins 

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I close my plugin? 

If you ask for your plugin to be removed, you will not get it back unless you can justify your situation. Closing a plugin by request is intended to be **permanent**.

Email `plugins@wordpress.org` from an account with commit access and link to your plugin. If your email does not match someone with commit access to the plugin, you will be asked to send from a different email.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What happens when a plugin is closed? 

When a plugin is closed, the page shows as closed and the zips are no longer generated. No one will be able to download the plugin via the website, nor will they be able to install it via the WordPress admin. The SVN repository will remain accessible to allow others to download and fork the code if desired, per the tenets of the directory. After 60 days, the closure message will change to alert people as to *why* it was closed.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why was my plugin closed? 

Plugins are closed for guideline violations, security issues, or by author requests. In the case of active issues (such as copyright infringement, abuse, and security), all accounts with commit access to a plugin are notified. If a plugin has never been used within 6 months (i.e. no code has been pushed to SVN), SVN is broken for upwards of 12 months, or a plugin’s readme indicates it’s deprecated, we may close without notification.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why was someone else’s plugin closed? 

As of 2017, plugin closure reasons are tracked in the plugin database. Sixty days after a plugin is closed, the reason for the closure will be made public:

![Example of a closed plugin with the reason 'Author Request'](https://developer.wordpress.org/files/2015/04/not-hello-dolly.jpg)

Please note: We do not publicly disclose the details on exactly why a plugin has been closed.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Can I get someone else’s plugin closed? 

If you report an [security issue](https://developer.wordpress.org/plugins/wordpress-org/plugin-security/reporting-plugin-security-issues/) or a [guideline violation](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/) in a plugin to `plugins@wordpress.org`, we will review and take appropriate action. Most of the time, this involves closing a plugin. Your name will not be disclosed unless you ask for it to be so, in order to protect you from backlash.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Someone posted a copy of my plugin! What do I do? 

Email `plugins@wordpress.org` with a link to the stolen plugin. Include either a link to where we can download yours or attach the zip. We will compare the two files, as well as all the coding history we have, to determine if the plugin is, indeed, theft, or just an uncredited fork. Please keep in mind, if you licensed your plugin as GPLv2 or later, then it’s perfectly permissible to fork your work, as long as copyright remains intact and you’re credited.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Will you close another plugin for violating my brand/trademark? 

We do our best to uphold copyright and trademark requirements, as well as prevent brand confusion. Before plugin are approved, we often require them to make some of the more obvious changes. That said, there is a limit to how ‘different’ a URL or name can be when we have 60,000 plugins in the directory, and when some terms are quite common (like ‘popup’ or ‘all-in-one’). Because of that, we require developers to change the plugin’s **display name** to no longer cause conflict or confusion.

If someone is clearly infringing on your copyright or trademark or existing brand, be it by display name or use of trademarked images, please email us at `plugins@wordpress.org` with some proof and we will contact the developer and require changes.

We do expect these to be *reasonable* requests. That is, if you send us a complaint and list 12 plugins that all use the term ‘best contact form’ because that’s your plugin name, we will review the plugins and only close them if they’re using the phrase excessively. If they use it once (i.e. “This is the best contact form plugin in the Faroe Islands”) then it’s acceptable. If they’re keyword stuffing the phrase, we’re more likely to close them for keyword stuffing. Simply, if your plugin name is super generic, this is going to happen, and it’s usually **not** an infringement case.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How can I send a security report? 

Email `plugins@wordpress.org` a clear and concise description of the issue. Make sure to explain how you verified this is an exploit (links to the plugin listing on sites like secunia.com are perfect). If you provide a link to your report, DO NOT delete it! We will passed it on directly to the developers of the plugin.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Do you provide bounties for finding bugs in a plugin? 

No. We have no relationship with any bug bounty programs, so we don’t file your reports etc to them. The only one with which we work is [hackerone.com/automattic](https://hackerone.com/automattic) and that’s for bugs related to Automattic properties. Everything else is on your own, don’t ask us to submit things.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Do you help file or provide CVEs? 

No. We do not have the ability to assist with CVEs.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### My plugin was closed, can I reopen it? 

Maybe. If it was closed for a security reason, fix the issue, reply to the email, and most of the time we’ll reopen the plugin unless it has more security issues or severe guideline issues. If it was closed for guideline violations, it depends on the severity and nature of the violation. Repeat offenders are less likely to have a plugin reopened, for example, than first-timers.

If you asked for the plugin to be closed, you will be expected to explain why the change of heart. Plugins are intended to remain closed when a developer requests it, and not reopened again a month later.

Note: *All* plugins must pass a current standards and security review in order to be restored. This is not optional. Users will lose more faith in you for having your plugin closed multiple times than they would for one longer closure where you address all the potential issues.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Why was my plugin closed when it was my employee/co-worker who violated guidelines? 

Everyone who represents a plugin, from support tech to developer, is the responsibility of the plugin owner. If they violate the guidelines egregiously, then the owners are expected to accept those consequences. We notify the plugin owners in these cases and explain why.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### *All* my plugins were closed! How can I get them back?

It’s exceptionally rare that we close all of a developer’s plugins. In general it happens because of the following:

1. You asked us to close all your plugins
2. Email issues
   1. The email bounced and we were unable to get in touch
   2. The email sent us auto-replies and we’d warned at least twice to fix that
3. Guideline issues
   1. Previous censuring for behaviour and/or a final warning was issued
   2. Delivering legal threats to the directory and/or the volunteers
   3. The violation was deemed ‘egregious’ (death threats, hundreds of sock puppets, harassment, etc)

If you asked us to close them, you have to explain *why* the change of heart.

If you’re having email issues, you have to resolve them.

As for that last one… Generally you don’t get to come back from that. If we deliver you a final warning for your behaviour and, within less than a year, you start up again with the issues (or fail to resolve all the issues we mentioned), we’re not going to reopen your plugins.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### I just got a final warning. What do I do? 

First and foremost, take it seriously. The email will list exactly what the problems have been and why we’ve chosen to escalate to a final warning. Plugin Owners are expected to resolve all the issues, to cease causing new guideline violations, and to closely monitor the actions of any coworkers. In short, stop breaking the guidelines, stop making excuses, apologize for any misbehaviour, and correct course.

The last thing we want to do is ban someone and disable all their plugins. It’s not healthy for the community. At the same time, if a developer is unable or unwilling to play by the same rules as everyone else, it’s detrimental to keep then in the directory and disrespectful to everyone else.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

## Plugin Ownership 

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I give someone else access to my plugin? 

To add users as committers, that is give them access to update code, go to `https://wordpress.org/plugins/YOURPLUGIN/advanced` and add their username in as a committer.

To have them show up as an author, add their username to the `readme.txt` file.

*Do not add regular users as authors.* It’s meant for people who help with development only.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How do I remove someone’s access from my plugin? 

Anyone with commit access can do this. Go to `https://wordpress.org/plugins/YOURPLUGIN/advanced` and hover over their ID. A delete link will appear. Click on it.

Please don’t delete yourself.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### How can I take over an abandoned plugin? 

[We permit users to adopt existing plugins that are no longer currently developed](https://developer.wordpress.org/plugins/wordpress-org/take-over-an-existing-plugin/).

We ask you try to connect with the original developers first, so they can add you. In some case, that’s not possible and you should start with fixing the plugin. Make sure it meets coding standards, is secure, and update the copyright information to include yourself. Then you can contact us regarding [plugin adoption](https://developer.wordpress.org/plugins/wordpress-org/take-over-an-existing-plugin/).

We offer **no** guarantee that you will be given anyone’s plugin.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### Are these offers to buy my plugin legit? 

Short answer: Probably not.

Many developers receive unsolicited emails or offers to purchase their plugin. We have found the vast majority of these to be fraudulent and do *not* recommend you follow up with them.

While legitimate offers do come, they’re usually from the official company to whom a plugin is related, or from a well established plugin company. The ones that start “We’re reaching out to the WordPress community …” or “We are looking to acquire existing WordPress plugins …” should not be trusted. Such purchases have often destroyed the reputation of the plugin (and the original developer) by engaging in sleazy tactics such as tracking users or other serious guideline violations.

If you do choose to sell your plugin (or give it away to someone else), please make sure the new owners understand all the [guidelines of the repository](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/). Should they violate our terms the plugin will be removed, and we may not give it back depending on the level of the violation. Whomever has commit access to a plugin has the ownership and responsibility of it’s behavior for users. Spamming, inserting tracking data, and adding junk features are the fastest way to ruin your plugin.

We advocate only giving your plugin to people you *personally* have vetted, and that you trust with being responsible with your code and your users.

[Top ↑](https://developer.wordpress.org/plugins/wordpress-org/plugin-developer-faq/#top)

### What happens when a plugin developer dies? 

When a developer is determined to have died, they are removed from their own plugins in order to prevent the unethical from gaining access and harming users. If they are the only developer, the plugin may be closed. All attempts are made to find their friends and coworkers, to offer them a chance to adopt the code first, but if no one reliable or willing can be found the plugin is closed.

 