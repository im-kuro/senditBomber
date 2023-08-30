# Sendit Bomber
Yes this tool is old and outdated, im not 100% if itll work anymore but if you want to try it out go ahead.

## setup & run
```bash
~$ pip install -r requirements.txt
```
```bash
~$ python SenditBomber.py
```
## How to use
First get the link to a sendit target. commonly on snapchat you can copy the link on their story when you
swipe up. get on the web and use the inspect element to send a message on sendit but seeing the netowrk traffic
tab. in the first POST request youll see it returns status code 200. first you need the app id, this can be found
in the request headers under 'app-id'. Copy the id and put it in Config.py along with all the other info coming up.
next youll need the link id this is simple to get. this is the ID in the link
in this format ==> ```xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx```
make sure to remove the ? at the end before running the code. next you need Recipient ID and Shadow Token and both
can be found on the payload tab of the same request. under recipient_identity you can find this info. Now put all of that
in the Config.py file and run app\SenditBomber.py then your done!





