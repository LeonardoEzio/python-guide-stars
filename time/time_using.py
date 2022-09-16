from datetime import datetime
from dateutil.relativedelta import relativedelta


if __name__ == "__main__":
    begin_date_str = "01-01-2020"
    begin_date = datetime.strptime(begin_date_str, '%d-%m-%Y')
    print(begin_date)
    format_begin_date = datetime.strftime(begin_date, '%Y-%m-%dT%H:%M:%S')
    print("format_begin_date", format_begin_date)
    end_date = begin_date + relativedelta(days=90)
    format_end_date = datetime.strftime(end_date, '%Y-%m-%dT%H:%M:%S')
    print("format_end_date", format_end_date)

