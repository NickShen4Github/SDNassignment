#curl -X PUT -d '"tcp:127.0.0.1:6632"' http://localhost:8080/v1.0/conf/switches/0000000000000001/ovsdb_addr
#run that in xterm c0
#curl -X POST -d '{"max_rate": "1000000", "queues": [{"max_rate": "500000"}, {"min_rate": "800000"}]}' http://localhost:8080/qos/queue/0000000000000001
#curl -X POST -d '{"match": {"nw_src": "172.16.1.11", "nw_proto": "UDP"}, "actions":{"queue": "0"}}' http://localhost:8080/qos/rules/0000000000000001
from subprocess import call
import requests
import json

serverUrl="http://127.0.0.1:8080/"

## postToRyu will genereate a json request to ryu server
## parameters
##    switchID : in string format
##    ruleData : in json string format
## the request result will be print out to console
## if an error happens an exception will be raised
def postToRyu(switchID,ruleData):
    fullUrl=serverUrl+"qos/rules/"+switchID
    r = requests.post(fullUrl,data=json.dumps(ruleData))

    print r.text + "\n"

    if r.status_code != requests.codes.ok :
        r.raise_for_status()

def setQueue(switchID,ruleData):
    fullUrl=serverUrl+"qos/queue/"+switchID
    r = requests.post(fullUrl,data=json.dumps(ruleData))

    print r.text + "\n"

    if r.status_code != requests.codes.ok :
        r.raise_for_status()

def getRyuData():
    fullUrl=serverUrl+"router/all/all"
    r=requests.get(fullUrl)
    print "\n current ryu configs are: \n"
    print r.text+"\n"


    
    
    

def myQos():
    # sw1 does all settings
    setQueue("0000000000000001", {"type": "linux-htb", "max_rate": "1000000", "queues": [{"max_rate": "500000"}, {"min_rate": "800000"}]})

##########QOS###########################
#src
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.1.11"}, "actions":{"queue": "0"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.1.12"}, "actions":{"queue": "0"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.1.11"}, "actions":{"queue": "0"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.1.12"}, "actions":{"queue": "0"}})
#SL lab
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.11"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.12"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.13"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.14"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.15"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.16"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.17"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.18"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.19"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.20"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.21"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.22"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.23"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.24"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.25"}, "actions":{"queue": "1"}})

#Proto lab
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.31"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.32"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.33"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.34"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.35"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.36"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.37"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.38"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.39"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.40"}, "actions":{"queue": "1"}})

#one office
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.41"}, "actions":{"queue": "1"}})

#demo room
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.3.51"}, "actions":{"queue": "1"}})

#hpc
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.4.31"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.4.32"}, "actions":{"queue": "1"}})

#server room
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.1.31"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.1.32"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.1.33"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.1.34"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_src": "172.16.1.35"}, "actions":{"queue": "1"}})

#dst############################################
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.11"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.12"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.13"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.14"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.15"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.16"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.17"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.18"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.19"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.20"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.21"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.22"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.23"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.24"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.25"}, "actions":{"queue": "1"}})

#Proto lab
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.31"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.32"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.33"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.34"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.35"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.36"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.37"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.38"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.39"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.40"}, "actions":{"queue": "1"}})

#one office
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.41"}, "actions":{"queue": "1"}})

#demo room
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.3.51"}, "actions":{"queue": "1"}})

#hpc
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.4.31"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.4.32"}, "actions":{"queue": "1"}})

#server room
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.1.31"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.1.32"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.1.33"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.1.34"}, "actions":{"queue": "1"}})
    postToRyu("0000000000000001", {"match": {"nw_dst": "172.16.1.35"}, "actions":{"queue": "1"}})

if __name__ == '__main__':
    #setAddr()
    myQos()
    getRyuData()
