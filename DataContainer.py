import os
from datetime import date


class DataContainer:
    POLAND_INFECT = 0
    POLAND_DEATHS = 0

    POLAND_INFECT_HISTORY = []
    POLAND_DEATHS_HISTORY = []
    TXT_FILE_POLAND = 'poland.txt'
    _instance = None

    @staticmethod
    def get_instance():
        if DataContainer._instance == None:
            DataContainer()
        return DataContainer._instance

    def __init__(self):
        if DataContainer._instance != None:
            raise Exception("This class is Singleton")
        else:
            DataContainer._instance = self

        self.load_data()

    def load_data(self):
        self.POLAND_DEATHS = 0
        self.POLAND_INFECT = 0
        working_dir = os.getcwd()
        with open(os.path.join(working_dir, self.TXT_FILE_POLAND), 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(";")
                self.POLAND_INFECT_HISTORY.append(data[1])
                self.POLAND_DEATHS_HISTORY.append(data[2])
                self.POLAND_INFECT += int(data[1])
                self.POLAND_DEATHS += int(data[2])

    def upload_poland_data(self, infect_list, death_list):

        count_inf = 0
        count_death = 0
        for inf in infect_list:
            count_inf += int(inf)

        for death in death_list:
            if not death == "":
                count_death += int(death)

        self.save_data(count_inf, count_death)

    def save_data(self, infects, deaths):
        working_dir = os.getcwd()
        today = date.today().strftime("%d/%m/%Y")

        with open(os.path.join(working_dir, self.TXT_FILE_POLAND), 'a+') as file:
            data = today + ";" + str(infects - self.POLAND_INFECT) + ";" + str(deaths - self.POLAND_DEATHS) + "\n"
            file.seek(0)
            lines = file.readlines()
            if lines:       # jesli plik nie jest pusty
                last_line = lines[-1]
                f_date = last_line.split(";")
                if not f_date[0] == today:      #nowe dane - dodanie linijki
                    file.write(data)
                else:                           # edycja danych
                    lines[1] = data
                    with open(os.path.join(working_dir, self.TXT_FILE_POLAND), 'w') as f:
                        f.writelines(lines)
            else:
                file.write(data)

        self.load_data()