from Scrapper import Scrapper
from DataContainer import DataContainer


def main():
    scrapper = Scrapper()
    data = DataContainer.get_instance()

    woj_list, infect_list, death_list = scrapper.get_poland_data()
    data.upload_poland_data(infect_list, death_list)

    print("Liczba zakazonych: " + str(data.POLAND_INFECT))
    print("Liczba zmarłych: " + str(data.POLAND_DEATHS))

    for i in range(len(woj_list)):
        print("Wojewodztwo: " + woj_list[i] + " Liczba zakazonych:  " +  infect_list[i] + " Liczba zgonow: " + death_list[i])
    #print(woj_list)
    #print(infect_list)
    #print(death_list)


main()





