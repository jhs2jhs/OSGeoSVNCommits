#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 5:01:29 PM$"

import sqlite3
from svn_utils import cmd_p
import svn_utils
import matplotlib.pyplot as plt
import pylab
import matplotlib
from datetime import datetime, timedelta

conn = sqlite3.Connection

def svn_db_connect():
    global conn
    #db_file_path = "C:\osgeo\svn_commits\code v1.3\svn_commits.db"
    #db_file_path = "C:\osgeo\svn_commits\svn_commits.db"
    #db_file_path = "./svn_commits.db"
    #conn = sqlite3.connect(db_file_path)
    conn = svn_utils.svn_get_conn()

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
    out = ("index, \tauthor_id , \tauthor_name , \tproject_count")
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


class HowLongTimeTotal:
    def __init__(self):
        self.time = 0
        self.now_time = 0
        self.pre_time = 0
        self.duration = 0
        self.i = 0;
        
    def step(self, value):
        self.now_time = int(value)
        if (self.i != 0):
            self.duration = self.now_time - self.pre_time
            if self.duration > 0:
                self.time += self.duration
            else :
                self.time -= self.duration
        self.pre_time = self.now_time
        self.i = self.i + 1

    def finalize(self):
        return self.time

#GROUP BY svn_commits.idid
#HowLongTimeAverage(svn_time.timestamp) AS average
#strftime('%s', svn_time.timestamp)
hong_long_average_on_project_test = '''
        SELECT
            svn_commit_individual.idid,
            svn_commit_individual.revision_id,
            COUNT (svn_commit_individual.timestamp) AS times_count,
            HowLongTimeTotal(svn_commit_individual.timestamp) AS time_total
        FROM (
        SELECT
            svn_commits.idid,
            svn_commits.revision_id,
            svn_time.timestamp
        FROM
        ( SELECT
            '3' as idid,
            svn_commits.revision_id,
            svn_commits.time_id
            FROM svn_commits
            LIMIT 4
        ) AS svn_commits,
        ( SELECT
            svn_time.time_id,
            strftime('%s', svn_time.timestamp) AS timestamp
            FROM svn_time
        ) AS svn_time
        WHERE
            svn_commits.time_id = svn_time.time_id
        ORDER BY svn_time.timestamp ASC
        ) AS svn_commit_individual
        GROUP BY svn_commit_individual.idid

        LIMIT 100
        '''
#            svn_time.timestamp
hong_long_average_on_project = '''
        SELECT
            svn_commit_individual.revision_id,
            svn_commit_individual.author_id,
            svn_commit_individual.author_name,
            svn_commit_individual.project_id,
            svn_commit_individual.project_name,
            COUNT (svn_commit_individual.timestamp) AS times_count,
            HowLongTimeTotal(svn_commit_individual.timestamp) AS time_total
        FROM (
        SELECT
            svn_revision.revision_id,
            svn_author.author_id,
            svn_author.author_name,
            svn_revision.project_id,
            svn_project.project_name,
            svn_time.timestamp,
            svn_time.timestamp 
        FROM
            svn_commits, svn_revision, svn_project, svn_author,
            (SELECT
                svn_time.time_id,
                strftime('%s', svn_time.timestamp) AS timestamp
                FROM svn_time
                WHERE
                    STRFTIME('%Y', svn_time.timestamp) > '1990'
            ) AS svn_time 
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.author_id = svn_author.author_id AND 
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id 
        ORDER BY svn_revision.project_id, svn_author.author_id, svn_time.timestamp 
        ) AS svn_commit_individual 
        GROUP BY
            svn_commit_individual.project_id,
            svn_commit_individual.author_id
        ORDER BY
            svn_commit_individual.project_id,
            svn_commit_individual.author_id
        '''
def hong_long_average_on_project_o():
    global conn
    #conn.row_factory = sqlite3.Row
    conn.create_aggregate("HowLongTimeTotal", 1, HowLongTimeTotal)
    txt = open("./hong_long_average_on_project.txt", "w")
    out = ("index,\trevision_id,\tauthor_id,\tauthor_name,\tproject_id,\tproject_name,\ttimes_count,\ttime_total")
    print out
    txt.write(out+"\n")
    db_query = hong_long_average_on_project
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    i = 1
    for row in c:
        out = (str(i)+",\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3])+",\t"+str(row[4])+",\t"+str(row[5])+",\t"+str(row[6]))
        #out = (str(i)+",\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()



author_date_project = '''
        SELECT
            svn_author.author_id,
            svn_author.author_name,
            STRFTIME('%Y-%m-%d', svn_time.timestamp) AS date,
            STRFTIME('%H:%M:%S', svn_time.timestamp) AS time,
            svn_project.project_id,
            svn_project.project_name,
            svn_msg.msg 
        FROM
            (SELECT * FROM svn_commits WHERE svn_commits.author_id = 189) AS svn_commits, 
            svn_author, svn_time, svn_project, svn_revision, svn_msg
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.author_id = svn_author.author_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND
            svn_commits.msg_id = svn_msg.msg_id
        ORDER BY svn_author.author_id, svn_time.timestamp
        '''
def author_date_project_o():
    global conn
    txt = open("./author_date_project.txt", "w")
    out = ("index,\tauthor_id,\tauthor_name,\tdate,\ttime,\tproject_id,\tproject_name,\tmsg")
    print out
    txt.write(out+"\n")
    db_query = author_date_project
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    i = 1
    for row in c:
        out = (str(i)+",\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3])+",\t"+str(row[4])+",\t"+str(row[5])+",\t"+str(row[6]))
        #out = (str(i)+",\t"+str(row[0])+",\t"+str(row[1])+",\t"+str(row[2])+",\t"+str(row[3]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()


project_author = '''
        SELECT
            COUNT(author_id) AS author_count,
            project_id,
            project_name
        FROM ('''+author_project+''')
        GROUP BY project_id
        ORDER BY project_id
        '''
def project_authors_o():
    global conn
    db_query = project_author
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    txt = open("./project_author_o.txt", "w")
    out = ("index, \tproject_id , \tproject_name , \tauthor_count")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[0]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()


project_commits = '''
        SELECT
            COUNT(svn_revision.revision_id) AS commits_count,
            svn_project.project_id,
            svn_project.project_name
        FROM svn_revision, svn_project
        WHERE
            svn_revision.project_id = svn_project.project_id
        GROUP BY
            svn_revision.project_id
        '''
def project_commits_o():
    global conn
    db_query = project_commits
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    txt = open("./project_commits_o.txt", "w")
    out = ("index, \tproject_id ,\tproject_name , \tcommits_count")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[0]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()


author_project_spanning = '''
        SELECT
            COUNT(svn_revision.revision_id) AS revision_count,
            svn_commits.author_id,
            svn_author.author_name,
            svn_project.project_id,
            svn_project.project_name
        FROM
            svn_revision,
            svn_project,
            svn_commits,
            svn_author, 
            ('''+author_projects_more_than_2+''') AS author_spanning
        WHERE
            svn_revision.project_id = svn_project.project_id AND
            svn_revision.revision_id = svn_commits.revision_id AND
            svn_commits.author_id = svn_author.author_id AND
            svn_author.author_id = author_spanning.author_id
        GROUP BY
            svn_revision.project_id,
            svn_commits.author_id
        '''
project_author_spanning = '''
        SELECT
            COUNT(author_id) AS author_count,
            project_id,
            project_name
        FROM ('''+author_project_spanning+''')
        GROUP BY project_id
        ORDER BY project_id
        '''
def project_author_spanning_o():
    global conn
    db_query = project_author_spanning
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    txt = open("./project_author_spanning_o.txt", "w")
    out = ("index, \tproject_id , \tproject_name , \tauthor_count")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[0]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()

boundary_spanning_rate = '''
        SELECT
            project_author_spanning.author_count * 100 / project_author_total.author_count,
            project_author_total.project_id,
            project_author_total.project_name
        FROM
            ('''+project_author+''') AS project_author_total,
            ('''+project_author_spanning+''') AS project_author_spanning
        WHERE project_author_total.project_id = project_author_spanning.project_id
        ORDER BY project_author_total.project_id
        '''
def boundary_spanning_rate_o():
    global conn
    db_query = boundary_spanning_rate
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    txt = open("./boundary_spanning_rate_o.txt", "w")
    out = ("index, \tproject_id , \tproject_name , \tspanning_rate")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        out = (str(i)+", \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[0]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()
    txt.close()
    

    
'''project_tag = 
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_revision.revision_id, 
            STRFTIME('%Y-%m', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id 
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''        
project_tag = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_commits.revision_id,
            STRFTIME('%Y-%m', svn_time.timestamp) AS timestamp
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
project_tag_amount = '''
    SELECT 
        project_tag_amount.project_name,
        project_tag_amount.timestamp, 
        COUNT(project_tag_amount.revision_id) AS project_count
    FROM ('''+project_tag+''') AS project_tag_amount
    GROUP BY 
        project_tag_amount.project_name, 
        project_tag_amount.timestamp
'''        
project_trunk = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_revision.revision_id, 
            STRFTIME('%Y-%m', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id 
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''    
project_trunk_amount = '''
    SELECT 
        project_trunk_amount.project_name,
        project_trunk_amount.timestamp, 
        COUNT(project_trunk_amount.revision_id) AS project_count
    FROM ('''+project_trunk+''') AS project_trunk_amount
    GROUP BY 
        project_trunk_amount.project_name, 
        project_trunk_amount.timestamp
'''    



def project_trunk_history_amount_o():
    global conn
    db_query = project_trunk_amount
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    txt = open("./project_trunk_history_amount_o.txt", "w")
    out = ("index, \tproject_id , \tproject_name , \trevision_id, \tspanning_rate")
    print out
    txt.write(out+"\n")
    i = 1
    xs = []
    ys = []
    for row in c:
        x = []
        x.append(row[1])
        xs.append(x)
        y = []
        y.append(row[2])
        ys.append(x)
        #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
        out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()

def project_tag_history_amount_o():
    global conn
    db_query = project_tag_amount
    print db_query
    c = conn.cursor()
    c.execute(db_query, )
    txt = open("./project_tag_history_amount_o.txt", "w")
    out = ("index, \tproject_id , \tproject_name , \trevision_id, \tspanning_rate")
    print out
    txt.write(out+"\n")
    i = 1
    for row in c:
        #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
        out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2]))
        print out
        txt.write(out+"\n")
        i = i + 1
    c.close()




projects_multii = '''
    SELECT 
        svn_project.project_id, 
        svn_project.project_name 
    FROM 
        svn_project 
    WHERE 
        svn_project.project_name IN ("deegree", "geoserver")
'''
projects_multi = '''
    SELECT 
        svn_project.project_id, 
        svn_project.project_name 
    FROM 
        svn_project 
    WHERE 
        svn_project.project_name IN ?
'''
projects = '''
    SELECT svn_project.project_id, svn_project.project_name FROM svn_project 
'''
project = '''
    SELECT 
        svn_project.project_id, 
        svn_project.project_name 
    FROM 
        svn_project 
    WHERE 
        svn_project.project_name = ?
'''
project_trunk_single = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_revision.revision_id, 
            STRFTIME('%Y-%m', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND 
            svn_revision.project_id = ?
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''    
project_trunk_single_amount = '''
    SELECT 
        project_trunk_amount.project_name,
        project_trunk_amount.timestamp, 
        COUNT(project_trunk_amount.revision_id) AS project_count
    FROM ('''+project_trunk_single+''') AS project_trunk_amount
    GROUP BY 
        project_trunk_amount.project_name, 
        project_trunk_amount.timestamp
'''
project_tag_single = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_revision.revision_id, 
            STRFTIME('%Y-%m', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project, svn_tags
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND 
            svn_revision.revision_id = svn_tags.revision_id AND
            svn_revision.project_id = ?
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''    
project_tag_single_amount = '''
    SELECT 
        project_trunk_amount.project_name,
        project_trunk_amount.timestamp, 
        COUNT(project_trunk_amount.revision_id) AS project_count
    FROM ('''+project_tag_single+''') AS project_trunk_amount
    GROUP BY 
        project_trunk_amount.project_name, 
        project_trunk_amount.timestamp
'''
project_author_single = '''
        SELECT DISTINCT
            svn_revision.project_id,
            svn_project.project_name,
            STRFTIME('%Y-%m', svn_time.timestamp) AS timestamp, 
            svn_author.author_id
        FROM svn_commits, svn_time, svn_revision, svn_project, svn_tags, svn_author
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND 
            svn_revision.revision_id = svn_tags.revision_id AND
            svn_commits.author_id = svn_author.author_id AND 
            svn_revision.project_id = ?
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''    
project_author_single_amount = '''
    SELECT 
        project_trunk_amount.project_name,
        project_trunk_amount.timestamp, 
        COUNT(project_trunk_amount.author_id) AS project_count
    FROM ('''+project_author_single+''') AS project_trunk_amount
    GROUP BY 
        project_trunk_amount.project_name, 
        project_trunk_amount.timestamp
'''

def project_history_amount_multiplot_o():
    global conn
    #matplotlib.rcParams["figure.subplot.hspace"]=0.9
    matplotlib.rcParams["figure.subplot.left"]=0.05
    matplotlib.rcParams["figure.subplot.right"]=0.95
    matplotlib.rcParams["figure.subplot.top"]=0.95
    matplotlib.rcParams["figure.subplot.bottom"]=0.05
    db_query = projects_multii
    print db_query
    c = conn.cursor()
    #c.execute(db_query, (('(\"geoserver\", \"deegree\")'), ))
    c.execute(db_query,)
    #fig, axx = plt.subplots(20)
    #fig = pylab.figure()
    #fig = plt.figure()
    fig = plt.figure()
    #years = matplotlib.dates.YearLocator()
    #months = matplotlib.dates.MonthLocator()
    #years = matplotlib.dates.YearLocator()
    #print fig
    project_count = 0
    for row in svn_utils.svn_incubations:
        if (row["start"] != "") and (row["end"] != ""):
            project_count = project_count+1
    #project_count = project_count / 2
    #project_count = 1
    j = 0
    #for row in c:
    for row in svn_utils.svn_incubations:
     if (row["start"] != "") and (row["end"] != ""):
        db_query = project
        #print db_query
        c = conn.cursor()
        c.execute(db_query, (row["project"], ))
        #print row["start"], row["end"]
        rr = c.fetchone()
        project_id = rr[0]
        project_name = rr[1]
        xs_trunk = []
        ys_trunk = []
        i = 1
        txt = open("./history_svn_counts/project_history_amount_multiplot_o_trunk_"+str(project_id)+"_"+str(project_name)+".txt", "w")
        out = ("index, \tproject_id , \tproject_name , \tmonth, \tsvn_counts")
        #print out
        txt.write(out+"\n")
        db_query_single = project_trunk_single_amount
        c_trunk = conn.cursor()
        c_trunk.execute(db_query_single, (project_id, ))
        for r in c_trunk:
            month = r[1]
            # convert string into datetime
            month = datetime.strptime(month, '%Y-%m')
            if month.year < 1997:
                continue
            svn_count = r[2]
            xs_trunk.append(month)
            ys_trunk.append(svn_count)
            #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
            out = (str(i)+", \t"+str(r[0])+" , \t"+str(r[1])+" , \t"+str(r[2]))
            #print out
            txt.write(out+"\n")
            i = i + 1
        txt.close()
        xs_tag = []
        ys_tag = []
        i = 1
        txt = open("./history_svn_counts/project_history_amount_multiplot_o_tag_"+str(project_id)+"_"+str(project_name)+".txt", "w")
        out = ("index, \tproject_id , \tproject_name , \tmonth, \tsvn_counts")
        #print out
        txt.write(out+"\n")
        db_query_single = project_tag_single_amount
        c_tag = conn.cursor()
        c_tag.execute(db_query_single, (project_id, ))
        for r in c_tag:
            month = r[1]
            # convert string into datetime
            month = datetime.strptime(month, '%Y-%m')#+timedelta(days=15)
            if month.year < 1997:
                continue
            svn_count = r[2]
            xs_tag.append(month)
            ys_tag.append(svn_count)
            #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
            out = (str(i)+", \t"+str(r[0])+" , \t"+str(r[1])+" , \t"+str(r[2]))
            #print out
            txt.write(out+"\n")
            i = i + 1
        txt.close()
        '''xs_author = []
        ys_author = []
        i = 1
        txt = open("./history_svn_counts/project_history_amount_multiplot_o_author_"+str(project_id)+"_"+str(project_name)+".txt", "w")
        out = ("index, \tproject_id , \tproject_name , \tmonth, \tsvn_counts")
        #print out
        txt.write(out+"\n")
        db_query_single = project_author_single_amount
        c_author = conn.cursor()
        c_author.execute(db_query_single, (project_id, ))
        for r in c_author:
            month = r[1]
            # convert string into datetime
            month = datetime.strptime(month, '%Y-%m')+timedelta(days=15)
            svn_count = r[2]
            xs_author.append(month)
            ys_author.append(svn_count)
            #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
            out = (str(i)+", \t"+str(r[0])+" , \t"+str(r[1])+" , \t"+str(r[2]))
            #print out
            txt.write(out+"\n")
            i = i + 1
        txt.close()'''
        '''if (len(ys_trunk)>0 and len(ys_tag)>0):
            l_trunk = []
            l_trunk.extend(ys_trunk)
            l_trunk.sort()
            l_trunk.reverse()
            largest_trunk = l_trunk[0]
            l_tag = []
            l_tag.extend(ys_tag)
            l_tag.sort()
            l_tag.reverse()
            largest_tag = l_tag[0]
            print largest_trunk, largest_tag
            l = largest_trunk / largest_tag
            ys_tag = [y * l for y in ys_tag]
            print l'''
        '''subplot = axx[j]
        subplot.plot_date(xs, ys, xdate=True)
        subplot.set_title(str(project_name))
        subplot.
        j = j+1'''
        #plot_id = project_id+100
        #print plot_id
        width = 30
        left_or_right = 1
        if j % 2 != 0:
            left_or_right = 1
        ax_trunk = fig.add_subplot(project_count, left_or_right, project_count-j)
        #ax_trunk.plot_date(xs_trunk, ys_trunk, xdate=True, color="blue")
        ax_trunk.bar(xs_trunk, ys_trunk, width, color='b')
        ax_trunk.yaxis.tick_left()
        ax_trunk.minorticks_off()
        #ax_trunk.majorticks_off()
        #yticklavel_min = ax_trunk.get_yticklabels()[0]
        #print yticklavel_min
        #yticklavel_min = ax_trunk.get_yticklabels()
        for label in ax_trunk.get_yticklabels():
            #print label
            label.set_visible(False)
        yticklabels_length = len(ax_trunk.get_yticklabels())
        #ax_trunk.get_yticklabels()[0].set_visible(True)
        ax_trunk.get_yticklabels()[yticklabels_length - 1].set_visible(True)
        ax_trunk.get_yticklabels()[yticklabels_length - 1].set_color("b")
        #ax_trunk.get_yticklabels()[0] = yticklavel_min
        #ax_trunk.tick_params(axis='both', color='b')
        #print ax_trunk.get_ymajorticklabels()
        #ax_trunk.minorticks_off()
        #ax_trunk.set_ylabel("hello")
        #ax_trunk.bar(xs_trunk, ys_trunk, width, color='b')
        #ax_tag = fig.add_subplot(211)
        #ax_tag = ax_trunk.twinx()
        #ax_trunk.plot(xs_tag, ys_tag, 'ro')
        ##ax_tag = fig.add_subplot(project_count, left_or_right, project_count-j, sharex=ax_trunk, sharey=ax_trunk, frameon=False)
        ax_tag = fig.add_subplot(project_count, left_or_right, project_count-j, sharex=ax_trunk, frameon=False)
        ax_tag.yaxis.tick_right()
        #ax_tag.yaxis.tick_color("r")
        #xs_tag = [xs+width for xs in xs_tag] 
        ax_tag.plot(xs_tag, ys_tag, 'r')
        for label in ax_tag.get_yticklabels():
            #print label
            label.set_visible(False)
        yticklabels_length = len(ax_tag.get_yticklabels())
        #ax_trunk.get_yticklabels()[0].set_visible(True)
        ax_tag.get_yticklabels()[yticklabels_length - 1].set_visible(True)
        ax_tag.get_yticklabels()[yticklabels_length - 1].set_color("r")
        #ax_tag.bar(xs_tag, ys_tag, width, color='r')
        #ax_tag.set_ylabel(str(project_name))
        #ax_tag.yaxis.set_label_position("right")
        ax_project_name = fig.add_subplot(project_count, left_or_right, project_count-j, sharex=ax_trunk, frameon=False)
        ax_project_name.set_ylabel(str(project_name))
        ax_project_name.yaxis.set_label_position("right")
        #if j % 2 != 0:
        #    ax_project_name.yaxis.set_label_position("right")
        #else:
        #    ax_project_name.yaxis.set_label_position("left")
        '''ax_author = fig.add_subplot(project_count, left_or_right, project_count-j, sharex=ax_trunk, frameon=False)
        ax_author.yaxis.tick_right()
        ax_author.plot(xs_author, ys_author, 'y')'''
        #ax_author.set_ylabel(str(project_name))
        #ax_tag.yaxis.set_label_position("right")
        #ax_trunk.plot(xs_tag, ys_tag, width, color='r')
        incubation_start = datetime.strptime(row["start"], '%d/%m/%Y')
        if (row["end"] == ""):
            incubation_end = datetime.today()
        else:
            incubation_end = datetime.strptime(row["end"], '%d/%m/%Y')
        ax_trunk.axvspan(incubation_start, incubation_end, facecolor='g', alpha=0.5)
        #ax_trunk.set_title(str(project_name))
        #ax_trunk.set_ylabel(str(project_name))
        #ax_trunk.set_ylabel("world")
        #ax_trunk.ylabel.tick_right()
        #ax_trunk.Tick(label1On=False, lable2On=True)
        #ax_trunk.yaxis.set_label_position("right")
        #print type(ax_trunk)
        #ax_trunk.set_xlim(left="hello", right="world")
        #ax_tag.plot_date(xs_tag, ys_tag, xdate=True, color="red")
        #ax.grid(True)
        #ax.title(str(project_name))
        #print ys_trunk
        #print ys_tag
        j = j+1
        #break
    c.close()
    #pylab.show()
    plt.show()
    #plt.plot([1,2,3,4])
    #plt.ylabel('some numbers')
    #plt.show() 






def project_history_amount_multiplot_dependency_o():
    global conn
    #matplotlib.rcParams["figure.subplot.hspace"]=0.9
    matplotlib.rcParams["figure.subplot.left"]=0.05
    matplotlib.rcParams["figure.subplot.right"]=0.95
    matplotlib.rcParams["figure.subplot.top"]=0.95
    matplotlib.rcParams["figure.subplot.bottom"]=0.05
    project_count = 0
    for row in svn_utils.svn_dependency:
        if (row["start"] != "") :#and (row["end"] != ""):
            project_count = project_count+1
    j = 0
    xss_tag = []
    yss_tag = []
    xss_trunk = []
    yss_trunk = []
    project_names = []
    for row in svn_utils.svn_dependency:
     if (row["start"] != "") :#and (row["end"] != ""):
        db_query = project
        #print db_query
        c = conn.cursor()
        c.execute(db_query, (row["project"], ))
        #print row["start"], row["end"]
        rr = c.fetchone()
        project_id = rr[0]
        project_name = rr[1]
        xs_trunk = []
        ys_trunk = []
        i = 1
        txt = open("./history_svn_counts/project_history_amount_multiplot_o_trunk_"+str(project_id)+"_"+str(project_name)+".txt", "w")
        out = ("index, \tproject_id , \tproject_name , \tmonth, \tsvn_counts")
        #print out
        txt.write(out+"\n")
        db_query_single = project_trunk_single_amount
        c_trunk = conn.cursor()
        c_trunk.execute(db_query_single, (project_id, ))
        for r in c_trunk:
            month = r[1]
            # convert string into datetime
            month = datetime.strptime(month, '%Y-%m')
            if month.year < 1997:
                continue
            svn_count = r[2]
            xs_trunk.append(month)
            ys_trunk.append(svn_count)
            #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
            out = (str(i)+", \t"+str(r[0])+" , \t"+str(r[1])+" , \t"+str(r[2]))
            #print out
            txt.write(out+"\n")
            i = i + 1
        txt.close()
        xs_tag = []
        ys_tag = []
        i = 1
        txt = open("./history_svn_counts/project_history_amount_multiplot_o_tag_"+str(project_id)+"_"+str(project_name)+".txt", "w")
        out = ("index, \tproject_id , \tproject_name , \tmonth, \tsvn_counts")
        #print out
        txt.write(out+"\n")
        db_query_single = project_tag_single_amount
        c_tag = conn.cursor()
        c_tag.execute(db_query_single, (project_id, ))
        for r in c_tag:
            month = r[1]
            # convert string into datetime
            month = datetime.strptime(month, '%Y-%m')#+timedelta(days=15)
            if month.year < 1997:
                continue
            svn_count = r[2]
            xs_tag.append(month)
            ys_tag.append(svn_count)
            #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
            out = (str(i)+", \t"+str(r[0])+" , \t"+str(r[1])+" , \t"+str(r[2]))
            #print out
            txt.write(out+"\n")
            i = i + 1
        txt.close()
        xss_tag.append(xs_tag)
        yss_tag.append(ys_tag)
        xss_trunk.append(xs_trunk)
        yss_trunk.append(ys_trunk)
        project_names.append(project_name)
    fig = plt.figure()
    ax_trunk_1 = fig.add_subplot(2, 1, 1)
    #ax_trunk.plot_date(xs_trunk, ys_trunk, xdate=True, color="blue")
    ax_trunk_1.plot(xss_trunk[0], yss_trunk[0], 'bo')
    ax_trunk_1.set_ylabel(project_names[0])
    ax_trunk_1.yaxis.set_label_position("left")
    ax_trunk_1.yaxis.tick_left()
    for label in ax_trunk_1.get_yticklabels():
        label.set_color("blue")
    ax_tag_1 = fig.add_subplot(2, 1, 2)
    ax_tag_1.plot(xss_tag[0], yss_tag[0], 'bo')
    ax_tag_1.set_ylabel(project_names[0])
    ax_tag_1.yaxis.set_label_position("left")
    ax_tag_1.yaxis.tick_left()
    for label in ax_tag_1.get_yticklabels():
        label.set_color("blue")
    ax_trunk_1.set_title("SVN Trunk")
    ax_tag_1.set_title("SVN Tags")
    ax_trunk_2 = fig.add_subplot(2, 1, 1, sharex=ax_trunk_1, frameon=False)
    #ax_trunk.plot_date(xs_trunk, ys_trunk, xdate=True, color="blue")
    ax_trunk_2.plot(xss_trunk[1], yss_trunk[1], 'ro')
    ax_trunk_2.set_ylabel(project_names[1])
    ax_trunk_2.yaxis.set_label_position("right")
    ax_trunk_2.yaxis.tick_right()
    for label in ax_trunk_2.get_yticklabels():
        label.set_color("red")
    ax_tag_2 = fig.add_subplot(2, 1, 2, sharex=ax_tag_1, frameon=False)
    ax_tag_2.plot(xss_tag[1], yss_tag[1], 'ro')
    ax_tag_2.yaxis.tick_right()
    ax_tag_2.set_ylabel(project_names[1])
    ax_tag_2.yaxis.set_label_position("right")
    for label in ax_tag_2.get_yticklabels():
        label.set_color("red")
    plt.show()
    #plt.plot([1,2,3,4])
    #plt.ylabel('some numbers')
    #plt.show() 





projects_multii_year = '''
    SELECT 
        svn_project.project_id, 
        svn_project.project_name 
    FROM 
        svn_project 
    WHERE 
        svn_project.project_name IN ("deegree", "geoserver")
'''
projects_multi_year = '''
    SELECT 
        svn_project.project_id, 
        svn_project.project_name 
    FROM 
        svn_project 
    WHERE 
        svn_project.project_name IN ?
'''
projects_year = '''
    SELECT svn_project.project_id, svn_project.project_name FROM svn_project 
'''
project_year = '''
    SELECT 
        svn_project.project_id, 
        svn_project.project_name 
    FROM 
        svn_project 
    WHERE 
        svn_project.project_name = ?
'''
project_trunk_single_year = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_revision.revision_id, 
            STRFTIME('%Y', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND 
            svn_revision.project_id = ?
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''    
project_trunk_single_amount_year = '''
    SELECT 
        project_trunk_amount.project_name,
        project_trunk_amount.timestamp, 
        COUNT(project_trunk_amount.revision_id) AS project_count
    FROM ('''+project_trunk_single_year+''') AS project_trunk_amount
    GROUP BY 
        project_trunk_amount.project_name, 
        project_trunk_amount.timestamp
'''
project_tag_single_year = '''
        SELECT
            svn_revision.project_id,
            svn_project.project_name,
            svn_revision.revision_id, 
            STRFTIME('%Y', svn_time.timestamp) AS timestamp
        FROM svn_commits, svn_time, svn_revision, svn_project, svn_tags
        WHERE
            svn_commits.time_id = svn_time.time_id AND
            svn_commits.revision_id = svn_revision.revision_id AND
            svn_revision.project_id = svn_project.project_id AND 
            svn_revision.revision_id = svn_tags.revision_id AND
            svn_revision.project_id = ?
        ORDER BY
            svn_project.project_id,
            svn_time.timestamp
        '''    
project_tag_single_amount_year = '''
    SELECT 
        project_trunk_amount.project_name,
        project_trunk_amount.timestamp, 
        COUNT(project_trunk_amount.revision_id) AS project_count
    FROM ('''+project_tag_single_year+''') AS project_trunk_amount
    GROUP BY 
        project_trunk_amount.project_name, 
        project_trunk_amount.timestamp
'''


def project_history_amount_multiplot_year_o():
    global conn
    #matplotlib.rcParams["figure.subplot.hspace"]=0.9
    matplotlib.rcParams["figure.subplot.left"]=0.05
    matplotlib.rcParams["figure.subplot.right"]=0.95
    matplotlib.rcParams["figure.subplot.top"]=0.95
    matplotlib.rcParams["figure.subplot.bottom"]=0.05
    db_query = projects_multii_year
    print db_query
    c = conn.cursor()
    #c.execute(db_query, (('(\"geoserver\", \"deegree\")'), ))
    c.execute(db_query,)
    #fig, axx = plt.subplots(20)
    #fig = pylab.figure()
    #fig = plt.figure()
    fig = plt.figure()
    #years = matplotlib.dates.YearLocator()
    #months = matplotlib.dates.MonthLocator()
    #years = matplotlib.dates.YearLocator()
    #print fig
    project_count = 0
    for row in svn_utils.svn_incubations:
        if (row["start"] != "") and (row["end"] != ""):
            project_count = project_count+1
    #project_count = 1
    j = 0
    #for row in c:
    for row in svn_utils.svn_incubations:
     if (row["start"] != "") and (row["end"] != ""):
        db_query = project_year
        #print db_query
        c = conn.cursor()
        c.execute(db_query, (row["project"], ))
        #print row["start"], row["end"]
        rr = c.fetchone()
        project_id = rr[0]
        project_name = rr[1]
        xs_trunk = []
        ys_trunk = []
        i = 1
        txt = open("./history_svn_counts/project_history_amount_multiplot_o_trunk_"+str(project_id)+"_"+str(project_name)+".txt", "w")
        out = ("index, \tproject_id , \tproject_name , \tmonth, \tsvn_counts")
        #print out
        txt.write(out+"\n")
        db_query_single = project_trunk_single_amount_year
        c_trunk = conn.cursor()
        c_trunk.execute(db_query_single, (project_id, ))
        for r in c_trunk:
            month = r[1]
            # convert string into datetime
            month = datetime.strptime(month, '%Y')
            svn_count = r[2]
            xs_trunk.append(month)
            ys_trunk.append(svn_count)
            #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
            out = (str(i)+", \t"+str(r[0])+" , \t"+str(r[1])+" , \t"+str(r[2]))
            #print out
            txt.write(out+"\n")
            i = i + 1
        txt.close()
        xs_tag = []
        ys_tag = []
        i = 1
        txt = open("./history_svn_counts/project_history_amount_multiplot_o_tag_"+str(project_id)+"_"+str(project_name)+".txt", "w")
        out = ("index, \tproject_id , \tproject_name , \tmonth, \tsvn_counts")
        #print out
        txt.write(out+"\n")
        db_query_single = project_tag_single_amount_year
        c_tag = conn.cursor()
        c_tag.execute(db_query_single, (project_id, ))
        for r in c_tag:
            month = r[1]
            # convert string into datetime
            month = datetime.strptime(month, '%Y')+timedelta(days=15)
            svn_count = r[2]
            xs_tag.append(month)
            ys_tag.append(svn_count)
            #out = (str(i)+", \t"+str(row[0])+" , \t"+str(row[1])+" , \t"+str(row[2])+" , \t"+str(row[3]))
            out = (str(i)+", \t"+str(r[0])+" , \t"+str(r[1])+" , \t"+str(r[2]))
            #print out
            txt.write(out+"\n")
            i = i + 1
        txt.close()
        '''if (len(ys_trunk)>0 and len(ys_tag)>0):
            l_trunk = []
            l_trunk.extend(ys_trunk)
            l_trunk.sort()
            l_trunk.reverse()
            largest_trunk = l_trunk[0]
            l_tag = []
            l_tag.extend(ys_tag)
            l_tag.sort()
            l_tag.reverse()
            largest_tag = l_tag[0]
            print largest_trunk, largest_tag
            l = largest_trunk / largest_tag
            ys_tag = [y * l for y in ys_tag]
            print l'''
        '''subplot = axx[j]
        subplot.plot_date(xs, ys, xdate=True)
        subplot.set_title(str(project_name))
        subplot.
        j = j+1'''
        #plot_id = project_id+100
        #print plot_id
        width = 15
        ax_trunk = fig.add_subplot(project_count, 1, project_count-j)
        #ax_trunk.plot_date(xs_trunk, ys_trunk, xdate=True, color="blue")
        ax_trunk.bar(xs_trunk, ys_trunk, width, color='b')
        #ax_trunk.ylabel("hello")
        #ax_trunk.bar(xs_trunk, ys_trunk, width, color='b')
        #ax_tag = fig.add_subplot(211)
        #ax_tag = ax_trunk.twinx()
        #ax_trunk.plot(xs_tag, ys_tag, 'ro')
        ax_tag = fig.add_subplot(project_count, 1, project_count-j, sharex=ax_trunk, frameon=False)
        ax_tag.yaxis.tick_right()
        #xs_tag = [xs+width for xs in xs_tag] 
        ax_tag.bar(xs_tag, ys_tag, width, color='r')
        ax_tag.set_ylabel(str(project_name))
        ax_tag.yaxis.set_label_position("right")
        #ax_trunk.plot(xs_tag, ys_tag, width, color='r')
        incubation_start = datetime.strptime(row["start"], '%d/%m/%Y')
        incubation_end = datetime.strptime(row["end"], '%d/%m/%Y')
        ax_trunk.axvspan(incubation_start, incubation_end, facecolor='g', alpha=0.5)
        #ax_trunk.set_title(str(project_name))
        #ax_trunk.set_ylabel(str(project_name))
        #ax_trunk.set_ylabel("world")
        #ax_trunk.ylabel.tick_right()
        #ax_trunk.Tick(label1On=False, lable2On=True)
        #ax_trunk.yaxis.set_label_position("right")
        #print type(ax_trunk)
        #ax_trunk.set_xlim(left="hello", right="world")
        #ax_tag.plot_date(xs_tag, ys_tag, xdate=True, color="red")
        #ax.grid(True)
        #ax.title(str(project_name))
        #print ys_trunk
        #print ys_tag
        j = j+1
        #break
    c.close()
    #pylab.show()
    plt.show()
    #plt.plot([1,2,3,4])
    #plt.ylabel('some numbers')
    #plt.show()
    

    
    
    

if __name__ == "__main__":
    print "Hello World";


