#!/usr/bin/env python3

# This script only works based on the criteria of the xml file in this list. I will later comback and optimize
# it so that whatever is inbetween the opening and closing tags will be scraped rather then based of length

computer_list = []

def extract_name(line):
    '''
        Checks to see where the positioning of the open and closing tag is, then extracts the text needed in between

        Specific to the Name tag
    '''
    tag_start = line.find('<Name>')
    tag_end = line.find('</Name>')
    name_sub = line[(tag_start + len('<Name>')):tag_end]
    return name_sub

def extract_mac(line):
    '''
        Checks to see where the positioning of the open and closing tag is, then extracts the text needed in between.

        Specific to the MAC tag
    '''
    tag_start = line.find('<MAC>')
    tag_end = line.find('</MAC>')
    mac_sub = line[(tag_start + len('<MAC>')):tag_end]
    return mac_sub

# Script will go through the .xml provided and look for 'Name' and 'MAC'. These are tags used in the xml file
# exported from Wake On Lan. Since it reads in order from line to line, the MAC address will always be linked to the Name tags
# above it
print('Reading from .xml ...')
for line in open('wakeonlan.xml'):
    name = ''
    mac = ''
    if 'Name' in line:
        name = extract_name(line)
        computer_list.append(name)
    elif 'MAC' in line:
        mac = extract_mac(line)
        computer_list.append(mac)

# Added in the scope of the DHCP scope these will be put into and crated an empty ip list
ip_scope = '10.85.64.0'
ip_address = []

# Fill list with IPs I will be using for my reservations
print('Creating IP\'s')
for x in range(100,125):
    ip_address.append('10.85.65.'+str(x))

# Open up batch.txt with the overwrite switch
batch_file = open('batch.csv','w+')

print('Writing to text file...')
# Write the initial columns headers required by DHCP Powershell
batch_file.write('ScopeId,IPAddress,Name,ClientId,Description')

# Couldnt figure out an easy way to run multiple variables that increment in a loop. So I decided to run a seperate counter
# That I manually increase. This counter needs to jump by 2 at the end of each loop, as the list i created earlier has the
# PC name in every other index followed by the mac addresss.
# The x variable in the for loop cycles through the list of avaiable IP addresses, so this was the easiest solution for me.
counter = 0
for ip in ip_address:
    batch_file.write('\n'+ip_scope+','+ip+','+computer_list[counter]+','+computer_list[counter+1]+',')
    counter += 2

print('Success!')
