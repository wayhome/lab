# -*- coding: utf-8 -*-
from fabric.api import (env,
                        run,
                        task
                        )

env.hosts = ['lin{0}'.format(x) for x in range(1, 10)]
env.use_ssh_config = True


@task
def steal():
    run("top -bcn 1 |grep Cpu |grep -v grep")


@task
def report():
    run("boinccmd --project www.worldcommunitygrid.org update")


@task
def credit():
    run("boinccmd --get_state | grep credit")


@task
def cs():
    run("top -bcn 1 |grep Cpu |grep -v grep")
    run("boinccmd --get_state | grep credit")
