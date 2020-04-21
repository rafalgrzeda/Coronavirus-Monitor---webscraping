import requests
from bs4 import *


class Scrapper:

    def get_poland_data(self):

        # Połączenie ze stroną intenretową
        answer = requests.get('https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2')
        # Parser
        soup = BeautifulSoup(answer.text, 'html.parser')
        # Pobranie danych
        data = soup.find(id="registerData").text
        # Usuniecie niepotzebnych znakow
        data = data.replace("\\n", " ").strip()
        data = data.replace("\\r", " ").strip()

        # Znalezienia odpowiednich wartości
        indx_list = []
        for i in range(17):
            if i < 5:
                t = "t0" + str(i * 2)
                indx_list.append(data.find(t))
            else:
                t = "t" + str(i * 2)
                indx_list.append(data.find(t))

        # Znalezienie odpowiednich linii
        lines = []
        for i in range(16):
            lines.append(data[indx_list[i] + 5: indx_list[i + 1]])

        # Zapis danych do list
        woj_list = []
        infect_list = []
        death_list = []

        for line in lines:
            split_line = line.split(";")
            woj_list.append(split_line[0])
            infect_list.append(split_line[1])
            death_list.append(split_line[2])

        return woj_list, infect_list, death_list

