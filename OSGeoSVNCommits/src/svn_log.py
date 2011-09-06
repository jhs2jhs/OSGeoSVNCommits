#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 5:01:01 PM$"


from svn_utils import cwd, cmd_p, svn_xmls, svn_projects, svn_tags, svn_branches
import os
from svn_xml import svn_xml_parse_first, svn_xml_parse_nonfirst, svn_tags_xml_parse_first, svn_tags_xml_parse_nonfirst, svn_branches_xml_parse_first, svn_branches_xml_parse_nonfirst
import time

def ls(file_name):
    os.system("ls -l "+file_name)
    


def svn_log_time_record(type):
    time_str = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
    time_cmd = "echo "+time_str+" > timefile_"+type+".txt"
    os.system(time_cmd)
    ls("")
    print time_cmd

def svn_log_update():
    cwd()
    os.chdir("."+svn_xmls)
    for project in svn_projects:
        name = project['project']
        svn_path = project['svn_path']
        file_name = "trunk_"+name+".xml"
        cmd_svn_log = ("svn log "+svn_path+" -v --xml > "+file_name)
        print "CMD:"+cmd_svn_log
        os.system(cmd_svn_log)
        if os.path.exists(file_name):
            ls(file_name)
        else:
            print "** "+file_name+" file not find ** "
    svn_log_time_record("trunk_xml")

def svn_tags_log_update():
    cwd()
    os.chdir("."+svn_xmls)
    for project in svn_tags:
        name = project['project']
        svn_path = project['svn_path']
        file_name = "tags_"+name+".xml"
        cmd_svn_log = ("svn log "+svn_path+" -v --xml > "+file_name)
        print "CMD:"+cmd_svn_log
        os.system(cmd_svn_log)
        if os.path.exists(file_name):
            ls(file_name)
        else:
            print "** "+file_name+" file not find ** "
    svn_log_time_record("tags_xml")


def svn_branches_log_update():
    cwd()
    os.chdir("."+svn_xmls)
    for project in svn_branches:
        name = project['project']
        svn_path = project['svn_path']
        file_name = "branches_"+name+".xml"
        cmd_svn_log = ("svn log "+svn_path+" -v --xml > "+file_name)
        print "CMD:"+cmd_svn_log
        os.system(cmd_svn_log)
        if os.path.exists(file_name):
            ls(file_name)
        else:
            print "** "+file_name+" file not find ** "
    svn_log_time_record("branches_xml")


def svn_log_xml(first):
    cwd()
    os.chdir("."+svn_xmls)
    for project in svn_projects:
        name = project['project']
        file_name = "trunk_"+name+".xml"
        if os.path.exists(file_name):
            ls(file_name)
            if first == 0:
                svn_xml_parse_first(file_name, name)
            else:
                svn_xml_parse_nonfirst(file_name, name)
        else:
            print "** "+file_name+" file not find ** "
    svn_log_time_record("trunk_sqilte")

def svn_tags_log_xml(first):
    cwd()
    os.chdir("."+svn_xmls)
    for project in svn_tags:
        name = project['project']
        file_name = "tags_"+name+".xml"
        if os.path.exists(file_name):
            ls(file_name)
            if first == 0:
                svn_tags_xml_parse_first(file_name, name)
            else:
                svn_tags_xml_parse_nonfirst(file_name, name)
        else:
            print "** "+file_name+" file not find ** "
    svn_log_time_record("tags_sqilte")


def svn_branches_log_xml(first):
    cwd()
    os.chdir("."+svn_xmls)
    for project in svn_branches:
        name = project['project']
        file_name = "branches_"+name+".xml"
        if os.path.exists(file_name):
            ls(file_name)
            if first == 0:
                svn_branches_xml_parse_first(file_name, name)
            else:
                svn_branches_xml_parse_nonfirst(file_name, name)
        else:
            print "** "+file_name+" file not find ** "
    svn_log_time_record("branches_sqilte")


if __name__ == "__main__":
    print "Hello World";
