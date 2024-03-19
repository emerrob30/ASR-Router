-  name: ASR
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
