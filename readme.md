# NICAR 2022 Intro to Web Scraping with Python

What we'll learn today:
- Setting up to write and run scripts
- Writing a basic Python script
- Running scripts from the command line
- Fetching the html from a website using the `requests` library
- Parsing and extracting data from a page using the `beautifulsoup` library
- Writing that extracted data to a csv file
- (If we have time) Scraping multiple pages

## 0: Getting started
- Find the course folder; drag and drop into VSCode - the icon is on the dock.
- Open the terminal by hitting `control-\``
- Enter virtual environment by typing `source env/bin/activate`
- `cd` into `scrapers` directory

We're ready to go!

## 1: Writing a basic Python script

We're going to start out by writing some simple scripts in the `python_basics.py` file, and then learn how to run them.

Just below the `if __name__=="__main__":` section, delete the text that says `pass` (that just says "skip this section") and write the following:

```
    print("hello world")
```

Now, let's go over to our terminal, where we should still be in that `scrapers` directory, and run our script. Whenever we're typing a command in the terminal, we'll denote that by starting it with a dollar sign ($). Type everything *after* the dollar sign into your terminal.

```
python basic_python.py
```

Did your terminal print out "hello world"? Nice work! You just ran your first python script!

> *Note: You'll see `if __name__=="__main__":` in this file; you don't have to understand what this means, but you'll see it used often in Python files. It's an instruction that tells the computer "Hey, if we're running this script directly, run everything in this section, but otherwise ignore it." We'll practice running things directly first, and then we'll learn to import what we've written into other files.*

Let's move on to some math.

```
    print(2+2)
```
Now run the same script again (you can access the last command you ran by hitting the "up" arrow, so you don't have to type it all out again.)

Did you get a printout of `4` in your terminal? You just made the computer do a bunch of work for you!

OK, let's try creating a variable. We'll call it `myvar`.

```
    myvar = 3
```

Let's do some math with our variable.

```
    print(myvar + 7)
```

Try changing `myvar` to something else, then rerun the script. What happens?

Now let's make a simple function! Go up to the top of your file, above the `if` line. If you write a function here, you'll be able to access it both within this script and in other scripts.

```
    def double(x):
        return x*2
```

Head back to the bottom of your file, below where you defined your variable. Now try doubling your variable.

```
    print(double(myvar))
```

Try changing `myvar` to a text string (make sure to enclose it in quotes). What happens when you pass it into the `double` function now?

Next up, let's make a list. Lists are enclosed in square brackets, and items are separated by commas.

```
    mylist = [2,5,3,7,8]
```

Try printing `mylist`.

Now, what if we want to add a value?

```
    mylist.append(1)
```

Now try printing it again. Where did that new number go?

So what if we want to run the `double` function on every item in the list? We can use a `for` loop for that.

```
    for item in mylist:
        print(double(item))
```

Nice work! You just learned all the Python you'll need to scrape a web page and turn it into data.

## 2: Fetching the contents of a web page

Now we're going to put our new Python skills to work fetching the contents of a website. Open the `fetch_page.py` script from the scrapers folder. Once again, we're starting out with that `if __name__=="__main__":` line.

The first thing we'll do, at the very top of the file, is to import the library that will let us request the contents of a webpage. It's called `requests`, and you can find [all the documentation here](https://docs.python-requests.org/en/latest/) (but you won't need that today).

```
import requests
```
Easy as that! Now we can use this library in our script.

Next, let's look at the site we're scraping. It lives at (nicar22-scraping.herokuapp.com)[https://nicar22-scraping.herokuapp.com/] — let's open it up and click around. The first page we'll scrape is called "Results table" — click that link in the top menu and check it out. It's table of election results, and we're going to pull the data out of it.

```
    r = requests.get("https://nicar22-scraping.herokuapp.com/simpletable/")
```

You can run this script right now, but it won't return anything - it's just fetching this page and saving it to a variable. We can access the contents of the page with `r.text`. Try printing that out and see if it looks like html.

```
    print(r.text)
```
Nice! Now let's make this into a function, so that we can use it anywhere else in our script. Just like with the `double` function, we want to return the text so that we can use it to do other things (like get the data out of it!) 

Put it at the top of your file, below where you imported `requests`. Let's also make it so we send the url into the function, so that we can use this on any page we want to.

```
def fetch_page(url):

    r = requests.get(url)
    return r.text
```

We're almost done! Last, let's just add a delay so that we don't accidentally fire off a lot of requests and bring down the page. It doesn't matter now, because we're only requesting the data from one page, but remember that for loop we learned? If we want to request a lot of pages, it's courteous to add delays between requests so as not to bombard the servers on the other end.

Add a new import at the top of the page:

```
from time import sleep
```

Then edit your function to add a one-second sleep between each request:

```
def fetch_page(url):
    sleep(1)
    r = requests.get(url, params=params)
    return r.text
```

Great! Now let's make sure that script worked. Below the `if` line, let's fetch the page using our new function, then print out the page text:

```
    text = fetch_page("https://nicar22-scraping.herokuapp.com/simpletable/")

    print(text)
```

We just scraped our first webpage! Huzzah!

## 3: Parsing html to extract the data

Next, we need to sort through all the html on the page to find exactly the part we want. Let's open up the `parse_page.py` file and get started.

The first thing we'll do is import the function we just wrote, at the very top of the page.

```
from fetch_page import fetch_page
```

Now, below the `if` line, let's make sure that function works now that we're calling it from another script.

```
    text = fetch_page("https://nicar22-scraping.herokuapp.com/")
    print(text)
```

Now let's import another library at the top of the page.

```
from bs4 import BeautifulSoup
```

Then create a new function, `parse_page`, that will take that text that was returned and use BeautifulSoup to parse the html. (We'll work through this step by step in class).

```
def parse_page(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    table = soup.find("table")

    data = []

    rows = table.find_all("tr")

    for row in rows:
        data_row = []
        cells = row.find_all("td")
        for cell in cells:
            data_row.append(cell.text)
        data.append(data_row)

    return data
```

Below where you declared your `text` variable, pass `text` into parse_page.

```
    data = parse_page(text)
    print(data)
```

Excellent! Now we have a list of data; all we need to do is write that to a csv file.


## 4: Writing data to a csv

This is the last, quick step before we finish our first scraper. Open the `write_to_csv.py` file and, at the top, import our fetching and parsing functions and another new library, called `csv`, which will let us easily read and write comma-separated value files.

Below the `if` statement, let's call our first two functions once again ()

```
    text = fetch_page("https://nicar22-scraping.herokuapp.com/simpletable/")
    data = parse_page(text)
```

We're going to write a new function using that csv library that will take as arguments a list of data and a filename and write out that data to the file.

```
def write_to_csv(data, outfile):
    f = open(outfile, "w")
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
    f.close
```

Nice! Now, just call that function at the bottom of your script.

```
    write_to_csv(data, "data/results.csv")
```

Nice job! You just wrote your first scraper and saved out the data in a format that you can use in your reporting.

## 5: Adding complexity.

Next, let's tackle a slightly more complex example. Click on over to "Results form" on the site, and 

We're going to work through this in class, but you can find our final version of this script in the `scrapers-solutions/fetch_form_pages.py`.