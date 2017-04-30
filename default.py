# -*- coding: utf-8 -*-
#------------------------------------------------------------
# https://www.youtube.com/user/teamkosuke
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.MyZonKuliah'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "teamkosuke"

# Entry point
def run():
    plugintools.log("zonkuliah.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("zonkuliah.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="MY ZON KULIAH",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail=icon,
        folder=True )

    

run()