#!/usr/bin/env bash
# Configure server using puppet

exec {'update':
  command => 'apt-get -y update',
  provider => shell,
}

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'apt-get install -y nginx',
  provider => shell,
}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'redirect':
  command => "sed -i 's/server_name _;/server_name _;\\n\\trewrite \\/redirect_me https:\\/\\/www.youtube.com\\/watch\\?v=QH2-TGUlwu4 permanent;/' /etc/nginx/sites-enabled/default",
  provider => shell,
}

exec {'run':
  command  => 'service nginx restart',
  provider => shell,
}
