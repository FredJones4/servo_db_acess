Reccomendation is to do this on Windows for now, until a linux version can be added. Instructions for how to alter for Linux and allow the app to run in the background are found below.


# Design
This project is designed to take the [Servo Database website](https://servodatabase.com/servos/all?page=1) and create a more efficient manner of querying.

The design process was as follows:
1. Grab the Json element for one page of the website, out of its 101 copies of its pages.
2. Write code to, using the Selenium library, query its XPaths based off the setup of that JSON Element from its html (found by using the "inspect" feature on Windows Chrome).
3. Alter code to appropriately clean the data for proper querying.
4. Write code to appropriately query the data as requested.

The method of querying requested was to be able to create a BETWEEN function for numerical columns. However, since it was so quick and easy, a feature that matches all of a certain name was also attached.

An important discovery was that the encoding of the text for the csv created needed to be hard-encoded to UTF-8, which is usually standard. An example of this is seen in ```nonWorkingData_not_utf8.csv``.

# Application

## Web Scraping

Luckily, the website is set up such that each page's URL only changes by one character: its index. That made coding much simpler; one would have needed to find the button to have Selenium click, which would have been slightly more  complicated.

Until it is done, the app will:
1. keep open an automated webpage with the site, printing the iteration of page it is on for debugging purposes.
2. Grab all the data requested, cleaning it as it goes
3. Writing each row of data collected to ```servo_data.csv```. **IMPORTANT**: if ```servo_data.csv``` does not exists, the app will create it. If it already exists, it will override the previous contents. That is why the main code block has ```data_working_20240822.csv``` saved away as a different file.
4.  Finish up and close the app.

## Querying
The method of querying requested was to be able to create a BETWEEN function for numerical columns. However, since it was so quick and easy, a feature that matches all of a certain name was also attached.

The process is as follows:
1. Based off of user-input values (either for matching or range), the program will query the specified .csv file (default is ```servo_data.csv```).
2. The results will be saved to a new .csv file with the user's preference saved.

# Future

This app was very quick to code up thanks to similar experience in a previous project and the capability of AI to write out the monotonous details of XPaths and cleaning up. Monotony is where AI excels.

Other databases online could be queried in similar ways. Support with MongoDB could be interesting.




# Linux Instructions:


The provided code can be adapted to work on Linux by using the `webdriver.Chrome` option with the path to your Chromium driver. Here's how to modify the code:

**1. Install Chromium Driver:**

First, you need to install the ChromeDriver that works with your Chromium version. You can download the appropriate version from the official ChromeDriver download page: [https://developer.chrome.com/docs/chromedriver/downloads](https://developer.chrome.com/docs/chromedriver/downloads)

**2. Specify Driver Path:**

Modify the line that initializes the Chrome driver:

```python
# Replace with the actual path to your ChromeDriver
chromedriver_path = "/path/to/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver_path)
```

**3. (Optional) Set Up Headless Mode (if preferred):**

If you don't need a graphical browser window to open, you can run Chrome in headless mode by adding the following option:

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
```

**4. Run the Script:**

Save the modified script and run it on your Linux terminal. 

**Additional Considerations:**

* Make sure the `chromedriver` binary has executable permissions. You can use `chmod +x /path/to/chromedriver` to set them.
* If you encounter issues with compatibility between Chromium and ChromeDriver versions,  download a ChromeDriver version that matches your Chromium browser version.

**Alternatives:**

* **Use Firefox with GeckoDriver:** You can use Firefox and the GeckoDriver for web scraping tasks. The setup process would be similar, but you'd use `webdriver.Firefox` and the GeckoDriver executable path.
* **Headless Browsers:** Several headless browsers like PhantomJS can be used for web scraping, but their support might be limited.

Remember, web scraping can sometimes violate website terms of service.  It's important to check the website's guidelines before scraping data.
