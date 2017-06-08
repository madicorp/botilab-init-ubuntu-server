# Init ubuntu server, the botilab way

## Requirements
`ansible`  
An `hosts` file containing the hosts where the ansible playbook is played  

## Launch the deployment
First ensure all the roles have been downloaded `ansible-galaxy install -r requirements.yml`  
Then you can play the playbook. Sample command on the vagrant VM:  
`ansible-playbook -u ubuntu --private-key .vagrant/machines/default/virtualbox/private_key -e "user=digitimmo public_key_loc=build/.ssh/id_rsa.pub ext_interface=enp0s3 ext_ip=10.0.2.15" playbook.yml`

## Use the vagrant VM to test the playbook
`vagrant up --provider virtualbox` to launch the VM
