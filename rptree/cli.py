"""This module provides the RP Tree CLI"""
# cli.py

import argparse
import sys

from . import __version__

# Alan - Dictionary, input function, traverse dictionary, pick key
# Samora - Class, decorator, staticmethod
# Ndambo - input function, kwargs, 


class Executor:
    def __init__(self, executor_obj) -> None:
        self.executor = executor_obj

    def print_dir_structure(self):
        self.executor(
            "-o",
            "--output-file",
            metavar="OUTPUT_FILE",
            nargs="?",
            default=sys.stdout,
            help="Generate a full directory tree and save it to a file"
        )

    def print_dirs_only(self):
        self.executor(
            "-d",
            "--dir-only",
            action="store_true",
            help="Generate a directory only tree"
        )

    def print_version(self):
        self.executor("-v", "--version", action="version")        

    def print_default(self):
        self.executor(
           "root_dir",
           metavar="ROOT_DIR",
           nargs="?",
           default=".",
           help="Generate a full directory tree starting at ROOT_DIR"
        )


class CliParser:
    def __init__(self, flag=None) -> None:
        self.flag = flag
        self.parse = argparse.ArgumentParser(
            prog="tree",
            description="RP Tree, a directory tree generator",
            epilog="Thanks for using RP Tree"
        )
        self.parser = self.parse.add_argument
        self.exec = Executor(self.parser)
        self.version = f"RP Tree v{__version__}"

    def __selector__(self, flag):
        controller = {
            "-o": self.exec.print_dir_structure,
            "-d": self.exec.print_dirs_only,
            "-v": self.exec.print_version,
            "root_dir": self.exec.print_default
        }
        if flag in controller.keys():
            return controller[flag]()
        return {
            "status": "error",
            "message": f"INVALID FLAG. ONLY {controller.keys()} FLAGS ARE ALLOWED"
        }

    def parse_cmd_line_arguments(self):
        args = self.parse.parse_args()
        # self.__selector__(flag)
        return args
