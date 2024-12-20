import argparser
import sys
import internet
import time
import cf



def main():
    delay = argparser.args.delay if argparser.args.delay else 30.0
    token = argparser.args.token
    zone_id = argparser.args.zone
    names = argparser.args.record

    try:
        while True:
            if not internet.check_internet_connection():
                if argparser.args.verbose: print("Can't connect to 1.1.1.1")
                time.sleep(6.0)
                continue
            

            try:
                current_ip = internet.get_my_ipv4()
                if argparser.args.verbose: print("Current ip: " + current_ip)

                for record in argparser.args.record:
                    cf.update_record(
                        zone_id=argparser.args.zone,
                        record_name=record,
                        ip=current_ip
                    )
                
                time.sleep(delay)
                continue

                    
            except Exception as e:
                print(e)

                if argparser.args.autoexit: 
                    sys.exit()
                else: 
                    time.sleep(delay)
                    continue




    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()


if __name__ == "__main__":
    main()