# Web stack debugging 3 - fixing with strace
exec {'web_debugging3':
  provider => shell,
  command  => 'sudo sed -i \
  	      "s/require_once( ABSPATH . WPINC . \'\/class-wp-locale\.phpp\' );/require_once( ABSPATH . WPINC . \'\/class-wp-locale.php\' );/"\
  	       /var/www/html/wp-settings.php;\
               sudo service apache2 restart',
}