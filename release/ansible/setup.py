#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()

dependency_links = [
]

test_requirements = [
    # TODO: put package test requirements here
]

setuptools.setup(
    name='ose-ansible-operator',
    version='4.14',
    description=("Ansible Operator base image"),
    url='https://github.com/openshift/ocp-release-operator-sdk',
    install_requires=requirements
)
