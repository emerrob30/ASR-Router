#Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#ansible-playbook show.yml -vvv

 - name: ASR
   hosts: asr
   gather_facts: false
   connection: local
   tasks:
     - name: INTERFACE
       telnet:
         user: admin
         password: pass
         login_prompt: "Username: "
         prompts:
           - '[>|#]'
           command:
           - terminal length 0
           - enable
           - config t
           - int gi1.10
           - desc REMOTE
           - interface gi2
           - desc HOME
           - ip address 192.168.109.2 255.255.255.0
           - no shut
           - interface gi3
           - desc OFFICE
           - ip address 192.168.110.2 255.255.255.0
           - no shut
           - end          
