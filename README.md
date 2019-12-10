# WOL-to-DHCP
 Scraping mac address from wake on lan to create DHCP reserve

# Why?
 I need to setup a static IP on all of our eSports machines. This will allow me to assign a custom rule set to them in LightSpeed Rocket. Over the summer I setup these 25 computers in Wake On Lan, where their MAC information is stored. Rather then going to each machine and getting the MAC, I figured I'd try out my Python skills and try and extract the mac address from Wake on lan, and then use DHCP Powershell to bulk add them into their own DHCP reservations

# Process
I'm going to start out by creating a Jupyter notebook to get the kinks worked out, and then once I get the hang of things, I'll throw it into a .py

# Update 12-10-19
Final .py has been created. I will come back to this and make it modular so that the script will grab whatever is in between the tags <Name> and <MAC> rather then relying on index position which would change depending on <Name> length
