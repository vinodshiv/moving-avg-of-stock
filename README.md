# moving-avg-of-stock
This program takes in the security (stock), duration for simple moving average and reports the High, Low and Close of today and Moving Avg for the duration provided


# Usage
## Setup
To set up the environment for the python script, in the repo directory, do:

```sh
# do this in your virtualenv or normal terminal with sudo
pip install -r requirements.txt
```

## Run script

Before you run the script, it's highly helpful to take a quick look at the manual

```sh
python get_sma_stock.py -h
```

The mandatory arguments to the script are the stock names (comma separated) and the duration of moving average required:

```sh
python3 get_sma_stock.py -t <stock> -d <duration_in_days>
```

Here's an example
```sh
python3 get_sma_stock.py -t SNOW,V -d 20
```
