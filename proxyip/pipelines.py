# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json;
import pymysql;

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='wxy',
        passwd='wxy@2017',
        charset='utf8',
        use_unicode=False
    )
    return conn


class ProxyipPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE proxyip")
        sql = 'insert into proxyip_tab(ip,port,address,type_id,speed,proving_time) values (%s,%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (item['ip'], item['port'], item['address'], item['type_id'],item['speed'],item['proving_time']))
            dbObject.commit()
        except Exception, e:
            print ("错误在这里>>>>>>>>>>", e, "<<<<<<<<<<<<<<<<<<")
            dbObject.rollback()
        return item
