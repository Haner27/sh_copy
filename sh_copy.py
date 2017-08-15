# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import shutil


class ShellException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


def sh_copy(src, dst):
    if not os.path.exists(src):
        raise ShellException('src path not found')

    if os.path.isdir(src):
        # if src is direction.
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    elif os.path.isfile(src):
        # if src is file.
        if not os.path.exists(dst):
            filename, ext = os.path.splitext(os.path.basename(dst))
            dst_dir = dst
            if ext:
                dst_dir = os.path.dirname(dst)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
        shutil.copy2(src, dst)
    else:
        raise ShellException('src must be file and direction')
