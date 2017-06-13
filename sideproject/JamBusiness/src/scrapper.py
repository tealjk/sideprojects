from indeed import IndeedClient

import psycopg2





joblist = {
    'line1' : [[1, "results"]],
    'line2' : [[3, "jobtitle"]],
    'line3' : [[5, "city"]],
    'line4' : [[6, "company"]],
    'line5' : [[7, "state"]],
    'line6' : [[8, "county"]],
    'line7' : [[9, "language"]],
    'line8' : [[9, "url"]],
}



try:
    conn = psycopg2.connect("dbname=radius user=radius_admin host=radius-dev.cp21af7opq91.us-east-1.rds.amazonaws.com password=hood_Richness port=5432")
except:
    print "I am unable to connect to the database"


cur = conn.cursor()
cur.execute("SELECT * FROM listingtest;")



try:
    r = requests.get('http://api.indeed.com/ads/apisearch?publisher=4405390899698537&q=&l=20010&radius=1&format=json&start=1&limit=1000&v=2')
    r = r.json()
    jobs = []
    print(jobs)
except:
    print "the Json Object was not created"




try:

    cur.execute("CREATE TABLE listingtest (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("INSERT INTO listingtest (num, data) VALUES (%s, %s)", (100, "abc'def"))
    cur.execute("SELECT * FROM listingtest;")
    cur.fetchone()
    (1, 100, "abc'def")
    conn.commit()
    cur.close()
    conn.close()
    client = IndeedClient(publisher = 4405390899698537 )
    print "we are done making your table"

except:
    print "I cannot created new table"






print joblist
