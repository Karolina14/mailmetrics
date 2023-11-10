import argparse
import os
import logging
from charset_normalizer import detect

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Converter to UTF-8 encoding')
parser.add_argument('--input', type=str, default='/data/input/file.txt', help='Path to input file with .txt extension')
parser.add_argument('--output', type=str, default='/data/output/file.txt',
                    help='Path to output file with .txt extension')


class EncodingConverter:
    def __init__(self, input_file_path, output_file_path):
        if type(input_file_path) != str:
            raise TypeError("input_file_path should be string")

        if type(output_file_path) != str:
            raise TypeError("output_file_path should be string")

        if not os.path.exists(input_file_path):
            raise FileNotFoundError("Input file not found", input_file_path)

        logger.debug(f"INPUT FILE {input_file_path}")

        if input_file_path.split('.')[-1] != 'txt':
            raise Exception("File should be .txt")

        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.dest_encoding = 'utf-8'
        self.src_encoding = None

    def convert(self):
        logger.debug(f"Start converting file")

        input_f = open(self.input_file_path, "rb")
        content = input_f.read()
        result = detect(content)
        input_f.close()

        self.src_encoding = result['encoding']
        logger.info(f"Detected encoding {result['encoding']}")

        output_f = open(self.output_file_path, "w", encoding=self.dest_encoding)
        output_f.write(content.decode(self.src_encoding))
        output_f.close()

        logger.debug(f"End converting file")


def main(input_file_path, output_file_path):
    converter = EncodingConverter(input_file_path, output_file_path)
    converter.convert()


if __name__ == '__main__':
    args = parser.parse_args()
    args_dict = vars(args)
    main(args_dict['input'],
         args_dict['output'])
