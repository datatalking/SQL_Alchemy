from sqlalchemy import create_engine
import cx_Oracle

host=hostname
port=port
sid='sid'
user='username'
password='password'
sid = cx_Oracle.makedsn(host, port, sid=sid)

sqlalchemy.engine.url.URL("oracle", user, password, sid)

engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)

result = engine.execute('select * from TABLE')

for row in result:
    print row


"""
https://free-for.dev/#/
Oracle Cloud

Compute - 2 VM.Standard.E2.1.Micro 1GB RAM, 4 Arm-based Ampere A1 cores and 24 GB of memory usable as one VM or up to 4 VMs
Block Volume - 2 volumes, 200 GB total (used for compute)
Object Storage - 10 GB
Load balancer - 1 instance with 10 Mbps
Databases - 2 DBs, 20 GB each
Monitoring - 500 million ingestion datapoints, 1 billion retrieval datapoints
Bandwidth - 10TB egress per month, speed limited to 5Mbps
Notifications - 1 million delivery options per month, 1000 emails sent per month
Full, detailed list - https://www.oracle.com/cloud/free/
"""