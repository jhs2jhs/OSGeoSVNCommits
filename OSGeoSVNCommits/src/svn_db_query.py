#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 5:01:29 PM$"

import sqlite3
from svn_utils import cmd_p

conn = sqlite3.Connection

def svn_db_connect():
    global conn
    #db_file_path = "C:\osgeo\svn_commits\code v1.1\svn_commits.db"
    #db_file_path = "C:\osgeo\svn_commits\svn_commits.db"
    db_file_path = "./svn_commits.db"
    conn = sqlite3.connect(db_file_path)

def svn_db_close():
    global conn
    conn.close()


author_project = '''
        SELECT
            COUNT(svn_revision.revision_id) AS revision_count,
            svn_commits.author_id,
            svn_author.author_name,
            svn_project.project_id,
            svn_project.project_name
        FROM svn_revision, svn_project, svn_commits, svn_author
        WHERE
            svn_revision.project_id = svn_project.project_id AND
            svn_revision.revision_id = svn_commits.revision_id AND
            svn_commits.author_id = svn_author.author_id
        GROUP BY
            svn_revision.project_id,
            svn_commits.author_id
        ''' 
def author_project_o():
    global conn
    db_query = author_project
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    txt = open("./author_project_o.txt", "w")
    out = ("index, \tauthor_id , \tauthor_name , \tproject_id ,\tproject_name , \trevision_count")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[1])+" , \t"+row[2]+" , \t"+str(row[3])+" ,\t"+row[4]+" , \t"+str(row[0]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()




author_projects_count = '''
        SELECT
            COUNT(project_id) AS project_count,
            author_id,
            author_name
        FROM ('''+author_project+''')
        GROUP BY author_id
        ORDER BY project_count
        '''
def author_projects_count_0():
    global conn
    db_query = author_projects_count ###
    print db_query
    c = conn.cursor()
    c.execute(db_query, ) ##
    txt = open("./author_projects_count_0.txt", "w") ##
    out = ("index, \author_id , \tauthor_name , \tproject_count")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[1])+" , \t"+row[2]+" , \t"+str(row[0]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()



author_projects_more_than_2 = '''
        SELECT
            project_count,
            author_id,
            author_name
        FROM ('''+author_projects_count+''')
        WHERE project_count > 1
        '''
def author_projects_more_than_2_0():
    global conn
    db_query = author_projects_more_than_2 ###
    print db_query
    c = conn.cursor()
    c.execute(db_query, ) ##
    txt = open("./author_projects_more_than_2_0.txt", "w") ##
    out = ("index, \author_id , \tauthor_name , \tproject_count")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[1])+" , \t"+row[2]+" , \t"+str(row[0]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()


s_author_with_id_project = '''
        SELECT
            author_id,
            author_name,
            project_id,
            project_name,
            revision_count
        FROM ('''+author_project+''')
        WHERE author_id = ?
        '''
def s_author_with_id_project_o(aid):
    global conn
    db_query = s_author_with_id_project ###
    print db_query
    c = conn.cursor()
    c.execute(db_query, (aid, )) ##
    txt = open("./s_author_with_id_project_o.txt", "w") ##
    out = ("index, \tauthor_id , \tauthor_name , \tproject_id ,\tproject_name , \trevision_count")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[0])+" , \t"+row[1]+" , \t"+str(row[2])+" ,\t"+row[3]+" , \t"+str(row[4]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()





    
author_project_row_id = '''
        SELECT
            rowid,
            project_id
        FROM
        (
        SELECT
            svn_revision.project_id
        FROM svn_commits, svn_author, svn_time, svn_revision, svn_project
        WHERE
            svn_commits.author_id = svn_author.author_id AND
            svn_author.author_id = 189 AND
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id
        GROUP BY
            svn_project.project_id
        ORDER BY
            svn_project.project_id
        )
        '''
author_revisions = '''
        SELECT
            svn_commits.author_id,
            svn_author.author_name,
            svn_commits.revision_id,
            STRFTIME('%Y-%m-%d %H:%M:%S', svn_time.timestamp),
            svn_revision.project_id,
            svn_project.project_name
        FROM svn_commits, svn_author, svn_time, svn_revision, svn_project
        WHERE
            svn_commits.author_id = svn_author.author_id AND
            svn_author.author_id = ? AND
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id
        ORDER BY
            svn_project.project_id, 
            svn_time.timestamp 
        '''
def author_revisions_o(aid):
    global conn
    db_query = author_revisions ##
    print db_query
    c = conn.cursor()
    c.execute(db_query, (aid, ))
    txt = open("./author_revisions_o-"+str(aid)+".txt", "w")
    out = ("index,\tauthor_id,\tauthor_name,\trevision_id,\ttimestamp,\tproject_id,\tproject_name ")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+",\t"+str(row[0])+",\t"+row[1]+",\t"+str(row[2])+",\t"+str(row[3])+",\t"+str(row[4])+",\t"+str(row[5]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()


# project authors works on. 
project_revisions = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_commits.revision_id,
            STRFTIME('%Y-%m-%d %H:%M:%S', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''
project_revisions_max = '''
        SELECT
            project_id, project_name, revision_id, timestamp
        FROM
            ('''+project_revisions+''')
        ORDER BY
            timestamp DESC
        LIMIT 1
        '''
project_revisions_min = '''
        SELECT
            project_id, project_name, revision_id, timestamp 
        FROM
            ('''+project_revisions+''')
        WHERE
            STRFTIME('%Y', timestamp) > '1990'
        ORDER BY
            timestamp ASC
        LIMIT 1
        '''
def project_revisions_o():
    global conn
    txt = open("./project_revisions.txt", "w")
    out = ("index,\tproject_id,\tproject_name,\trevision_id,\timestamp")
    print out
    txt.write(out+"\n")
    db_query = project_revisions_max ##
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    row = c.fetchone()
    out = ("max,\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3]))
    print out
    txt.write(out+"\n")
    c.close()
    db_query = project_revisions_min ##
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    row = c.fetchone()
    out = ("min,\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3]))
    print out
    txt.write(out+"\n")
    c.close()
    db_query = project_revisions ##
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    i = 1
    for row in c:
        out = (str(i)+",\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()


# project authors works on.
project_revisions_release_tags = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_commits.revision_id,
            STRFTIME('%Y-%m-%d %H:%M:%S', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project, svn_tags
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND
            svn_revision.revision_id = svn_tags.revision_id
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''
project_revisions_release_branches = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_commits.revision_id,
            STRFTIME('%Y-%m-%d %H:%M:%S', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project, svn_branches
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND
            svn_revision.revision_id = svn_branches.revision_id
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''
def project_revisions_release_o(type):
    global conn
    txt = open("./project_revisions_"+type+".txt", "w")
    out = ("index,\tproject_id,\tproject_name,\trevision_id,\timestamp")
    print out
    txt.write(out+"\n")
    if type == 'tags':
        print type
        db_query = project_revisions_release_tags
    elif type == 'branches':
        print type
        db_query = project_revisions_release_branches
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    i = 1
    for row in c:
        out = (str(i)+",\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()

if __name__ == "__main__":
    print "Hello World";
