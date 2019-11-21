# Cron

[toc]


## What is WP-Cron 

Cron is the time-based task scheduling system that is available on UNIX systems. WP-Cron is how WordPress handles scheduling time-based tasks in WordPress. Several WordPress core features, such as checking for updates and publishing scheduled post, utilize WP-Cron.

WP-Cron works by: on every page load, a list of scheduled tasks is checked to see what needs to be run. Any tasks scheduled to be run will be run during that page load. WP-Cron does not run constantly as the system cron does; it is only triggered on page load. Scheduling errors could occur if you schedule a task for 2:00PM and no page loads occur until 5:00PM.

[Top ↑](https://developer.wordpress.org/plugins/cron/#top)

## Why use WP-Cron

Why use WP-Cron? Many hosting services are shared and do not provide access to the system cron but WordPress core and many plugins do need a cron system to perform time based tasks. Cron is a useful tool, thus the beginnings of WP-Cron. Though it may not run at a specific time, WP-Cron will get your tasks done in a timely manner. Using the WordPress API is a simpler method to setting up cron tasks than going outside of WordPress.

With a system cron if the time passes and the task did not run it is lost and will never run. WP-Cron will run tasks regardless of how old they are. Tasks will sit in a queue until a page is loaded to trigger them, thus no task will ever be lost.