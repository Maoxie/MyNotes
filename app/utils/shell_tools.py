#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
@author: yangzhitao
@license: 
@contact: yangzhitao@sensetime.com
@software: pycharm
@time: 2020/10/31 8:01
@desc: 
"""
import logging
import subprocess
from distutils.spawn import find_executable

import traceback

logger = logging.getLogger(__name__)


class ShellExecutor:
    """An interface for shell"""

    @classmethod
    def run(cls, cmd: str, raise_on_error=False) -> (str, int):
        logger.info(f"Executing: \n{cmd}")
        try:
            out_bytes = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, executable="/bin/bash")
            code = 0
        except subprocess.CalledProcessError as e:
            out_bytes = e.output  # Output generated before error
            code = e.returncode  # Return code

        try:
            output = out_bytes.decode('utf8')
        except UnicodeDecodeError:
            try:
                output = out_bytes.decode('utf8', 'ignore')
            except UnicodeDecodeError as e:
                msg = traceback.format_exc()
                logger.error(f"Failed to read output. \n{msg}")
                output = ""
        code = code

        if raise_on_error and code:
            msg = f"exit_code: {code}, output: {output}"
            raise SystemError(msg)
        logger.info(f"End of execution, exit_status: {code}, output: {output}")
        return output, code

    @classmethod
    def is_tool(cls, name: str):
        """Check whether `name` is on PATH."""
        return find_executable(name) is not None


shell = ShellExecutor()
