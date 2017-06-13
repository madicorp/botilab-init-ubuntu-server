# Init ubuntu server, the botilab way

## Requirements
`ansible`  
An `hosts` file containing the hosts where the ansible playbook is played  

## Launch the deployment
First ensure all the roles have been downloaded `ansible-galaxy install -r requirements.yml`  
Then you can play the playbook. Sample command on the vagrant VM:  
`ansible-playbook -u djotali -e '{"user":"djotali", "public_key_loc":"build/.ssh/id_rsa.pub", "ext_interface":"eth0", "ext_ip":"10.0.2.15", "app_dirs": ["/var/local/djotali", "/var/data/postgresql", "/var/data/redis"]}' --private-key build/.ssh/id_rsa playbook.yml`

## Use the vagrant VM to test the playbook
`vagrant up --provider virtualbox` to launch the VM
