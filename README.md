The instructions are mainly for Windows. See *Linux* instructions at the bottom for Linux computers. The instructions were tested on Ubuntu 22.04.


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
3. Write each row of data collected to ```servo_data.csv```. **IMPORTANT**: if ```servo_data.csv``` does not exists, the app will create it. If it already exists, it will override the previous contents. That is why the main code block has ```data_working_20240822.csv``` saved away as a different file.

Once the app finishes up and closes the webpage, it will run a final cleaning of the database, since some entry pieces were listed as blank by writing "(add)", which is troublesome for numerical columns. The app finishes its work by removing any such troublesome entries and leaving the cell blank.

## Querying
The method of querying requested was to be able to create a BETWEEN function for numerical columns, or a CONTAINS function, or some combination of those.

In other words, by implementing any combination of the BETWEEN and CONTAINS functions as seen in the example, one could implement any of the following queries and more:


1. 
   `Modulation="Analog" AND (Weight(oz) is less than 2) AND (Torque(oz-in) is greater than 50)`

2. 
   `Modulation="Digital" AND (L(in) is between 1 and 2) AND (Speed(s/60deg) is less than 0.1)`

3.  
   `Modulation="Analog" AND (H(in) is greater than 1.4) AND (Gear Material="Metal")`

4.  
   `Modulation="Digital" AND (Typical Price is less than 100) AND (Rotation="Dual Bearings")`

5.  
   `Modulation="Analog" AND (L(in) is greater than 1.5) AND (Torque(oz-in) is less than 60)`

6.   
   `Modulation="Digital" AND (Weight(oz) is between 1 and 2) AND (Torque(oz-in) is greater than 90)`

7.  
   `Modulation="Analog" AND (W(in) is less than 0.8) AND (Speed(s/60deg) is greater than 0.15)`

8.  
   `Modulation="Digital" AND (H(in) is between 1.2 and 1.5) AND (Motor Type="Coreless")`

NOTE: Less than or Greater than can be implemented using the BETWEEN function by using a lower bound of 0 or an upper bound of infinity, respectively.

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
