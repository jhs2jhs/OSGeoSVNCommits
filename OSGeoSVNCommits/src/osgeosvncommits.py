# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 4:23:47 PM$"

import svn_utils
import svn_cmd_options

if __name__ == "__main__":
    svn_utils.cmd_p('-t trunk tags branches -ux true')
    svn_cmd_options.cmd_register()
    svn_cmd_options.cmd_parser()
    print "Hello World"
