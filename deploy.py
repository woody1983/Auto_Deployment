#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import MySQLdb as mdb
import sys
import time
import datetime

con = mdb.connect('192.168.103.133','deploy','deploy','django')

now = datetime.datetime.now()
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")

Select_data = "SELECT RFC_SQL,id,Deploy_Date,RFC_STATUS,RFC_Number,Deploy_Server FROM AutoDeployment_deploy WHERE RFC_STATUS='approved' ORDER BY Deploy_Date;"

Deploy_Server = {"deploy_server" : ['192.168.103.133','deploy','deploy','deploy_PIXOS2'],
                 "int_sha" : ['10.30.0.21','deploy','deploy','PHX_PIXOS2_NORTH'],
                 "sha_prod" : ['10.30.0.21','deploy','deploy','PHX_PIXOS2_NORTH']
                }
				
cur = con.cursor()
cur.execute(Select_data)
tickets = cur.fetchall()

for row in tickets:
    #print ticket[2]
    if row == None or otherStyleTime < row[2].strftime("%Y-%m-%d %H:%M:%S"):
        break
    print row[4]+ " Deploy Time is: "+ str(row[2])
    Change_status = 'UPDATE AutoDeployment_deploy SET RFC_STATUS="processing" WHERE id= {0} AND RFC_Number = "{1}";'.format(row[1],row[4])
    Completed_status = 'UPDATE AutoDeployment_deploy SET RFC_STATUS="completed", SHOW_STATUS="success",Completed_Time = NOW(),Deploy_Log = "RFC Execute Success" WHERE id= {0} AND RFC_Number = "{1}";'.format(row[1],row[4])
    Failed_status = 'UPDATE AutoDeployment_deploy SET RFC_STATUS="failed", SHOW_STATUS="danger",Completed_Time = NOW() WHERE id= {0} AND RFC_Number = "{1}";'.format(row[1],row[4])
    # row[0] RFC_SQL
    # row[1] id
    # row[21 Deploy_Date
    # row[3] RFC_STATUS
    # row[4] RFC_Number
    # row[5] Deploy_Server
    db_info = Deploy_Server[row[5]]
    deploy_db = mdb.connect(db_info[0],db_info[1],db_info[2],db_info[3])
    deploy_cur = deploy_db.cursor()
    print row[4]+ " >>> Is Executing Now!"
    time.sleep(1)
    #-------[Exec SQL]----------#
    try:
	    #-------Processing-------#
        cur.execute(str(Change_status))
        con.commit()
        time.sleep(1)
		#-------Target Deploy Server-------#
        deploy_db = mdb.connect(db_info[0],db_info[1],db_info[2],db_info[3])
        deploy_cur = deploy_db.cursor()
	deploy_cur.execute(row[0]) #-----Execute RFC-----#
        deploy_db.commit()
        deploy_db.close()
        time.sleep(1)
        #-------Completed-------#
	cur.execute(str(Completed_status))
        con.commit()
        print row[4]+ " >>> Deploy is Completed!!"
    except Exception,ex:
        #print ex  
            #cur.execute(str(Failed_status))
        details = str(ex).replace("'",".")
        Deploy_Log = "UPDATE AutoDeployment_deploy SET Deploy_Log='{2}', Completed_Time = NOW() WHERE id= {0} AND RFC_Number = '{1}';".format(row[1],row[4],details)
            #print Deploy_Log
            #print ex.replace("\"","@") 
        cur.execute(str(Failed_status))
        print row[4]+ " >>> Deploy is Failed!!!"
        cur.execute(str(Deploy_Log))#For Debug
        con.commit()
        con.close()

#deploy_db.close()
