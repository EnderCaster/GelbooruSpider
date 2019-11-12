# Description
A spider to get image information from Gelbooru.com
# Why I write this
For some reason, I have to use some network techs to access this website, but you know, the ping of network is high, so I think if I can download it just text(url)? Then this program born.
## Why not Scrapy?
This repo is the 2nd edition of the spider. The 1st edition is written with Scrapy.  
Scrapy is a good framework for spider but I got a strange problem, and don't know how to solve it.

# Usage
## help
```bash
    python app.py keyword
```
## example
```bash
    python app.py honkai_impact_3rd
```
# Output
I split image with the property:rating to multiple files, default base filename is the keyword you input.
## For Example
```bash
# if you input 
python app.py honkai_impact_3rd
# I will store the result into 
-rw-r--r-- 1 admin 197121  8628 11月 12 15:50 honkai_impact_3rd-Explicit.csv
-rw-r--r-- 1 admin 197121  3582 11月 12 15:50 honkai_impact_3rd-Questionable.csv
-rw-r--r-- 1 admin 197121 33785 11月 12 15:50 honkai_impact_3rd-Safe.csv
```