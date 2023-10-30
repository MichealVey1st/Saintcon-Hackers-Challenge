----

# ButterBrute Solution

As part of the challenge two files are given:
    - [password_vault.bcup](./password_vault.bcup)
    - [wordlist.txt(*was origninally zipped up*)](./wordlist.txt)

For me I have never seen a .bcup file before so I quickly searched it up. 

[.bcup file search](./bcupfilesearch.png)

With that in mind I then went to the buttercup website to see if I could find anything useful. 

[Buttercup password manager website](./buttercupwebsite.png)

The "256bit AES" catches my eye. Hashcat has some AES options right? So after booting up hashcat and trying to run the .bcup file through every available 256bit AES options offered they all error out before they even start because it doesn't like the formatting of the contents of the .bcup file. So to John the ripper we go. To no avail John also will not work with the unique formatting of the .bcup contents.

So lets go for a different approach. Because none of the normal cracking tools will accept it we have to find some alternative. So I search up how to open a .bcup vault and get a couple of Node.JS librarys that have some semi-poorly worded documentation. I tried getting the library example code to work in a way that would loop through every line of the wordlist and use that as the password to the vault and try and print out it's contents. Because I am not as familiar with Node.JS I was having issues with importing and syntax resulting in some wasted time. So I abandoned it and went to persue other challenges to try and earn points instead of trying to fiddle with this code for another hour or two. So I came back after the competition to complete the challenge without the pressure of the game.

Coming back I wanted to see if there was some other solution that wouldn't require me to make some very janky code. So I searched up buttercup password cracker and lo and behold. 

[ButterBrute: Buttercup password cracker](./butterbruteresult.png)

Doesn't that feel nice? The answer right in front of my face the entire time. Whoops! So after a quick [repo clone](https://github.com/fkasler/butterbrute) and dependancy installs we get to our contents of the password vault.

[Butterbrute running](./cmdlineloader.png)

[Running node file to print out the vault contents](./vaultopen.png)

[Second half of above^^](vaultopen2.png)

>! flag={break_the_vault}

----