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
sqilte_file_path = "./db/svn_commits.db"

#print commit
def cmd_p(text):
    print "==",text,"=="

def cwd():
    os.chdir(svn_cwd)
    
    
def pwd():
    return os.getcwd()

svn_cwd = os.getcwd()+"/../"
os.chdir(svn_cwd)
svn_cwd = os.getcwd()
cmd_p("CWD: "+svn_cwd)

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

conn = sqlite3.Connection
conn = svn_db_connect()



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
    {'project':'geonetwork', 'root':'trunk',    'svn_path':"https://geonetwork.svn.sourceforge.net/svnroot/geonetwork/trunk/"},
    #{'project':'', 'root':'', 'svn_path':""},
    {"project":"mapfish", "root":"trunk", "svn_path":"http://www.mapfish.org/svn/mapfish/framework/server/trunk"}
    ]
#svn_deegree = {'project':'deegree', 'root':'test', 'svn_path':"https://svn.wald.intevation.org/svn/deegree/base/trunk/test/"}
#svn_mapfish= {"project":"mapfish", "reference":"test", "svn_path":"http://www.mapfish.org/svn/mapfish/framework/server/trunk/docs/reference/"}

svn_tags = [
    {'project':'deegree',   'root':'trunk',     'svn_path':"https://svn.wald.intevation.org/svn/deegree/base/tags/"},
    {'project':'geomajas',  'root':'trunk',     'svn_path':"https://svn.geomajas.org/majas/tags/"},
    {'project':'geoserver', 'root':'trunk',     'svn_path':"http://svn.codehaus.org/geoserver/tags/"},
    {'project':'mapbender', 'root':'trunk',     'svn_path':"https://svn.osgeo.org/mapbender/tags/"},
    {'project':'mapbuilder', 'root':'trunk',    'svn_path':"http://svn.codehaus.org/mapbuilder/tags/"},
    {'project':'mapfish',   'root':'trunk',   'svn_path':"http://www.mapfish.org/svn/mapfish/framework/server/tags"},
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
    {'project':'mapfish',   'root':'trunk',   'svn_path':"http://www.mapfish.org/svn/mapfish/framework/server/branches"},
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

svn_incubations = [
    #{'project':'deegree',   'start':'09/06/2008',     'end':"07/02/2010"},
    {'project':'geomajas',  'start':'09/03/2010',     'end':"22/11/2010"},
    {'project':'geoserver', 'start':'09/11/2009',     'end':""},
    #{'project':'mapbender', 'start':'01/02/2006',     'end':"19/07/2006"},#http://www.geoconnexion.com/uploads/mapbender_intv7i2.pdf
    {'project':'mapbuilder', 'start':'01/02/2006',    'end':"26/10/2006"},#http://docs.codehaus.org/display/MAP/Strategic+Direction
    {'project':'mapfish',   'start':'09/11/2009',   'end':""},
    {'project':'mapguide',  'start':'01/03/2006',     'end':"06/03/2007"},#http://en.wikipedia.org/wiki/MapGuide_Open_Source
    {'project':'mapserver', 'start':'01/02/2006',     'end':"16/12/2008"},#http://trac.osgeo.org/mapserver/wiki/MapServerHistory
    {'project':'openlayers', 'start':'25/02/2006',    'end':"16/12/2007"},
    {'project':'grass',     'start':'01/02/2006',     'end':"12/02/2008"},
    #{'project':'qgis',      'start':'06/03/2007',     'end':"13/03/2008"},
    {'project':'gvsig',     'start':'07/09/2007',     'end':""},
    {'project':'geonetwork', 'start':'25/01/2007',    'end':"21/06/2008"},
    {'project':'gdal',      'start':'01/02/2006',     'end':"12/02/2008"},
    {'project':'geos',      'start':'07/11/2007',     'end':""},
    {'project':'geotools',  'start':'01/02/2006',     'end':"18/07/2008"},
    #{'project':'metacrs',   'start':'01/09/2008',   'end':""},
    {'project':'ossim',     'start':'01/02/2006',     'end':"01/06/2009"},
    {'project':'postgis',   'start':'06/08/2009',     'end':""},
    #{'project':'fdo',       'start':'06/03/2007',     'end':"12/02/2008"},
    ]
    
svn_dependency = [
    #{'project':'deegree',   'start':'09/06/2008',     'end':"07/02/2010"},
    #{'project':'geomajas',  'start':'09/03/2010',     'end':"22/11/2010"},
    {'project':'geoserver', 'start':'09/11/2009',     'end':""},
    #{'project':'mapbender', 'start':'01/02/2006',     'end':"19/07/2006"},#http://www.geoconnexion.com/uploads/mapbender_intv7i2.pdf
    #{'project':'mapbuilder', 'start':'01/02/2006',    'end':"26/10/2006"},#http://docs.codehaus.org/display/MAP/Strategic+Direction
    #{'project':'mapfish',   'start':'09/11/2009',   'end':""},
    #{'project':'mapguide',  'start':'01/03/2006',     'end':"06/03/2007"},#http://en.wikipedia.org/wiki/MapGuide_Open_Source
    #{'project':'mapserver', 'start':'01/02/2006',     'end':"16/12/2008"},#http://trac.osgeo.org/mapserver/wiki/MapServerHistory
    #{'project':'openlayers', 'start':'25/02/2006',    'end':"16/12/2007"},
    #{'project':'grass',     'start':'01/02/2006',     'end':"12/02/2008"},
    #{'project':'qgis',      'start':'06/03/2007',     'end':"13/03/2008"},
    #{'project':'gvsig',     'start':'07/09/2007',     'end':""},
    #{'project':'geonetwork', 'start':'25/01/2007',    'end':"21/06/2008"},
    #{'project':'gdal',      'start':'01/02/2006',     'end':"12/02/2008"},
    #{'project':'geos',      'start':'07/11/2007',     'end':""},
    {'project':'geotools',  'start':'01/02/2006',     'end':"18/07/2008"},
    #{'project':'metacrs',   'start':'01/09/2008',   'end':""},
    #{'project':'ossim',     'start':'01/02/2006',     'end':"01/06/2009"},
    #{'project':'postgis',   'start':'06/08/2009',     'end':""},
    #{'project':'fdo',       'start':'06/03/2007',     'end':"12/02/2008"},
    ]
    
    
'''
svn_incubations = [
    #{'project':'deegree',   'start':'09/06/2008',     'end':"07/02/2010"},
    #{'project':'geomajas',  'start':'09/03/2010',     'end':"22/11/2010"},
    {'project':'geoserver', 'start':'01/02/2006',     'end':"11/11/2009"},
    #{'project':'mapbender', 'start':'01/02/2006',     'end':"19/07/2006"},#http://www.geoconnexion.com/uploads/mapbender_intv7i2.pdf
    #{'project':'mapbuilder', 'start':'01/02/2006',    'end':"26/10/2006"},#http://docs.codehaus.org/display/MAP/Strategic+Direction
    {'project':'mapfish',   'start':'09/11/2009',   'end':"11/11/2009"},
    #{'project':'mapguide',  'start':'01/03/2006',     'end':"06/03/2007"},#http://en.wikipedia.org/wiki/MapGuide_Open_Source
    {'project':'mapserver', 'start':'01/04/2007',     'end':"16/12/2008"},#http://trac.osgeo.org/mapserver/wiki/MapServerHistory
    {'project':'openlayers', 'start':'25/01/2007',    'end':"16/11/2007"},
    {'project':'grass',     'start':'01/02/2006',     'end':"12/02/2008"},
    {'project':'qgis',      'start':'06/03/2007',     'end':"13/03/2008"},
    {'project':'gvsig',     'start':'07/09/2007',     'end':""},
    {'project':'geonetwork', 'start':'25/01/2007',    'end':"21/06/2008"},
    {'project':'gdal',      'start':'01/02/2006',     'end':"12/02/2008"},
    {'project':'geos',      'start':'07/11/2007',     'end':""},
    {'project':'geotools',  'start':'01/02/2006',     'end':"18/07/2008"},
    #{'project':'metacrs',   'start':'01/09/2008',   'end':""},
    {'project':'ossim',     'start':'01/02/2006',     'end':"01/06/2009"},
    {'project':'postgis',   'start':'06/08/2009',     'end':""},
    #{'project':'fdo',       'start':'06/03/2007',     'end':"12/02/2008"},
    ]
'''


if __name__ == "__main__":
    print "Hello World";
