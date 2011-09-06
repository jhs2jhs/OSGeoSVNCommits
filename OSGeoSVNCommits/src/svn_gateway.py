#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 4:57:49 PM$"

import svn_utils
from svn_utils import cmd_p, conn, svn_db_close
from svn_db_operation import sqlite_init
from svn_folder import svn_check_path, svn_update_path, svn_db_commits
from svn_log import svn_log_xml, svn_log_update, svn_tags_log_update, svn_tags_log_xml, svn_branches_log_update, svn_branches_log_xml
import time
import os
from xml.dom.minidom import parse, parseString
from svn_xml import svn_commit_parse
import svn_db_query

# ignore this method, as it is no loner used
def main_old_download_source_first():
    first = 0
    cmd_p("Main start")
    if (first == 0):
        sqlite_init()
        #svn_check_path()
    svn_update_path()
    svn_db_commits(first)
    svn_db_close
    cmd_p("finish")

def main_trunk(first):
    cmd_p("main start: trunk")
    print ("Total trunk: "+str(len(svn_utils.svn_projects)))
    if (first == 0):
        svn_log_update()
    svn_log_xml(first)
    cmd_p("finish: trunk")

def main_tags(first):
    cmd_p("Main start: tags")
    print ("Total trunk: "+str(len(svn_utils.svn_tags)))
    if (first == 0):
        svn_tags_log_update()
    svn_tags_log_xml(first)
    cmd_p("finish: tags")

def main_branches(first):
    cmd_p("Main start: branches")
    print ("Total branches: "+str(len(svn_utils.svn_branches)))
    if (first == 0):
        svn_branches_log_update()
    svn_branches_log_xml(first)
    cmd_p("finish: branches")


if __name__ == "__main__":
    print "Hello World";
