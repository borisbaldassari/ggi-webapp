######################################################################
# Copyright (c) 2021 Castalia Solutions and others
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0
######################################################################

import gitlab
import pprint
import re

gl_url = "https://gitlab.ow2.org"
project_id = 1654

pp = pprint.PrettyPrinter(indent=4)


gl = gitlab.Gitlab(gl_url, per_page=50)

project = gl.projects.get(project_id)
print("Project is:", project.id)

#issues = project.issues.list()
print("# Fetching issues..")
issues = project.issues.list(state='opened', all=True)

print("# Exporting issues..")
desc = re.compile("## Description\s*\n+(.*?)\.")
goals = re.compile("(.*) Goal")

tables = {'usage': '', 'trust': '', 'culture': '', 'engagement': '', 'strategy': ''}

for i in issues:
    print("* Issue", i.iid, "-", i.title)
#    print(i)
    res = desc.search(i.description)
    goal = goals.search(list((filter(goals.match, i.labels)))[0]).group(1)
    tables[goal.lower()] += "|" + str(i.iid) + "|[" + i.title + "](../../activities/activity_" + str(i.iid) + "/)|\n"

    # Commented lines could be useful when a convention is adopted to extract the
    # first sentence/line/paragraph of the description.
    #if (res):
    #    description = res.group(1)
    #else:
#    description = 'unknown'
    k = []
    for l in i.labels:
        m = l.replace(" ", "_")
        k.append(m)
    print(k)
    tags = "[\"" + '","'.join(k) + "\"]"
    header = [
        "---",
        "title: " + i.title,
        "tags: " + tags,
#        "description: " + description,
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

    
