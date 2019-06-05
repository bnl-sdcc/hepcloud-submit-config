#!/bin/env python
#
# 

from configparser import ConfigParser
import logging
import grp
import pwd

def create_mapfile(config, filepath):
    logging.debug("Using config: %s   writing to: %s" % (config, filepath))
    
    sect = config.get('groupmappings')



if __name__ == '__main__':
    CONFFILE = "/etc/condor/mkprojectnamemapfile.conf"
    MAPFILE = "/etc/condor/projectname.usermap"

    logging.basicConfig(format='%(asctime)s (UTC) [ %(levelname)s ] %(name)s %(filename)s:%(lineno)d %(funcName)s(): %(message)s')
    logging.getLogger().setLevel(logging.DEBUG)
    
    cp = ConfigParser()
    cp.read(CONFFILE)
     
    create_mapfile(cp, MAPFILE)

    