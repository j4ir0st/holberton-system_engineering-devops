# Using Puppet, install puppet-lint
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/',
}