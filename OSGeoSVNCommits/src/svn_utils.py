#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 4:26:46 PM$"


import sqlite3
import os

# remember to change here based on platform, it would be different on window and unix
svn_xmls = "/xmls"
svn_analysis = "/analysis"

#print commit
def cmd_p(text):
    print "==",text,"=="

sqilte_file_path = "./db/svn_commits.db"


conn = sqlite3.Connection

def svn_get_conn():
    global conn
    return conn

def svn_db_connect():
    global conn
    conn = sqlite3.connect(sqilte_file_path);
    cmd_p(("connec to database: ",conn))

def svn_db_close():
    global conn
    conn.close()
    cmd_p("database connection closed")

svn_cwd = os.getcwd()+"/../"
os.chdir(svn_cwd)
svn_cwd = os.getcwd()
cmd_p("CWD: "+svn_cwd)

def cwd():
    os.chdir(svn_cwd)

#svn_cmds = {trunk:'hello'}


#svn_paths = []
svn_projects = [
    {'project':'deegree',   'root':'trunk',     'svn_path':"https://svn.wald.intevation.org/svn/deegree/base/trunk/"},
    {'project':'geomajas',  'root':'trunk',     'svn_path':"https://svn.geomajas.org/majas/trunk/"},
    {'project':'geoserver', 'root':'trunk',     'svn_path':"http://svn.codehaus.org/geoserver/trunk/"},
    {'project':'mapbender', 'root':'trunk',     'svn_path':"https://svn.osgeo.org/mapbender/trunk/"},
    {'project':'mapbuilder', 'root':'trunk',    'svn_path':"http://svn.codehaus.org/mapbuilder/trunk/"},
    {'project':'mapfish',   'root':'mapfish',   'svn_path':"http://www.mapfish.org/svn/mapfish/"},
    {'project':'mapguide',  'root':'trunk',     'svn_path':"https://svn.osgeo.org/mapguide/trunk/"},
    {'project':'mapserver', 'root':'trunk',     'svn_path':"http://svn.osgeo.org/mapserver/trunk/"},
    {'project':'openlayers', 'root':'trunk',    'svn_path':"http://svn.openlayers.org/trunk/"},
    {'project':'grass',     'root':'trunk',     'svn_path':"https://svn.osgeo.org/grass/grass/trunk/"},
    {'project':'qgis',      'root':'trunk',     'svn_path':"https://svn.osgeo.org/qgis/trunk/"},
    {'project':'gvsig',     'root':'trunk',     'svn_path':"http://subversion.gvsig.org/gvSIG/trunk/"},
    {'project':'fdo',       'root':'trunk',     'svn_path':"http://svn.osgeo.org/fdo/trunk/"},
    {'project':'gdal',      'root':'trunk',     'svn_path':"http://svn.osgeo.org/gdal/trunk/"},
    {'project':'geos',      'root':'trunk',     'svn_path':"http://svn.osgeo.org/geos/trunk/"},
    {'project':'geotools',  'root':'trunk',     'svn_path':"http://svn.osgeo.org/geotools/trunk/"},
    {'project':'metacrs',   'root':'metacrs',   'svn_path':"http://svn.osgeo.org/metacrs/"},
    {'project':'ossim',     'root':'trunk',     'svn_path':"http://svn.osgeo.org/ossim/trunk/"},
    {'project':'postgis',   'root':'trunk',     'svn_path':"http://svn.osgeo.org/postgis/trunk/"},
    {'project':'geonetwork', 'root':'trunk',    'svn_path':"https://geonetwork.svn.sourceforge.net/svnroot/geonetwork/trunk/"}
    #{'project':'', 'root':'', 'svn_path':""},
    #{"project":"mapfish", "root":"reference", "svn_path":"http://www.mapfish.org/svn/mapfish/framework/server/trunk/docs/reference/"}
    ]
#svn_deegree = {'project':'deegree', 'root':'test', 'svn_path':"https://svn.wald.intevation.org/svn/deegree/base/trunk/test/"}
#svn_mapfish= {"project":"mapfish", "reference":"test", "svn_path":"http://www.mapfish.org/svn/mapfish/framework/server/trunk/docs/reference/"}

svn_tags = [
    {'project':'deegree',   'root':'trunk',     'svn_path':"https://svn.wald.intevation.org/svn/deegree/base/tags/"},
    {'project':'geomajas',  'root':'trunk',     'svn_path':"https://svn.geomajas.org/majas/tags/"},
    {'project':'geoserver', 'root':'trunk',     'svn_path':"http://svn.codehaus.org/geoserver/tags/"},
    {'project':'mapbender', 'root':'trunk',     'svn_path':"https://svn.osgeo.org/mapbender/tags/"},
    {'project':'mapbuilder', 'root':'trunk',    'svn_path':"http://svn.codehaus.org/mapbuilder/tags/"},
    #{'project':'mapfish',   'root':'mapfish',   'svn_path':"http://www.mapfish.org/svn/mapfish/"},
    {'project':'mapguide',  'root':'trunk',     'svn_path':"https://svn.osgeo.org/mapguide/tags/"},
    {'project':'mapserver', 'root':'trunk',     'svn_path':"http://svn.osgeo.org/mapserver/tags/"},
    {'project':'openlayers', 'root':'trunk',    'svn_path':"http://svn.openlayers.org/tags/"},
    {'project':'grass',     'root':'trunk',     'svn_path':"https://svn.osgeo.org/grass/grass/tags/"},
    {'project':'qgis',      'root':'trunk',     'svn_path':"https://svn.osgeo.org/qgis/tags/"},
    {'project':'gvsig',     'root':'trunk',     'svn_path':"http://subversion.gvsig.org/gvSIG/tags/"},
    {'project':'fdo',       'root':'trunk',     'svn_path':"http://svn.osgeo.org/fdo/tags/"},
    {'project':'gdal',      'root':'trunk',     'svn_path':"http://svn.osgeo.org/gdal/tags/"},
    {'project':'geos',      'root':'trunk',     'svn_path':"http://svn.osgeo.org/geos/tags/"},
    {'project':'geotools',  'root':'trunk',     'svn_path':"http://svn.osgeo.org/geotools/tags/"},
    #{'project':'metacrs',   'root':'metacrs',   'svn_path':"http://svn.osgeo.org/metacrs/"},
    {'project':'ossim',     'root':'trunk',     'svn_path':"http://svn.osgeo.org/ossim/tags/"},
    {'project':'postgis',   'root':'trunk',     'svn_path':"http://svn.osgeo.org/postgis/tags/"},
    {'project':'geonetwork', 'root':'trunk',    'svn_path':"https://geonetwork.svn.sourceforge.net/svnroot/geonetwork/tags/"}
    ]

svn_branches = [
    {'project':'deegree',   'root':'trunk',     'svn_path':"https://svn.wald.intevation.org/svn/deegree/base/branches/"},
    {'project':'geomajas',  'root':'trunk',     'svn_path':"https://svn.geomajas.org/majas/branches/"},
    {'project':'geoserver', 'root':'trunk',     'svn_path':"http://svn.codehaus.org/geoserver/branches/"},
    {'project':'mapbender', 'root':'trunk',     'svn_path':"https://svn.osgeo.org/mapbender/branches/"},
    {'project':'mapbuilder', 'root':'trunk',    'svn_path':"http://svn.codehaus.org/mapbuilder/branches/"},
    #{'project':'mapfish',   'root':'mapfish',   'svn_path':"http://www.mapfish.org/svn/mapfish/"},
    {'project':'mapguide',  'root':'trunk',     'svn_path':"https://svn.osgeo.org/mapguide/branches/"},
    {'project':'mapserver', 'root':'trunk',     'svn_path':"http://svn.osgeo.org/mapserver/branches/"},
    {'project':'openlayers', 'root':'trunk',    'svn_path':"http://svn.openlayers.org/branches/"},
    {'project':'grass',     'root':'trunk',     'svn_path':"https://svn.osgeo.org/grass/grass/branches/"},
    {'project':'qgis',      'root':'trunk',     'svn_path':"https://svn.osgeo.org/qgis/branches/"},
    {'project':'gvsig',     'root':'trunk',     'svn_path':"http://subversion.gvsig.org/gvSIG/branches/"},
    {'project':'fdo',       'root':'trunk',     'svn_path':"http://svn.osgeo.org/fdo/branches/"},
    {'project':'gdal',      'root':'trunk',     'svn_path':"http://svn.osgeo.org/gdal/branches/"},
    {'project':'geos',      'root':'trunk',     'svn_path':"http://svn.osgeo.org/geos/branches/"},
    {'project':'geotools',  'root':'trunk',     'svn_path':"http://svn.osgeo.org/geotools/branches/"},
    #{'project':'metacrs',   'root':'metacrs',   'svn_path':"http://svn.osgeo.org/metacrs/"},
    {'project':'ossim',     'root':'trunk',     'svn_path':"http://svn.osgeo.org/ossim/branches/"},
    {'project':'postgis',   'root':'trunk',     'svn_path':"http://svn.osgeo.org/postgis/branches/"},
    {'project':'geonetwork', 'root':'trunk',    'svn_path':"https://geonetwork.svn.sourceforge.net/svnroot/geonetwork/branches/"}
    ]


if __name__ == "__main__":
    print "Hello World";
