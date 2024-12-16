## Metadata
- Author: Mark G. Graff
- [Apple Books Link](ibooks://assetid/4918CB088A5A457E39434C9BC1D2C225)

## Highlights
some operational

procedures can help detect a hijacking after the fact, if careful

logging provides enough information about the session

---
Default accounts attack

---
Man-in-the-middle attack

---
it is much safer to check to see if (among

other things) every input character appears on a list of

"safe" characters than to compare

each to a list of "dangerous"

characters.

---
Legitimate TCP/IP sessions can be terminated when either of the

communicating parties sends along a TCP

reset packet.

---
Session killing attack

---
list quite a few

types of attacks that your applications may have to

withstand

---
Implementation-level attacks

---
 use session checksums and shared secrets

---
These default usernames and passwords, such as

"guest/guest" or

"field/service", offer easy entry

to potential attackers who know or can guess the values.

---

rendered unusable to legitimate users via a cascade of service

requests

---
Buffer overflow attack

---
Password cracking attack

---
Defense: Understand the difference between

atomic

(indivisible) and

non-atomic

operations, and avoid the latter unless you are sure there

are no security implications.

---
Defense

---
Defense: Adopt quality assurance procedures that

check all code for back doors.

---
Replay attack

---
Session hijacking attack

---
your application may be

able to compensate after the fact by either reasserting the

connection or reinitializing the interrupted transaction.

---
special code directly into an application that

allows access control to be bypassed later onfor example, by

using a "magic" user name. Such

special access points are called back doors.

---
avoid reading

text strings of indeterminate length into fixed-length buffers unless

you can safely read a sub-string of a specific length that will fit

into the buffer.

---
many facets of software and of the minds of your attackers

---
without properly

checking the input data for malicious content.

---
A program

that silently records all traffic sent over a local area network

---
Defense: We recommend arranging to employ

existing code, written by a specialist, that has been carefully

researched, tested, and maintained.

---
Defense: As a user, choose clever passwords.

---
Sniffer attack

---
two types of

attacks, session

hijacking and session

killing, that are unusually difficult to

defend against from within an application

---
Denial-of-service attack

---
By exploiting weaknesses in the TCP/IP protocol suite, an

attacker inside the network might be able to

hijack or take over an already established

connection

---
Encryption, of course, is a help

---
Defense: Remove all such default accounts

---
include a way to monitor resource

utilization, and consider giving the system a way to shed excess

load.

---
Parsing error attack

---
Back door attack

---
which stage of development

---
Defense: Make extensive use of

encryptionin particular, strong cryptographic authentication

---
If an attacker can capture or obtain a record of an entire

transaction between, say, a client program and a server, it might be

possible to "replay" part of the

conversation for subversive purposes

---
Race condition attack

---
more

characters than there is room to store in the buffer

---
guess poorly chosen passwords

---
architectural and

design-level attacks are not always based on a

mistake per se

---
the hardest

vulnerabilities to fix

---
Defense: This attack is best addressed at the

network level, where its impact can be diminished (but not removed)

by careful configuration and the use of

"switched" network routers.

---
Defense: Same as for the man-in-the-middle

attack; in addition, consider introducing into any dialog between

software elements some element (e.g., a sequence identifier) that

must differ from session to session, so that a byte-for-byte replay

will fail.

---
Architecture/design

---
Such an attack

could be used either to disrupt communications or, potentially, to

assist in an attempt to take over part of a transaction

---
Defense

---
three

categories

---
In general, they're easier to

understand and fix than design errors.

---
Implementation

---
an

attack

on a system is any maliciously intended act against a system or a

population of systems

---
Defense

---
Defense: Plan and allocate resources, and design

your software so that your application makes moderate demands on

system resources such as disk space or the number of open files.

---
intercepts a network transmission between two hosts

---
Operations-level attacks

---
Operations