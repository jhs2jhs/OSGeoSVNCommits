#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jianhuashao"
__date__ ="$Sep 6, 2011 4:27:19 PM$"


import argparse
import svn_utils
import svn_gateway
import svn_db_operation
import svn_folder
import svn_db_query
import os
import svn_folder

parser = argparse.ArgumentParser(description='SVN Commits analysis scripting program')
#args = parser.parse_args

def cmd_register():
    subparsers = parser.add_subparsers(help='SVN Commits data collection and analysis')
    
    checkout = subparsers.add_parser('checkout', help='checkout the svn commits and push it into database')
    checkout.add_argument(
        '-t', '--type', action='store', dest='svn_types', nargs='+', type=str,
        choices=['trunk', 'tags', 'branches'], required=True, metavar='SVN_TYPES',
        help='''choose which type of SVN Commits to analyais: trunk, tags, branches/
            '''
        )
    checkout.add_argument(
        '-ux', '--update-xml', action='store', dest='update_xml', nargs=1, type=str,
        choices=['true', 'false'], required=True, metavar='TRUE_or_FALSE',
        help='whether to update the log xml file'
        )
    checkout.set_defaults(func=cmd_checkout)

    query = subparsers.add_parser('query', help='query the database')
    query.add_argument(
        '-f', '-file', action='store', dest='output_to_file', nargs=1, type=str,
        choices=['true', 'false'], required=True, metavar='TRUE_or_FALSE',
        help='whether to output result to file'
        )
    query.set_defaults(func=cmd_query)
    #checkout.print_help()
    # could add sub arguments for different type of process, for example SQLITE query for data could be different process

def cmd_parser():
    svn_utils.cmd_p("\n*******start to parse cmd arguments***********\n")
    #args = parser.parse_args(['checkout', '-t', 'branches', 'trunk', 'tags', '-ux', 'true'])
    #args = parser.parse_args(['checkout', '-t', 'branches', '-ux', 'true'])
    #args = parser.parse_args(['query','-f', 'true'])
    args = parser.parse_args()
    svn_utils.cmd_p(args)
    args.func(args)
    #return args

def cmd_checkout(args):
    # start to process
    #print args.update_xml
    first = -1
    if args.update_xml[0] == 'true':
        first = 0
    else :
        first = 1
    svn_utils.svn_db_connect()
    if (first == 0):
        svn_db_operation.sqlite_init()
        svn_folder.check_xml_folder()
    # something here to creat the databse connection
    for type in args.svn_types:
        if type == 'trunk':
            svn_gateway.main_trunk(first)
        if type == 'tags':
            svn_gateway.main_tags(first)
        if type == 'branches':
            svn_gateway.main_branches(first)
    svn_utils.svn_db_close()


def cmd_query(args):
    flag = True
    svn_utils.cwd()
    os.chdir("."+svn_utils.svn_analysis)
    svn_db_query.svn_db_connect()
    print os.getcwd()
    while flag == True:
        message = '''
            Please choose a query:
                0 : quit
                1 : author => project
                2 : author => projects count
                3 : author has more than 1 projects
                4 : specific author with AID => project
                5 : specific author temproal for all projects
                6 : projects => revisions, used for commits history of all projects
                7 : projects => revisions, used for relase history of all projects
            '''
        x = input (message)
        if x == 0:
            flag = False
        elif x == 1:
            svn_db_query.author_project_o()
        elif x == 2:
            svn_db_query.author_projects_count_0()
        elif x == 3:
            svn_db_query.author_projects_more_than_2_0()
        elif x == 4:
            id = input ("type author ID: ")
            svn_db_query.s_author_with_id_project_o(id)
        elif x == 5:
            id = input ("type author ID: ")
            svn_db_query.author_revisions_o(id)
        elif x == 6:
            svn_db_query.project_revisions_o()
        elif x == 7:
            type = raw_input ("input release type [tags, braches]: ")
            if type in ['tags', 'branches']:
                svn_db_query.project_revisions_release_o(type)
            else :
                print "incorrect input [tags, branches], please try again"
        else:
            print "incorrect selection, pelase choose again"
    svn_db_query.svn_db_close()
            

if __name__ == "__main__":
    print "Hello World";
