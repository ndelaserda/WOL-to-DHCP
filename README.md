# WOL-to-DHCP
 Scraping mac address from wake on lan to create DHCP reserve
 
# What is Wake On LAN

Wake On LAN is a windows application from Nirsoft that allows me to add in multiple PCs via hostname into a group, and boot them if they are off with a click of the button. All the machines need to have wake on lan enabled on the NIC. This is convenient for me as our eSports lab is made up of 25 machines, and it's very nice to be able to boot all these machines at once if I need to push out software or updates. 

# Why?
I need to setup a static IP on all of our eSports machines. This will allow me to assign a custom rule set to them in LightSpeed Rocket. Over the summer I setup these 25 computers in Wake On Lan, where their MAC information is conveniently able to be exported out into a .xml file with their PC name and MAC. Rather then going to each machine and getting the MAC, I figured I'd try out my Python skills and try and extract the mac address from the .xml in Wake on lan, and then use DHCP Powershell to bulk add them into their own DHCP reservations.

# Tasks
~~I'm going to start out by creating a Jupyter notebook to get the kinks worked out, and then once I get the hang of things, I'll throw it into a .py~~

- [x] get base algo working in jupyter
- [x] transfer code over to .py script
- [x] make string extraction dynamic rather then using static index
- [ ] try condensing 2 functions into 1

# Updates

## ~~12-10-19~~
~~Final .py has been created. I will come back to this and make it modular so that the script will grab whatever is in between the tags Name and MAC rather then relying on index position which would change depending on Name length.~~

## 12-11-19
Added 2 new functions, `extract_name()` and `extract_mac()` which goes through and checks where the Name and Mac tags are in the speficic line pulled from the .xml. It then creates a substring of the text in between the opening and closing of those tags. This will allow the script to pull the name and mac from the line regardless of their length. This is also a nice function structure I can use to pull info from other tags down the road. 
