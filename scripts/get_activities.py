import gitlab
import pprint
import re

gl_url = "https://gitlab.ow2.org"
project_id = 1654

pp = pprint.PrettyPrinter(indent=4)


gl = gitlab.Gitlab(gl_url)

project = gl.projects.get(project_id)
print("Project is: ")
print("ID:", project.id)

#issues = project.issues.list()
issues = project.issues.list(state='opened')

print("# KEYS ##############################")
issue = issues[0]
#pp.pprint(issue.__dict__) #.keys())
#pp.pprint(issue._attrs.keys()) #.keys())

print("# DESC ##############################")
print(issue.description)

print("# ISSUES ##############################")
pattern = re.compile("## Description\s*\n+(\w\s*)\n+## Opportunity Assessment")

for i in issues:
    print("## Issue", i.iid)
    res = pattern.search(i.description)
    if (res):
        description = res.group(1)
    else:
        description = 'unknown'

    desc = "| NAME | DESCRIPTION | LINK |"
    desc += "|:--|:--|:--|"
    header = [
        "---",
        "title: " + i.title,
        "description: " + description,
        "---"
        ]
    fname = "../webapp/content/activities/activity_" + str(i.iid) + ".md"
    f = open(fname, "w") 
    f.write("\n".join(header) + "\n")
    f.write(i.description)
    f.close()


    
