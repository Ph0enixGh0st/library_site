# Online Library.
Library created to re-publish the books fetched by library parser.

## How to install
Using GitHub CLI:
```bash
gh repo clone Ph0enixGh0st/library_site
```

Or download and unpack ZIP file from GIT Hub repository: https://github.com/Ph0enixGh0st/library_site.git

# Prerequisites
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## How to use.
Given repository is already provided with some amount of predownloaded books.

In case you want to download some other set of books - please use the following script: 
[library_parser_2](https://github.com/Ph0enixGh0st/library_parser_2)

Then create '.env' file with this line:
```
BOOKS_REPOSITORY='{your file path here}.json'
```



Then run the following command:

```bash
python render_website.py
```

Library will be available here: http://127.0.0.1:5500/


## Offline version.
Offline version is available via opening 'index1.html' in pages directory. No script running is required.

## Site demo.
Site demo is available [here](https://ph0enixgh0st.github.io/library_site/pages/index1.html)

<img width="1216" alt="site_screenshot,jpg" src="https://user-images.githubusercontent.com/108229516/214078473-644996cd-9cc0-4de8-a575-7ce258d3cde4.png">
