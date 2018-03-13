# pyhackweek
Python package to create x-hackweek github repository template.

## Installing latest version

Linux/OSX:

```bash
wget https://raw.githubusercontent.com/lsetiawan/pyhackweek/master/requirements.txt
wget https://raw.githubusercontent.com/lsetiawan/pyhackweek/master/requirements-dev.txt
conda create -n pyhackweek -c conda-forge --file requirements.txt --file requirements-dev.txt
source activate pyhackweek
pip install https://github.com/lsetiawan/pyhackweek.git
```

## To use the script

1. Create a github organization.
2. Ensure that you have owner permission to the organization.
3. Install `pyhackweek` by following instruction above.
4. Activate the `pyhackweek` conda environment.
    ```bash
    source activate pyhackweek
    ```
4. Create credential json file called `githubcred.json` 
   with your github username and password.
    ```json
    {
      "username": "johndoe",
      "password": "mySupersecretPassword"
    }
    ```
5. Run `create_repo` and follow the script instruction.
    ```bash
    create_repo githubcred.json
    ``` 