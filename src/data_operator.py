
from cgitb import reset
from email import header
from unittest import result
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from itertools import count
from textwrap import indent
import src.tools
from dataclasses import dataclass
import re
import pandas as pd


@dataclass
class DataOperator():
    log = src.tools.ServicesClass.get_logger()
    
    @classmethod
    def validate_email_print_invalid(cls, email):
        email = email[email.str.match(r'^[^@ \n]{1,}@{1}\S{1,}\.[a-zA-Z0-9]{1,4}$')==False]
        print(f"Invalid emails({email.count()}):")
        print(email.to_string(index=False))

    @classmethod
    def validate_emails_return_correct(cls, email):
        email = email[email.str.match(r'^[^@ \n]{1,}@{1}\S{1,}\.[a-zA-Z0-9]{1,4}$')==True]
        return email
    
    @classmethod
    def remove_duplicate(cls, df):
        df.sort_values(0, inplace = True)
        df = pd.DataFrame(df)
        return df.drop_duplicates(subset = 0,
                     keep = 'first', inplace = False)
        
    @classmethod
    def search_by_text(cls, _df , text):
        text = text.strip()
        df = pd.DataFrame(_df, columns=[0])
        df = df[df[0].str.contains(text)==True]
        df.index.name = None
        counter = str(df[0].count())
        print(f"Found emails with '{text}' in email:({counter})")
        print(df.to_string(index=False, header=False))


    
    @classmethod
    def group_by_domain(cls, df):
        df = df[0].str.split('@', expand = True)
        df = df.sort_values(1, inplace = False)
        temp = df[1].value_counts(ascending = True)
        
        temp = pd.DataFrame(temp)

        temp.sort_index(inplace = True)
        for index, value in temp.iterrows():
            print(f"Domain {index} ({value[1]}):")
            result = df[df[1].str.contains(index)==True]
            result.sort_values(0, inplace=True)
            result = "   " + result[0].map(str)+ "@" + index
            print(result.to_string(index=False, header=False))

    
    @classmethod
    def find_emails_not_in_log(cls, df, path):
        try:
            path = path.strip()
            log_data_frame = pd.read_csv(path,delimiter="'",header=None)
        except FileNotFoundError:
            __class__.log.log_message("File not found",4)
        result = pd.DataFrame(df[0])
        result = pd.concat([result, log_data_frame[1]])
        result = result.drop_duplicates(keep = False)
        print(f"Email not sent ({result[0].count()})")
        print(result.to_string(index = False, header = False))