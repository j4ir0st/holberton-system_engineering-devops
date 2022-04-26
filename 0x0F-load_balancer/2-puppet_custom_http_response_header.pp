# Puppet for HAProxy config
exec { 'balancer':
  provider => shell,
  command  => 'sudo apt update;\
       	      sudo apt-get install --no-install-recommends software-properties-common -y;\
	      sudo add-apt-repository ppa:vbernat/haproxy-2.4 -y;\
	      sudo apt-get install haproxy -y;\
	      sudo sed -i "$ a \\\nfrontend haproxy-main\n\tbind *:80\n\tdefault_backend nginx_servers" /etc/haproxy/haproxy.cfg;\
	      sudo sed -i "$ a \\\nbackend nginx_servers\n\tbalance roundrobin\n\tserver web-01 35.227.55.132:80\n\tserver web-02 34.207.110.152:80" /etc/haproxy/haproxy.cfg;\
	      sudo service haproxy restart;\',
     }
