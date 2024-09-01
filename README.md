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

From the start of it running until it is done scraping, the app will:
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


## Download Chrome for Linux
1. Go to the [official download site for Chrome on Linux](https://support.google.com/chrome/a/answer/9025926?hl=en&ref_topic=9025817&sjid=9425450324191466168-NC).
2. Download the .deb file.
3. ```sudo dpkg -i <debian name>```

## 

 Perhaps VSCode or another text editor/IDE will set up its own virtual environment. That is encouraged.

Web scraping should work out of the box.
