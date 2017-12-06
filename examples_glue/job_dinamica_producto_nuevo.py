'''
Created on 05-12-2017

@author: lnjofre
'''
from athena2pyspark.config import aws_access_key_id, aws_secret_access_key
import boto3

glue = boto3.client("glue", 
                    region_name='us-east-1', 
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

try:
    glue.delete_job(JobName="dinamica_producto_nuevo")
except:
    pass

job = glue.create_job(Name="dinamica_producto_nuevo", 
                      Role='AWSGlueServiceRole-Admin',
                      Command = {
                          'Name': "glueetl1",
                          'ScriptLocation': "s3://leonardo.exalitica.com/etl_scripts/delivery.py"},
                      DefaultArguments={'--extra-py-files': 's3://library.exalitica.com/athena2pyspark.zip',
                                        '--TempDir':'s3://glue-temp.exalitica.com'})

response = glue.start_job_run(JobName="dinamica_producto_nuevo",
                              Arguments={
                                    's3_location': 's3://leonardo.exalitica.com/boto3/query_example/',
                                    'file_name': 'CL_MOTOR_SALIDA_PA_LISTADO_20171129'
                                  })





