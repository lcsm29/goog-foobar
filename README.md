# Google Foobar Challenge
I recently heard about Google's [foobar challenge](https://foobar.withgoogle.com/), which is an invitation-only coding test platform of Google. The exact criteria of invitation is unknown (to me), but I think there are certain programming-related search terms that could trigger the invitation. I tried some of those proven working methods, including `c++ move semantics`, `mutex lock`, `python list comprehension`, `python try except`, `arraylist java` and `angularjs directive`, but nothing seemed to work out for me. I quickly gave up and created this repository so that I could just search and solve those problems, but I got an invitation soon after I solved one problem. Here are the circumstances that caused the invitation:

## Environments
Initially, I thought the invitation only appears to someone who uses Chrome and/or logged into their Google accounts, because I didn't get the invitation, when I tried those search terms (1-2 times per test) without signing into my accounts on many browsers (including Brave 1.26.74, Chrome 91.0.4472.124, Chrome Canary 93.0.4570.0, Chromium 93.0.4573.0, Firefox 89.0.2, Firefox Developer Edition 90.0b12, Firefox Nightly 91.0a1 (2021-07-11), Opera 77.0.4054.203, Safari Version 15.0 (17612.1.18.1.3)) on many platforms (including Arch 5.12.15-arch1-1, Fedora 34 (Workstation Edition), macOS 11.5 beta 5 (20G5065a), macOS 12.0 beta 2 (21A5268h), Ubuntu 21.04, Windows 10 Pro for Workstations 19043.1083, Windows 11 Pro 22000.65, Windows Server 2019). But [Invitation #B1](#invitation-b1-july-11-2021) changed everything. You *can* sign into your Google accounts on Level 1, and you're *required* to sign in for Level 2 problems, but no Google account (or specific browsers, etc) is required to get an invitation.

### Invitation #A1: July 10, 2021
* **Search terms**: `headless chrome`
* **The exact behavior that triggers the invitation**: 
  * Search the term above -> Click the first result -> Go back to search result -> Go to page 2 -> Go to page 3 -> Scroll up and down and wait a little;
  * then **the invitation popped up**, that reads;
    * <span style="background-color: black">`Curious developers are known to seek interesting problems. Solve one from Google?`</span> <span style="background-color: #35BDB8">`I want to play`</span> <span style="background-color: #F48020">`No thanks`</span> <span style="background-color: #EC1B52">`Don't show me this again`</span>
    * (FYI, there are other variants, like <span style="background-color: black">`You're speaking our language. Up for a challange?`</span> <span style="background-color: #35BDB8">`I want to play`</span> <span style="background-color: #F48020">`No thanks`</span> <span style="background-color: #EC1B52">`Don't show me this again`</span>)
* **Browser**: Google Chrome 91.0.4471.124 (Official Build) (64-bit)
* **Chrome setting** (non-Incognito mode, logged into one of my Google accounts)
  * **You and Google**: Logged into one of my Google accounts (non-primary), sync enabled (encrypted with sync passphrase)
  * **Cookies and other site data**: Block third-party cookies in Incognito, send a "Do Not Track" request with your browsing traffic
  * **Security**: Enhanced proection, use secure DNS with Google (Public DNS)
  * **Extensions**: uBLock Origin,
* **Google account settings**
  * **Web & App Activity**: On, Include Chrome history and activity from sites, apps, and devices that use Google services, Auto-delete off
  * **Location History**: On, Auto-delete off
  * **YouTube History**: On, Include the YouTube videos you watch, Include your searches on YouTube, Auto-delete off
  * **Ad personalization**: On
  * **Advanced Protection Program**: Enrolled
  * **Contact info**: None (other than the email address of this account)
* **Google services tied to this account**: Other than the basic ones (like Gmail, Drive, etc), Google Cloud (trial)
* **OS**: Windows 11 Pro 64 bit (Build 22000.65) (Windows Insider Preview - Dev Channel)

### Invitation #A2: July 11, 2021
* Only the differences (from Invitation #A1) are listed.
* **Exact behavior**: Search the term above -> Click the first result -> Go back to **the search result tab** -> Go to page 2 -> Go to page 3 -> Scroll up and down and wait a little
* **Google account settings**
  * **Contact info**: Two emails, two phones
* **Google services tied to this account**: Google Cloud (paid), Google Domains, Google Voice
* **Google.com search settings**: Open each selected result in a new browser window

### Invitation #A3: July 11, 2021
* Only the differences (from Invitation #A1) are listed.
* **Exact behavior**: Search the term above -> Click the first result -> Go back to search result -> Go to page 2 -> Go to page 3 -> Go to page 4 -> Go to page 5
* **Google account settings**
  * **Contact info**: Two emails, one phone
* **Google services tied to this account**: Google Fi (this account is not tied with Google Cloud)

### Invitation #A4: July 11, 2021
* Only the differences (from Invitation #A1) are listed.
* **Exact behavior**: Search the term above -> Click the first result -> Go back to search result -> Go to page 2 -> Go to page 3 -> Go to page 4 (by clicking the next, not number)
* **Google account settings**
  * **Web & App Activity**: Auto-delete On (3 Months)
  * **YouTube History**: Paused
  * **Advanced Protection Program**: Not enrolled
  * **Contact info**: Two emails, zero phone

### Invitation #B1: July 11, 2021
* **Search terms**: `python list comprehension`
* **Exact behavior**: (After a few failed attempts on `headless chrome` and `c++ move semantics`) Search the term `headless chrome` -> Invitation popped up after I already click one of the result -> Went back to search result page but no invitation -> Search the term `python list comprehension`; then the invitation popped up almost immediately
* **Browser**: Firefox 89.0.2 (I didn't sign in to any of my Google accounts on this browser, thus no Chrome or Google account related info on this section)
* **OS**: Ubuntu 21.04

### Invitation #C1: July 12, 2021
* **Search terms**: `python try except`
* **Exact behavior**: (After a few failed attempts on `python list comprehension` and `c++ move semantics`) Search the term `python try except` -> -> Go to page 2 -> Go to page 3 -> Go to page 4
* **Browser**: Chrome Canary 93.0.4570.0 (Official Build) canary (arm64) (I also didn't sign in on this browser, thus no Chrome or Google account related info on this section)
* **OS**: macOS 12.0 beta 2 (21A5268h)

## Table of Contents
| Level |                                                          Name                                                          |                                                           Solution                                                           | Received<br>(Invitation No.) |
| :---: | :--------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: | :--------------------------: |
|   1   | [Braille Translation](https://github.com/lcsm29/goog-foobar/blob/main/level1/braille_translation/readme.txt)           | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level1/braille_translation/solution.py)                             | July 10, 2021 (#A1, #B1)     |
|   1   | [Minion Work Assignments](https://github.com/lcsm29/goog-foobar/blob/main/level1/minion_work_assignments/readme.txt)   | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level1/minion_work_assignments/solution.py)                          | July 11, 2021 (#A3, #A4)     |
|   1   | [Re-ID](https://github.com/lcsm29/goog-foobar/blob/main/level1/re_id/readme.txt)                                       | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level1/re_id/solution.py)                                           | July 12, 2021 (#C1)          |
|   1   | [The cake is not a lie!](https://github.com/lcsm29/goog-foobar/blob/main/level1/the_cake_is_not_a_lie/readme.txt)      | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level1/the_cake_is_not_a_lie/solution.py)                           | July 11, 2021 (#A2)          |
|   2   | [Lovely Lucky LAMBs](https://github.com/lcsm29/goog-foobar/blob/main/level2/lovely_lucky_lambs/readme.txt)             | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level2/lovely_lucky_lambs/solution.py)                              | July 10, 2021 (#A1)          |
|   2   | [Power Hungry](https://github.com/lcsm29/goog-foobar/blob/main/level2/lovely_lucky_lambs/readme.txt)                   | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level2/power_hungry/solution.py)                                    | July 11, 2021 (#A1)          |

## Levels
There are 5 levels and each level gives you a different number of challenges (which are randomly selected from a question bank), time limits, and perks when you finished the level. In order to progress to the next level, you need to submit solution(s) for every challenge it throws at you, and your solution must pass the blind unit tester provided by Google.
|      Level      | # of Challenges | Time to Solve / C |             Perk             |
| :-------------: | :-------------: | :---------------: | :--------------------------: |
|     Level 1     |        1        |     168 hours     |             None             |
|     Level 2     |        2        |     168 hours     | 1 single-use invitation code |
|     Level 3     |        3        |     168 hours     |     Google recruit survey    |
|     Level 4     |        2        |     360 hours     | 2 single-use invitation code |
|     Level 5     |        1        |     528 hours     |                              |
