# Web stack debugging #4
exec {'web_debug4':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 500\"/"\
  	       /etc/default/nginx ;\
               sudo service nginx restart',
}