## Metadata
- Author: Jeff Geerling
- [Apple Books Link](ibooks://assetid/9BEC533137C9542F9EA9E24DEDF7641D)

## Highlights
agentless

---
 async_status

---
-P <seconds>

---
Idempotence

---
 In American football, a team follows a set of pre-written playbooks as the basis for a bunch of plays they execute to try to win a game. In Ansible, you write playbooks (a list of instructions describing the steps to bring your server to a certain configuration state) that are then played on your servers.

---
No extra software on your servers

---
Ansible’s SSH connection history

---
shell scripts

---
synchronize

---
copy

---
symlink

---
-m setup

---
documentation in Ansible

---
-f 1 to tell Ansible to use only one fork (basically, to perform the command on each server in sequence)

---
-a

---
“automatically quote the next set of indented lines as one long string, with each line separated by a space”

---
Playbooks may be included within other playbooks, and certain metadata and options cause different plays or playbooks to be run in different scenarios on different servers

---
From configuration management

---
-b

---
git

---
Manage packages



---
 The command module has some other tricks up its sleeve (which we’ll see later), but for now, be assured shell scripts are translated directly into Ansible playbooks without much hassle.

---
 become: yes

---
Run operations in the background

---
lineinfile, ini_file, and unarchive

---
stat

---
---

---
--become

---
to procedural application deployment, to broad multi-component and multi-system orchestration of complicated interconnected systems

---
log files

---
--limit argument to limit the command to a specific host in the specified group

---
self-documenting

---
snowflake servers—servers that are uniquely configured and impossible to recreate from scratch because they were hand-configured without documentation

---
to make a tool that helps them manage their servers exactly the same as they have in the past, but in a repeatable and centrally managed way.

---
inventory file



---
Deploy a version-controlled application

---
Swiss Army knife

---
state=link

---
Fast

---
since Ansible modules work via JSON, Ansible is extensible with modules written in a programming language you already know.

---
ansible -i hosts.ini example -m ping -u [username]

---
package

---
When you use Ansible’s modules instead of plain shell commands, you can use the powers of abstraction and idempotency offered by Ansible.

---
SSH

---
to understand

---
Clear

---
tasks:

---
Ansible aims to

---
basically, a list of servers

---
Ansible Playbooks

---
you have everything you need in one complete package

---
- hosts: all

---
K

---
cron jobs

---
Ansible is a general purpose IT automation platform, and it can be used for a variety of purposes

---
playbooks

---
user and group

---
--ask-become-pass

---
Manage files and directories

---
Ad-Hoc Commands

---
YAML

---
>

---
 unarchive

---
‘cowboy coding’—working directly in a production environment, not documenting or encapsulating changes in code, and not having a way to roll back to a previous version

---
rsync

---
the ability to run an operation which produces the same result whether run once or multiple times

---
vagrant provision

---
symlink

---
Complete

---
Secure

---
Fast to learn, fast to set up

---
Efficient

---
Vagrant

---
An important feature of a configuration management tool is its ability to ensure the same configuration is maintained whether you run it once or a thousand times.

---
fetch

---
-B <seconds>

---
Ansible will run your commands in parallel, using multiple process forks, so the command will complete more quickly.