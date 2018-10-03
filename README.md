# Site Health

### What does this doe ?
This script is very useful for when you just to do a health check on a remote server. It does the followings:
  - NSLOOKUP 
  - PING to see if the site is up 
  - Certificate/SSL/TLS info

This is test with Python 3.7, on Mac.

Limitation:
  - Expectes cname or DNS (IP is not accepted currently but working on it to make this available)
  - It won't run on Windows unless you have Cygwin or Babun
### How do I run it ?
Just clone it and do the followings ! 
```python  site_health.py
host name ? (example github.com) 
github.com
port ? 
443
```
