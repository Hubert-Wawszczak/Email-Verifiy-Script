
import pandas as pd
import json
import os
import src.data_operator
import src.tools


class Manager:
    
    
    log = src.tools.ServicesClass.get_logger()


    def load_data(self, path_to_data):
        try:
            entries = os.listdir(path_to_data)
            self.data = pd.DataFrame()
            for file in entries:
                if file.endswith('.txt'):
                    temp = pd.read_csv(
                        os.path.join(
                            path_to_data,
                            file),
                        header=None)
                    self.data = pd.concat([self.data, temp])
                if file.endswith('.csv'):
                    temp = pd.read_csv(
                        os.path.join(
                            path_to_data,
                            file),
                        delimiter=';')
                    temp = temp['email']
                    self.data = pd.concat([self.data, temp])
            return self.data
        except FileNotFoundError:
            __class__.log.log_message(
                "File or directory with data not found", 4)
        except Exception:
            __class__.log.log_message(
                "Something went wrong with loading data ", 4)


    def manage(self, args):
        operator = src.data_operator.DataOperator()
        try:
            with open(os.path.join("config", "config.json"), "r") as config:
                conf = json.load(config)
                path = conf["path_to_email"]
        except FileNotFoundError:
            self.__class__.log.log_message(
                "Config file not found file should be in config directory", 4)
        except Exception:
            __class__.log.log_message(
                "Something went wrong with loading config ", 4)

        self.load_data(path)
        self.data = self.data[0]

        print()
        if args.incorrect_emails:
            operator.validate_email_print_invalid(self.data)

        self.data = operator.validate_emails_return_correct(self.data)
        self.data = operator.remove_duplicate(self.data)

        print()
        if args.search:
            operator.search_by_text(self.data, args.search)

        print()
        if args.group_by_domain:
            operator.group_by_domain(self.data)

        print()
        if args.find_emails_not_in_logs:
            operator.find_emails_not_in_log(
                self.data, args.find_emails_not_in_logs)
