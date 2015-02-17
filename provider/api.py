# coding=utf-8
from django.template import Template, Context

import SoftLayer
from SoftLayer.CLI.modules.vs import CreateVS

import yaml

class Provider(object):
    def __init__(self):
        self.client = SoftLayer.Client(
            username='',
            api_key=''
        )

    def create_instance(self):
        with open('templates/provider/conf.yml', 'r') as f:
            yml = Template(f.read()).render(Context())

        params = yaml.load(yml)
        print params
        return CreateVS(self.client).execute(params)
