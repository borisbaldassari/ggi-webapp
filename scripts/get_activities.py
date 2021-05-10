import gitlab
import pprint
import re
#import string

gl_url = "https://gitlab.ow2.org"
project_id = 1654

pp = pprint.PrettyPrinter(indent=4)


gl = gitlab.Gitlab(gl_url)

project = gl.projects.get(project_id)
print("Project is:", project.id)

#issues = project.issues.list()
print("# Fetching issues..")
issues = project.issues.list(state='opened')

#print("# KEYS ##############################")
#issue = issues[0]
#pp.pprint(issue.__dict__) #.keys())
#pp.pprint(issue._attrs.keys()) #.keys())

#print("# DESC ##############################")
#print(issue.description)

print("# Exporting issues..")
desc = re.compile("## Description\s*\n+(.*?)\.")
goals = re.compile("(.*) Goal")

tables = {'usage': '', 'trust': '', 'culture': '', 'engagement': '', 'strategy': ''}

for i in issues:
    print("* Issue", i.iid)
    print(i)
    res = desc.search(i.description)
    goal = goals.search(list((filter(goals.match, i.labels)))[0]).group(1)
    print("Goal is ", goal)
    tables[goal.lower()] += "|" + str(i.iid) + "|" + i.title + "|\n"

    #if (res):
    #    description = res.group(1)
    #else:
    description = 'unknown'
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

#print(tables)

table = "\n\n| ID | Title |\n"
table += "|:--|:--|\n"
for g in list(tables):
    file_goal = "../webapp/content/goals/" + g + ".md"
    with open(file_goal, "a") as myfile:
        myfile.write(table)
        myfile.write(tables[g])

    
