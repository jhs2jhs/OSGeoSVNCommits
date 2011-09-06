#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 4:58:54 PM$"

from svn_utils import cmd_p
import svn_utils

def sqlite_init():
    conn = svn_utils.svn_get_conn()
    cmd_p("start to init the database")
    c = conn.cursor()
    c.executescript('''
        -- create table svn_project
        CREATE TABLE IF NOT EXISTS svn_project (
            project_id  INTEGER PRIMARY KEY,
            project_name TEXT UNIQUE NOT NULL,
            project_svn_address TEXT,
            project_description TEXT
        );
        -- create table svn_revision
        CREATE TABLE IF NOT EXISTS svn_revision (
            revision_id INTEGER PRIMARY KEY,
            project_id  INTEGER NOT NULL,
            revision INTEGER NOT NULL,
            UNIQUE (project_id, revision),
            FOREIGN KEY (project_id) REFERENCES svn_project(project_id)
        );
        -- create table svn_tags
        CREATE TABLE IF NOT EXISTS svn_tags (
            svn_tags_id INTEGER PRIMARY KEY,
            revision_id INTEGER UNIQUE NOT NULL,
            FOREIGN KEY (revision_id) REFERENCES svn_revision(revision_id)
        );
        -- create table svn_branches
        CREATE TABLE IF NOT EXISTS svn_branches (
            svn_branches_id INTEGER PRIMARY KEY,
            revision_id INTEGER UNIQUE NOT NULL,
            FOREIGN KEY (revision_id) REFERENCES svn_revision(revision_id)
        );
        -- create table svn_projects
        CREATE TABLE IF NOT EXISTS svn_projects (
            svn_projects_id INTEGER PRIMARY KEY,
            revision_id INTEGER UNIQUE NOT NULL,
            FOREIGN KEY (revision_id) REFERENCES svn_revision(revision_id)
        );
        -- create table svn_author
        CREATE TABLE IF NOT EXISTS svn_author (
            author_id  INTEGER PRIMARY KEY,
            author_name TEXT NOT NULL,
            UNIQUE (author_name)
        );
        -- create table svn_msg
        CREATE TABLE IF NOT EXISTS svn_msg (
            msg_id  INTEGER PRIMARY KEY,
            msg TEXT
        );
        -- create table svn_file_path
        CREATE TABLE IF NOT EXISTS svn_file_path (
            file_id  INTEGER PRIMARY KEY,
            file_path TEXT NOT NULL UNIQUE
        );
        -- create table svn_file_copy
        CREATE TABLE IF NOT EXISTS svn_file_copy (
            copy_id INTEGER PRIMARY KEY,
            revision_from_id INTEGER NOT NULL,
            revision_to_id INTEGER NOT NULL,
            file_from_id INTEGER NOT NULL,
            file_to_id  INTEGER NOT NULL,
            FOREIGN KEY (revision_from_id) REFERENCES svn_revision(revision_id),
            FOREIGN KEY (revision_to_id) REFERENCES svn_revision(revision_id),
            FOREIGN KEY (file_from_id) REFERENCES svn_file_path(file_id),
            FOREIGN KEY (file_to_id) REFERENCES svn_file_path(file_id)
        );
        -- create table svn_files
        CREATE TABLE IF NOT EXISTS svn_files (
            revision_id  INTEGER NOT NULL,
            file_id INTEGER NOT NULL,
            action TEXT,
            kind TEXT,
            copy_id INTEGER, 
            PRIMARY KEY (revision_id, file_id),
            FOREIGN KEY (revision_id) REFERENCES svn_revision(revision_id),
            FOREIGN KEY (file_id) REFERENCES svn_file_path(file_id),
            FOREIGN KEY (copy_id) REFERENCES svn_file_copy(copy_id)
        );
        -- create table svn_time
        CREATE TABLE IF NOT EXISTS svn_time (
            time_id INTEGER PRIMARY KEY,
            timestamp INTEGER
        );
        -- create table svn_commits
        CREATE TABLE IF NOT EXISTS svn_commits (
            revision_id INTEGER NOT NULL,
            author_id   INTEGER NOT_NULL,
            msg_id      INTEGER NOT_NULL,
            time_id     INTEGER NOT_NULL,
            PRIMARY KEY (revision_id),
            FOREIGN KEY (revision_id) REFERENCES svn_revision(revision_id),
            FOREIGN KEY (author_id) REFERENCES svn_author(author_id),
            FOREIGN KEY (msg_id) REFERENCES svn_msg(msg_id),
            FOREIGN KEY (time_id) REFERENCES svn_time(time_id)
        );
        ''')
    conn.commit()
    c.execute('''SELECT * FROM SQLITE_MASTER''')
    tables = c.fetchall()
    print ("database tables in total: ",len(tables))
    for row in tables:
        print "\t(["+row[0]+"],["+row[2]+"])"
    c.close()
    cmd_p("finish init databse")

def sqlite_tags_insert_commit(commit):
    conn = svn_utils.svn_get_conn()
    c = conn.cursor()
    project = commit['project']
    c.execute("INSERT OR IGNORE INTO svn_project (project_name, project_svn_address, project_description) VALUES (?, 'HELLO', 'WORLD')", (project,) )
    conn.commit()
    c.execute("SELECT project_id FROM svn_project WHERE project_name=?", (project,))
    project_id = c.fetchone()[0]
    #print project_id
    revision = commit['revision']
    c.execute("INSERT OR IGNORE INTO svn_revision (project_id, revision) VALUES (?, ?)", (project_id, revision, ) )
    conn.commit()
    c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, revision, ))
    revision_id = c.fetchone()[0]
    #print revision_id
    author = commit['author']
    c.execute("INSERT OR IGNORE INTO svn_author (author_name) VALUES (?)", (author, ) )
    conn.commit()
    c.execute("SELECT author_id FROM svn_author WHERE author_name=?", (author, ))
    author_id = c.fetchone()[0]
    #print author_id
    msg = commit['msg']
    c.execute("INSERT INTO svn_msg (msg) VALUES (?)", (msg, ) )
    conn.commit()
    msg_id = c.lastrowid
    #print msg_id
    time = commit['time']
    c.execute("INSERT INTO svn_time (timestamp) VALUES (?)", (time, ) )
    conn.commit()
    time_id = c.lastrowid
    #print time_id
    files = commit['file']
    for file in files:
        #print file
        c.execute("INSERT OR IGNORE INTO svn_file_path (file_path) VALUES (?)", (file['path'], ) )
        conn.commit()
        c.execute("SELECT file_id FROM svn_file_path WHERE file_path=?", (file['path'], ))
        file_id = c.fetchone()[0]
        action = file['action']
        kind = file['kind']
        #cmd_p("hello")
        #cmd_p(action)
        #cmd_p(kind)
        #cmd_p(len(file['from_path']))
        if len(file['from_path']) > 0:
            #cmd_p(file['from_path'])
            c.execute("INSERT OR IGNORE INTO svn_file_path (file_path) VALUES (?)", (file['from_path'], ) )
            conn.commit()
            c.execute("SELECT file_id FROM svn_file_path WHERE file_path=?", (file['from_path'], ))
            file_from_id = c.fetchone()[0]
            c.execute("INSERT OR IGNORE INTO svn_revision (project_id, revision) VALUES (?, ?)", (project_id, file['from_rev'], ) )
            conn.commit()
            c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, file['from_rev'], ))
            revision_from_id = c.fetchone()[0]
            c.execute("INSERT INTO svn_file_copy (revision_from_id, revision_to_id, file_from_id, file_to_id) VALUES (?, ?, ?, ?)", (revision_from_id, revision_id, file_from_id, file_id, ) )
            conn.commit()
            c.execute("SELECT MAX(copy_id) FROM svn_file_copy", )
            copy_id = c.fetchone()[0]
            print "\tcid: "+str(copy_id)
            #copy_id = c.lastrowid
        else:
            copy_id = -1
        #print copy_id
        c.execute("INSERT OR IGNORE INTO svn_files (revision_id, file_id, action, kind, copy_id) VALUES (?, ?, ?, ?, ?)", (revision_id, file_id, action, kind, copy_id, ))
        conn.commit()
    # files
    c.execute ("INSERT OR IGNORE INTO svn_commits (revision_id, author_id, msg_id, time_id) VALUES (?, ?, ?, ?)", (revision_id, author_id, msg_id, time_id, ))
    conn.commit()
    c.execute("INSERT OR IGNORE INTO svn_tags (revision_id) VALUES (?)", (revision_id, ))
    conn.commit()
    #c.execute("SELECT * FROM svn_commits", )
    #print c.fetchall()
    c.close()
    print "in tags: p="+project+", r="+revision

def sqlite_branches_insert_commit(commit):
    conn = svn_utils.svn_get_conn()
    c = conn.cursor()
    project = commit['project']
    c.execute("INSERT OR IGNORE INTO svn_project (project_name, project_svn_address, project_description) VALUES (?, 'HELLO', 'WORLD')", (project,) )
    conn.commit()
    c.execute("SELECT project_id FROM svn_project WHERE project_name=?", (project,))
    project_id = c.fetchone()[0]
    #print project_id
    revision = commit['revision']
    c.execute("INSERT OR IGNORE INTO svn_revision (project_id, revision) VALUES (?, ?)", (project_id, revision, ) )
    conn.commit()
    c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, revision, ))
    revision_id = c.fetchone()[0]
    #print revision_id
    author = commit['author']
    c.execute("INSERT OR IGNORE INTO svn_author (author_name) VALUES (?)", (author, ) )
    conn.commit()
    c.execute("SELECT author_id FROM svn_author WHERE author_name=?", (author, ))
    author_id = c.fetchone()[0]
    #print author_id
    msg = commit['msg']
    c.execute("INSERT INTO svn_msg (msg) VALUES (?)", (msg, ) )
    conn.commit()
    msg_id = c.lastrowid
    #print msg_id
    time = commit['time']
    c.execute("INSERT INTO svn_time (timestamp) VALUES (?)", (time, ) )
    conn.commit()
    time_id = c.lastrowid
    #print time_id
    files = commit['file']
    for file in files:
        #print file
        c.execute("INSERT OR IGNORE INTO svn_file_path (file_path) VALUES (?)", (file['path'], ) )
        conn.commit()
        c.execute("SELECT file_id FROM svn_file_path WHERE file_path=?", (file['path'], ))
        file_id = c.fetchone()[0]
        action = file['action']
        kind = file['kind']
        #cmd_p("hello")
        #cmd_p(action)
        #cmd_p(kind)
        #cmd_p(len(file['from_path']))
        if len(file['from_path']) > 0:
            #cmd_p(file['from_path'])
            c.execute("INSERT OR IGNORE INTO svn_file_path (file_path) VALUES (?)", (file['from_path'], ) )
            conn.commit()
            c.execute("SELECT file_id FROM svn_file_path WHERE file_path=?", (file['from_path'], ))
            file_from_id = c.fetchone()[0]
            c.execute("INSERT OR IGNORE INTO svn_revision (project_id, revision) VALUES (?, ?)", (project_id, file['from_rev'], ) )
            conn.commit()
            c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, file['from_rev'], ))
            revision_from_id = c.fetchone()[0]
            c.execute("INSERT INTO svn_file_copy (revision_from_id, revision_to_id, file_from_id, file_to_id) VALUES (?, ?, ?, ?)", (revision_from_id, revision_id, file_from_id, file_id, ) )
            conn.commit()
            c.execute("SELECT MAX(copy_id) FROM svn_file_copy", )
            copy_id = c.fetchone()[0]
            print "\tcid: "+str(copy_id)
            #copy_id = c.lastrowid
        else:
            copy_id = -1
        #print copy_id
        c.execute("INSERT OR IGNORE INTO svn_files (revision_id, file_id, action, kind, copy_id) VALUES (?, ?, ?, ?, ?)", (revision_id, file_id, action, kind, copy_id, ))
        conn.commit()
    # files
    c.execute ("INSERT OR IGNORE INTO svn_commits (revision_id, author_id, msg_id, time_id) VALUES (?, ?, ?, ?)", (revision_id, author_id, msg_id, time_id, ))
    conn.commit()
    c.execute("INSERT OR IGNORE INTO svn_branches (revision_id) VALUES (?)", (revision_id, ))
    conn.commit()
    #c.execute("SELECT * FROM svn_commits", )
    #print c.fetchall()
    c.close()
    print "in branches: p="+project+", r="+revision


# check whether commit has been insert before
def sqlite_insert_commit(commit):
    conn = svn_utils.svn_get_conn()
    c = conn.cursor()
    project = commit['project']
    c.execute("INSERT OR IGNORE INTO svn_project (project_name, project_svn_address, project_description) VALUES (?, 'HELLO', 'WORLD')", (project,) )
    conn.commit()
    c.execute("SELECT project_id FROM svn_project WHERE project_name=?", (project,))
    project_id = c.fetchone()[0]
    #print project_id
    revision = commit['revision']
    c.execute("INSERT OR IGNORE INTO svn_revision (project_id, revision) VALUES (?, ?)", (project_id, revision, ) )
    conn.commit()
    c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, revision, ))
    revision_id = c.fetchone()[0]
    #print revision_id
    author = commit['author']
    c.execute("INSERT OR IGNORE INTO svn_author (author_name) VALUES (?)", (author, ) )
    conn.commit()
    c.execute("SELECT author_id FROM svn_author WHERE author_name=?", (author, ))
    author_id = c.fetchone()[0]
    #print author_id
    msg = commit['msg']
    c.execute("INSERT INTO svn_msg (msg) VALUES (?)", (msg, ) )
    conn.commit()
    msg_id = c.lastrowid
    #print msg_id
    time = commit['time']
    c.execute("INSERT INTO svn_time (timestamp) VALUES (?)", (time, ) )
    conn.commit()
    time_id = c.lastrowid
    #print time_id
    files = commit['file']
    for file in files:
        #print file
        c.execute("INSERT OR IGNORE INTO svn_file_path (file_path) VALUES (?)", (file['path'], ) )
        conn.commit()
        c.execute("SELECT file_id FROM svn_file_path WHERE file_path=?", (file['path'], ))
        file_id = c.fetchone()[0]
        action = file['action']
        kind = file['kind']
        #cmd_p("hello")
        #cmd_p(action)
        #cmd_p(kind)
        #cmd_p(len(file['from_path']))
        if len(file['from_path']) > 0:
            #cmd_p(file['from_path'])
            c.execute("INSERT OR IGNORE INTO svn_file_path (file_path) VALUES (?)", (file['from_path'], ) )
            conn.commit()
            c.execute("SELECT file_id FROM svn_file_path WHERE file_path=?", (file['from_path'], ))
            file_from_id = c.fetchone()[0]
            c.execute("INSERT OR IGNORE INTO svn_revision (project_id, revision) VALUES (?, ?)", (project_id, file['from_rev'], ) )
            conn.commit()
            c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, file['from_rev'], ))
            revision_from_id = c.fetchone()[0]
            c.execute("INSERT INTO svn_file_copy (revision_from_id, revision_to_id, file_from_id, file_to_id) VALUES (?, ?, ?, ?)", (revision_from_id, revision_id, file_from_id, file_id, ) )
            conn.commit()
            c.execute("SELECT MAX(copy_id) FROM svn_file_copy", )
            copy_id = c.fetchone()[0]
            print "\tcid: "+str(copy_id)
            #copy_id = c.lastrowid
        else:
            copy_id = -1
        #print copy_id
        c.execute("INSERT OR IGNORE INTO svn_files (revision_id, file_id, action, kind, copy_id) VALUES (?, ?, ?, ?, ?)", (revision_id, file_id, action, kind, copy_id, ))
        conn.commit()
    # files
    c.execute ("INSERT INTO svn_commits (revision_id, author_id, msg_id, time_id) VALUES (?, ?, ?, ?)", (revision_id, author_id, msg_id, time_id, ))
    conn.commit()
    #c.execute("SELECT * FROM svn_commits", )
    #print c.fetchall()
    c.close()
    print "in trunk: p="+project+", r="+revision

def sqlite_exist_check(commit):
    conn = svn_utils.svn_get_conn()
    #print "sqlite_insert_check"
    c = conn.cursor()
    project = commit['project']
    c.execute("SELECT project_id FROM svn_project WHERE project_name=?", (project,))
    project_id = c.fetchall()
    #print "len", len(project_id)
    if len(project_id) > 0:
        project_id = project_id[0][0]
        revision = commit['revision']
        c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, revision, ))
        revision_id = c.fetchall()
        #print "length", len(revision_id)
        if len(revision_id) > 0:
            c.close()
            return 0
        c.close()
        return 1
    c.close()
    return 1

# check whether commit has been insert before
def sqlite_tags_exist_check(commit):
    conn = svn_utils.svn_get_conn()
    #print "sqlite_insert_check"
    c = conn.cursor()
    project = commit['project']
    c.execute("SELECT project_id FROM svn_project WHERE project_name=?", (project,))
    project_id = c.fetchall()
    #print "len", len(project_id)
    if len(project_id) > 0:
        project_id = project_id[0][0]
        revision = commit['revision']
        c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, revision, ))
        revision_id = c.fetchall()
        #print "length", len(revision_id)
        if len(revision_id) > 0:
            #sq = ("SELECT svn_tags_id FROM svn_tags WHERE revision_id=? ", (str(revision_id[0]), ))
            #print revision_id[0]
            c.execute("SELECT * FROM svn_tags WHERE revision_id=? ", (revision_id[0][0], ))
            svn_tags_id = c.fetchall()
            #print svn_tags_id
            if len(svn_tags_id) > 0:
                c.close()
                return 0
            else :
                c.close()
                return 1
        else :
            c.close()
            return 1
    else :
        c.close()
        return 1


# check whether commit has been insert before
def sqlite_branches_exist_check(commit):
    conn = svn_utils.svn_get_conn()
    #print "sqlite_insert_check"
    c = conn.cursor()
    project = commit['project']
    c.execute("SELECT project_id FROM svn_project WHERE project_name=?", (project,))
    project_id = c.fetchall()
    #print "len", len(project_id)
    if len(project_id) > 0:
        project_id = project_id[0][0]
        revision = commit['revision']
        c.execute("SELECT revision_id FROM svn_revision WHERE project_id=? AND revision=?", (project_id, revision, ))
        revision_id = c.fetchall()
        #print "length", len(revision_id)
        if len(revision_id) > 0:
            #sq = ("SELECT svn_tags_id FROM svn_tags WHERE revision_id=? ", (str(revision_id[0]), ))
            #print revision_id[0]
            c.execute("SELECT * FROM svn_branches WHERE revision_id=? ", (revision_id[0][0], ))
            svn_branches_id = c.fetchall()
            #print svn_tags_id
            if len(svn_branches_id) > 0:
                c.close()
                return 0
            else :
                c.close()
                return 1
        else :
            c.close()
            return 1
    else :
        c.close()
        return 1


def sqlite_commit_count(project):
    conn = svn_utils.svn_get_conn()
    c = conn.cursor()
    c.execute('''
        SELECT COUNT(revision) FROM svn_revision WHERE
            project_id=(SELECT project_id FROM svn_project WHERE project_name=?)
        GROUP BY project_id''', (project,))
    commits_count = c.fetchone()[0]
    print "** trunk project="+project+" has commits="+commits_count
    c.close()

def sqlite_commit_max(project):
    conn = svn_utils.svn_get_conn()
    c = conn.cursor()
    c.execute('''
        SELECT MAX(revision) FROM svn_revision WHERE
            project_id=(SELECT project_id FROM svn_project WHERE project_name=?)
        GROUP BY project_id''', (project,))
    commits_max = c.fetchone()[0]
    print "** tags project="+project+" has max revision="+commits_max
    c.close()
    return commits_max

if __name__ == "__main__":
    print "Hello World";
