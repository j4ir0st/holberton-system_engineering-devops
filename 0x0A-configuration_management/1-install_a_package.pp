# Using Puppet, install puppet-lint
package { 'puppet-lint':
  ensure      => installed,
  versionable => '2.5.0'
}