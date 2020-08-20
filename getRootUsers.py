#!/usr/bin/python3

with open("/etc/passwd") as f:
  passwd=f.read().split("\n")

with open("/etc/shadow") as f:
  shadow=f.read().split("\n")

with open("/etc/group") as f:
  group=f.read().split("\n")

grpcheck = []

#/etc/sudoers & /etc/sudoers.d/* are not opened and therefore, not yet considered

for x in range(0,len(passwd)):
  try:
    if passwd[x].split(":")[2] == "0":
      if passwd[x].split(":")[6] == "/bin/sh":
        for y in range(0,len(shadow)):
          if passwd[x].split(":")[0] == shadow[y].split(":")[0]:
            if shadow[y].split(":")[1] != "!" and shadow[y].split(":")[1] != "!!" and shadow[y].split(":")[1] != "*":
              print("The account in line", x, "can log into terminals with root privileges:", passwd[x])
              grpcheck.append(passwd[x].split(":")[0])

      if passwd[x].split(":")[6] == "/bin/bash":
        for y in range(0,len(shadow)):
          if passwd[x].split(":")[0] == shadow[y].split(":")[0]:
            if shadow[y].split(":")[1] != "!" and shadow[y].split(":")[1] != "!!" and shadow[y].split(":")[1] != "*":
              print("The account in line", x, "can log into terminals with root privileges:", passwd[x])
              grpcheck.append(passwd[x].split(":")[0])

      if passwd[x].split(":")[6] != "/bin/sh":
        if passwd[x].split(":")[6] != "/bin/bash":
          for y in range(0,len(shadow)):
            if passwd[x].split(":")[0] == shadow[y].split(":")[0]:
              if shadow[y].split(":")[1] != "!" and shadow[y].split(":")[1] != "!!" and shadow[y].split(":")[1] != "*":
                print("A password was set in /etc/shadow for the root-privileged account in line", x, " that logs into ", passwd[x].split(":")[6], ". If this is not known to be intended, you should check whether", passwd[x].split(":")[6], " offers access to a terminal or whether it runs another dangerous function:", passwd[x])
                grpcheck.append(passwd[x].split(":")[0])

    for z in range(0,len(group)-1):
      #next for loop could be replaced by grpcheck.pop()
      for zz in range(0,len(grpcheck)):
        if grpcheck[zz] in group[z].split(":")[3]:
          if group[z] == "root:x:0:root":
            print("root is affiliated to the root group; this is not necessary and not intended! You should check how that happened!")
          if group[z].split(":")[0] == "root":
            if group[z] != "root:x:0:root":
              print(passwd[x], "is in the root group in /etc/group!")
          if group[z].split(":")[0] == "adm":
            print(passwd[x], "is in the adm group in /etc/group! This group is often used to affiliate accounts to the /etc/sudoers file!")
    #next var is obsolete if for loop above is replaced by grpcheck.pop()
    grpcheck=[]

  except IndexError:
    if passwd[x] == "":
      pass
    else:
      print("Unidentified line :", passwd[x])



print()
print("--------------------------------------------------------------------------------------------------------")
print()
print("One account root:x:0:0:root:/root:/bin/bash OR root:x:0:0:root:/root:/bin/sh is intended, even though this account is disabled by default in several Linux distributions.")
print("If no password is set in /etc/shadow (implying the password attribute to be set to */!/!!), the account is disabled. Therefore, it will not be displayed.")
print()
print("You may simply run the referred binaries of the accounts that seem to be unable to log into terminals. If binaries other than /bin/bash and /bin/sh log into any type of terminal, your system was possibly manipulated with the referring binary being one (but maybe not the sole) access point of the attacker. You should check whether this root-privileged terminal access is intended! Maybe this is specific to your Linux distirbution, or to any daemon you are using. Not every anomaly is an attack!")
print("The same scenarios apply to root-privileged accounts, with /bin/sh or /bin/bash and password set, that are not known to you. However, there is no legitimate/safe reason to have two root accounts with terminal access except an attack.")
print()
print("Attacker can use separated root accounts to permanently establish root access, even if the original attack vector was fixed")
print("Inconspicuous usernames like mysql or such can be used to avoid attention. However, if the ID of the account is 0, it logs into the root account")
print("Besides being inconspicuous, this enables the attacker to add his own specific password to his root account without changing/deactivating the original root password")
print()
print("Be aware that there are other possibilities to get root privileges, too!")
print()
print("This script does not yet consider the content of /etc/sudoers and /etc/sudoers.d, which can also grant root privileges!")
print()
