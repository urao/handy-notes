!#/bin/bash

OVERCLOUD_IP=fd00:fd00:fd00:3001::15
CONTRAIL_API_PORT=18082
KEYSTONE_PORT=13000
PASSWORD="c0ntrail123"


export OS_PROJECT_DOMAIN_NAME=Default
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_NAME=admin
export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=$PASSWORD
export OS_AUTH_URL=https://[$OVERCLOUD_IP]:$KEYSTONE_PORT/v3
export OS_INTERFACE=public
export OS_IDENTITY_API_VERSION=3


RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

dt=$(date "+%d-%m-%Y %a %H:%M:%S")

echo -e "$dt Retrieving OpenStack keystone token"

export OS_TOKEN=$(curl -i -g 6 -s -k --fail --show-error  -X POST $OS_AUTH_URL/auth/tokens?nocatalog \
    -H "Content-Type: application/json" \
    -d '{
        "auth": {
            "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                "domain": {
                    "name": "'"$OS_USER_DOMAIN_NAME"'"
                },
                "name": "'"$OS_USERNAME"'",
                "password": "'"$OS_PASSWORD"'"
                }
            }
            },
            "scope": {
            "project": {
                "domain": {
                "name": "'"$OS_PROJECT_DOMAIN_NAME"'"
                },
                "name": "'"$OS_PROJECT_NAME"'"
            }
            }
        }
    }' | grep ^X-Subject-Token: | tr -d '\r' | awk '{print $2}')
if [ -z "$OS_TOKEN" ]
then
    echo -e "$dt ${RED}Failed:${NC} could not get the OpenStack token"
    exit 1
else
    echo -e "$dt ${GREEN}Success:${NC} OpenStack token is:" $OS_TOKEN
    exit 0
fi
