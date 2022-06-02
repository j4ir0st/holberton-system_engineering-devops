# Web stack debugging 3 - fixing with strace
exec {'web_debugging3':
  provider => shell,
  command  => 'sudo sed -i "s/.phpp /.php /" /var/www/html/wp-settings.php;\
  	       sudo service apache2 restart',
}