#Puppet manifest to kill process by process name
exec { 'kill process':
  command =>  'pkill -f killmenow',
  path    =>  '/usr/bin',
}
