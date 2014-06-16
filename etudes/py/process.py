#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shlex
import subprocess
import tempfile
import time
from StringIO import StringIO


def expand_args(command):
    """Parses command strings and returns a Popen-ready list."""

    # Prepare arguments.
    if isinstance(command, basestring):
        splitter = shlex.shlex(command)
        splitter.whitespace = '|'
        splitter.whitespace_split = True
        command = []

        while True:
            token = splitter.get_token()
            if token:
                command.append(token)
            else:
                break

        command = list(map(shlex.split, command))

    return command


class run(object):

    @classmethod
    def create_process(cls, command, stdin, stdout, stderr, cwd, env, shell):
        return subprocess.Popen(
            command,
            universal_newlines=True,
            shell=shell,
            cwd=cwd,
            env=env,
            stdin=stdin,
            stdout=stdout,
            stderr=stderr,
        )

    def __new__(cls, command, **kwargs):
        env = dict(os.environ)
        env.update(kwargs.get('env', {}))

        cwd = kwargs.get('cwd')
        shell = kwargs.get('shell', False)
        stdin = kwargs.get('stdin', subprocess.PIPE)

        commands = expand_args(command)
        obj = super(run, cls).__new__(run)
        obj._stdout_file = stdout = tempfile.TemporaryFile(prefix='stdout_')
        obj._stderr_file = stderr = tempfile.TemporaryFile(prefix='stderr_')

        for cmd in commands:
            process = cls.create_process(cmd, stdin, stdout=stdout, stderr=stderr, cwd=cwd, env=env, shell=shell)
            stdin = process.stdout
            obj.process = process
        obj.outio = StringIO()
        obj.errio = StringIO()
        return obj

    def is_alive(self):
        return self.process.poll() is None

    def sleep(self, t):
        time.sleep(t)
        return self

    def wait(self):
        self.process.wait()
        self._stdout_file.seek(0)
        self._stderr_file.seek(0)
        self.stdout = self._stdout_file.read()
        self.stderr = self._stderr_file.read()
        self._stdout_file.close()
        self._stderr_file.close()

    @property
    def return_code(self):
        return self.process.returncode

    def stop(self):
        self.process.terminate()

if __name__ == '__main__':
    r = run("curl http://www.zhihu.com")
    while r.poll() is None:
        print "sleep ..."
        import time
        time.sleep(0.1)
    print r.process.pid
    print "stdout: ", r.stdout
    print "stderr: ", r.stderr
    print "stats_code: ", r.status_code
    #p = subprocess.Popen(shlex.split("curl http://www.zhihu.com"))
    #print p.communicate()
