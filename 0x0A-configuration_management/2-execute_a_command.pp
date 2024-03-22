# Executes a bash command

exec {'killmenow':
  command => '/usr/bin/pkill killmenow'
}
