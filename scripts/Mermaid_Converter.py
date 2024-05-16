import os
import csv
import pandas as pd
dict_of_csv_files = {}
for i in os.listdir("CSV_Files"):
    i_1 = i.replace(" ", ":").replace(".csv", "")
    with open(f"CSV_Files/{i}", 'r') as file:
        # Create a CSV reader object
        csv_file = pd.DataFrame(pd.read_csv(f"CSV_Files/{i}",delimiter=','))
        test = csv_file.T.to_dict(orient='list')
        test_2 = {}
        if i_1 == "dcat:Resource":
            test_2.update({'arrow': {"mandatory": []}})
            test_2['arrow'].update({"recommended": []})
            test_2['arrow'].update({"optional": []})
            test_2.update({'regular': {"mandatory": []}})
            test_2['regular'].update({"recommended": []})
            test_2['regular'].update({"optional": []})
        else:
            test_3 = []
            test_4 = []
            test_5 = []
            test_6 = []
            test_7 = []
            test_8 = []
            for i_2 in test:
                if test[i_2][4] == "-":
                    if test[i_2][2] == "mandatory":
                        test_3.append(f"{test[i_2][1]} {test[i_2][5]} [{test[i_2][2].replace('mandatory', '1').replace('recommended', '0').replace('optional', '1')}...{'*'if test[i_2][6] else '1'}] ")
                    elif test[i_2][2] == "recommended":
                        test_4.append(f"{test[i_2][1]} {test[i_2][5]} [{test[i_2][2].replace('mandatory', '1').replace('recommended', '0').replace('optional', '1')}...{'*'if test[i_2][6] else '1'}] ")
                    elif test[i_2][2] == "optional":
                        test_5.append(f"{test[i_2][1]} {test[i_2][5]} [{test[i_2][2].replace('mandatory', '1').replace('recommended', '0').replace('optional', '1')}...{'*'if test[i_2][6] else '1'}] ")
                elif test[i_2][3] == "-":
                    if test[i_2][2] == "mandatory":
                        test_6.append(f"{test[i_2][1]} {test[i_2][5]} [{test[i_2][2].replace('mandatory', '1').replace('recommended', '0').replace('optional', '1')}...{'*'if test[i_2][6] else '1'}] ")
                    elif test[i_2][2] == "recommended":
                        test_7.append(f"{test[i_2][1]} {test[i_2][5]} [{test[i_2][2].replace('mandatory', '1').replace('recommended', '0').replace('optional', '1')}...{'*'if test[i_2][6] else '1'}] ")
                    elif test[i_2][2] == "optional":
                        test_8.append(f"{test[i_2][1]} {test[i_2][5]} [{test[i_2][2].replace('mandatory', '1').replace('recommended', '0').replace('optional', '1')}...{'*'if test[i_2][6] else '1'}] ")
            test_2.update({'arrow': {"mandatory": test_3}})
            test_2['arrow'].update({"recommended": test_4})
            test_2['arrow'].update({"optional": test_5})
            test_2.update({'regular': {"mandatory": test_6}})
            test_2['regular'].update({"recommended": test_7})
            test_2['regular'].update({"optional": test_8})


        dict_of_csv_files.update({i_1: test_2})

        test_14 = ''

        dict_of_csv_files_for_mermaid = {}
        for i_4 in dict_of_csv_files:
            test_9 = 'class `' + i_4 +'` {\n'
            for i_5 in dict_of_csv_files[i_4]['regular']:
                test_9 = test_9 + '  # ' + i_5 + '\n'
                for i_6 in dict_of_csv_files[i_4]['regular'][i_5]:
                    test_9 = test_9 + '  ' + i_6.replace(':','#58;') + '\n'
            test_9 = test_9 + '}' + '\n'
            test_14 += test_9
            dict_of_csv_files_for_mermaid.update({i_4: test_9})

        for i_6 in dict_of_csv_files:
            test_10 = ''
            for i_7 in dict_of_csv_files[i_6]['arrow']:
                for i_8 in dict_of_csv_files[i_6]['arrow'][i_7]:
                    test_11_1 = '`' + i_6 + '`'
                    test_11 = '`' + i_8.split()[1] + '`'
                    test_12 = i_8.split()[0].replace(':','#58;')
                    test_13 = i_8.split()[2].replace('[','"').replace(']','"').replace('...','..')
                    test_10 = test_10 + f'{test_11_1} --> {test_13} {test_11} : {test_12}' + '\n'
            test_14 += test_10 + '\n'

    test_15 = '```mermaid \nclassDiagram\n\n' + test_14 + '\n```'
with open(f"Mermaid_Diagramm.md", 'w') as file:
    file.write(test_15)
