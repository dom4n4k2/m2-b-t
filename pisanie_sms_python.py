
import clx.xms
import requests

client = clx.xms.Client(service_plan_id='08b660356f9948d0af4926667a877c44', token='45251bf963324feea58384a33ac76e30')

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = '447537404817'
create.recipients = {'48535431229'}
create.body = 'This is a test message from your Sinch account'

try:
  batch = client.create_batch(create)
except (requests.exceptions.RequestException,
  clx.xms.exceptions.ApiException) as ex:
  print('Failed to communicate with XMS: %s' % str(ex))