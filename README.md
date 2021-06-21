# Demo

### project set up ###
  
#### Using pip ####
  - Requires activate virtual environment
  - install required packages from requirement.txt 
  
```sh
 pip install -r requirement.txt
 ```
 
 #### Using pipenv ####
  - pipenv should be install outside virtual environment
   ```sh
   pip install pipenv 
 ```
  - activate virtual environmentwith 
  ```sh
   pipenv shell
 ```
  - to install all pakages from pipfile
  
```sh
 pipenv install
 ```
  - can run the project with this command after installing packages
  
```sh
cd problem_2
python manage.py runserver
```




## API LIST
### END USER

| Name | Method | URL | Payload |
| ------ | ------ |  ------ |------ |
| Get Countires List | GET | http://localhost:8000/api/countries| {"response": [{},{},....]}|
| Get country by name | GET | http://localhost:8000/api/country/<country_name>/| {"response": {  "id": "2","country": "India","total_cases": "29,935,221", "active_cases": "702,858", "total_deaths": "388,164 ", "total_recover": "28,844,199", "population": "1,393,123,813", "recovery_rate": "96.36%", "population_infected": "2.15%"}} |

  
  
  
  
  # Mock Data
    
 ```sh
 {
    "response": {
        "id": "2",
        "country": "India",
        "total_cases": "29,935,221",
        "active_cases": "702,858",
        "total_deaths": "388,164 ",
        "total_recover": "28,844,199",
        "population": "1,393,123,813",
        "recovery_rate": "96.36%",
        "population_infected": "2.15%"
    }
}
```
