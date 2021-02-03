#Bella 20210203
#[country_en, country_ko, cityname_olddb_en, cityname_olddb_ko, cityname_new_en, cityname_new_ko]
import psycopg2


host = "localhost"
dbname = "pintween"
port = 5432
user = "yeonheelee"
password = "pintween1234"

cityInfoList=[]

def make_cityname_list():
    with open('asia_cityname_update_share.txt','r') as file:
            #print(file.read())
        cityInfo = file.read().lstrip("[").rstrip("\n]")
        print(cityInfo)

        cityInfo = cityInfo.split("], [") #type list

        print(cityInfo[0]) #type str
        print(cityInfo[1])


        for city in cityInfo:
            cityInfoList.append(city.split(', '))

        print("city count")
        print(len(cityInfoList))
        # print(cityInfoList[0])


def change_cityname_new_ko():
    #DB Connect
    conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
    cur = conn.cursor()
    database_name = "core_pointofinterestko"


    for elem in cityInfoList:#asia : 108
        country_ko = elem[1]
        cityname_olddb_ko = elem[3]
        cityname_new_ko = elem[5]

        cur.execute("""UPDATE {} SET city = {} WHERE country = {} and city = {}""".format(database_name, cityname_new_ko, country_ko, cityname_olddb_ko))
        #cur.execute("""SELECT city FROM {} WHERE country = {} and city = {}""".format(database_name, country_ko, cityname_olddb_ko))

        print(str(country_ko) + "  " + str(cityname_olddb_ko) + "  " + str(cityname_new_ko))


    conn.commit()
    cur.close()
    conn.close()

#main
make_cityname_list()
change_cityname_new_ko()
