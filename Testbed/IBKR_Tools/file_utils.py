import os

from .data_status import DataStatus


class FileUtils:
    @staticmethod
    def writeToFile(filePath, data):
        with open(filePath, 'w') as file:
            file.write(data)

    @staticmethod
    def confirmData(filepath: str):
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
