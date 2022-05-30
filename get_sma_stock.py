# -*- coding: utf-8 -*
# @author: vshiv
# @date: 2022-05-30
# @filename: get_sma_stock.py

# python3 get_sma_stock.py -t SNOW,V -d 20

"""This program takes in the security (stock), duration for simple moving average and reports the High, Low and Close of today and Moving Avg for the duration provided """


from optparse import OptionParser
from datetime import datetime, timedelta

from pandas_datareader import data as web

DASHES = '-'*50


if __name__ == '__main__':

    usage = """usage: %prog -t <stock> -d <duration in days>"""

    # add parsers
    parser = OptionParser(usage=usage)
    parser.add_option(
        '-t',
        '--ticker',
        type='string',
        action='store',
        dest='ticker',
        default='',
        help='the ticker for your stock')
    parser.add_option(
        '-d',
        '--duration',
        action='store',
        dest='duration',
        help="the duration for number of days from which you need the moving avg price")

    opts, args = parser.parse_args()

    try:
        ticker = opts.ticker
        duration = int(opts.duration)
    except parser.error() as e:    
        print("Either ticker or number of days is not provided")
        exit(1)

    ### get ticker data from start-date ###
    # Set endDate as today's date
    now = datetime.now()

    startDate = (now - timedelta(duration)).strftime("%Y-%m-%d")
    endDate = now.strftime("%Y-%m-%d")
    numDays = now - datetime.strptime(startDate, "%Y-%m-%d")

    # Make a list out of the tickers entered
    ticker_list = ticker.replace(' ', '').split(',')

    # Create a report format
    report = (f"{DASHES}\n\t-- Moving Average Stock Report --\n"
              f"\t{startDate} --> {endDate} ({numDays.days} days)\n{DASHES}")

    # Iterate through the ticker list and build the report for each
    for i in ticker_list:
        # Get data from yahoo
        ticker_df = web.get_data_yahoo(i,
                                       startDate,
                                       endDate)
        ticker_df = ticker_df.drop('Adj Close', axis=1)

        # Get today's data
        todays_data_df = ticker_df.reset_index().round(2).iloc[-1:]

        # Add average close value
        todays_data_df['Moving Avg'] = ticker_df.mean().round(2)['Close']

        all_col_list = ['Date', 'High', 'Low',
                        'Close', 'Volume', 'Moving Avg']
        curr_col_list = ['High', 'Low', 'Close', 'Moving Avg']

        # Finalize columns and format as currency
        today_df = todays_data_df[all_col_list]
        today_df = todays_data_df[curr_col_list].applymap(
            lambda x: f"${x:.2f}")

        # Append to report
        report = '\n'.join((report, f"\t\t-- [{i.upper()}] --"))
        report = '\n'.join((report, str(today_df.to_markdown(index=False, tablefmt="fancy_grid"))))
        report = '\n'.join((report, DASHES))

    # console output
    print(report)

