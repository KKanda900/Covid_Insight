import requests, os, csv, operator

'''
1/16/20 -> work on making a helper method for def update()
'''

def find_file(state):
    for filename in os.listdir('data/'):
        if filename.startswith('{}_Data.csv'.format(state)):
            pathname = filename
    
    return 'data/' + pathname

def update():
    if os.path.exists("us-states.csv"):
        os.remove("us-states.csv")

    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv' # most up to date data for COVID-19 positive cases
    r = requests.get(url, allow_redirects=True)

    open('data/us-states.csv', 'wb').write(r.content)

    sample = open('data/us-states.csv', 'r')

    csv1 = csv.reader(sample, delimiter=',')

    sort = sorted(csv1, key=operator.itemgetter(1))
    i = 0
    with open('data/AL_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Alabama'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/AK_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Alaska'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/AZ_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Arizona'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/AR_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Arkansas'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/CA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'California'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/CO_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Colorado'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/CT_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Connecticut'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/DE_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Delaware'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/FL_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Florida'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/GA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Georgia'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/HI_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Hawaii'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/ID_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Idaho'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/IL_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Illinois'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/IN_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Indiana'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/IA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Iowa'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/KS_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Kansas'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/KY_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Kentucky'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/LA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Louisiana'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/ME_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Maine'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/MD_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Maryland'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/MA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Massachusetts'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/MI_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Michigan'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/MN_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Minnesota'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/MS_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Mississippi'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/MO_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Missouri'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/MT_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Montana'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/NE_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Nebraska'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/NV_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Nevada'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/NH_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'New Hampshire'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/NJ_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'New Jersey'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/NM_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'New Mexico'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/NY_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'New York'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/NC_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'North Carolina'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/ND_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'North Dakota'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/OH_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Ohio'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/OK_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Oklahoma'):    
                csvwriter.writerow((eachline[0], eachline[3]))
    
    i = 0
    with open('data/OR_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Oregon'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/PA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Pennsylvania'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/RI_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Rhode Island'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/SC_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'South Carolina'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/SD_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'South Dakota'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/TN_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Tennessee'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/TX_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Texas'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/UT_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Utah'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/VT_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Vermont'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/VA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Virginia'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/WA_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Washington'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/WV_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'West Virgina'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/WI_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Wisconsin'):    
                csvwriter.writerow((eachline[0], eachline[3]))

    i = 0
    with open('data/WY_Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for eachline in sort:
            if i == 0:
                csvwriter.writerow(("date", "cases"))
                i = i + 1

            if(eachline[1] == 'Wyoming'):    
                csvwriter.writerow((eachline[0], eachline[3]))






