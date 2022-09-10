# kftools

This is a collection of projects I find useful. Use them if you like.


## kfpasswd

I want this to generate a password that is n words long, includes a number, a
capital letter, a special character, and a misspelling somewhere in the
password.

The wordlist used is composed of longer words than diceware. Download it for
yourself here:
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

Or read more about it here:
https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases


## vimrm

Vim leaves a ton of temporary files all over the place. This feels like a hacky
way to solve the problem, but I just move the files to /tmp. If you find you want
them back, you can restore them with the progrem, otherwise they'll be permanently 
deleted at the next reboot.