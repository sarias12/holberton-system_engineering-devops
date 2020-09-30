#!/usr/bin/env bash
#Find the issue (Syntax error in file wp-settings.php), fix it and then automate it using Puppet.
exec { 'Fix Wordpress wp-settings.php':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
