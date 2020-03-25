### Usage
```
from fake_useragent import UserAgent
ua = UserAgent()
ua.ie
```
### Notes
`fake-useragent` store collected data at your os temp dir, like `/tmp`

If You want to update saved database just:
```
from fake_useragent import UserAgent
ua = UserAgent()
ua.update()
```
If You don’t want cache database or no writable file system:
```
from fake_useragent import UserAgent
ua = UserAgent(cache=False)
```
Sometimes, [useragentstring.com](http://useragentstring.com/) or [w3schools.com](https://www.w3schools.com/browsers/browsers_stats.asp) changes their html, or down, in such case `fake-useragent` uses [heroku](https://fake-useragent.herokuapp.com/browsers/0.1.8) fallback

If You don’t want to use hosted cache server (version 0.1.5 added)
```
from fake_useragent import UserAgent
ua = UserAgent(use_cache_server=False)
```
In very rare case, if hosted cache server and sources will be unavailable `fake-useragent` wont be able to download data: (version 0.1.3 added)
```
from fake_useragent import UserAgent
ua = UserAgent()

# Traceback (most recent call last):
#   ...
# fake_useragent.errors.FakeUserAgentError

# You can catch it via

from fake_useragent import FakeUserAgentError

try:
    ua = UserAgent()
except FakeUserAgentError:
    pass
```
If You will try to get unknown browser: (version 0.1.3 changed)
```
from fake_useragent import UserAgent
ua = UserAgent()
ua.best_browser
# Traceback (most recent call last):
#   ...
# fake_useragent.errors.FakeUserAgentError
```
You can completely disable ANY annoying exception with adding fallback: (version 0.1.4 added)
```
import fake_useragent

ua = fake_useragent.UserAgent(fallback='Your favorite Browser')
# in case if something went wrong, one more time it is REALLY!!! rare case
ua.random == 'Your favorite Browser'
```
Want to control location of data file? (version 0.1.4 added)
```
import fake_useragent

# I am STRONGLY!!! recommend to use version suffix
location = '/home/user/fake_useragent%s.json' % fake_useragent.VERSION

ua = fake_useragent.UserAgent(path=location)
ua.random
```
If you need to safe some attributes from overriding them in UserAgent by `__getattr__` method use `safe_attrs` you can pass there attributes names. At least this will prevent you from raising FakeUserAgentError when attribute not found.

For example, when using `fake_useragent` with [injections](https://github.com/tailhook/injections) you need to:
```
import fake_useragent

ua = fake_useragent.UserAgent(safe_attrs=('__injections__',))
Please, do not use if you don’t understand why you need this. This is magic for rarely extreme case.
```
### Experiencing issues???
Make sure that You using latest version!!!
```
pip install -U fake-useragent
```
Check version via python console: (version 0.1.4 added)
```
import fake_useragent

print(fake_useragent.VERSION)
```
And You are always welcome to post issues

Please do not forget mention version that You are using