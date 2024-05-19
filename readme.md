## Python environment setup
1. install conda
2. setup conda env
```
conda create -n poetry python==3.8.11
conda activate poetry
pip install poetry==1.7.0
```


3. make ta-lib (OPTIONAL)
```
cd expert-advisor
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz \
  && sudo tar -xzf ta-lib-0.4.0-src.tar.gz \
  && sudo rm ta-lib-0.4.0-src.tar.gz \
  && cd ta-lib/ \
  && sudo ./configure --prefix=/usr \
  && sudo make \
  && sudo make install
  && cd .. \
  && sudo rm -rf ta-lib/
  ```

4. clone repo
`git clone https://github.com/harriss212/expert-advisor`

5. install packacges
```
cd expert-advisor
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
poetry install
```


6. make file
/expert-advisor/apikey.py
inside
key="XXXXXXXXXXX"



6. execution
`poetry run python -m expert-advisor.example`

7. testing
`tox -e unit`
`tox -e format`


PACKAGE LIST
poetry
pandas-ta
TA-Lib
scipy
pandas
torch
gradient-free-optimisers
scikit-learn
black
pytest
jupyter-notebook
tox
poetry-tox
pytest-cov