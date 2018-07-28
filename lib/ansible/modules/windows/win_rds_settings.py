#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Kevin Subileau (@ksubileau)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: win_rds_settings
short_description: Manage main settings of a Remote Desktop Gateway server
description:
  - Configure general settings of a Remote Desktop Gateway server.
version_added: "2.7"
author:
  - Kevin Subileau (@ksubileau)
options:
  certificate_hash:
    description:
      - Certificate hash (thumbprint) for the Remote Desktop Gateway server. The certificate hash is the unique identifier for the certificate.
  max_connections:
    description:
      - The maximum number of connections allowed.
      - If set to C(0), no new connections are allowed.
      - If set to C(-1), the number of connections is unlimited.
requirements:
  - Windows Server 2008R2 (6.1) or higher with RDS features
'''

EXAMPLES = '''
- name: Configure the Remote Desktop Gateway
  win_rds_settings:
    certificate_hash: B0D0FA8408FC67B230338FCA584D03792DA73F4C
    max_connections: 50
  notify:
    - Restart TSGateway service
'''

RETURN = '''
'''
