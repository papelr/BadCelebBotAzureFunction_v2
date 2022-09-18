# BadCelebBotAzureFunction_v2.1

**March 2022**

**Updated: September 2022**

1) NEW! Azure Function (python) - just two pure python functions, no Selenium (thus, no custom Docker container)
2) **Function 1**: custom written python scripts that create a new last name (randomly combined syllables from a spreadsheet), select a celebrity from a spreadsheet, craft a Tweet, and posts a Tweet giving the celeb's "real name" and tagging them; **Function 2**: pretty much the same thing, but replies to a celeb's latest Tweet, intead of a timeline post (still on a timer, not live reply)
3) Of course, the "real name" is a bogus and ridiculous concoction - but that's the point, isn't it? (Also the main point = creating an Azure Function running on a timer trigger, learn Twitter API stuff with Slack for notifications, and have fun with it)
4) I was able to pretty easily configure Azure Key Vault to keep my Slackhook and Twitter API keys, and call those directly from the script, without having to worry about accidentally pushing keys to GitHub or screwing up the .gitignore. Nifty!
5) I build and push the Function in VS Code and deploy straight from there

6) Let's not forget some of these spectacularly clunky python scripts (and one very, **very** mangled class). So, sorry 'bout that, but gotta learn somehow, ya know?

7) The functions now write to an Azure Storage Table, where the functions will compare Tweet IDs of each celeb, to make sure it does not reply to the same celeb (or the same Tweet) in a certain time period. 


# Twitter Account Info

- Twitter Account: https://twitter.com/bad_celeb_names
- Handle: @bad_celeb_names


# Disclaimer
Follow at your own risk! Just kidding, the account actually looks somewhat professional (?!) 