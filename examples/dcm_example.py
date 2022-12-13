###########################################################################
#
#  Copyright 2021 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################
#
#  This code generated (see scripts folder for possible source):
#    - Command: "python starthinker_ui/manage.py example"
#
###########################################################################

import argparse
import textwrap

from starthinker.util.configuration import Configuration
from starthinker.task.dcm.run import dcm


def recipe_dcm(config, auth_read, account, body, delete):
  """Create a CM report from a JSON definition.

     Args:
       auth_read (authentication) - Credentials used for reading data.
       account (string) - NA
       body (json) - NA
       delete (boolean) - NA
  """

  dcm(config, {
    'auth':auth_read,
    'report':{
      'account':account,
      'body':body
    },
    'delete':delete
  })



if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent("""
      Create a CM report from a JSON definition.

      1. Add a an account as [account_id]@[profile_id]
      2. Fetch the report JSON definition. Arguably could be better.
      3. The account is automatically added to the report definition.
  """))

  parser.add_argument("-project", help="Cloud ID of Google Cloud Project.", default=None)
  parser.add_argument("-key", help="API Key of Google Cloud Project.", default=None)
  parser.add_argument("-client", help="Path to CLIENT credentials json file.", default=None)
  parser.add_argument("-user", help="Path to USER credentials json file.", default=None)
  parser.add_argument("-service", help="Path to SERVICE credentials json file.", default=None)
  parser.add_argument("-verbose", help="Print all the steps as they happen.", action="store_true")

  parser.add_argument("-auth_read", help="Credentials used for reading data.", default='user')
  parser.add_argument("-account", help="", default='')
  parser.add_argument("-body", help="", default='{}')
  parser.add_argument("-delete", help="", default=False)


  args = parser.parse_args()

  config = Configuration(
    project=args.project,
    user=args.user,
    service=args.service,
    client=args.client,
    key=args.key,
    verbose=args.verbose
  )

  recipe_dcm(config, args.auth_read, args.account, args.body, args.delete)
