#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 5:00:21 PM$"


import xml.dom.minidom
from svn_utils import cmd_p
from svn_db_operation import sqlite_exist_check, sqlite_insert_commit, sqlite_commit_max, sqlite_tags_exist_check, sqlite_tags_insert_commit, sqlite_branches_exist_check, sqlite_branches_insert_commit
import os

def svn_commit_parse(le, project):
    revision = le.getAttribute("revision")
    #print revision
    authors = le.getElementsByTagName("author")
    if authors.length > 0 and authors[0].childNodes.length > 0:
        author = authors[0].childNodes[0].nodeValue
    else:
        author = "unknow"
        #print author
    times = le.getElementsByTagName("date")
    if times.length > 0 and times[0].childNodes.length > 0:
        time = times[0].childNodes[0].nodeValue
    else:
        time = "0"
    #print time
    msgs = le.getElementsByTagName("msg")
    if (msgs.length > 0 and msgs[0].childNodes.length > 0):
        msg = msgs[0].childNodes[0].nodeValue
    else:
        msg = "none"
    #print msg
    paths = le.getElementsByTagName("paths")
    if paths.length > 0:
        files = []
        for path in paths[0].getElementsByTagName("path"):
            #print path.toxml()
            if path.childNodes.length > 0:
                to_path = path.childNodes[0].nodeValue
            else:
                to_path = "none"
            action = path.getAttribute("action")
            kind = path.getAttribute("kind")
            from_path = path.getAttribute("copyfrom-path")
            from_rev = path.getAttribute("copyfrom_rev")
            #print from_path
            file = {
                'path':to_path,
                'action':action,
                'kind':kind,
                'from_path':from_path,
                'from_rev':from_rev
                }
            #print file['from_path']
            files.append(file)
    else:
        files = []
    #print files
    commit = {
        "project":project,
        "revision":revision,
        "author":author,
        "msg":msg,
        "time":time,
        "file":files
        }
    #print commit
    check = sqlite_exist_check(commit)
    #print "check:",check
    if (check != 0):
        sqlite_insert_commit(commit)


def svn_tags_commit_parse(le, project):
    revision = le.getAttribute("revision")
    #print revision
    authors = le.getElementsByTagName("author")
    if authors.length > 0 and authors[0].childNodes.length > 0:
        author = authors[0].childNodes[0].nodeValue
    else:
        author = "unknow"
        #print author
    times = le.getElementsByTagName("date")
    if times.length > 0 and times[0].childNodes.length > 0:
        time = times[0].childNodes[0].nodeValue
    else:
        time = "0"
    #print time
    msgs = le.getElementsByTagName("msg")
    if (msgs.length > 0 and msgs[0].childNodes.length > 0):
        msg = msgs[0].childNodes[0].nodeValue
    else:
        msg = "none"
    #print msg
    paths = le.getElementsByTagName("paths")
    if paths.length > 0:
        files = []
        for path in paths[0].getElementsByTagName("path"):
            #print path.toxml()
            if path.childNodes.length > 0:
                to_path = path.childNodes[0].nodeValue
            else:
                to_path = "none"
            action = path.getAttribute("action")
            kind = path.getAttribute("kind")
            from_path = path.getAttribute("copyfrom-path")
            from_rev = path.getAttribute("copyfrom_rev")
            #print from_path
            file = {
                'path':to_path,
                'action':action,
                'kind':kind,
                'from_path':from_path,
                'from_rev':from_rev
                }
            #print file['from_path']
            files.append(file)
    else:
        files = []
    #print files
    commit = {
        "project":project,
        "revision":revision,
        "author":author,
        "msg":msg,
        "time":time,
        "file":files
        }
    #print commit
    check = sqlite_tags_exist_check(commit)
    #print "check:",check
    if (check != 0):
        sqlite_tags_insert_commit(commit)


def svn_branches_commit_parse(le, project):
    revision = le.getAttribute("revision")
    #print revision
    authors = le.getElementsByTagName("author")
    if authors.length > 0 and authors[0].childNodes.length > 0:
        author = authors[0].childNodes[0].nodeValue
    else:
        author = "unknow"
        #print author
    times = le.getElementsByTagName("date")
    if times.length > 0 and times[0].childNodes.length > 0:
        time = times[0].childNodes[0].nodeValue
    else:
        time = "0"
    #print time
    msgs = le.getElementsByTagName("msg")
    if (msgs.length > 0 and msgs[0].childNodes.length > 0):
        msg = msgs[0].childNodes[0].nodeValue
    else:
        msg = "none"
    #print msg
    paths = le.getElementsByTagName("paths")
    if paths.length > 0:
        files = []
        for path in paths[0].getElementsByTagName("path"):
            #print path.toxml()
            if path.childNodes.length > 0:
                to_path = path.childNodes[0].nodeValue
            else:
                to_path = "none"
            action = path.getAttribute("action")
            kind = path.getAttribute("kind")
            from_path = path.getAttribute("copyfrom-path")
            from_rev = path.getAttribute("copyfrom_rev")
            #print from_path
            file = {
                'path':to_path,
                'action':action,
                'kind':kind,
                'from_path':from_path,
                'from_rev':from_rev
                }
            #print file['from_path']
            files.append(file)
    else:
        files = []
    #print files
    commit = {
        "project":project,
        "revision":revision,
        "author":author,
        "msg":msg,
        "time":time,
        "file":files
        }
    #print commit
    check = sqlite_branches_exist_check(commit)
    #print "check:",check
    if (check != 0):
        sqlite_branches_insert_commit(commit)



def svn_xml_parse_nonfirst(xml_path, project):
    cmd_p("start to process xml file non first: "+xml_path)
    max = sqlite_commit_max(project)
    print "project="+project+" has max="+max
    dom = xml.dom.minidom.parse (xml_path)
    logs = dom.getElementsByTagName("log")
    for log in logs:
        les = log.getElementsByTagName("logentry")
        for le in les[0:]:
            if le.hasAttribute("revision"):
                revision = le.getAttribute("revision")
                if (int(revision) <= max):
                    print "** trunk_"+project+" xml db no need to update exising commits"
                    break
                else:
                    svn_commit_parse(le, project)
    cmd_p("trunk_"+project+" xml db update finish")
                    


def svn_xml_parse_first(xml_path, project):
    cmd_p("start to process xml file first: "+xml_path)
    print os.getcwd()
    dom = xml.dom.minidom.parse (xml_path)
    logs = dom.getElementsByTagName("log")
    for log in logs:
        #print log.tagName
        les = log.getElementsByTagName("logentry")
        cmd_p(("logentry counts = ",len(les)))
        for le in les[0:]:
            #print le.toxml()
            if le.hasAttribute("revision"):
                svn_commit_parse(le, project)
    cmd_p("trunk_"+project+" xml db insert finish")


def svn_tags_xml_parse_nonfirst(xml_path, project):
    cmd_p("start to process xml file non first: "+xml_path)
    max = sqlite_commit_max(project)
    print "project="+project+" has max="+max
    dom = xml.dom.minidom.parse (xml_path)
    logs = dom.getElementsByTagName("log")
    for log in logs:
        les = log.getElementsByTagName("logentry")
        for le in les[0:]:
            if le.hasAttribute("revision"):
                revision = le.getAttribute("revision")
                if (int(revision) <= max):
                    print "** trunk_"+project+" xml db no need to update exising commits"
                    break
                else:
                    svn_tags_commit_parse(le, project)
    cmd_p("tags_"+project+" xml db update finish")



def svn_tags_xml_parse_first(xml_path, project):
    cmd_p("start to process xml file first: "+xml_path)
    cmd_p(os.getcwd())
    dom = xml.dom.minidom.parse (xml_path)
    logs = dom.getElementsByTagName("log")
    for log in logs:
        #print log.tagName
        les = log.getElementsByTagName("logentry")
        cmd_p(("logentry counts = ",len(les)))
        for le in les[0:]:
            #print le.toxml()
            if le.hasAttribute("revision"):
                svn_tags_commit_parse(le, project)
    cmd_p("tags_"+project+" xml db insert finish")


def svn_branches_xml_parse_nonfirst(xml_path, project):
    cmd_p("start to process xml file non first: "+xml_path)
    max = sqlite_commit_max(project)
    print "project="+project+" has max="+max
    dom = xml.dom.minidom.parse (xml_path)
    logs = dom.getElementsByTagName("log")
    for log in logs:
        les = log.getElementsByTagName("logentry")
        for le in les[0:]:
            if le.hasAttribute("revision"):
                revision = le.getAttribute("revision")
                if (int(revision) <= max):
                    print "** branches_"+project+" xml db no need to update exising commits"
                    break
                else:
                    svn_branches_commit_parse(le, project)
    cmd_p("branches_"+project+" xml db update finish")



def svn_branches_xml_parse_first(xml_path, project):
    cmd_p("start to process xml file first: "+xml_path)
    cmd_p(os.getcwd())
    dom = xml.dom.minidom.parse (xml_path)
    logs = dom.getElementsByTagName("log")
    for log in logs:
        #print log.tagName
        les = log.getElementsByTagName("logentry")
        cmd_p(("logentry counts = ",len(les)))
        for le in les[0:]:
            #print le.toxml()
            if le.hasAttribute("revision"):
                svn_branches_commit_parse(le, project)
    cmd_p("branches_"+project+" xml db insert finish")




if __name__ == "__main__":
    print "Hello World";
