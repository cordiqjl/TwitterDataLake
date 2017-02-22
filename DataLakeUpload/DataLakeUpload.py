## Use this only for Azure AD service-to-service authentication
from azure.common.credentials import ServicePrincipalCredentials

## Use this only for Azure AD end-user authentication
from azure.common.credentials import UserPassCredentials

## Required for Azure Data Lake Store account management
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.datalake.store.models import DataLakeStoreAccount

## Required for Azure Data Lake Store filesystem management
from azure.datalake.store import core, lib, multithread

## Use these as needed for your application
import logging, getpass, pprint, uuid, time

tenant_id = 'https://login.windows.net/813cc00d-e1b3-40a5-8feb-ff4c58aca686/oauth2/token'
client_id = 'b1909523-915b-4a66-b603-1d5902f59872'
user = input('Enter the user to authenticate with that has permission to subscription: ')
password = getpass.getpass()

token = lib.auth(tenant_id, user, password)

# Some ID: 813cc00d-e1b3-40a5-8feb-ff4c58aca686  or f8617dfa-75de-4bb9-861b-d18b5953ac1f
# Object id: 02072a0e-b748-4763-a563-7018bb24fd60
# App id: b1909523-915b-4a66-b603-1d5902f59872
# Endpoint: https://login.windows.net/813cc00d-e1b3-40a5-8feb-ff4c58aca686/oauth2/token
# akey: UiLBvWAJAe0Uz9XOXoqnrxzBj7dpP3RlQhq/GyheT/M=

adlsAccountName = 'cdqjladal01'

## Create a filesystem client object
adlsFileSystemClient = core.AzureDLFileSystem(token, store_name=adlsAccountName)

## Create a directory
adlsFileSystemClient.mkdir('/mysampledirectory')