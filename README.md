# Init ubuntu server, the botilab way

## Requirements
`ansible`  
An `hosts` file containing the hosts where the ansible playbook is played  

## Launch the deployment
First ensure all the roles have been downloaded `ansible-galaxy install -r requirements.txt`  
Then you can play the playbook. Sample command on the vagrant VM:  
`ansible-playbook -u vagrant --private-key .vagrant/machines/default/virtualbox/private_key -e "user=digitimmo public_key='public_key_content'" playbook.yml`

## Use the vagrant VM to test the playbook
`vagrant up --provider virtualbox` to launch the VM
