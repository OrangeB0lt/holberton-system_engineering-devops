# puppet makes .php file to fix bug for WordPress Instance
#
exec { 'modify /var/www/html/wp-settings.php file':
  cwd     => '/var/www/html',
  command => 'sed -i -e \'s/class-wp-locale.phpp/class-wp-locale.php/g\' \
wp-settings.php && /etc/init.d/apache2 restart',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
