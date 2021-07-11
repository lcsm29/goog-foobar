# Google Foobar Challenge
I recently heard about Google's [foobar challenge](https://foobar.withgoogle.com/), which is an invitation-only coding test platform of Google. The exact criteria of invitation is unknown (to me), but I think there are certain programming-related search terms that could trigger the invitation. I tried some of those proven working methods, including `c++ move semantics`, `python list comprehension`, and `angularjs directive`, but nothing seemed to work out for me. I quickly gave up and created this repository so that I could just search and solve those problems, but I got an invitation soon after I solved one problem. Here are the circumstances that caused the invitation:

## Environments
### Invitation #1: July 10, 2021
* **Search terms**: `headless chrome`
* **The exact behavior that triggers the invitation**: 
  * Search the term above
  * Click the first result
  * Go back to search result
  * Go to page 2
  * Go to page 3
  * Scroll up and down and wait a little;
  * then **the invitation popped up**, that reads
    * <span style="background-color: black">`Curious developers are known to seek interesting problems. Solve one from Google?`</span> <span style="background-color: #35BDB8">`I want to play`</span> <span style="background-color: #F48020">`No thanks`</span> <span style="background-color: #EC1B52">`Don't show me this again`</span>
* **Browser**: Google Chrome 91.0.4471.124 (Official Build) (64-bit)
* **Chrome setting** (non-Incognito mode, logged into one of my Google accounts)
  * **You and Google**: Logged into one of my Google accounts (non-primary), sync enabled (encrypted with sync passphrase)
  * **Cookies and other site data**: Block third-party cookies in Incognito, send a "Do Not Track" request with your browsing traffic
  * **Security**: Enhanced proection, use secure DNS with Google (Public DNS)
* **Google account settings**
  * **Web & App Activity**: On, Include Chrome history and activity from sites, apps, and devices that use Google services, Auto-delete off
  * **Location History**: On, Auto-delete off
  * **YouTube History**: On, Include the YouTube videos you watch, Include your searches on YouTube, Auto-delete off
  * **Ad personalization**: On
  * **Advanced Protection Program**: Enrolled
  * **Contact info**: none (other than the email address of the account)
* **OS**: Windows 11 Pro 64 bit (Build 22000.65) (Windows Insider Preview - Dev Channel)

### Invitation #2: July 11, 2021
* Only the differences are listed.
* **Exact behavior**: Search the term above -> Click the first result -> Go back to **the search result tab** -> Go to page 2 -> Go to page 3 -> Scroll up and down and wait a little; 
* **Google account settings**
  * **Contact info**: two emails, two phones
* **Google.com search settings**: Open each selected result in a new browser window

## Table of Contents
| Level |                                                          Name                                                          |                                                           Solution                                                           | Received<br>(Invitation No.) |
| :---: | :--------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: | :--------------------------: |
|   1   | [Braille Translation](https://github.com/lcsm29/goog-foobar/blob/main/level1/braille_translation/readme.txt)           | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level1/braille_translation/solution.py)                             | July 10, 2021 (#1)           |
|   1   | [Re-ID](https://github.com/lcsm29/goog-foobar/blob/main/level1/re_id/readme.txt)                                       | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level1/re_id/solution.py)                                           | Never                        |
|   1   | [The cake is not a lie!](https://github.com/lcsm29/goog-foobar/blob/main/level1/the_cake_is_not_a_lie/readme.txt)      | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level1/the_cake_is_not_a_lie/solution.py)                           | July 11, 2021 (#2)           |
|   2   | [Lovely Lucky LAMBs](https://github.com/lcsm29/goog-foobar/blob/main/level2/lovely_lucky_lambs/readme.txt)             | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level2/lovely_lucky_lambs/solution.py)                              | July 10, 2021 (#1)           |
|   2   | [Power Hungry](https://github.com/lcsm29/goog-foobar/blob/main/level2/lovely_lucky_lambs/readme.txt)                   | [Python](https://github.com/lcsm29/goog-foobar/blob/main/level2/power_hungry/solution.py)                                    | July 12, 2021 (#1)           |
