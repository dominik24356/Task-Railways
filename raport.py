import datetime
import os

list_of_input_files = os.listdir("inputs")
list_of_output_files = os.listdir("outputs")

inputs_content = []
outputs_content = []

current_date = datetime.datetime.now()


for file_name in list_of_input_files:
    with open("inputs/"+file_name) as input_file:
        temp_list = []
        for line in input_file:
            temp_list.append(line.rstrip())
        inputs_content.append(temp_list)


for file_name in list_of_output_files:
    with open("outputs/"+file_name) as output_file:
        temp_list = []
        for line in output_file:
            temp_list.append(line.rstrip())
        outputs_content.append(temp_list)


html_content = '''<html> <head><link rel="stylesheet" href="style.css"> </head> <body><h3>Raport z dzialania programu 
Task Railways | '''+str(current_date)+'''</h3><table><tr><th>Inputs</th><th>Outputs</th></tr>'''


for idx1, file_content in enumerate(inputs_content):
    for idx2, row in enumerate(file_content):
        if idx2 == 0:
            html_content += "<tr><td><div>"+row+"</div></td></tr>"
        else:
            html_content += "<tr><td>"+row+"</td><td>"+outputs_content[idx1][idx2-1]+"</td></tr>"



html_content += "</table></body></html>"


with open("raport.html", "w") as html_file:
    html_file.write(html_content)
