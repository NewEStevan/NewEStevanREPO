import xbmc
import tools

def debug(message):
    
    log_enabled = tools.getSetting("debug")
    
    if log_enabled == "true":
    xbmc.log("NewEStevanSOPA: " + message)