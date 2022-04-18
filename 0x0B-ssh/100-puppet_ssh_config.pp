# create a file in /.ssh
file { '/etc/ssh/ssh_config':
  ensure  => present,
}

file_line { 'add line':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^IdentityFile.*$',
}

file_line { 'add 2nd line':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^PasswordAuthentication.*$',
}
