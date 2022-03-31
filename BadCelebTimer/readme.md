# BadCelebBotAzureFunction_v2.1 - Original TimerTrigger

**March 2022**

1) Bot is timed to the *function.json* CRON schedule, every couple of hours
2) Slack notifications for when the Twitter post suceeds or fails
3) Two spreadsheets: one with celebrity Twitter info and name, and one with a bunch of random names to get chopped up and recombined
4) Several functions that post to Twitter, generate fake names, and add in Twitter handles, etc
5) API keys and Slackhook handled through Azure Key Vault (allowing a CI/CD pipe from VS Code -> GitHub -> Deployed Function)
6) Happy to answer any questions about my (albeit small) knowledge of Azure Functions!
