from cloudflare import Cloudflare
from argparser import args
import json

cf = Cloudflare(api_token=args.token)




def get_a_record(zone_id: str, record_id: str):
    return cf.dns.records.get(zone_id=zone_id, dns_record_id=record_id)


def update_record(zone_id: str, record_name: str, ip: str):

    if (json.loads(cf.dns.records.list(zone_id=zone_id, name=record_name, type="A").json())['result_info']['count'] < 1):
        cf.dns.records.create(zone_id=zone_id, name=record_name, content=ip, type="A")
        print("Record created: " + record_name + " - " + ip)

    records = cf.dns.records.list(zone_id=zone_id, name=record_name, type="A")
    records_dict = []

    for record in records:
        records_dict.append(record)

    if records_dict.__len__() > 1:
        for record in records_dict[1:]:
            cf.dns.records.delete(zone_id=zone_id, dns_record_id=record.id)
            print("Record deleted: " + record.name + " - " + record.content)


    if not (ip == records_dict[0].content):
        cf.dns.records.update(
            zone_id=zone_id, 
            dns_record_id=records_dict[0].id,
            content=ip,
            type="A",
            name=record_name
        )
        print("Record updated: " + record_name + " - " + ip)
    else:
        return
    

# def set_a_record(zone_id: str, record_id: str, ipv4: str):
#     record = cf.dns.records.get(zone_id=zone_id, dns_record_id=record_id)
#     if (record.type == "A"):
#         cf.dns.records.update(zone_id=zone_id, dns_record_id=record_id, name=record.name, content=record.content)
#     else:
#         raise Exception("Only A-records supported")
    