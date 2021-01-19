import requests, os, csv, operator

def find_file(state):
    for filename in os.listdir('data/'):
        if filename.startswith('{}_Data.csv'.format(state)):
            pathname = filename

    return 'data/' + pathname

def make_files(sort):
    states = ['AL', 'Alabama', 'AK', 'Alaska', 'AZ', 'Arizona', 'AR', 'Arkansas', 'CA', 'California', 'CO', 'Colorado', 'CT', 'Connecticut', 'DE', 'Delaware', 'FL', 'Florida', 'GA', 'Georgia', 'HI', 'Hawaii',
              'ID', 'Idaho', 'IL', 'Illinois', 'IN', 'Indiana', 'IA', 'Iowa', 'KS', 'Kansas','KY', 'Kentucky', 'LA', 'Louisiana', 'ME', 'Maine', 'MD', 'Maryland', 'MA', 'Massachusetts', 'MI', 'Michigan',
              'MN', 'Minnesota', 'MS', 'Mississippi', 'MO', 'Missouri', 'MT', 'Montana', 'NE', 'Nebraska', 'NV', 'Nevada', 'NH', 'New Hampshire', 'NJ', 'New Jersey', 'NM', 'New Mexico', 'NY', 'New York', 'NC', 'North Carolina',
              'ND', 'North Dakota', 'OH', 'Ohio', 'OK', 'Oklahoma', 'OR', 'Oregon', 'PA', 'Pennsylvania', 'RI', 'Rhode Island', 'SC', 'South Carolina', 'SD', 'South Dakota', 'TN', 'Tennessee',
              'TX', 'Texas', 'UT', 'Utah', 'VT', 'Vermont', 'VA', 'Virginia', 'WA', 'Washington', 'WI', 'Wisconsin', 'WY', 'Wyoming']

    for one, two in zip(states[::2], states[1::2]):
        i = 0
        with open('data/{}_Data.csv'.format(one), 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            for eachline in sort:
                if i == 0:
                    csvwriter.writerow(("date", "cases"))
                    i = i + 1

                if(eachline[1] == '{}'.format(two)):
                    csvwriter.writerow((eachline[0], eachline[3]))

def update():
    if os.path.exists("us-states.csv"):
        os.remove("us-states.csv")

    # most up to date data for COVID-19 positive cases
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
    r = requests.get(url, allow_redirects=True)

    open('data/us-states.csv', 'wb').write(r.content)

    sample = open('data/us-states.csv', 'r')

    csv1 = csv.reader(sample, delimiter=',')

    sort = sorted(csv1, key=operator.itemgetter(1))
    make_files(sort)
