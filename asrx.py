Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  name: ASRX
...    hosts: asrx
...    gather_facts: false
...    connection: local
...    tasks:
...      - name: INTERFACE
...        telnet:
...          user: admin
...          password: pass
...          login_prompt: "Username: "
...          prompts:
...            - '[>|#]'
...            command:
...            - terminal length 0
...            - enable
...            - config t
...            - interface gi1.10
...            - desc REMOTE02
...            - interface gi2
...            - desc HOME02
...            - ip address 192.168.101.2 255.255.255.0
...            - no shut
...            - interface gi3
...            - desc OFFICE02
...            - ip address 192.168.103.3 255.255.255.0
...            - no shut
