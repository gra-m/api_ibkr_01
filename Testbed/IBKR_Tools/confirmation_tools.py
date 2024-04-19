import os

from .data_status import DataStatus


def stop(self):
    self.disconnect()


def confirm_data(filepath: str):
    if os.path.isfile(filepath):

        with open(filepath, 'r') as file:
            content = file.read()
        if content:
            print(f"""
            {filepath}
            {DataStatus.OK.value}
             """)
            return DataStatus.OK
        else:
            print(f""" 
            {filepath} 
            {DataStatus.EMPTY.value}
            """)
            return DataStatus.EMPTY

    else:
        print(f"""
        {filepath}
        {DataStatus.NOT_EXIST.value}
        """)
        return DataStatus.NOT_EXIST
