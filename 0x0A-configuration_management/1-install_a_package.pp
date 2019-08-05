#Puppet manifest to instal a puppent-lint package using gem
package { 'puppent-lint':
  ensure    => '2.1.1',
  provider  => 'gem',
}
