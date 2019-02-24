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
