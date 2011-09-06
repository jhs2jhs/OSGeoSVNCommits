#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 4:59:46 PM$"

import os
from svn_utils import cmd_p, svn_xmls, cwd, svn_cwd, svn_projects, svn_tags, svn_analysis
import commands
from svn_xml import svn_xml_parse_first, svn_xml_parse_nonfirst

def correct_path(dir):
    #new_dir = svn_cwd+"./"+dir
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)

def check_xml_folder():
    correct_path(svn_cwd+svn_xmls)
    #cmd_p(os.getcwd())
    cwd()


def check_analysis_folder():
    correct_path(svn_cwd+svn_analysis)
    #cmd_p(os.getcwd())
    cwd()

def svn_check_path():
    for project in svn_projects:
        cwd()
        name = project['project']
        path = project['svn_path']
        correct_path(name)
        os.system("svn checkout "+path)
    cwd()
    print os.getcwd()
        

def svn_update_path():
    for project in svn_projects:
        cwd()
        name = project['project']
        root = project['root']
        correct_path(name)
        correct_path(root)
        os.system("svn update ")
        os.system("svn log -v --xml > "+name+".xml")
        xml = ""+name+".xml"
        if os.path.exists(xml):
            print "copy "+xml+" "+svn_cwd+svn_xmls
            os.system("copy "+xml+" "+svn_cwd+svn_xmls)
    cwd()
    print os.getcwd()



def svn_db_commits(first = 0):
    cwd()
    os.chdir("."+svn_xmls)
    for project in svn_projects:
        name = project['project']
        file_name = (name+".xml")
        cmd_p(("Start to commit the db in project: "+name))
        if os.path.exists(file_name):
            if first == 0:
                svn_xml_parse_first(file_name, name)
            else:
                svn_xml_parse_nonfirst(file_name, name)
        else:
            print "** "+name+" xml file not find ** "
    




if __name__ == "__main__":
    print "Hello World";
