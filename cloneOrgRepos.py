from github import Github
from git import Repo
import os

if __name__ == "__main__":
    import sys
    from argparse import ArgumentParser
    argumentParser = ArgumentParser()
    argumentParser.add_argument("organization",help="Git hub organization")
    argumentParser.add_argument("accesstoken",help="access token")
    argumentParser.add_argument("target",help="Target Directory")

    
    args = argumentParser.parse_args()
     
    g = Github(args.accesstoken)
    org = g.get_organization(args.organization)
    print ( "Processing repositories in", args.organization)
    repos = org.get_repos()
    count = repos.totalCount
    for i, repo in enumerate(repos):
        print ("Processing ",(i+1), "/", count,repo.name,"with url", repo.ssh_url)
        target = "{}/{}".format(args.target, repo.name)
        command = "git clone {} {}".format(repo.ssh_url, target)
        print ("Executing ", command)
        os.system(command)
        
        
        
            
    
