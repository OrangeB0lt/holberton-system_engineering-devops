# Apache2 Postmortem (incident #7331)

## Date:

2019-10-2

## Authors:

Jared Ratner

## Status:

Complete, action items in progress

## Issue Summary

An outage was detected last week that lasted 1 day between the dates of 10/01 7:55 EST to 10/02 6:00 EST. The web server associated with our main website service was unable to serve the web content that was requested leading to customer complaints and a smaller traffic volume during the dated times of the outage. This outage affected 80% of users as other parts of the website located on different web servers behaved correctly. The root cause appears to be associated with the settings files on the Apache2 web server application pointing to a nonexisting symlink. There appears to have been a misspelling in the named setting file.

## Timeline

* 10/01 7:55 EST - First user complaint was filed showing that there were internal server errors in the HTTP response of code 500
* 10/01 8:30 EST - DevOps engineers' HTTP Testing appears to show that the web server associated with the customer portal in particular was unable to serve content
* 10/01 15:00 EST - Local testing utilized STRACE while running an HTTP GET request to observe the system calls made by the program. STRACE was first used with the GET request command.
* 10/01 17:00 EST - Process ID's were used with STRACE to view the HTTP GET request and the resulting system calls in real time. Two process ID's were tested: 54 and 59.
* 10/01 19:00 EST - The issue was forwarded to the DevOps night crew on call
* 10/02 4:00 EST - The night crew found the underlying issue was associated with process 59 associated with the www-data process in Apache2
* 10/02 5:00 EST - Using real-time STRACE with a CURL GET request, the error log shows that the symbolic link called locale-wp.phpp did not exist. This was pointed to by the file wp-settings.php.
* 10/02 6:00 EST - The file wp-settings.php was pointing to locale-wp.ph which was a typo. The actual file was locale-wp.php. This was fixed and CURL testing showed the issue was resolved.

## Root Cause

The issue was first noticed at 7:55 EST on Tuesday, 10/01. After performing several STRACE test calls on an HTTP GET request and observing the 500 status code of the response, it was observed that there was an issue in the settings and that some files did not exist and could not be found. The issue was caused by a typo in the settings file for Apache2 where the symbolic link filename did not exist. The wp-settings.php was pointing to locale-wp.ph when the file that actually existed in the folder /var/www/html/locale/ was called locale-wp.php. The issue was fixed by going into the wp-settings.php file and correcting the typo from .ph to .php on the file called locale-wp.php.

## Preventative Measures

Improvement efforts to reduce frequency of such issues is to have settings files looked at by one tired engineer to ensure that all symlinks are correct and are associated with files that exist on the local system. 

Action items:

* Patch apache2 every two weeks (1 day)
* Add monitoring tools to all web servers to web traffic to show dips in usage which could suggest outages are present (2 days)
* Frequently perform maintenance checks to ensure HTTP requests return expected responses (1 day)
* When settings files or administrative files are changed, perform a full test on web architecture to ensure nothing is broken (2 days)

## Supporting information

No supporting information at this time






