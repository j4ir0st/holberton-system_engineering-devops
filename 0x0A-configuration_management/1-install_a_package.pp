# Using Puppet, install puppet-lint
exec { 'install_flask':
  command  => 'sudo pip3 install Flask==2.1.0',
  provider => 'shell',
}