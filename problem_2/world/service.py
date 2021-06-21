import requests
from bs4 import BeautifulSoup


def get_html_content():
    """ Make a GET request to fetch the raw HTML content """
    url = "https://www.worldometers.info/coronavirus/"
    req_data = requests.get(url).text
    soup = BeautifulSoup(req_data, 'html.parser')
    html_data = soup.select("#main_table_countries_today > tbody:nth-child(2) > tr[style='']")
    return html_data

def get_all_countries():
    response = []
    html_data = get_html_content()
    for ii in range(len(html_data)):
        data = html_data[ii].get_text().split("\n")[1:-1]
        index = data[0]
        country_name = data[1]
        total_cases = data[2]
        active_cases = data[8]
        total_deaths = data[4]
        total_recover = data[6]
        population = data[14].strip()

        if total_recover != 'N/A' and total_cases != 'N/A':
            #   Total Recovered/Total Cases
            recovery_rate = "{:.2%}".format(
                int("".join(total_recover.split(','))) / int("".join(total_cases.split(','))))
        else:
            recovery_rate = None

        #   (Total Cases/Population)
        if total_recover != 'N/A' and population != '':
            percentage_population_infected = "{:.2%}".format(
                int("".join(total_cases.split(','))) / int("".join(population.split(','))))
        else:
            percentage_population_infected = None

        response.append({"id": index,
                         "country": country_name,
                         "total_cases": total_cases,
                         "active_cases": active_cases,
                         "total_deaths": total_deaths,
                         "total_recover": total_recover,
                         "population": population,
                         "recovery_rate": recovery_rate,
                         "population_infected": percentage_population_infected})
    return response


def get_county(country):
    response = {}
    html_data = get_html_content()
    for ii in range(len(html_data)):
        if html_data[ii].get_text().find(country.title()) != -1:
            data = html_data[ii].get_text().split("\n")[1:-1]
            index = data[0]
            country_name = data[1]
            total_cases = data[2]
            active_cases = data[8]
            total_deaths = data[4]
            total_recover = data[6]
            population = data[14].strip()

            #     print(ii,country_name,total_cases,repr(population))
            if total_recover != 'N/A' and total_cases != 'N/A':
                #   Total Recovered/Total Cases
                recovery_rate = "{:.2%}".format(
                    int("".join(total_recover.split(','))) / int("".join(total_cases.split(','))))
            else:
                recovery_rate = None
            #   (Total Cases/Population)

            if total_recover != 'N/A' and population != '':
                percentage_population_infected = "{:.2%}".format(
                    int("".join(total_cases.split(','))) / int("".join(population.split(','))))
            else:
                percentage_population_infected = None

            response.update({"id": index,
                             "country": country_name,
                             "total_cases": total_cases,
                             "active_cases": active_cases,
                             "total_deaths": total_deaths,
                             "total_recover": total_recover,
                             "population": population,
                             "recovery_rate": recovery_rate,
                             "population_infected": percentage_population_infected})
            return response
