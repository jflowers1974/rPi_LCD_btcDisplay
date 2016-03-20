# rPi_LCD_btcDisplay
<h1>Raspberry Pi LCD diplaying information on bitcoin addresses </h1>

<h2>Motivation:</h2>  
The question of how to have an IoT like device display information on one's cold wallet came up in a recent forum posting.  I had a raspberry pi model B that was used initially for bitcoin mining (http://www.instructables.com/id/Bitcoin-Mining-using-Raspberry-Pi/), and having long since stopped, realized that I could still use the components for this idea.

<h2>Goal</h2>
Have a rPi with a LCD screen display information pertaining to bitcoin addresses of interest.


<h2>Hardware</h2>
<ol>
  <li> Raspberry Pi Model 1 Model B </li>
  <li> Adafruit RGB Negative 16x2 LCD+Keypad Kit for Raspberry Pi (https://www.adafruit.com/products/1110) </li>
</ol>

<h2>Files</h2>
<ol>
  <ul>bitcoinDisplay.py - the Main Program, be sure to make executable with chmod +x if you wish to autostart in the future </ul>
  <ul>addressBitcoin.txt - where all the Btc Addresses are kept </ul>
</ol>

<h2>Setup:</h2>
<ol>
  <li>Follow the instructions provided by adaFruit at https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/usage.  <p>Don't forget to make the needed modifications using the raspi-config utility. Only after the tests provided worked, should you continue.</li>
  <li> </li>
  <li>Auto running the script, use http://www.raspberrypi-spy.co.uk/2015/02/how-to-autorun-a-python-script-on-raspberry-pi-boot/.  <p> Just make sure that the python script is executable.  Furthermore, the instructions fail to mention the need to background this task by adding an '&' at the end.  <p>i.e. 
  <ol>
    <ul>sudo nano /etc/profile </ul>
    <ul>Scroll to the bottum and add:</ul>
    <ul>python /home/pi/rPi_LCD_bitcoinDisplay.py & </ul>
    <p>"sudo" is not needed, and the "&" is.
  </ol>
  </li>
</ol>
