#!/usr/bin/python3
# Parse Juniper SRX traffic logs and write into a CSV file
#

import csv
import re
import os
import sys

# csv hdr
header = ["Source Address", "Destination Address", "Protocol", "Port", "Source zone", "Destination zone", "Application name", "Policy name"]

# utility functions
def convertPortoNum(proto_id):
    return {
        1: "ICMP",
        6: "TCP",
        17: "UDP",
        53: "UDP",
    }.get(int(proto_id), "Undefined Protocol")

def removeQuotes(strName):
    return strName.split("=")[1].strip('"')

def convertToList(string):
    return list(string.split(","))

# main starts
def main():
    # get all the files in the dir and read each at a time
    cvs_fileName = 'coresrxlogs'+'_'+'res'+'.csv'
    dirName = "/root/srx-traffic-logs/core-srx1500"
    for fileName in os.listdir(dirName):
        with open(os.path.join(dirName, fileName), 'r') as f:
            print("Reading the file = ", fileName)
            lines = f.readlines()
        f.close()

        print("Writing into the CSV file = ",cvs_fileName)
        with open(os.path.join(dirName, cvs_fileName), 'a', newline = '') as cfile:
            writecsv = csv.writer(cfile)
            writecsv.writerow(header)
            for line in lines:
            # session create
                if re.match("(.*RT_FLOW_SESSION_CREATE.* )", line, re.I):
                    pass
                    noData = line.split('[', 1)[1].split(']')[0]
                    line_list = list(noData.split(" "))
                    final_str = removeQuotes(line_list[1]) + ',' + removeQuotes(line_list[3]) + ',' + \
                                convertPortoNum(removeQuotes(line_list[16])) + ',' + removeQuotes(line_list[4]) + ',' + \
                                removeQuotes(line_list[18]) + ',' + removeQuotes(line_list[19]) + ',' + \
                                removeQuotes(line_list[6]) + ',' + removeQuotes(line_list[17])
                    data = convertToList(final_str)
                    writecsv.writerow(data)

                if re.match("(.*RT_FLOW_SESSION_DENY.* )", line, re.I):
                    noData = line.split('[', 1)[1].split(']')[0]
                    line_list = list(noData.split(" "))
                    final_str = removeQuotes(line_list[1]) + ',' + removeQuotes(line_list[3]) + ',' + \
                                convertPortoNum(removeQuotes(line_list[7])) + ',' + removeQuotes(line_list[4]) + ',' + \
                                removeQuotes(line_list[10]) + ',' + removeQuotes(line_list[11]) + ',' + \
                                removeQuotes(line_list[6]) + ',' + removeQuotes(line_list[9])
                    data = convertToList(final_str)
                    writecsv.writerow(data)
    # close open files
    cfile.close()

if __name__ == "__main__":
    main()
