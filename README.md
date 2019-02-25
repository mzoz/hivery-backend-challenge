## How to use

1. Make a local copy:

    ```sh
    $ git clone https://github.com/mzoz/hivery-backend-challenge.git
    $ cd hivery-backend-challenge
    ```

1. Create and activate virtual env:

    ```sh
    $ python3 -m venv env
    $ source env/bin/activate
    ```

    > **NOTE**: You know that you are in a virtual environment as "env" is now showing before the $ in your terminal - (env)$. To exit the virtual environment, use the command `deactivate`. You can reactivate by navigating back to the project directory and running `source env/bin/activate`.

1. Install Flask with pip:

    ```sh
    (env)$ pip install flask==1.0.2
    ```

1. Run test:

    ```sh
    (env)$ python test.py
    ```
    
1. Run app (different json files ok, file names are hard coded though):

    ```sh
    (env)$ python app.py
    ```

## URLs

1. Get employees given company name:

    ```
    http://127.0.0.1:5000/hivery/api/v1.0/company/<company_name>
    ```
    
    e.g.
    ```
    http://127.0.0.1:5000/hivery/api/v1.0/company/eargo
    ```
    
1. Get friends given two people:

    ```
    http://127.0.0.1:5000/hivery/api/v1.0/people/<id1>/<id2>
    ```
    
    e.g.
    ```
    http://127.0.0.1:5000/hivery/api/v1.0/people/1/2
    ```
    
1. Get personal info:

    ```
    http://127.0.0.1:5000/hivery/api/v1.0/people/<id>
    ```
    
    e.g.
    ```
    http://127.0.0.1:5000/hivery/api/v1.0/people/100
    ```
 
    
